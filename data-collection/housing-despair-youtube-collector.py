#!/usr/bin/env python3
"""
Collect YouTube videos about housing despair and homeownership crisis
Uses YouTube Data API v3 to search for housing crisis content
"""

import os
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from content_filters import filter_content

# Load environment variables
load_dotenv()

# YouTube API setup
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')

# Search terms for housing despair
SEARCH_TERMS = [
    "never own a home",
    "priced out of housing market",
    "gave up on buying house",
    "rent is killing me",
    "can't afford down payment",
    "housing crisis 2025",
    "landlord raised rent",
    "kicked out of apartment",
    "housing unaffordable",
    "millennial homeownership impossible",
    "living in my car",
    "homeless living in vehicle",
    "van life not by choice",
    "couch surfing housing crisis"
]

# Level 3: Crisis - Housing insecurity, gave up entirely
LEVEL_3_KEYWORDS = [
    'evicted', 'eviction', 'homeless', 'living in car',
    'couch surfing', 'lost apartment', 'foreclosure',
    "can't pay rent", 'behind on rent',
    'gave up on homeownership', 'will never own', 'homeownership impossible',
    'accepted i will never', 'dream is dead', 'given up on buying',
    'living with parents', 'moved back home', 'multi-generational',
    'forced to relocate', 'priced out of city', 'left my hometown',
    'depressed about housing', 'anxiety about rent', 'panic',
    'hopeless', 'breaking point'
]

# Level 2: Frustrated - Can't buy, rent struggles
LEVEL_2_KEYWORDS = [
    "can't save for down payment", 'down payment impossible',
    "can't afford house", 'priced out', 'outbid',
    'lost bidding war', 'housing too expensive',
    'rent increase', 'rent went up', 'landlord raised rent',
    "can't afford rent increase", 'rent is 50%',
    'paycheck goes to rent', 'nothing left after rent',
    'smaller apartment', 'worse neighborhood', 'longer commute',
    'roommates at 30', 'roommates at 40', 'shared housing',
    'housing market broken', 'system is rigged', 'investors ruining',
    'corporations buying homes', 'private equity', 'wall street landlords'
]

# Core housing keywords that MUST be present to avoid false positives
HOUSING_REQUIRED_KEYWORDS = [
    'housing', 'house', 'home', 'apartment', 'rent', 'renting', 'rental',
    'landlord', 'evict', 'eviction', 'mortgage', 'homeowner', 'homeownership',
    'real estate', 'property', 'market', 'afford', 'down payment',
    'homeless', 'housing crisis', 'van life', 'car living', 'couch surf'
]

def is_housing_related(title, description):
    """
    Validate that video is actually about housing (not false positive)
    Returns True if at least one housing keyword is present
    """
    text = (title + " " + description).lower()
    return any(keyword in text for keyword in HOUSING_REQUIRED_KEYWORDS)

def categorize_video(title, description):
    """
    Categorize video into Level 1/2/3 based on crisis language
    Returns None if video is not housing-related (false positive)
    """
    # First check: Is this actually about housing?
    if not is_housing_related(title, description):
        return None  # Filter out non-housing videos

    # Filter out clickbait/promotional content
    if not filter_content(title, description):
        return None

    text = (title + " " + description).lower()

    # Count Level 3 keywords (crisis/housing insecurity)
    level_3_count = sum(1 for keyword in LEVEL_3_KEYWORDS if keyword in text)

    # Level 3: Crisis - gave up, evicted, homeless
    if level_3_count >= 2 or any(phrase in text for phrase in [
        'evicted', 'eviction', 'homeless', 'living in car',
        'gave up on homeownership', 'will never own', 'dream is dead',
        'living with parents', 'moved back home', 'hopeless'
    ]):
        return 'LEVEL_3_CRISIS'

    # Count Level 2 keywords (frustrated but still trying)
    level_2_count = sum(1 for keyword in LEVEL_2_KEYWORDS if keyword in text)

    # Level 2: Frustrated - can't afford, rent struggles
    if level_2_count >= 2 or any(phrase in text for phrase in [
        "can't afford", 'priced out', 'down payment impossible',
        'rent increase', 'landlord raised rent', 'housing market broken'
    ]):
        return 'LEVEL_2_FRUSTRATED'

    # Level 1: Mild awareness, still hopeful
    return 'LEVEL_1_AWARE'

def search_youtube(query, max_results=10):
    """Search YouTube for a query and return video data"""
    if not YOUTUBE_API_KEY:
        print("ERROR: YOUTUBE_API_KEY not found in .env file")
        print("Please add it: YOUTUBE_API_KEY=your_key_here")
        return []

    try:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

        # Calculate date 90 days ago for recent content only
        from datetime import timedelta
        ninety_days_ago = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')

        # Search for videos (last 90 days only)
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=max_results,
            order='relevance',
            regionCode='US',
            publishedAfter=ninety_days_ago  # Only videos from last 90 days
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

            # Skip if not housing-related (false positive)
            if category is None:
                continue

            # Find crisis keywords present
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
    print("HOUSING DESPAIR YOUTUBE VIDEO COLLECTOR")
    print("=" * 70)

    all_videos = []

    # Search each term (10 videos per term = 100 total)
    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        videos = search_youtube(term, max_results=10)
        all_videos.extend(videos)

    # Convert to DataFrame
    df = pd.DataFrame(all_videos)

    # Remove duplicates (same video might appear in multiple searches)
    df_unique = df.drop_duplicates(subset=['video_id'])

    # Skip writing if no data collected (preserves previous good data)
    if len(df_unique) == 0:
        print("\nWARNING: No videos collected. Skipping file write to preserve previous data.")
        print("Check your YOUTUBE_API_KEY - it may be expired or invalid.")
        return

    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = 'data-collection/collected-data'
    os.makedirs(output_dir, exist_ok=True)
    output_file = f'{output_dir}/housing_despair_youtube_{timestamp}.csv'
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
        level_2 = len(df_unique[df_unique['category'] == 'LEVEL_2_FRUSTRATED'])
        level_1 = len(df_unique[df_unique['category'] == 'LEVEL_1_AWARE'])

        print(f"\nLevel 1 (Aware): {level_1} ({level_1/total*100:.1f}%)")
        print(f"Level 2 (Frustrated): {level_2} ({level_2/total*100:.1f}%)")
        print(f"Level 3 (Crisis): {level_3} ({level_3/total*100:.1f}%)")
        print(f"\nCrisis ratio (Level 3 only): {level_3/total*100:.1f}%")

        # Calculate preliminary score
        # Using Gen Z rent burden data: 58.2%
        gen_z_rent_burden = 58.2
        threshold = 30.0
        excess_burden = gen_z_rent_burden - threshold
        official_score = (excess_burden / threshold) * 100 * 0.4  # 40% weight

        crisis_ratio = (level_3/total*100)
        social_score = crisis_ratio * 0.6  # 60% weight

        preliminary_score = official_score + social_score

        print(f"\n" + "=" * 70)
        print(f"PRELIMINARY HOUSING DESPAIR SCORE")
        print("=" * 70)
        print(f"Official component (Gen Z rent burden): {official_score:.2f}")
        print(f"Social sentiment (crisis ratio): {social_score:.2f}")
        print(f"TOTAL SCORE: {preliminary_score:.2f}/100")

        if preliminary_score < 15:
            label = "Homeownership Feels Achievable"
        elif preliminary_score < 30:
            label = "Starter Home Exists (Somewhere)"
        elif preliminary_score < 50:
            label = "Landlord's Retirement Fund"
        elif preliminary_score < 70:
            label = "Multiple Organs Required"
        else:
            label = "Welcome To Neo-Feudalism"

        print(f"Label: {label}")

        # Top videos by views
        print(f"\n\nTOP 5 MOST-VIEWED VIDEOS:")
        print("-" * 70)
        top_5 = df_unique.nlargest(5, 'view_count')[['title', 'view_count', 'category', 'url']]
        for idx, row in top_5.iterrows():
            print(f"\n{row['title']}")
            print(f"  Views: {row['view_count']:,} | Category: {row['category']}")
            print(f"  {row['url']}")

        print("\n" + "=" * 70)
        print("NEXT STEPS:")
        print("=" * 70)
        print("1. Review the CSV file and verify categorizations look correct")
        print("2. Run Reddit collector to get 200 more data points")
        print("3. Combine YouTube + Reddit data for final score")
        print("4. Update metricDetailData.ts with results")

if __name__ == '__main__':
    main()
