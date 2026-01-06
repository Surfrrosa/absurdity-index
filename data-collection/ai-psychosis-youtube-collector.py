#!/usr/bin/env python3
"""
Collect YouTube videos about AI psychosis/parasocial relationships
Uses YouTube Data API v3 to search for AI companion content
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Search terms for AI psychosis
SEARCH_TERMS = [
    "my AI girlfriend",
    "addicted to Character.AI",
    "Replika breakup",
    "in love with AI",
    "AI boyfriend",
    "Character AI addiction",
    "Replika emotional attachment",
    "AI companion mental health"
]

# Crisis keywords to categorize content
CRISIS_KEYWORDS = [
    'love', 'addiction', 'addicted', 'breakup', 'broke up', 'depressed',
    'depression', 'only friend', 'cant stop', "can't stop", 'dependent',
    'attached', 'relationship', 'feelings', 'real', 'sentient', 'alive',
    'miss', 'lonely', 'loneliness', 'obsessed', 'need', 'withdrawal',
    'grief', 'mourning', 'devastated', 'heartbroken', 'parasocial'
]

def categorize_video(title, description):
    """
    Categorize video into Level 1/2/3 based on crisis language
    """
    text = (title + " " + description).lower()

    # Count crisis keywords
    crisis_count = sum(1 for keyword in CRISIS_KEYWORDS if keyword in text)

    # Level 3: Multiple crisis keywords or extreme language
    if crisis_count >= 4 or any(phrase in text for phrase in [
        'in love with', 'addicted', 'addiction', 'breakup', 'mental health',
        'devastated', 'heartbroken', 'parasocial', 'obsessed'
    ]):
        return 'LEVEL_3_CRISIS'

    # Level 2: Some attachment/dependency language
    elif crisis_count >= 2 or any(word in text for word in [
        'love', 'attached', 'feelings', 'relationship', 'emotional'
    ]):
        return 'LEVEL_2_DEPENDENT'

    # Level 1: Casual/informational
    else:
        return 'LEVEL_1_CASUAL'

def search_youtube(query, max_results=20):
    """Search YouTube for a query and return video data"""
    if not YOUTUBE_API_KEY:
        print("ERROR: YOUTUBE_API_KEY not found in .env file")
        print("Please add it: YOUTUBE_API_KEY=your_key_here")
        return []

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

        # Search for videos
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results,
            order='relevance',
            regionCode='US'
        ).execute()

        videos = []
        for item in search_response.get('items', []):
            video_id = item['id']['videoId']
            snippet = item['snippet']

            # Get video title and description
            title = snippet.get('title', '')
            description = snippet.get('description', '')
            published_at = snippet.get('publishedAt', '')[:10]  # YYYY-MM-DD

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

            # Find crisis keywords
            text_lower = (title + " " + description).lower()
            found_keywords = [kw for kw in CRISIS_KEYWORDS if kw in text_lower]

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
    print("AI PSYCHOSIS YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []

    # Search each term
    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=20)
        all_videos.extend(videos)

    # Convert to DataFrame
    df = pd.DataFrame(all_videos)

    # Remove duplicates (same video might appear in multiple searches)
    df_unique = df.drop_duplicates(subset=['video_id'])

    # Save to CSV
    output_file = f'collected-data/ai_psychosis_youtube_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df_unique.to_csv(output_file, index=False)

    print("\n" + "=" * 70)
    print(f"RESULTS SAVED: {output_file}")
    print("=" * 70)
    print(f"\nTotal videos collected: {len(df)}")
    print(f"Unique videos (after deduplication): {len(df_unique)}")

    print(f"\nBreakdown by category:")
    print(df_unique['category'].value_counts())

    # Calculate crisis ratio
    total = len(df_unique)
    if total > 0:
        level_3 = len(df_unique[df_unique['category'] == 'LEVEL_3_CRISIS'])
        level_2 = len(df_unique[df_unique['category'] == 'LEVEL_2_DEPENDENT'])
        level_1 = len(df_unique[df_unique['category'] == 'LEVEL_1_CASUAL'])

        print(f"\nLevel 1 (Casual): {level_1} ({level_1/total*100:.1f}%)")
        print(f"Level 2 (Dependent): {level_2} ({level_2/total*100:.1f}%)")
        print(f"Level 3 (Crisis): {level_3} ({level_3/total*100:.1f}%)")
        print(f"\nCrisis ratio (Level 2 + Level 3): {(level_2+level_3)/total*100:.1f}%")

        # Top videos by views
        print(f"\n\nTOP 5 MOST-VIEWED VIDEOS:")
        print("-" * 70)
        top_5 = df_unique.nlargest(5, 'view_count')[['title', 'view_count', 'category', 'url']]
        for idx, row in top_5.iterrows():
            print(f"\n{row['title']}")
            print(f"  Views: {row['view_count']:,} | Category: {row['category']}")
            print(f"  {row['url']}")

if __name__ == '__main__':
    main()
