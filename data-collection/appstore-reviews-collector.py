#!/usr/bin/env python3
"""
App Store reviews collector for the Absurdity Index.
Uses Apple's public iTunes RSS feed to collect app reviews.

No API key required - uses public RSS endpoints.

Usage:
    python appstore-reviews-collector.py
"""

import os
import json
import time
import csv
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# AI companion apps to track (App Store IDs)
AI_APPS = {
    'Replika': '1158555867',
    'Character.AI': '1631797909',
    'Chai': '1544750895',
    'Anima': '1501283629',
    'Paradot': '6447293657',
    'Talkie': '6446665746',
}

# Keywords for severity categorization
LEVEL_3_KEYWORDS = [
    'addicted', 'addiction', 'cant stop', "can't stop", 'obsessed',
    'ruined my life', 'destroyed', 'mental health', 'depressed',
    'lonely', 'only friend', 'replaced', 'prefer ai', 'real relationships'
]

LEVEL_2_KEYWORDS = [
    'attached', 'emotional', 'feelings', 'love', 'relationship',
    'companion', 'talk every day', 'hours', 'dependent', 'need'
]


def categorize_review(text):
    """Categorize review by severity level."""
    text_lower = text.lower()

    for keyword in LEVEL_3_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_3_CRISIS'

    for keyword in LEVEL_2_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_2_DEPENDENT'

    return 'LEVEL_1_CASUAL'


def fetch_reviews(app_id, app_name, country='us', page=1):
    """Fetch reviews from iTunes RSS feed."""
    url = f'https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby=mostrecent/json'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    try:
        req = Request(url, headers=headers)
        response = urlopen(req, timeout=30)
        data = json.loads(response.read().decode('utf-8'))

        entries = data.get('feed', {}).get('entry', [])

        # First entry is app info, rest are reviews
        if entries and len(entries) > 1:
            return entries[1:]  # Skip first entry (app metadata)
        return []

    except HTTPError as e:
        print(f"    HTTP Error {e.code}: {url}")
        return []
    except URLError as e:
        print(f"    URL Error: {e.reason}")
        return []
    except json.JSONDecodeError:
        print(f"    JSON decode error")
        return []
    except Exception as e:
        print(f"    Error: {e}")
        return []


def collect_app_reviews(app_name, app_id, max_pages=10):
    """Collect reviews for a single app."""
    print(f"\n  Collecting reviews for {app_name} (ID: {app_id})...")

    all_reviews = []

    for page in range(1, max_pages + 1):
        reviews = fetch_reviews(app_id, app_name, page=page)

        if not reviews:
            break

        for review in reviews:
            try:
                title = review.get('title', {}).get('label', '')
                content = review.get('content', {}).get('label', '')
                rating = review.get('im:rating', {}).get('label', '0')
                author = review.get('author', {}).get('name', {}).get('label', 'Anonymous')
                review_id = review.get('id', {}).get('label', '')

                full_text = f"{title} {content}"
                category = categorize_review(full_text)

                all_reviews.append({
                    'app_name': app_name,
                    'app_id': app_id,
                    'review_id': review_id,
                    'title': title[:200] if title else '',
                    'content': content[:500] if content else '',
                    'rating': rating,
                    'author': author,
                    'category': category,
                    'collected_date': datetime.now().strftime('%Y-%m-%d')
                })

            except Exception as e:
                continue

        print(f"    Page {page}: {len(reviews)} reviews")
        time.sleep(1)  # Rate limiting

    return all_reviews


def main():
    print("=" * 80)
    print("APP STORE REVIEWS COLLECTION (AI Companion Apps)")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    all_reviews = []
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}

    for app_name, app_id in AI_APPS.items():
        reviews = collect_app_reviews(app_name, app_id)
        all_reviews.extend(reviews)

        # Count levels for this app
        app_l1 = sum(1 for r in reviews if 'LEVEL_1' in r['category'])
        app_l2 = sum(1 for r in reviews if 'LEVEL_2' in r['category'])
        app_l3 = sum(1 for r in reviews if 'LEVEL_3' in r['category'])

        print(f"    Total: {len(reviews)} | L1: {app_l1}, L2: {app_l2}, L3: {app_l3}")

        level_counts['L1'] += app_l1
        level_counts['L2'] += app_l2
        level_counts['L3'] += app_l3

        time.sleep(2)  # Pause between apps

    # Save results
    if all_reviews:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'collected-data/appstore_ai_reviews_{timestamp}.csv'

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=all_reviews[0].keys())
            writer.writeheader()
            writer.writerows(all_reviews)

        total = len(all_reviews)
        crisis_ratio = ((level_counts['L2'] + level_counts['L3']) / total * 100) if total > 0 else 0

        print(f"\n{'='*80}")
        print("COLLECTION COMPLETE")
        print(f"{'='*80}")
        print(f"Total reviews: {total}")
        print(f"Distribution: L1={level_counts['L1']}, L2={level_counts['L2']}, L3={level_counts['L3']}")
        print(f"Crisis ratio: {crisis_ratio:.1f}%")
        print(f"Saved to: {output_file}")
    else:
        print("\nNo reviews collected!")


if __name__ == '__main__':
    main()
