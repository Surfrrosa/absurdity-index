#!/usr/bin/env python3
"""
Collect YouTube videos about dating app frustration and burnout
Uses YouTube Data API v3 to search for dating app despair content
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

SEARCH_TERMS = [
    "quit dating apps",
    "dating app burnout",
    "dating apps ruined dating",
    "gave up on dating apps",
    "dating app fatigue",
    "modern dating is broken",
    "dating apps waste of time",
    "no matches dating apps",
    "ghosted dating apps",
    "dating app depression"
]

DATING_REQUIRED_KEYWORDS = [
    'dating', 'dating app', 'tinder', 'hinge', 'bumble', 'match',
    'online dating', 'swipe', 'swiping', 'relationship', 'single'
]

LEVEL_3_KEYWORDS = [
    'quit', 'gave up', 'given up', 'hopeless', 'will never find',
    'mental health', 'depression', 'anxiety', 'suicidal thoughts',
    'self esteem destroyed', 'confidence destroyed', 'broken',
    'therapy', 'emotional damage', 'trauma'
]

LEVEL_2_KEYWORDS = [
    'burnt out', 'burnout', 'exhausted', 'frustrated', 'waste of time',
    'no matches', 'ghosted', 'breadcrumbing', 'situationship',
    'endless swiping', 'algorithm rigged', 'pay to win',
    'considering quitting', 'taking break', 'pause'
]

def is_dating_related(title, description):
    text = (title + " " + description).lower()
    return any(keyword in text for keyword in DATING_REQUIRED_KEYWORDS)

def categorize_video(title, description):
    if not is_dating_related(title, description):
        return None

    text = (title + " " + description).lower()

    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    if level_3_count >= 2 or any(phrase in text for phrase in [
        'gave up', 'quit', 'hopeless', 'mental health', 'depression'
    ]):
        return 'LEVEL_3_CRISIS'

    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    if level_2_count >= 2 or any(phrase in text for phrase in [
        'burnt out', 'exhausted', 'frustrated', 'ghosted'
    ]):
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
    print("DATING APP DESPAIR YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []
    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=12)
        all_videos.extend(videos)

    df = pd.DataFrame(all_videos)
    df_unique = df.drop_duplicates(subset=['video_id'])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'data-collection/collected-data/dating_app_despair_youtube_{timestamp}.csv'
    df_unique.to_csv(output_file, index=False)

    print(f"\n{'=' * 70}")
    print(f"RESULTS: {len(df_unique)} unique videos")
    print(df_unique['category'].value_counts())

    total = len(df_unique)
    if total > 0:
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        print(f"\nCrisis ratio: {level_3/total*100:.1f}%")

if __name__ == '__main__':
    main()
