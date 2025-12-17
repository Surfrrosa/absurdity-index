#!/usr/bin/env python3
"""
Google Trends Data Collection for Disappointments Dashboard
Collects 12 weeks of trend data for all metrics
"""

from pytrends.request import TrendReq
import pandas as pd
import time
from datetime import datetime

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define all search terms by category
search_terms = {
    'wages': [
        "can't afford groceries",
        "wages too low",
        "need a raise"
    ],
    'housing': [
        "can't afford rent",
        "housing crisis"
    ],
    'customer_service': [
        "customer service complaints",
        "terrible customer service"
    ],
    'streaming': [
        "cancel Netflix",
        "too many streaming services",
        "streaming fatigue"
    ],
    'dating': [
        "dating apps suck",
        "I hate dating apps",
        "dating app fatigue"
    ],
    'ai_psychosis': [
        "in love with AI",
        "AI therapy addiction",
        "AI is sentient"
    ]
}

def pull_trends(keywords, category_name):
    """Pull Google Trends data for a list of keywords"""
    print(f"\n{'='*60}")
    print(f"Pulling trends for: {category_name}")
    print(f"Keywords: {keywords}")
    print(f"{'='*60}")

    try:
        # Build payload (last 3 months = ~12 weeks)
        pytrends.build_payload(
            kw_list=keywords,
            timeframe='today 3-m',
            geo='US'
        )

        # Get interest over time
        data = pytrends.interest_over_time()

        if not data.empty:
            # Drop 'isPartial' column if it exists
            if 'isPartial' in data.columns:
                data = data.drop('isPartial', axis=1)

            # Calculate average for each keyword
            print("\nAverage Interest (0-100):")
            for keyword in keywords:
                if keyword in data.columns:
                    avg = data[keyword].mean()
                    print(f"  {keyword}: {avg:.2f}")

            # Calculate overall category average
            category_avg = data[keywords].mean().mean()
            print(f"\n{category_name.upper()} CATEGORY AVERAGE: {category_avg:.2f}/100")

            return data, category_avg
        else:
            print(f"No data returned for {category_name}")
            return None, 0

    except Exception as e:
        print(f"Error pulling trends for {category_name}: {e}")
        return None, 0

# Collect all data
results = {}
category_averages = {}

for category, keywords in search_terms.items():
    data, avg = pull_trends(keywords, category)
    results[category] = data
    category_averages[category] = avg

    # Be nice to Google - add delay between requests
    time.sleep(2)

# Print summary
print("\n" + "="*60)
print("SUMMARY - Category Averages (0-100)")
print("="*60)
for category, avg in category_averages.items():
    print(f"{category.upper()}: {avg:.2f}/100")

# Save raw data to CSV
print("\n" + "="*60)
print("Saving data to CSV files...")
print("="*60)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
for category, data in results.items():
    if data is not None:
        filename = f"google_trends_{category}_{timestamp}.csv"
        data.to_csv(filename)
        print(f"Saved: {filename}")

print("\nData collection complete!")
print(f"Run date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
