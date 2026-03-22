#!/usr/bin/env python3
"""
Shared collection logic for Reddit metric collectors.

Each per-metric collector defines its own constants (subreddits, search terms,
keywords, phrases) and calls run_collection() from this module.

Uses reddit_client.py for OAuth2-authenticated search (works from CI).
"""

import csv
import sys
import time
from datetime import datetime
from reddit_client import search_subreddit, is_authenticated


def categorize_post(title, selftext, level_3_keywords, level_2_keywords,
                    level_3_phrases, level_2_phrases):
    """Categorize a post into Level 1/2/3 based on keyword/phrase matching."""
    text = (title + " " + selftext).lower()

    level_3_count = sum(1 for kw in level_3_keywords if kw in text)
    if level_3_count >= 2 or any(p in text for p in level_3_phrases):
        return "LEVEL_3_CRISIS"

    level_2_count = sum(1 for kw in level_2_keywords if kw in text)
    if level_2_count >= 2 or any(p in text for p in level_2_phrases):
        return "LEVEL_2_STRUGGLING"

    return "LEVEL_1_AWARE"


def collect_from_subreddit(subreddit, search_terms, level_3_keywords,
                           level_2_keywords, level_3_phrases, level_2_phrases,
                           posts_per_term=10):
    """Collect and categorize posts from a single subreddit."""
    print(f"\n  Collecting from r/{subreddit}")

    all_posts = []
    seen_ids = set()

    for term in search_terms:
        print(f"    Searching: '{term}'")
        posts = search_subreddit(subreddit, term, limit=posts_per_term)

        for post_data in posts:
            post = post_data["data"]
            post_id = post["id"]

            if post_id in seen_ids:
                continue
            seen_ids.add(post_id)

            title = post.get("title", "")
            selftext = post.get("selftext", "")
            url = f"https://www.reddit.com{post.get('permalink', '')}"
            score = post.get("score", 0)
            num_comments = post.get("num_comments", 0)
            created_utc = post.get("created_utc", 0)
            author = post.get("author", "[deleted]")

            date = datetime.fromtimestamp(created_utc).strftime("%Y-%m-%d")

            category = categorize_post(
                title, selftext,
                level_3_keywords, level_2_keywords,
                level_3_phrases, level_2_phrases,
            )

            tag = "L3" if "CRISIS" in category else "L2" if "STRUGGLING" in category else "L1"
            print(f"      [{tag}] {title[:60]}...")

            all_posts.append({
                "subreddit": subreddit,
                "post_id": post_id,
                "title": title,
                "selftext_snippet": selftext[:300] if selftext else "",
                "url": url,
                "score": score,
                "num_comments": num_comments,
                "author": author,
                "created_date": date,
                "search_term": term,
                "category": category,
            })

        time.sleep(2)

    print(f"    Collected {len(all_posts)} unique posts from r/{subreddit}")
    return all_posts


def run_collection(metric_slug, banner, subreddits, search_terms,
                   level_3_keywords, level_2_keywords,
                   level_3_phrases, level_2_phrases):
    """Run the full collection pipeline for a single metric."""
    print("=" * 70)
    print(f"REDDIT {banner} (OAuth2)")
    print("=" * 70)

    if not is_authenticated():
        print("\nFATAL: Cannot authenticate with Reddit. Exiting.")
        print("  Set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET env vars.")
        sys.exit(1)

    print(f"\nCollecting from {len(subreddits)} subreddits:")
    for sub in subreddits:
        print(f"  - r/{sub}")
    print(f"Using {len(search_terms)} search terms")

    all_posts = []

    for subreddit in subreddits:
        posts = collect_from_subreddit(
            subreddit, search_terms,
            level_3_keywords, level_2_keywords,
            level_3_phrases, level_2_phrases,
        )
        all_posts.extend(posts)
        time.sleep(3)

    # Deduplicate
    unique = {}
    for post in all_posts:
        unique[post["post_id"]] = post
    all_posts = list(unique.values())

    total = len(all_posts)
    level_3 = len([p for p in all_posts if p["category"] == "LEVEL_3_CRISIS"])
    level_2 = len([p for p in all_posts if p["category"] == "LEVEL_2_STRUGGLING"])
    level_1 = len([p for p in all_posts if p["category"] == "LEVEL_1_AWARE"])

    print(f"\n{'=' * 70}")
    print("COLLECTION COMPLETE")
    print(f"{'=' * 70}")
    print(f"\nTotal unique posts: {total}")
    if total > 0:
        print(f"  Level 3 (Crisis):      {level_3} ({level_3/total*100:.1f}%)")
        print(f"  Level 2 (Struggling):  {level_2} ({level_2/total*100:.1f}%)")
        print(f"  Level 1 (Aware):       {level_1} ({level_1/total*100:.1f}%)")
        crisis_ratio = (level_2 + level_3) / total * 100
        print(f"  Crisis ratio (L2+L3):  {crisis_ratio:.1f}%")
    else:
        print("  No posts collected. Reddit may be blocking requests.")

    if total == 0:
        print("\nWARNING: Skipping file write to preserve previous data.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"collected-data/{metric_slug}_reddit_{timestamp}.csv"

    fieldnames = [
        "subreddit", "post_id", "title", "selftext_snippet",
        "url", "score", "num_comments", "author", "created_date",
        "search_term", "category",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_posts)

    print(f"\nData saved to: {filename}")
    print("=" * 70)
