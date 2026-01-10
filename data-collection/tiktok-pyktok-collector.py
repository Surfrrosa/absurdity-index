#!/usr/bin/env python3
"""
TikTok collector using pyktok - the nuclear option.

pyktok uses Playwright (browser automation) to bypass TikTok's JavaScript
rendering and anti-scraping measures. This is the most reliable method
but requires additional setup.

Install:
    pip install pyktok
    playwright install  # Downloads browser binaries

Usage:
    python tiktok-pyktok-collector.py
    python tiktok-pyktok-collector.py --hashtag techlayoffs
    python tiktok-pyktok-collector.py --metric healthcare
"""

import os
import sys
import csv
import time
import argparse
from datetime import datetime

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

try:
    import pyktok as pyk
    PYKTOK_AVAILABLE = True
except ImportError:
    PYKTOK_AVAILABLE = False
    print("=" * 60)
    print("pyktok not installed!")
    print("=" * 60)
    print()
    print("To install:")
    print("  pip install pyktok")
    print("  playwright install")
    print()
    print("pyktok uses browser automation to bypass TikTok's")
    print("JavaScript rendering and anti-scraping measures.")
    print()

# Hashtags by metric
METRIC_HASHTAGS = {
    'healthcare': [
        'insurancedenied', 'healthcarenightmare', 'medicaldebt',
        'priorauthorization', 'americanhealthcare'
    ],
    'ai_psychosis': [
        'replika', 'characterai', 'aiboyfriend', 'aigirlfriend', 'aicompanion'
    ],
    'subscription_overload': [
        'subscriptionfatigue', 'cancelsubscriptions', 'streamingwars'
    ],
    'wage_stagnation': [
        'paychecktopaycheck', 'workingpoor', 'costoflivingcrisis', 'sidehustle'
    ],
    'housing_despair': [
        'housingcrisis', 'cantaffordrent', 'rentcrisis', 'pricedout'
    ],
    'dating_app_despair': [
        'datingapps', 'datingishard', 'moderndating', 'ghosted'
    ],
    'layoff_watch': [
        'techlayoffs', 'laidoff', 'layoffs2025', 'firedtiktok'
    ],
    'airline_chaos': [
        'flightcancelled', 'airlinenightmare', 'lostluggage', 'airportchaos'
    ]
}

# Severity keywords
LEVEL_3_KEYWORDS = [
    'destroyed', 'ruined', 'nightmare', 'horror', 'worst', 'crisis',
    'cant afford', "can't afford", 'homeless', 'bankrupt', 'died',
    'depressed', 'anxiety', 'panic', 'trauma', 'addicted', 'crying'
]

LEVEL_2_KEYWORDS = [
    'struggle', 'frustrated', 'angry', 'unfair', 'ridiculous',
    'expensive', 'stress', 'worried', 'scared', 'difficult', 'hard'
]


def categorize_content(text):
    """Categorize by severity level."""
    text_lower = text.lower() if text else ''

    for keyword in LEVEL_3_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_3_CRISIS'

    for keyword in LEVEL_2_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_2_FRUSTRATED'

    return 'LEVEL_1_CASUAL'


def collect_hashtag(hashtag, n_videos=30, metric_name='unknown'):
    """Collect videos from a single hashtag using pyktok."""
    print(f"\n  #{hashtag} (target: {n_videos} videos)...")

    try:
        # pyktok saves to a JSON file, then we parse it
        pyk.specify_browser('chrome')

        # Get hashtag videos
        pyk.hashtag_videos(
            hashtag,
            n_videos,
            'headless'  # Run browser in headless mode
        )

        # pyktok saves to hashtag_videos_<hashtag>.json
        json_file = f'hashtag_videos_{hashtag}.json'

        if os.path.exists(json_file):
            import json
            with open(json_file, 'r') as f:
                data = json.load(f)

            videos = []
            for item in data:
                desc = item.get('desc', '') or item.get('video_description', '')
                author = item.get('author', {})
                stats = item.get('stats', {})

                videos.append({
                    'metric': metric_name,
                    'hashtag': hashtag,
                    'video_id': item.get('id', ''),
                    'url': f"https://www.tiktok.com/@{author.get('uniqueId', 'unknown')}/video/{item.get('id', '')}",
                    'description': desc[:300] if desc else '',
                    'author': author.get('uniqueId', ''),
                    'author_name': author.get('nickname', ''),
                    'views': stats.get('playCount', 0),
                    'likes': stats.get('diggCount', 0),
                    'comments': stats.get('commentCount', 0),
                    'shares': stats.get('shareCount', 0),
                    'category': categorize_content(desc),
                    'collected_date': datetime.now().strftime('%Y-%m-%d'),
                    'source': 'pyktok'
                })

            # Clean up JSON file
            os.remove(json_file)

            print(f"    Collected {len(videos)} videos")
            return videos
        else:
            print(f"    No output file generated")
            return []

    except Exception as e:
        print(f"    Error: {e}")
        return []


def collect_metric(metric_name, hashtags, videos_per_hashtag=20):
    """Collect videos for a single metric."""
    print(f"\n{'='*60}")
    print(f"Collecting: {metric_name.upper().replace('_', ' ')}")
    print(f"{'='*60}")

    all_videos = []
    seen_ids = set()

    for hashtag in hashtags:
        videos = collect_hashtag(hashtag, videos_per_hashtag, metric_name)

        for video in videos:
            if video['video_id'] and video['video_id'] not in seen_ids:
                seen_ids.add(video['video_id'])
                all_videos.append(video)

        # Pause between hashtags
        time.sleep(2)

    return all_videos


def main():
    parser = argparse.ArgumentParser(description='TikTok collector using pyktok')
    parser.add_argument('--hashtag', help='Collect single hashtag')
    parser.add_argument('--metric', help='Collect single metric')
    parser.add_argument('--videos', type=int, default=20, help='Videos per hashtag')
    args = parser.parse_args()

    if not PYKTOK_AVAILABLE:
        sys.exit(1)

    print("=" * 80)
    print("TIKTOK COLLECTION (pyktok - browser automation)")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    all_results = []

    if args.hashtag:
        # Single hashtag mode
        videos = collect_hashtag(args.hashtag, args.videos, 'manual')
        all_results.extend(videos)

    elif args.metric:
        # Single metric mode
        if args.metric in METRIC_HASHTAGS:
            videos = collect_metric(args.metric, METRIC_HASHTAGS[args.metric], args.videos)
            all_results.extend(videos)
        else:
            print(f"Unknown metric: {args.metric}")
            print(f"Available: {', '.join(METRIC_HASHTAGS.keys())}")
            sys.exit(1)

    else:
        # Full collection
        for metric_name, hashtags in METRIC_HASHTAGS.items():
            videos = collect_metric(metric_name, hashtags, args.videos)
            all_results.extend(videos)

            # Stats
            if videos:
                l3 = sum(1 for v in videos if v['category'] == 'LEVEL_3_CRISIS')
                l2 = sum(1 for v in videos if v['category'] == 'LEVEL_2_FRUSTRATED')
                l1 = sum(1 for v in videos if v['category'] == 'LEVEL_1_CASUAL')
                total_views = sum(v.get('views', 0) for v in videos)
                print(f"\n  Total: {len(videos)} | Views: {total_views:,}")
                print(f"  Distribution: L1={l1}, L2={l2}, L3={l3}")

            # Pause between metrics
            time.sleep(5)

    # Save results
    if all_results:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'collected-data/tiktok_pyktok_{timestamp}.csv'

        fieldnames = ['metric', 'hashtag', 'video_id', 'url', 'description',
                      'author', 'author_name', 'views', 'likes', 'comments',
                      'shares', 'category', 'collected_date', 'source']

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_results)

        print(f"\n{'='*80}")
        print("COLLECTION COMPLETE")
        print(f"{'='*80}")
        print(f"Total videos: {len(all_results)}")
        print(f"Saved to: {output_file}")

        # Level distribution
        l1 = sum(1 for r in all_results if r['category'] == 'LEVEL_1_CASUAL')
        l2 = sum(1 for r in all_results if r['category'] == 'LEVEL_2_FRUSTRATED')
        l3 = sum(1 for r in all_results if r['category'] == 'LEVEL_3_CRISIS')
        total = len(all_results)

        print(f"\nSeverity Distribution:")
        print(f"  Level 1: {l1} ({l1/total*100:.1f}%)")
        print(f"  Level 2: {l2} ({l2/total*100:.1f}%)")
        print(f"  Level 3: {l3} ({l3/total*100:.1f}%)")
    else:
        print("\nNo videos collected.")


if __name__ == '__main__':
    main()
