#!/usr/bin/env python3
"""
Collect YouTube videos about airline chaos and travel nightmares
Uses YouTube Data API v3
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
from content_filters import filter_content

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

SEARCH_TERMS = [
    "flight cancelled nightmare",
    "stranded at airport",
    "airline lost luggage",
    "flight delay horror story",
    "airline customer service nightmare",
    "stuck at airport overnight",
    "missed connection airline",
    "airline ruined vacation",
    "flight cancelled no refund",
    "airline travel disaster 2025"
]

AIRLINE_REQUIRED_KEYWORDS = [
    'flight', 'airline', 'airport', 'plane', 'travel', 'flying',
    'cancelled', 'delayed', 'luggage', 'baggage', 'passenger'
]

LEVEL_3_KEYWORDS = [
    'stranded for days', 'missed funeral', 'missed wedding',
    'lost all luggage', 'no compensation', 'no refund',
    'sleeping at airport', 'stuck overnight', 'abandoned',
    'medical emergency', 'medication in luggage', 'wheelchair',
    'ruined vacation', 'lost money', 'thousands of dollars'
]

LEVEL_2_KEYWORDS = [
    'hours delayed', 'cancelled twice', 'rebookedmultiple times',
    'missed connection', 'lost luggage', 'damaged luggage',
    'rude staff', 'no help', 'customer service terrible',
    'long wait', 'compensation denied'
]

def is_airline_related(title, description):
    text = (title + " " + description).lower()
    return any(keyword in text for keyword in AIRLINE_REQUIRED_KEYWORDS)

def categorize_video(title, description):
    if not is_airline_related(title, description):
        return None

    # Filter out clickbait/promotional content
    if not filter_content(title, description):
        return None

    text = (title + " " + description).lower()

    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    if level_3_count >= 2 or any(phrase in text for phrase in [
        'stranded', 'missed funeral', 'missed wedding', 'sleeping at airport'
    ]):
        return 'LEVEL_3_CRISIS'

    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    if level_2_count >= 2 or 'delayed' in text or 'cancelled' in text:
        return 'LEVEL_2_FRUSTRATED'

    return 'LEVEL_1_AWARE'

def search_youtube(query, max_results=10):
    if not YOUTUBE_API_KEY:
        return []

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        ninety_days_ago = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')

        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results,
            order='relevance',
            regionCode='US',
            publishedAfter=ninety_days_ago
        ).execute()

        videos = []
        for item in search_response.get('items', []):
            video_id = item['id']['videoId']
            snippet = item['snippet']

            title = snippet.get('title', '')
            description = snippet.get('description', '')

            category = categorize_video(title, description)
            if category is None:
                continue

            videos.append({
                'search_term': query,
                'video_id': video_id,
                'url': f'https://www.youtube.com/watch?v={video_id}',
                'title': title,
                'category': category
            })

        print(f"  ✓ Found {len(videos)} videos for '{query}'")
        return videos

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return []

def main():
    print("=" * 70)
    print("AIRLINE CHAOS YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []
    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=10)
        all_videos.extend(videos)

    df = pd.DataFrame(all_videos)
    df_unique = df.drop_duplicates(subset=['video_id'])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'collected-data/airline_chaos_youtube_{timestamp}.csv'
    df_unique.to_csv(output_file, index=False)

    print(f"\n{'=' * 70}")
    print(f"RESULTS: {len(df_unique)} unique videos")
    if len(df_unique) > 0:
        print(df_unique['category'].value_counts())

        total = len(df_unique)
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        print(f"\nCrisis ratio: {level_3/total*100:.1f}%")

if __name__ == '__main__':
    main()
