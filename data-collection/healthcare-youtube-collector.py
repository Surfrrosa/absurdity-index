#!/usr/bin/env python3
"""
What Healthcare? YouTube Data Collector
Collects videos about healthcare system failures and medical debt
"""

import os
import csv
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../.env')

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Search queries for systematic collection
SEARCH_QUERIES = [
    "insurance denied my claim",
    "can't afford healthcare",
    "medical bankruptcy",
    "prior authorization nightmare",
    "health insurance horror story",
    "denied life-saving treatment",
    "can't afford medication",
    "hospital bill nightmare",
    "out of network surprise bill",
    "fighting insurance company"
]

# Categorization keywords
CRISIS_KEYWORDS = {
    'medical_debt': ['bankruptcy', 'collections', 'medical debt', 'going broke', 'cant afford treatment'],
    'denied_care': ['denied', 'claim denied', 'rejected', 'appeal denied', 'wont cover'],
    'life_threatening': ['life-saving', 'cancer treatment', 'dying', 'emergency', 'life or death']
}

def categorize_video(title, description):
    """Categorize video into Level 1, 2, or 3 based on content"""
    title_lower = title.lower()
    desc_lower = description.lower() if description else ''
    combined = title_lower + ' ' + desc_lower

    found_keywords = []

    # Level 3: Medical debt/denied life-saving care
    if any(kw in combined for kw in CRISIS_KEYWORDS['medical_debt']) or \
       any(kw in combined for kw in CRISIS_KEYWORDS['life_threatening']):
        for category, keywords in CRISIS_KEYWORDS.items():
            for keyword in keywords:
                if keyword in combined:
                    found_keywords.append(keyword)
        return 'LEVEL_3_CRISIS', ', '.join(found_keywords[:3])

    # Level 2: Can't afford treatment/denied care
    if any(kw in combined for kw in CRISIS_KEYWORDS['denied_care']) or \
       'cant afford' in combined or 'prior authorization' in combined:
        for category, keywords in CRISIS_KEYWORDS.items():
            for keyword in keywords:
                if keyword in combined:
                    found_keywords.append(keyword)
        return 'LEVEL_2_STRUGGLING', ', '.join(found_keywords[:3])

    # Level 1: Billing confusion/delays
    return 'LEVEL_1_AWARE', ''

def search_youtube(query, max_results=15):
    """Search YouTube for videos matching query"""
    # Search for videos from the last 90 days
    published_after = (datetime.now() - timedelta(days=90)).isoformat() + 'Z'

    try:
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            type='video',
            maxResults=max_results,
            publishedAfter=published_after,
            relevanceLanguage='en',
            safeSearch='none'
        ).execute()

        return search_response.get('items', [])
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        return []

def get_video_stats(video_id):
    """Get view count and other stats for a video"""
    try:
        stats_response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        if stats_response['items']:
            stats = stats_response['items'][0]['statistics']
            return {
                'view_count': stats.get('viewCount', 0),
                'like_count': stats.get('likeCount', 0),
                'comment_count': stats.get('commentCount', 0)
            }
    except Exception as e:
        print(f"Error getting stats for video {video_id}: {e}")

    return {'view_count': 0, 'like_count': 0, 'comment_count': 0}

def main():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f'collected-data/healthcare_youtube_{timestamp}.csv'

    print("Starting What Healthcare? YouTube data collection...")
    print(f"Output file: {output_file}\n")

    all_videos = []

    for query in SEARCH_QUERIES:
        print(f"Searching: {query}")
        videos = search_youtube(query, max_results=15)

        for video in videos:
            video_id = video['id']['videoId']
            snippet = video['snippet']

            # Get video statistics
            stats = get_video_stats(video_id)

            # Categorize video
            category, keywords = categorize_video(snippet['title'], snippet.get('description', ''))

            video_data = {
                'search_term': query,
                'video_id': video_id,
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'title': snippet['title'],
                'description_snippet': snippet.get('description', '')[:200],
                'published_date': snippet['publishedAt'][:10],
                'view_count': stats['view_count'],
                'crisis_keywords': keywords,
                'category': category,
                'notes': ''
            }

            all_videos.append(video_data)
            print(f"  ✓ {snippet['title'][:60]}... ({category})")

        print(f"  Collected {len(videos)} videos\n")

    # Write to CSV
    if all_videos:
        os.makedirs('collected-data', exist_ok=True)

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['search_term', 'video_id', 'url', 'title', 'description_snippet',
                         'published_date', 'view_count', 'crisis_keywords', 'category', 'notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(all_videos)

        # Print statistics
        level_counts = {
            'LEVEL_1_AWARE': 0,
            'LEVEL_2_STRUGGLING': 0,
            'LEVEL_3_CRISIS': 0
        }

        for video in all_videos:
            level_counts[video['category']] += 1

        total = len(all_videos)
        crisis_ratio = (level_counts['LEVEL_3_CRISIS'] / total * 100) if total > 0 else 0

        print(f"\n=== COLLECTION COMPLETE ===")
        print(f"Total videos collected: {total}")
        print(f"Level 1 (Aware): {level_counts['LEVEL_1_AWARE']}")
        print(f"Level 2 (Struggling): {level_counts['LEVEL_2_STRUGGLING']}")
        print(f"Level 3 (Crisis): {level_counts['LEVEL_3_CRISIS']}")
        print(f"Crisis ratio: {crisis_ratio:.1f}%")
        print(f"\nData saved to: {output_file}")
    else:
        print("No videos collected.")

if __name__ == "__main__":
    main()
