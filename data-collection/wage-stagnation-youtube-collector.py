#!/usr/bin/env python3
"""
Collect YouTube videos about wage stagnation and financial stress
Uses YouTube Data API v3 to search for wage/income crisis content
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
from content_filters import filter_content

# Load environment variables
load_dotenv()

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Search terms for wage stagnation
SEARCH_TERMS = [
    "can't afford rent on salary",
    "paycheck to paycheck",
    "living paycheck to paycheck",
    "wages not keeping up inflation",
    "can't make ends meet",
    "working poor",
    "poverty wages",
    "minimum wage not enough",
    "second job to survive",
    "multiple jobs still broke"
]

# Core wage/income keywords that MUST be present
WAGE_REQUIRED_KEYWORDS = [
    'wage', 'salary', 'income', 'pay', 'paycheck', 'minimum wage',
    'working', 'job', 'work', 'afford', 'money', 'broke', 'poor',
    'poverty', 'financial', 'bills', 'rent', 'inflation'
]

# Level 3: Crisis - Can't meet basic needs
LEVEL_3_KEYWORDS = [
    "can't meet basic needs", "can't afford food", "food insecurity",
    "choosing between food and rent", "choosing between bills",
    "homeless", "housing insecurity", "evicted", "living in car",
    "skipping meals", "can't afford medicine", "medical debt",
    "bankruptcy", "suicidal", "hopeless", "breaking point",
    "mental health crisis", "panic attacks", "depressed",
    "working multiple jobs still broke", "three jobs"
]

# Level 2: Struggling - Paycheck to paycheck, constant stress
LEVEL_2_KEYWORDS = [
    "paycheck to paycheck", "nothing left after bills",
    "can't save", "no savings", "zero savings",
    "can't afford unexpected expense", "one emergency away",
    "second job", "side hustle to survive", "gig economy",
    "cutting back", "can't afford", "living with parents",
    "inflation killing me", "wages not keeping up",
    "CEO pay ratio", "rich get richer", "wealth inequality"
]

def is_wage_related(title, description):
    """Validate that video is actually about wages/income"""
    text = (title + " " + description).lower()
    return any(keyword in text for keyword in WAGE_REQUIRED_KEYWORDS)

def categorize_video(title, description):
    """Categorize video into Level 1/2/3 based on crisis language"""
    if not is_wage_related(title, description):
        return None

    # Filter out clickbait/promotional content
    if not filter_content(title, description):
        return None

    text = (title + " " + description).lower()

    # Count Level 3 keywords
    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    # Level 3: Crisis
    if level_3_count >= 2 or any(phrase in text for phrase in [
        "can't afford food", "homeless", "evicted", "suicidal",
        "choosing between", "skipping meals", "three jobs"
    ]):
        return 'LEVEL_3_CRISIS'

    # Count Level 2 keywords
    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    # Level 2: Struggling
    if level_2_count >= 2 or any(phrase in text for phrase in [
        "paycheck to paycheck", "can't save", "second job",
        "inflation killing", "wages not keeping up"
    ]):
        return 'LEVEL_2_STRUGGLING'

    # Level 1: Aware
    return 'LEVEL_1_AWARE'

def search_youtube(query, max_results=10):
    """Search YouTube for a query and return video data"""
    if not YOUTUBE_API_KEY:
        print("ERROR: YOUTUBE_API_KEY not found in .env file")
        return []

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

        # Only videos from last 90 days
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

            # Get view count
            video_response = youtube.videos().list(
                part='statistics',
                id=video_id
            ).execute()

            view_count = 0
            if video_response['items']:
                stats = video_response['items'][0]['statistics']
                view_count = int(stats.get('viewCount', 0))

            # Categorize
            category = categorize_video(title, description)

            if category is None:
                continue

            # Find crisis keywords
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
                'category': category,
                'notes': ''
            })

        print(f"  ✓ Found {len(videos)} videos for '{query}'")
        return videos

    except Exception as e:
        print(f"  ✗ Error searching for '{query}': {e}")
        return []

def main():
    """Main execution"""
    print("=" * 70)
    print("WAGE STAGNATION YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []

    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=10)
        all_videos.extend(videos)

    df = pd.DataFrame(all_videos)
    df_unique = df.drop_duplicates(subset=['video_id'])

    # Skip writing if no data collected (preserves previous good data)
    if len(df_unique) == 0:
        print("\nWARNING: No videos collected. Skipping file write to preserve previous data.")
        print("Check your YOUTUBE_API_KEY - it may be expired or invalid.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs('collected-data', exist_ok=True)
    output_file = f'collected-data/wage_stagnation_youtube_{timestamp}.csv'
    df_unique.to_csv(output_file, index=False)

    print("\n" + "=" * 70)
    print(f"RESULTS SAVED: {output_file}")
    print("=" * 70)
    print(f"\nTotal videos: {len(df)}")
    print(f"Unique videos: {len(df_unique)}")

    if len(df_unique) > 0:
        print(f"\nBreakdown by category:")
        print(df_unique['category'].value_counts())

        total = len(df_unique)
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        level_2 = len(df_unique[df_unique['category'] == 'LEVEL_2_STRUGGLING'])
        level_1 = len(df_unique[df_unique['category'] == 'LEVEL_1_AWARE'])

        print(f"\nLevel 1 (Aware): {level_1} ({level_1/total*100:.1f}%)")
        print(f"Level 2 (Struggling): {level_2} ({level_2/total*100:.1f}%)")
        print(f"Level 3 (Crisis): {level_3} ({level_3/total*100:.1f}%)")
        print(f"\nCrisis ratio: {level_3/total*100:.1f}%")

if __name__ == '__main__':
    main()
