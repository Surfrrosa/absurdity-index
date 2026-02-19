#!/usr/bin/env python3
"""
Bluesky Post Collector - All Metrics
Uses the free AT Protocol public API (no auth needed) to collect posts
relevant to Absurdity Index metrics.

Endpoint: https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts
"""

import requests
import time
import csv
from datetime import datetime
from content_filters import filter_content


# ---------------------------------------------------------------------------
# Metric definitions: search terms + severity keywords
# ---------------------------------------------------------------------------

METRICS = {
    "healthcare": {
        "search_terms": [
            "medical debt",
            "insurance denied",
            "healthcare nightmare",
            "can't afford doctor",
            "hospital bill",
        ],
        "level_3_keywords": [
            "bankruptcy", "collections", "medical debt", "going broke",
            "can't afford treatment", "life-saving", "cancer treatment",
            "dying", "emergency", "life or death", "denied life-saving",
            "filed for bankruptcy", "lost everything",
        ],
        "level_3_phrases": [
            "filed for bankruptcy", "going to die", "denied life-saving",
            "can't afford cancer", "medical bankruptcy",
        ],
        "level_2_keywords": [
            "denied", "claim denied", "rejected", "appeal denied",
            "won't cover", "can't afford", "prior authorization",
            "high deductible", "out of pocket", "surprise bill",
            "out of network",
        ],
        "level_2_phrases": [
            "claim denied", "appeal denied", "prior authorization",
            "can't afford", "won't cover",
        ],
    },
    "ai_psychosis": {
        "search_terms": [
            "AI addiction",
            "ChatGPT obsession",
            "AI companion",
            "Character AI",
        ],
        "level_3_keywords": [
            "can't stop", "addicted", "lost touch with reality",
            "replacing human", "emotional dependency", "isolated",
            "obsessed", "lost friends", "mental health",
            "parasocial", "broke down crying",
        ],
        "level_3_phrases": [
            "can't stop talking to", "replaced my therapist",
            "only friend is AI", "lost touch with reality",
        ],
        "level_2_keywords": [
            "too much time", "distracted", "obsession", "hours a day",
            "compulsive", "dependent", "prefer AI", "relationship with AI",
        ],
        "level_2_phrases": [
            "spend hours", "can't stop using", "prefer talking to AI",
        ],
    },
    "subscription_overload": {
        "search_terms": [
            "subscription fatigue",
            "streaming costs",
            "too many subscriptions",
            "price increase",
        ],
        "level_3_keywords": [
            "can't afford", "cancelled everything", "going broke",
            "hundreds a month", "subscription trap", "debt",
            "overdraft", "can't keep up",
        ],
        "level_3_phrases": [
            "cancelled everything", "can't afford subscriptions",
            "hundreds a month on subscriptions",
        ],
        "level_2_keywords": [
            "too expensive", "price hike", "another increase",
            "nickel and dime", "cutting back", "cancelling",
            "not worth it", "frustrating",
        ],
        "level_2_phrases": [
            "price increase", "too many subscriptions",
            "cutting back on subscriptions",
        ],
    },
    "wage_stagnation": {
        "search_terms": [
            "paycheck to paycheck",
            "wages not keeping up",
            "can't afford rent salary",
            "working poor",
        ],
        "level_3_keywords": [
            "can't afford food", "starving", "homeless", "eviction",
            "two jobs", "three jobs", "can't survive", "going hungry",
            "food bank", "behind on rent", "utilities shut off",
        ],
        "level_3_phrases": [
            "working full time and homeless", "can't afford to eat",
            "two jobs and still broke", "behind on rent",
        ],
        "level_2_keywords": [
            "paycheck to paycheck", "barely surviving", "can't save",
            "no savings", "wages stagnant", "inflation",
            "not keeping up", "struggling", "can't get ahead",
        ],
        "level_2_phrases": [
            "paycheck to paycheck", "can't afford rent",
            "wages not keeping up", "working poor",
        ],
    },
    "housing_despair": {
        "search_terms": [
            "housing crisis",
            "can't afford home",
            "rent increase",
            "priced out housing",
        ],
        "level_3_keywords": [
            "homeless", "eviction", "living in car", "shelter",
            "priced out", "displaced", "can't afford anywhere",
            "nowhere to go", "sleeping on couch",
        ],
        "level_3_phrases": [
            "living in car", "facing eviction", "priced out of",
            "nowhere to live", "homeless",
        ],
        "level_2_keywords": [
            "can't afford", "rent increase", "housing crisis",
            "outbid", "can't buy", "saving impossible",
            "rent too high", "bidding war",
        ],
        "level_2_phrases": [
            "rent increase", "can't afford home", "housing crisis",
            "priced out",
        ],
    },
    "dating_app_despair": {
        "search_terms": [
            "dating app burnout",
            "swiping fatigue",
            "deleted dating apps",
            "dating app despair",
        ],
        "level_3_keywords": [
            "gave up", "hopeless", "never find anyone", "depressed",
            "lonely", "years of swiping", "suicidal", "unlovable",
            "completely alone", "self-worth destroyed",
        ],
        "level_3_phrases": [
            "gave up on dating", "lost all hope", "years of swiping nothing",
            "self-worth destroyed",
        ],
        "level_2_keywords": [
            "burnout", "exhausting", "frustrating", "waste of time",
            "deleted apps", "fatigue", "no matches", "ghosted",
            "toxic", "pay to play",
        ],
        "level_2_phrases": [
            "deleted dating apps", "swiping fatigue", "dating app burnout",
            "no matches",
        ],
    },
    "layoff_watch": {
        "search_terms": [
            "laid off",
            "tech layoffs 2025",
            "job search nightmare",
            "500 applications no response",
        ],
        "level_3_keywords": [
            "lost everything", "can't find work", "months unemployed",
            "depression", "family suffering", "running out of savings",
            "about to be homeless", "hundreds of applications",
            "500 applications",
        ],
        "level_3_phrases": [
            "months unemployed", "hundreds of applications no response",
            "running out of savings", "500 applications",
        ],
        "level_2_keywords": [
            "laid off", "layoffs", "job search", "no callbacks",
            "ghost", "ghosted by employer", "hiring freeze",
            "restructuring", "downsizing", "severance",
        ],
        "level_2_phrases": [
            "laid off", "tech layoffs", "job search nightmare",
            "no response", "ghosted",
        ],
    },
    "airline_chaos": {
        "search_terms": [
            "flight cancelled",
            "stranded airport",
            "airline nightmare",
            "flight delayed",
        ],
        "level_3_keywords": [
            "stranded for days", "missed funeral", "missed wedding",
            "lost all luggage", "no compensation", "no refund",
            "sleeping at airport", "stuck overnight", "abandoned",
            "medical emergency", "medication in luggage",
        ],
        "level_3_phrases": [
            "stranded", "missed funeral", "missed wedding",
            "sleeping at airport",
        ],
        "level_2_keywords": [
            "hours delayed", "cancelled twice", "rebooked multiple times",
            "missed connection", "lost luggage", "damaged luggage",
            "rude staff", "no help", "customer service terrible",
            "compensation denied",
        ],
        "level_2_phrases": [
            "delayed", "cancelled", "lost luggage", "missed connection",
        ],
    },
}


# ---------------------------------------------------------------------------
# API / categorization helpers
# ---------------------------------------------------------------------------

BLUESKY_SEARCH_URL = "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts"


def search_bluesky(query, limit=100):
    """Search Bluesky public API for posts matching a query."""
    params = {
        "q": query,
        "limit": limit,
        "sort": "top",
    }

    try:
        response = requests.get(BLUESKY_SEARCH_URL, params=params, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return data.get("posts", [])
        elif response.status_code == 429:
            print("    Rate limited, waiting 10s...")
            time.sleep(10)
            response = requests.get(BLUESKY_SEARCH_URL, params=params, timeout=15)
            if response.status_code == 200:
                data = response.json()
                return data.get("posts", [])
            print(f"    Still rate limited (HTTP {response.status_code})")
            return []
        else:
            print(f"    Error HTTP {response.status_code}")
            return []
    except Exception as e:
        print(f"    Exception: {e}")
        return []


def categorize_post(text, metric_cfg):
    """Categorize a post into Level 1/2/3 using the metric's keyword lists."""
    text_lower = text.lower()

    # Filter out clickbait / promo content
    if not filter_content(text_lower):
        return None

    # Level 3 check
    level_3_count = sum(
        1 for kw in metric_cfg["level_3_keywords"] if kw in text_lower
    )
    if level_3_count >= 2 or any(
        phrase in text_lower for phrase in metric_cfg["level_3_phrases"]
    ):
        return "LEVEL_3_CRISIS"

    # Level 2 check
    level_2_count = sum(
        1 for kw in metric_cfg["level_2_keywords"] if kw in text_lower
    )
    if level_2_count >= 2 or any(
        phrase in text_lower for phrase in metric_cfg["level_2_phrases"]
    ):
        return "LEVEL_2_STRUGGLING"

    return "LEVEL_1_AWARE"


# ---------------------------------------------------------------------------
# Per-metric collection
# ---------------------------------------------------------------------------

def collect_metric(metric_slug, metric_cfg):
    """Collect and categorize Bluesky posts for a single metric."""
    print(f"\n{'- ' * 35}")
    print(f"METRIC: {metric_slug}")
    print(f"{'- ' * 35}")

    all_posts = []
    seen_uris = set()

    for term in metric_cfg["search_terms"]:
        print(f"  Searching: '{term}'")
        raw_posts = search_bluesky(term, limit=100)
        new_count = 0

        for post in raw_posts:
            uri = post.get("uri", "")
            if uri in seen_uris:
                continue

            record = post.get("record", {})
            text = record.get("text", "")
            created_at = record.get("createdAt", "")
            author_handle = post.get("author", {}).get("handle", "")
            like_count = post.get("likeCount", 0)
            reply_count = post.get("replyCount", 0)
            repost_count = post.get("repostCount", 0)

            category = categorize_post(text, metric_cfg)
            if category is None:
                continue

            seen_uris.add(uri)
            new_count += 1

            all_posts.append({
                "uri": uri,
                "text": text[:300],
                "author_handle": author_handle,
                "like_count": like_count,
                "reply_count": reply_count,
                "repost_count": repost_count,
                "category": category,
                "created_at": created_at,
                "search_term": term,
                "metric": metric_slug,
            })

        print(f"    Found {new_count} new posts ({len(raw_posts)} raw)")
        time.sleep(1)  # polite delay between requests

    return all_posts


def write_csv(metric_slug, posts):
    """Write posts to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"collected-data/{metric_slug}_bluesky_{timestamp}.csv"

    fieldnames = [
        "uri", "text", "author_handle", "like_count", "reply_count",
        "repost_count", "category", "created_at", "search_term", "metric",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

    return filename


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("BLUESKY POST COLLECTOR - ALL ABSURDITY INDEX METRICS")
    print("=" * 70)
    print(f"\nUsing public AT Protocol API (no auth needed)")
    print(f"Metrics to collect: {len(METRICS)}")

    summary = {}

    for metric_slug, metric_cfg in METRICS.items():
        posts = collect_metric(metric_slug, metric_cfg)

        total = len(posts)
        if total == 0:
            print(f"\n  WARNING: No posts collected for {metric_slug}. "
                  "Skipping file write to preserve previous data.")
            summary[metric_slug] = {"total": 0, "file": None}
            continue

        filename = write_csv(metric_slug, posts)

        level_3 = len([p for p in posts if p["category"] == "LEVEL_3_CRISIS"])
        level_2 = len([p for p in posts if p["category"] == "LEVEL_2_STRUGGLING"])
        level_1 = len([p for p in posts if p["category"] == "LEVEL_1_AWARE"])

        print(f"\n  Saved {total} posts -> {filename}")
        print(f"    Level 3 (Crisis):      {level_3} ({level_3/total*100:.1f}%)")
        print(f"    Level 2 (Struggling):  {level_2} ({level_2/total*100:.1f}%)")
        print(f"    Level 1 (Aware):       {level_1} ({level_1/total*100:.1f}%)")

        summary[metric_slug] = {
            "total": total,
            "level_3": level_3,
            "level_2": level_2,
            "level_1": level_1,
            "file": filename,
        }

    # Final summary
    print(f"\n{'=' * 70}")
    print("COLLECTION SUMMARY")
    print(f"{'=' * 70}")

    grand_total = 0
    for slug, stats in summary.items():
        t = stats["total"]
        grand_total += t
        if t > 0:
            crisis_ratio = (stats["level_2"] + stats["level_3"]) / t * 100
            print(f"  {slug:<25} {t:>5} posts  "
                  f"(crisis ratio: {crisis_ratio:.1f}%)")
        else:
            print(f"  {slug:<25}     0 posts  (no data)")

    print(f"\n  Grand total: {grand_total} posts across {len(METRICS)} metrics")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
