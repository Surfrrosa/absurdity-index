#!/usr/bin/env python3
"""Collect official data scores from FRED API.

Pulls live economic data from the Federal Reserve Economic Data (FRED) API
and normalizes each metric to a 0-100 absurdity score. For metrics without
suitable FRED series, falls back to hardcoded values from config.json.

Usage:
    python fred-collector.py

Requires FRED_API_KEY in .env file. Get a free key at:
    https://fred.stlouisfed.org/docs/api/api_key.html
"""

import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "collected-data"
OUTPUT_FILE = OUTPUT_DIR / "official_scores.json"
CONFIG_FILE = SCRIPT_DIR / "config.json"

# FRED series IDs
SERIES = {
    "avg_hourly_earnings": "CES0500000003",
    "cpi": "CPIAUCSL",
    "median_home_price": "MSPUS",
    "median_household_income": "MEHOINUSA672N",
    "initial_claims": "ICSA",
    "consumer_sentiment": "UMCSENT",
}

# Metrics that have no good FRED mapping -- use config.json fallback
FALLBACK_ONLY_SLUGS = [
    "ai_psychosis",
    "subscription_overload",
    "dating_app_despair",
    "airline_chaos",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_config():
    """Load config.json and return a dict of slug -> official_score."""
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
    return {m["slug"]: m["official_score"] for m in config["metrics"]}


def clamp(value, lo=0.0, hi=100.0):
    return max(lo, min(hi, value))


def pct_change_yoy(series):
    """Return year-over-year percent change from the two most recent
    observations that are roughly 12 months apart.

    `series` is a pandas Series indexed by date, sorted ascending.
    """
    if series is None or len(series) < 2:
        return None

    latest = series.iloc[-1]
    latest_date = series.index[-1]

    # Walk backwards to find an observation roughly 12 months prior
    target_date = latest_date - timedelta(days=365)
    # Find closest date in the index
    diffs = abs(series.index - target_date)
    closest_idx = diffs.argmin()
    prior = series.iloc[closest_idx]

    if prior == 0:
        return None

    return ((latest - prior) / prior) * 100.0


# ---------------------------------------------------------------------------
# Metric calculations
# ---------------------------------------------------------------------------

def calc_wage_stagnation(fred):
    """Real wage growth: earnings growth minus CPI growth.
    Lower real growth = higher absurdity.
    """
    print("\n--- Wage Stagnation ---")
    try:
        earnings = fred.get_series(SERIES["avg_hourly_earnings"])
        cpi = fred.get_series(SERIES["cpi"])
    except Exception as e:
        print(f"  FRED fetch error: {e}")
        return None

    wage_growth = pct_change_yoy(earnings)
    cpi_growth = pct_change_yoy(cpi)

    if wage_growth is None or cpi_growth is None:
        print("  Could not compute YoY changes.")
        return None

    real_growth = wage_growth - cpi_growth
    print(f"  Nominal wage growth (YoY): {wage_growth:.2f}%")
    print(f"  CPI growth (YoY):          {cpi_growth:.2f}%")
    print(f"  Real wage growth:           {real_growth:.2f}%")

    # Normalization:
    #   2%+ positive  -> 0-20
    #   0%            -> 50
    #   negative      -> 60-100  (more negative = higher absurdity)
    if real_growth >= 2.0:
        # Map [2, inf) -> [0, 20], with 4%+ clamped to 0
        score = clamp(20.0 - (real_growth - 2.0) * 10.0, 0.0, 20.0)
    elif real_growth >= 0.0:
        # Map [0, 2) -> [20, 50]
        score = 50.0 - (real_growth / 2.0) * 30.0
    else:
        # Map (-inf, 0) -> [50, 100], with -3% or worse clamped to 100
        score = clamp(50.0 + abs(real_growth) * (50.0 / 3.0), 50.0, 100.0)

    score = clamp(score)
    print(f"  Absurdity score: {score:.1f}")
    return round(score, 1)


def calc_housing_despair(fred):
    """Price-to-income ratio. Higher = more absurd."""
    print("\n--- Housing Despair ---")
    try:
        home_prices = fred.get_series(SERIES["median_home_price"])
        income = fred.get_series(SERIES["median_household_income"])
    except Exception as e:
        print(f"  FRED fetch error: {e}")
        return None

    if home_prices is None or len(home_prices) == 0:
        print("  No home price data.")
        return None
    if income is None or len(income) == 0:
        print("  No income data.")
        return None

    latest_price = home_prices.iloc[-1]
    latest_income = income.iloc[-1]

    if latest_income == 0:
        print("  Income is zero -- cannot compute ratio.")
        return None

    ratio = latest_price / latest_income
    print(f"  Median home price:  ${latest_price:,.0f}")
    print(f"  Median HH income:   ${latest_income:,.0f}")
    print(f"  Price-to-income:    {ratio:.2f}x")

    # Normalization:
    #   3x  -> 20
    #   5x  -> 50
    #   7x+ -> 80-100
    if ratio <= 3.0:
        score = clamp((ratio / 3.0) * 20.0, 0.0, 20.0)
    elif ratio <= 5.0:
        score = 20.0 + ((ratio - 3.0) / 2.0) * 30.0  # 20 -> 50
    elif ratio <= 7.0:
        score = 50.0 + ((ratio - 5.0) / 2.0) * 30.0  # 50 -> 80
    else:
        score = clamp(80.0 + ((ratio - 7.0) / 2.0) * 20.0, 80.0, 100.0)

    score = clamp(score)
    print(f"  Absurdity score: {score:.1f}")
    return round(score, 1)


def calc_layoff_watch(fred):
    """Weekly initial jobless claims."""
    print("\n--- Layoff Watch ---")
    try:
        claims = fred.get_series(SERIES["initial_claims"])
    except Exception as e:
        print(f"  FRED fetch error: {e}")
        return None

    if claims is None or len(claims) == 0:
        print("  No claims data.")
        return None

    latest = claims.iloc[-1]
    print(f"  Latest initial claims: {latest:,.0f}")

    # Normalization (thousands):
    #   <200k  -> 20
    #   250k   -> 50
    #   400k+  -> 90-100
    claims_k = latest / 1000.0

    if claims_k <= 200:
        score = clamp((claims_k / 200.0) * 20.0, 0.0, 20.0)
    elif claims_k <= 250:
        score = 20.0 + ((claims_k - 200.0) / 50.0) * 30.0  # 20 -> 50
    elif claims_k <= 400:
        score = 50.0 + ((claims_k - 250.0) / 150.0) * 40.0  # 50 -> 90
    else:
        score = clamp(90.0 + ((claims_k - 400.0) / 200.0) * 10.0, 90.0, 100.0)

    score = clamp(score)
    print(f"  Absurdity score: {score:.1f}")
    return round(score, 1)


def calc_healthcare(fred):
    """Consumer Sentiment as a proxy -- inverted."""
    print("\n--- Healthcare (proxy: Consumer Sentiment) ---")
    try:
        sentiment = fred.get_series(SERIES["consumer_sentiment"])
    except Exception as e:
        print(f"  FRED fetch error: {e}")
        return None

    if sentiment is None or len(sentiment) == 0:
        print("  No sentiment data.")
        return None

    latest = sentiment.iloc[-1]
    print(f"  Latest Consumer Sentiment: {latest:.1f}")

    # Invert: sentiment 100 = absurdity 0, sentiment 50 = absurdity 50
    # Linearly: absurdity = 100 - sentiment, clamped to [0, 100]
    score = clamp(100.0 - latest)
    print(f"  Absurdity score: {score:.1f}")
    return round(score, 1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    load_dotenv(SCRIPT_DIR / ".env")

    api_key = os.getenv("FRED_API_KEY")
    if not api_key:
        print("ERROR: FRED_API_KEY not found in environment.")
        print("Set it in data-collection/.env or export it directly.")
        print("Get a free key at: https://fred.stlouisfed.org/docs/api/api_key.html")
        sys.exit(1)

    try:
        from fredapi import Fred
    except ImportError:
        print("ERROR: fredapi not installed. Run: pip install fredapi")
        sys.exit(1)

    fred = Fred(api_key=api_key)

    # Load fallback scores from config.json
    fallbacks = load_config()
    print(f"Loaded {len(fallbacks)} fallback scores from config.json")

    # Collect FRED-based scores
    fred_scores = {}
    collectors = {
        "wage_stagnation": calc_wage_stagnation,
        "housing_despair": calc_housing_despair,
        "layoff_watch": calc_layoff_watch,
        "healthcare": calc_healthcare,
    }

    for slug, calc_fn in collectors.items():
        try:
            result = calc_fn(fred)
            if result is not None:
                fred_scores[slug] = result
            else:
                print(f"  -> Using fallback: {fallbacks.get(slug, 'N/A')}")
        except Exception as e:
            print(f"  Unexpected error for {slug}: {e}")
            print(f"  -> Using fallback: {fallbacks.get(slug, 'N/A')}")

    # Assemble final output: FRED scores + fallbacks for everything else
    output = {}

    for slug, fallback_score in fallbacks.items():
        if slug in fred_scores:
            output[slug] = {
                "score": fred_scores[slug],
                "source": "fred",
            }
        elif slug in FALLBACK_ONLY_SLUGS:
            output[slug] = {
                "score": fallback_score,
                "source": "config_fallback",
            }
        elif slug in collectors:
            # FRED collector exists but failed -- use fallback
            output[slug] = {
                "score": fallback_score,
                "source": "config_fallback (fred failed)",
            }
        else:
            output[slug] = {
                "score": fallback_score,
                "source": "config_fallback",
            }

    # Empty-data guard
    collected_count = sum(1 for v in output.values() if v["source"] == "fred")
    total_count = len(output)

    print("\n" + "=" * 60)
    print(f"RESULTS: {collected_count} from FRED, "
          f"{total_count - collected_count} from fallback")
    print("=" * 60)

    for slug, info in output.items():
        print(f"  {slug:30s} -> {info['score']:6.1f}  ({info['source']})")

    if total_count == 0:
        print("\nNo scores collected at all. Skipping file write.")
        return

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    result = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "fred_series_used": SERIES,
        "scores": output,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nWrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
