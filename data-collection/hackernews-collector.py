#!/usr/bin/env python3
"""
Hacker News Collector - Absurdity Index
Uses the free Algolia HN Search API - NO API KEY NEEDED

Collects stories across multiple metrics:
  - layoff_watch
  - ai_psychosis
  - subscription_overload
  - wage_stagnation
  - housing_despair

Categorizes by severity (Level 1/2/3) and outputs per-metric CSVs.
"""

import requests
import time
import csv
from datetime import datetime, timedelta
from content_filters import filter_content

# ---------------------------------------------------------------------------
# API configuration
# ---------------------------------------------------------------------------

BASE_URL = "https://hn.algolia.com/api/v1/search"

HEADERS = {
    "User-Agent": "AbsurdityIndexResearch/1.0 (Academic Research Project)"
}

# 90-day lookback window
NINETY_DAYS_AGO = int((datetime.utcnow() - timedelta(days=90)).timestamp())

# ---------------------------------------------------------------------------
# Metrics and their search terms
# ---------------------------------------------------------------------------

METRICS = {
    "layoff_watch": [
        "laid off",
        "tech layoffs",
        "job search nightmare",
        "500 applications",
        "fired from tech",
        "layoff wave",
    ],
    "ai_psychosis": [
        "AI addiction",
        "ChatGPT obsession",
        "AI companion",
        "AI replacing humans",
        "Character.AI",
    ],
    "subscription_overload": [
        "subscription fatigue",
        "price increase",
        "streaming costs",
        "SaaS pricing",
    ],
    "wage_stagnation": [
        "paycheck to paycheck",
        "can't afford rent",
        "wages not keeping up",
        "cost of living",
    ],
    "housing_despair": [
        "housing crisis",
        "can't afford home",
        "rent too high",
        "priced out",
    ],
}

# ---------------------------------------------------------------------------
# Severity classification keywords
# ---------------------------------------------------------------------------

LEVEL_3_KEYWORDS = [
    "homeless", "bankrupt", "crisis", "emergency",
    "can't survive", "lost everything", "eviction",
    "sleeping in car", "living in car", "suicidal",
    "no food", "starving", "destitute",
]

LEVEL_2_KEYWORDS = [
    "struggling", "frustrated", "exhausted",
    "can't afford", "giving up", "burned out",
    "desperate", "overwhelmed", "anxiety",
    "drowning in", "breaking point", "hopeless",
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def search_hn(query, hits_per_page=50):
    """
    Search Hacker News via Algolia API.
    Returns a list of hit dicts, limited to stories from the last 90 days.
    """
    params = {
        "query": query,
        "tags": "story",
        "numericFilters": f"created_at_i>{NINETY_DAYS_AGO}",
        "hitsPerPage": hits_per_page,
    }

    try:
        response = requests.get(
            BASE_URL, headers=HEADERS, params=params, timeout=15
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("hits", [])
        elif response.status_code == 429:
            print("  Rate limited, waiting 10s...")
            time.sleep(10)
            response = requests.get(
                BASE_URL, headers=HEADERS, params=params, timeout=15
            )
            if response.status_code == 200:
                return response.json().get("hits", [])
            print(f"  Still rate limited after retry")
            return []
        else:
            print(f"  Error {response.status_code} for query '{query}'")
            return []
    except Exception as e:
        print(f"  Exception fetching '{query}': {e}")
        return []


def categorize_story(title):
    """
    Categorize a story into LEVEL_3_CRISIS, LEVEL_2_FRUSTRATED,
    or LEVEL_1_AWARE based on title keywords.
    """
    text = title.lower()

    level_3_count = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
    if level_3_count >= 1:
        return "LEVEL_3_CRISIS"

    level_2_count = sum(1 for kw in LEVEL_2_KEYWORDS if kw in text)
    if level_2_count >= 1:
        return "LEVEL_2_FRUSTRATED"

    return "LEVEL_1_AWARE"


def collect_metric(metric_slug, search_terms):
    """
    Collect HN stories for a single metric across all its search terms.
    Deduplicates by objectID within the metric.
    Returns a list of row dicts ready for CSV.
    """
    print(f"\n  Metric: {metric_slug}")
    print(f"  Search terms: {len(search_terms)}")

    seen_ids = set()
    rows = []

    for term in search_terms:
        print(f"    Searching: '{term}'")
        hits = search_hn(term)

        term_count = 0
        for hit in hits:
            object_id = hit.get("objectID")
            if object_id in seen_ids:
                continue
            seen_ids.add(object_id)

            title = hit.get("title") or ""
            url = hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
            points = hit.get("points") or 0
            num_comments = hit.get("num_comments") or 0
            created_at = hit.get("created_at") or ""

            # Filter out clickbait/promotional content
            if not filter_content(title):
                continue

            category = categorize_story(title)
            term_count += 1

            rows.append({
                "title": title,
                "url": url,
                "points": points,
                "num_comments": num_comments,
                "category": category,
                "created_at": created_at,
                "search_term": term,
                "metric": metric_slug,
            })

        print(f"      Found {term_count} new stories")

        # Be respectful with rate limiting
        time.sleep(1)

    print(f"  Total unique stories for {metric_slug}: {len(rows)}")
    return rows


def write_metric_csv(metric_slug, rows):
    """Write a CSV file for a single metric. Returns the filename or None."""
    if len(rows) == 0:
        print(f"\n  WARNING: No stories for {metric_slug}. Skipping file write.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"collected-data/{metric_slug}_hackernews_{timestamp}.csv"

    fieldnames = [
        "title", "url", "points", "num_comments",
        "category", "created_at", "search_term", "metric",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return filename


def print_summary(metric_slug, rows):
    """Print severity breakdown for a metric."""
    total = len(rows)
    if total == 0:
        return

    level_3 = len([r for r in rows if r["category"] == "LEVEL_3_CRISIS"])
    level_2 = len([r for r in rows if r["category"] == "LEVEL_2_FRUSTRATED"])
    level_1 = len([r for r in rows if r["category"] == "LEVEL_1_AWARE"])

    print(f"\n  {metric_slug}: {total} stories")
    print(f"    Level 3 (Crisis):      {level_3} ({level_3/total*100:.1f}%)")
    print(f"    Level 2 (Frustrated):  {level_2} ({level_2/total*100:.1f}%)")
    print(f"    Level 1 (Aware):       {level_1} ({level_1/total*100:.1f}%)")

    avg_points = sum(r["points"] for r in rows) / total
    print(f"    Avg points:            {avg_points:.0f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("HACKER NEWS COLLECTOR - ABSURDITY INDEX")
    print("=" * 70)
    print(f"\nUsing Algolia HN Search API (no auth needed)")
    print(f"Lookback: 90 days (since {datetime.utcfromtimestamp(NINETY_DAYS_AGO).strftime('%Y-%m-%d')})")
    print(f"Metrics: {len(METRICS)}")

    all_results = {}
    saved_files = []

    for metric_slug, search_terms in METRICS.items():
        rows = collect_metric(metric_slug, search_terms)
        all_results[metric_slug] = rows

        filename = write_metric_csv(metric_slug, rows)
        if filename:
            saved_files.append(filename)

    # Summary
    print("\n" + "=" * 70)
    print("COLLECTION COMPLETE")
    print("=" * 70)

    grand_total = 0
    for metric_slug, rows in all_results.items():
        print_summary(metric_slug, rows)
        grand_total += len(rows)

    print(f"\nGrand total: {grand_total} stories across {len(METRICS)} metrics")

    if saved_files:
        print(f"\nFiles saved:")
        for f in saved_files:
            print(f"  {f}")
    else:
        print("\nNo files saved (no data collected).")
        print("Check your network connection or try again later.")

    print("=" * 70)


if __name__ == "__main__":
    main()
