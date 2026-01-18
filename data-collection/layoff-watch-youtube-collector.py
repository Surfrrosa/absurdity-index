#!/usr/bin/env python3
"""
Collect YouTube videos about layoffs and job search despair
Uses YouTube Data API v3 to search for layoff/unemployment content
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
    "laid off tech 2025",
    "job search nightmare",
    "hundreds of applications no response",
    "can't find job",
    "laid off and struggling",
    "unemployment running out",
    "job market is broken",
    "overqualified unemployed",
    "desperate for job",
    "laid off what now"
]

LAYOFF_REQUIRED_KEYWORDS = [
    'layoff', 'laid off', 'unemployed', 'unemployment', 'job search',
    'job hunting', 'applications', 'resume', 'interview', 'hired',
    'fired', 'terminated', 'job loss', 'career', 'work'
]

LEVEL_3_KEYWORDS = [
    'financial crisis', 'bankruptcy', 'losing home', 'eviction',
    "can't pay bills", 'savings gone', 'running out of money',
    'depressed', 'suicidal', 'hopeless', 'gave up',
    'mental health crisis', 'panic attacks', 'anxiety',
    'months unemployed', 'year unemployed', 'still no job'
]

LEVEL_2_KEYWORDS = [
    'hundreds of applications', '500 applications', '1000 applications',
    'no response', 'no callbacks', 'ghosted',
    'overqualified', 'entry level requires experience',
    'job search exhausting', 'burnt out', 'frustrated',
    'unemployment benefits', 'running out', 'losing hope',
    '6 months', 'several months', 'long time'
]

def is_layoff_related(title, description):
    text = (title + " " + description).lower()
    return any(keyword in text for keyword in LAYOFF_REQUIRED_KEYWORDS)

def categorize_video(title, description):
    if not is_layoff_related(title, description):
        return None

    # Filter out clickbait/promotional content
    if not filter_content(title, description):
        return None

    text = (title + " " + description).lower()

    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    if level_3_count >= 2 or any(phrase in text for phrase in [
        'financial crisis', 'bankruptcy', 'suicidal', 'hopeless',
        'months unemployed', 'year unemployed', 'savings gone'
    ]):
        return 'LEVEL_3_CRISIS'

    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    if level_2_count >= 2 or any(phrase in text for phrase in [
        'hundreds of applications', 'no response', 'ghosted',
        'overqualified', 'job search exhausting'
    ]):
        return 'LEVEL_2_STRUGGLING'

    return 'LEVEL_1_AWARE'

def search_youtube(query, max_results=10):
    if not YOUTUBE_API_KEY:
        print("ERROR: YOUTUBE_API_KEY not found")
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
            published_at = snippet.get('publishedAt', '')[:10]

            video_response = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            view_count = 0
            if video_response['items']:
                stats = video_response['items'][0]['statistics']
                view_count = int(stats.get('viewCount', 0))

            category = categorize_video(title, description)

            if category is None:
                continue

            text_lower = (title + " " + description).lower()
            found_level_3 = [kw for kw in LEVEL_3_KEYWORDS if kw in text_lower]
            found_level_2 = [kw for kw in LEVEL_2_KEYWORDS if kw in text_lower]
            found_keywords = found_level_3 + found_level_2

            videos.append({
                'search_term': query,
                'video_id': video_id,
                'url': f'https://www.youtube.com/watch?v={video_id}',
                'title': title,
                'description_snippet': description[:200],
                'published_date': published_at,
                'view_count': view_count,
                'crisis_keywords': ', '.join(found_keywords[:5]),
                'category': category
            })

        print(f"  ✓ Found {len(videos)} videos for '{query}'")
        return videos

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return []

def main():
    print("=" * 70)
    print("LAYOFF WATCH YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []

    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=10)
        all_videos.extend(videos)

    df = pd.DataFrame(all_videos)
    df_unique = df.drop_duplicates(subset=['video_id'])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'data-collection/collected-data/layoff_watch_youtube_{timestamp}.csv'
    df_unique.to_csv(output_file, index=False)

    print("\n" + "=" * 70)
    print(f"RESULTS SAVED: {output_file}")
    print("=" * 70)
    print(f"\nUnique videos: {len(df_unique)}")

    if len(df_unique) > 0:
        print(f"\nBreakdown:")
        print(df_unique['category'].value_counts())

        total = len(df_unique)
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        print(f"\nCrisis ratio: {level_3/total*100:.1f}%")

if __name__ == '__main__':
    main()
