#!/usr/bin/env python3
"""
Scrape App Store reviews for AI companion apps
Collects reviews from Replika, Character.AI, Chai, and Anima AI
"""

from app_store_scraper import AppStore
import pandas as pd
import time
from datetime import datetime

# App IDs for AI companion apps (using numeric App Store IDs)
APPS = {
    'Replika': '1423496346',
    'Character.AI': '1648145636',
    'Chai': '1544750895',
    'Anima AI': '1506263566'
}

# Crisis keywords to look for
CRISIS_KEYWORDS = [
    'love', 'addiction', 'addicted', 'breakup', 'broke up', 'depressed',
    'depression', 'only friend', 'cant stop', "can't stop", 'dependent',
    'attached', 'relationship', 'feelings', 'real', 'sentient', 'alive',
    'miss', 'lonely', 'loneliness', 'obsessed', 'need', 'withdrawal',
    'grief', 'mourning', 'devastated', 'heartbroken'
]

def categorize_review(review_text):
    """
    Categorize review into Level 1/2/3 based on crisis language
    Level 1: Casual use, normal enjoyment
    Level 2: Dependency language, emotional attachment
    Level 3: Crisis language, mental health concerns
    """
    text_lower = review_text.lower()

    # Count crisis keywords
    crisis_count = sum(1 for keyword in CRISIS_KEYWORDS if keyword in text_lower)

    # Level 3: Multiple crisis keywords or extreme language
    if crisis_count >= 3 or any(phrase in text_lower for phrase in [
        'in love with', 'only friend', "can't stop", 'cant stop',
        'addicted', 'breakup', 'devastated', 'heartbroken'
    ]):
        return 'LEVEL_3_CRISIS'

    # Level 2: Some attachment/dependency language
    elif crisis_count >= 1 or any(word in text_lower for word in [
        'love', 'attached', 'feelings', 'relationship', 'miss', 'need'
    ]):
        return 'LEVEL_2_DEPENDENT'

    # Level 1: Casual use
    else:
        return 'LEVEL_1_CASUAL'

def scrape_app_reviews(app_name, app_id, num_reviews=50):
    """Scrape reviews for a single app"""
    print(f"\nScraping {app_name} ({app_id})...")

    try:
        app = AppStore(country='us', app_name=app_id)
        app.review(how_many=num_reviews)

        reviews_data = []
        for review in app.reviews[:num_reviews]:
            # Extract crisis keywords found
            text_lower = review['review'].lower()
            found_keywords = [kw for kw in CRISIS_KEYWORDS if kw in text_lower]

            reviews_data.append({
                'app_name': app_name,
                'review_date': review['date'].strftime('%Y-%m-%d') if review['date'] else '',
                'rating': review['rating'],
                'review_text_snippet': review['review'][:200],  # First 200 chars
                'crisis_keywords': ', '.join(found_keywords[:5]),  # First 5 keywords
                'category': categorize_review(review['review']),
                'notes': ''
            })

        print(f"  ✓ Collected {len(reviews_data)} reviews from {app_name}")
        return reviews_data

    except Exception as e:
        print(f"  ✗ Error scraping {app_name}: {e}")
        return []

def main():
    """Main execution"""
    print("=" * 60)
    print("AI PSYCHOSIS APP STORE REVIEW SCRAPER")
    print("=" * 60)

    all_reviews = []

    # Scrape each app
    for app_name, app_id in APPS.items():
        reviews = scrape_app_reviews(app_name, app_id, num_reviews=50)
        all_reviews.extend(reviews)
        time.sleep(2)  # Be nice to the API

    # Convert to DataFrame
    df = pd.DataFrame(all_reviews)

    # Save to CSV
    output_file = f'collected-data/ai_psychosis_appstore_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(output_file, index=False)

    print("\n" + "=" * 60)
    print(f"RESULTS SAVED: {output_file}")
    print("=" * 60)
    print(f"\nTotal reviews collected: {len(df)}")
    print(f"\nBreakdown by app:")
    print(df['app_name'].value_counts())
    print(f"\nBreakdown by category:")
    print(df['category'].value_counts())

    # Calculate crisis ratio
    total = len(df)
    level_3 = len(df[df['category'] == 'LEVEL_3_CRISIS'])
    level_2 = len(df[df['category'] == 'LEVEL_2_DEPENDENT'])
    level_1 = len(df[df['category'] == 'LEVEL_1_CASUAL'])

    print(f"\nLevel 1 (Casual): {level_1} ({level_1/total*100:.1f}%)")
    print(f"Level 2 (Dependent): {level_2} ({level_2/total*100:.1f}%)")
    print(f"Level 3 (Crisis): {level_3} ({level_3/total*100:.1f}%)")
    print(f"\nCrisis ratio (Level 2 + Level 3): {(level_2+level_3)/total*100:.1f}%")

if __name__ == '__main__':
    main()
