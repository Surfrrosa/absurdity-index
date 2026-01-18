#!/usr/bin/env python3
"""
YouTube TikTok Compilation Collector for the Absurdity Index.

The sneaky approach: TikTok content frequently gets re-uploaded to YouTube
as compilations. This collector specifically targets those videos, effectively
capturing viral TikTok content through YouTube's accessible API.

Requires: YOUTUBE_API_KEY environment variable

Usage:
    python tiktok-youtube-collector.py
"""

import os
import csv
import math
from datetime import datetime
from content_filters import filter_content

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("ERROR: google-api-python-client not installed.")
    print("Run: pip install google-api-python-client")
    exit(1)

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

API_KEY = os.environ.get('YOUTUBE_API_KEY')

if not API_KEY:
    print("ERROR: YOUTUBE_API_KEY environment variable not set")
    exit(1)

# TikTok compilation search queries by metric
# These queries specifically target TikTok content on YouTube
TIKTOK_QUERIES = {
    'healthcare': [
        'tiktok compilation insurance denied',
        'tiktok healthcare nightmare',
        'tiktok medical bill shock',
        'viral tiktok hospital bill',
        'tiktok prior authorization denied',
        'tiktok american healthcare',
    ],
    'ai_psychosis': [
        'tiktok replika ai',
        'tiktok character ai addiction',
        'tiktok ai boyfriend girlfriend',
        'viral tiktok chatgpt',
        'tiktok ai companion',
        'tiktok fell in love with ai',
    ],
    'subscription_overload': [
        'tiktok cancel subscriptions',
        'tiktok too many streaming services',
        'viral tiktok subscription prices',
        'tiktok streaming fatigue',
    ],
    'wage_stagnation': [
        'tiktok paycheck to paycheck',
        'tiktok cant afford',
        'viral tiktok minimum wage',
        'tiktok side hustle culture',
        'tiktok working poor',
        'tiktok cost of living',
    ],
    'housing_despair': [
        'tiktok housing crisis',
        'tiktok cant afford rent',
        'viral tiktok apartment prices',
        'tiktok first time home buyer',
        'tiktok priced out',
        'tiktok rent too high',
    ],
    'dating_app_despair': [
        'tiktok dating apps',
        'tiktok hinge bumble tinder',
        'viral tiktok modern dating',
        'tiktok dating is hard',
        'tiktok ghosted',
        'tiktok dating app fatigue',
    ],
    'layoff_watch': [
        'tiktok laid off',
        'tiktok tech layoffs',
        'viral tiktok fired',
        'tiktok job search nightmare',
        'tiktok unemployment',
        'tiktok layoff day',
    ],
    'airline_chaos': [
        'tiktok flight cancelled',
        'tiktok airline nightmare',
        'viral tiktok lost luggage',
        'tiktok airport chaos',
        'tiktok worst airline',
        'tiktok flight delayed',
    ]
}

# Keywords for severity categorization
LEVEL_3_KEYWORDS = [
    'destroyed', 'ruined', 'nightmare', 'horror', 'worst', 'crisis',
    'cant afford', "can't afford", 'homeless', 'bankrupt', 'died',
    'depressed', 'anxiety', 'panic', 'trauma', 'addicted', 'crying',
    'broke down', 'mental health', 'viral', 'insane', 'unbelievable'
]

LEVEL_2_KEYWORDS = [
    'struggle', 'frustrated', 'angry', 'unfair', 'ridiculous',
    'expensive', 'stress', 'worried', 'scared', 'difficult', 'hard',
    'reaction', 'shocked', 'wow', 'crazy'
]


def categorize_content(text, description=''):
    """Categorize content by severity level."""
    # Filter out clickbait/promotional content
    if not filter_content(text, description):
        return None

    text_lower = text.lower()

    for keyword in LEVEL_3_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_3_CRISIS'

    for keyword in LEVEL_2_KEYWORDS:
        if keyword in text_lower:
            return 'LEVEL_2_FRUSTRATED'

    return 'LEVEL_1_CASUAL'


def calculate_engagement_score(views, likes, comments):
    """Calculate engagement-weighted score using log scale."""
    if views == 0:
        return 0
    engagement_rate = (likes + comments * 2) / views
    view_weight = math.log10(max(views, 1))
    return round(engagement_rate * view_weight * 100, 2)


def search_tiktok_compilations(youtube, query, max_results=15):
    """Search YouTube for TikTok compilation videos."""
    try:
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            maxResults=max_results,
            type='video',
            order='relevance',
            relevanceLanguage='en',
            regionCode='US',
            publishedAfter='2024-01-01T00:00:00Z',  # Recent content only
        ).execute()

        video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

        if not video_ids:
            return []

        # Get detailed video stats
        videos_response = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids)
        ).execute()

        return videos_response.get('items', [])

    except HttpError as e:
        if e.resp.status == 403:
            print(f"    API quota exceeded")
        else:
            print(f"    HTTP Error: {e}")
        return []
    except Exception as e:
        print(f"    Error: {e}")
        return []


def collect_metric_tiktoks(youtube, metric_name, queries):
    """Collect TikTok compilation videos for a metric."""
    print(f"\n{'='*60}")
    print(f"Collecting TikTok compilations: {metric_name.upper().replace('_', ' ')}")
    print(f"{'='*60}")

    all_videos = []
    seen_ids = set()

    for query in queries:
        print(f"\n  Searching: '{query}'")

        videos = search_tiktok_compilations(youtube, query)

        new_count = 0
        for video in videos:
            video_id = video['id']

            if video_id in seen_ids:
                continue

            seen_ids.add(video_id)

            snippet = video['snippet']
            stats = video.get('statistics', {})

            title = snippet.get('title', '')
            description = snippet.get('description', '')[:500]
            channel = snippet.get('channelTitle', '')

            views = int(stats.get('viewCount', 0))
            likes = int(stats.get('likeCount', 0))
            comments = int(stats.get('commentCount', 0))

            full_text = f"{title} {description}"
            category = categorize_content(title, description)

            # Skip filtered content (clickbait/spam)
            if category is None:
                continue

            engagement = calculate_engagement_score(views, likes, comments)

            all_videos.append({
                'metric': metric_name,
                'video_id': video_id,
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'title': title[:200],
                'channel': channel,
                'description': description,
                'views': views,
                'likes': likes,
                'comments': comments,
                'engagement_score': engagement,
                'category': category,
                'published': snippet.get('publishedAt', '')[:10],
                'collected_date': datetime.now().strftime('%Y-%m-%d'),
                'source': 'youtube_tiktok_compilation'
            })
            new_count += 1

        print(f"    Found {new_count} new videos")

    return all_videos


def main():
    print("=" * 80)
    print("YOUTUBE TIKTOK COMPILATION COLLECTOR")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print("\nStrategy: Find TikTok content via YouTube compilation videos")

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    all_results = []

    for metric_name, queries in TIKTOK_QUERIES.items():
        videos = collect_metric_tiktoks(youtube, metric_name, queries)
        all_results.extend(videos)

        # Stats for this metric
        if videos:
            l3 = sum(1 for v in videos if v['category'] == 'LEVEL_3_CRISIS')
            l2 = sum(1 for v in videos if v['category'] == 'LEVEL_2_FRUSTRATED')
            l1 = sum(1 for v in videos if v['category'] == 'LEVEL_1_CASUAL')
            total_views = sum(v['views'] for v in videos)
            print(f"\n  Total: {len(videos)} | Views: {total_views:,} | L1: {l1}, L2: {l2}, L3: {l3}")

    # Deduplicate - same video can appear in multiple metric searches
    if all_results:
        seen_ids = set()
        deduplicated = []
        for video in all_results:
            if video['video_id'] not in seen_ids:
                seen_ids.add(video['video_id'])
                deduplicated.append(video)

        duplicates_removed = len(all_results) - len(deduplicated)
        if duplicates_removed > 0:
            print(f"\n  Removed {duplicates_removed} cross-metric duplicates")

        all_results = deduplicated

    # Save results
    if all_results:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'collected-data/tiktok_youtube_{timestamp}.csv'

        fieldnames = ['metric', 'video_id', 'url', 'title', 'channel', 'description',
                      'views', 'likes', 'comments', 'engagement_score', 'category',
                      'published', 'collected_date', 'source']

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_results)

        print(f"\n{'='*80}")
        print("COLLECTION COMPLETE")
        print(f"{'='*80}")
        print(f"Total TikTok compilation videos: {len(all_results)}")
        print(f"Saved to: {output_file}")

        # Summary by metric
        print(f"\n{'='*80}")
        print("BY METRIC")
        print(f"{'='*80}")
        for metric in TIKTOK_QUERIES.keys():
            count = sum(1 for r in all_results if r['metric'] == metric)
            views = sum(r['views'] for r in all_results if r['metric'] == metric)
            print(f"  {metric.replace('_', ' ').title():25} {count:3} videos ({views:,} views)")

        # Overall level distribution
        print(f"\n{'='*80}")
        print("SEVERITY DISTRIBUTION")
        print(f"{'='*80}")
        l1 = sum(1 for r in all_results if r['category'] == 'LEVEL_1_CASUAL')
        l2 = sum(1 for r in all_results if r['category'] == 'LEVEL_2_FRUSTRATED')
        l3 = sum(1 for r in all_results if r['category'] == 'LEVEL_3_CRISIS')
        total = len(all_results)
        print(f"  Level 1 (Casual):     {l1:3} ({l1/total*100:.1f}%)")
        print(f"  Level 2 (Frustrated): {l2:3} ({l2/total*100:.1f}%)")
        print(f"  Level 3 (Crisis):     {l3:3} ({l3/total*100:.1f}%)")
    else:
        print("\nNo videos collected. API quota may be exceeded.")


if __name__ == '__main__':
    main()
