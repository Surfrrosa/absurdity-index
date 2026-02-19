#!/usr/bin/env python3
"""
CFPB Consumer Complaint Database Collector for the Absurdity Index.
Uses the free, public CFPB API (no authentication needed) to collect
complaint data relevant to healthcare, housing_despair, and
subscription_overload metrics.

API docs: https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/

Usage:
    python cfpb-collector.py
"""

import os
import csv
import time
import requests
from datetime import datetime, timedelta

# Change to the script's directory so collected-data/ paths resolve correctly
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

API_BASE = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"

# How many complaints to fetch per query (stay respectful)
MAX_RESULTS = 100

# Delay between API requests (seconds)
REQUEST_DELAY = 1

# Lookback window in days
LOOKBACK_DAYS = 90

# -----------------------------------------------------------------------
# Severity keyword lists
# -----------------------------------------------------------------------

LEVEL_3_KEYWORDS = [
    "bankruptcy", "lawsuit", "foreclosure", "denied treatment",
    "emergency", "life-threatening", "sued", "wage garnishment",
    "court order", "eviction", "homeless", "lost my home",
    "filed chapter", "repossession"
]

LEVEL_2_KEYWORDS = [
    "repeated", "multiple times", "denied claim", "denied claims",
    "high cost", "collections", "collection agency", "unaffordable",
    "struggling to pay", "can't afford", "overcharged", "unfair fees",
    "hidden fees", "unauthorized charge", "predatory", "harassment",
    "ruined credit", "credit score dropped", "deceptive"
]

# -----------------------------------------------------------------------
# Metric query configurations
# -----------------------------------------------------------------------

METRIC_QUERIES = {
    "healthcare": {
        "slug": "healthcare",
        "description": "Medical debt and healthcare-related complaints",
        "queries": [
            {
                "label": "Medical debt collection",
                "params": {
                    "product": "Debt collection",
                    "sub_product": "Medical debt",
                }
            },
            {
                "label": "Health care / medical debt",
                "params": {
                    "product": "Debt collection",
                    "sub_product": "Health care medical",
                }
            },
        ]
    },
    "housing_despair": {
        "slug": "housing_despair",
        "description": "Mortgage and housing credit complaints",
        "queries": [
            {
                "label": "Mortgage complaints",
                "params": {
                    "product": "Mortgage",
                }
            },
            {
                "label": "Credit reporting - mortgage issues",
                "params": {
                    "product": "Credit reporting, credit repair services, or other personal consumer reports",
                    "issue": "mortgage",
                }
            },
        ]
    },
    "subscription_overload": {
        "slug": "subscription_overload",
        "description": "Credit card billing disputes and subscription-related complaints",
        "queries": [
            {
                "label": "Credit card billing disputes",
                "params": {
                    "product": "Credit card or prepaid card",
                    "issue": "billing",
                }
            },
        ]
    },
}


def build_date_range():
    """Return (min_date, max_date) strings for the last 90 days."""
    today = datetime.now()
    start = today - timedelta(days=LOOKBACK_DAYS)
    return start.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d")


def fetch_complaints(params_override):
    """
    Query the CFPB complaints API and return a list of complaint dicts.

    params_override: dict of extra query params (product, sub_product, issue, etc.)
    """
    date_min, date_max = build_date_range()

    params = {
        "date_received_min": date_min,
        "date_received_max": date_max,
        "size": MAX_RESULTS,
        "sort": "created_date_desc",
        "no_aggs": "true",
        "field": "all",
    }
    params.update(params_override)

    try:
        response = requests.get(API_BASE, params=params, timeout=30)

        if response.status_code == 200:
            data = response.json()
            hits = data.get("hits", {}).get("hits", [])
            total = data.get("hits", {}).get("total", {})
            # total may be an int or a dict with 'value'
            if isinstance(total, dict):
                total_count = total.get("value", 0)
            else:
                total_count = total
            return hits, total_count
        elif response.status_code == 429:
            print("  Rate limited. Waiting 10 seconds...")
            time.sleep(10)
            response = requests.get(API_BASE, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                hits = data.get("hits", {}).get("hits", [])
                return hits, len(hits)
            print(f"  Still rate limited ({response.status_code}). Skipping.")
            return [], 0
        else:
            print(f"  API error {response.status_code}: {response.text[:200]}")
            return [], 0
    except requests.exceptions.RequestException as e:
        print(f"  Request failed: {e}")
        return [], 0


def categorize_complaint(narrative, product, issue, sub_product):
    """
    Categorize a complaint into LEVEL_3_CRISIS, LEVEL_2_FRUSTRATED, or LEVEL_1_AWARE.

    Uses the narrative text if available, otherwise falls back to product/issue fields.
    """
    # Build the text corpus to scan -- combine all available fields
    parts = []
    if narrative:
        parts.append(narrative)
    if product:
        parts.append(product)
    if issue:
        parts.append(issue)
    if sub_product:
        parts.append(sub_product)

    text = " ".join(parts).lower()

    # Check for Level 3 (crisis) keywords
    level_3_hits = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
    if level_3_hits >= 1:
        return "LEVEL_3_CRISIS"

    # Check for Level 2 (frustrated) keywords
    level_2_hits = sum(1 for kw in LEVEL_2_KEYWORDS if kw in text)
    if level_2_hits >= 1:
        return "LEVEL_2_FRUSTRATED"

    # Default
    return "LEVEL_1_AWARE"


def snippet(text, max_len=200):
    """Return first max_len chars of text, cleaned for CSV safety."""
    if not text:
        return ""
    # Replace newlines and excessive whitespace
    cleaned = " ".join(text.split())
    if len(cleaned) > max_len:
        return cleaned[:max_len] + "..."
    return cleaned


def collect_metric(metric_key, metric_config):
    """
    Collect all complaints for a single Absurdity Index metric.
    Returns a list of row dicts ready for CSV output.
    """
    slug = metric_config["slug"]
    description = metric_config["description"]
    queries = metric_config["queries"]

    print(f"\n{'='*70}")
    print(f"  {metric_key.upper().replace('_', ' ')} -- {description}")
    print(f"{'='*70}")

    all_rows = []
    seen_ids = set()

    for query in queries:
        label = query["label"]
        params = query["params"]
        print(f"\n  Query: {label}")
        print(f"    Params: {params}")

        hits, total_count = fetch_complaints(params)
        print(f"    Total matching: {total_count} | Fetched: {len(hits)}")

        for hit in hits:
            source = hit.get("_source", {})
            complaint_id = source.get("complaint_id", hit.get("_id", ""))

            # Deduplicate across queries within same metric
            if complaint_id in seen_ids:
                continue
            seen_ids.add(complaint_id)

            product = source.get("product", "")
            sub_product = source.get("sub_product", "")
            issue = source.get("issue", "")
            narrative = source.get("complaint_what_happened", "")
            date_received = source.get("date_received", "")

            category = categorize_complaint(narrative, product, issue, sub_product)

            all_rows.append({
                "complaint_id": complaint_id,
                "product": product,
                "sub_product": sub_product,
                "issue": issue,
                "category": category,
                "date_received": date_received,
                "narrative_snippet": snippet(narrative, 200),
                "metric": slug,
            })

        # Respectful delay between requests
        time.sleep(REQUEST_DELAY)

    # Print summary for this metric
    total = len(all_rows)
    l3 = sum(1 for r in all_rows if r["category"] == "LEVEL_3_CRISIS")
    l2 = sum(1 for r in all_rows if r["category"] == "LEVEL_2_FRUSTRATED")
    l1 = sum(1 for r in all_rows if r["category"] == "LEVEL_1_AWARE")

    print(f"\n  Results for {slug}:")
    print(f"    Total unique complaints: {total}")
    if total > 0:
        print(f"    LEVEL_3_CRISIS:    {l3} ({l3/total*100:.1f}%)")
        print(f"    LEVEL_2_FRUSTRATED: {l2} ({l2/total*100:.1f}%)")
        print(f"    LEVEL_1_AWARE:     {l1} ({l1/total*100:.1f}%)")
    else:
        print("    No complaints returned for this metric.")

    return all_rows


def write_csv(rows, slug, timestamp):
    """Write collected rows to a CSV file. Returns the filename or None."""
    if not rows:
        return None

    filename = f"collected-data/{slug}_cfpb_{timestamp}.csv"
    fieldnames = [
        "complaint_id",
        "product",
        "sub_product",
        "issue",
        "category",
        "date_received",
        "narrative_snippet",
        "metric",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return filename


def main():
    date_min, date_max = build_date_range()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    print("=" * 70)
    print("CFPB CONSUMER COMPLAINT COLLECTOR -- Absurdity Index")
    print("=" * 70)
    print(f"Date range: {date_min} to {date_max} ({LOOKBACK_DAYS} days)")
    print(f"Max results per query: {MAX_RESULTS}")
    print(f"Metrics: {', '.join(METRIC_QUERIES.keys())}")

    files_written = []
    grand_total = 0

    for metric_key, metric_config in METRIC_QUERIES.items():
        rows = collect_metric(metric_key, metric_config)
        grand_total += len(rows)

        # Empty-data guard: only write if we got results
        if len(rows) == 0:
            print(f"\n  Skipping CSV write for {metric_key} (0 results).")
            continue

        filename = write_csv(rows, metric_config["slug"], timestamp)
        if filename:
            files_written.append(filename)
            print(f"\n  Saved: {filename}")

    # Final summary
    print(f"\n{'='*70}")
    print("COLLECTION COMPLETE")
    print(f"{'='*70}")
    print(f"Grand total complaints collected: {grand_total}")
    print(f"Files written: {len(files_written)}")
    for f in files_written:
        print(f"  - {f}")

    if not files_written:
        print("\nNo data collected. The API may be temporarily unavailable,")
        print("or the date range may have no matching complaints.")

    print(f"{'='*70}")


if __name__ == "__main__":
    main()
