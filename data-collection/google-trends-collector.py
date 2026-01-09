#!/usr/bin/env python3
"""
Google Trends data collector for the Absurdity Index.
Uses pytrends to pull search interest data for relevant terms.

Install: pip install pytrends pandas

Usage:
    python google-trends-collector.py
"""

import os
import time
from datetime import datetime
import pandas as pd

try:
    from pytrends.request import TrendReq
except ImportError:
    print("ERROR: pytrends not installed. Run: pip install pytrends")
    exit(1)

# Change to the script's directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

# Search terms by metric
METRIC_TERMS = {
    'healthcare': [
        'insurance denied claim',
        'medical debt',
        'prior authorization',
        'health insurance nightmare',
        'cant afford healthcare'
    ],
    'ai_psychosis': [
        'character ai addiction',
        'replika ai relationship',
        'ai girlfriend',
        'chatgpt therapy',
        'ai companion loneliness'
    ],
    'subscription_overload': [
        'cancel subscriptions',
        'subscription fatigue',
        'too many streaming services',
        'subscription audit',
        'streaming prices'
    ],
    'wage_stagnation': [
        'paycheck to paycheck',
        'cant afford rent',
        'wages not keeping up',
        'working poor',
        'side hustle'
    ],
    'housing_despair': [
        'cant afford house',
        'housing crisis',
        'rent too high',
        'priced out housing',
        'never own home'
    ],
    'dating_app_despair': [
        'quit dating apps',
        'dating app burnout',
        'hinge bumble tinder',
        'dating is hard',
        'ghosted dating'
    ],
    'layoff_watch': [
        'tech layoffs',
        'laid off',
        'job search nightmare',
        'unemployment',
        'hiring freeze'
    ],
    'airline_chaos': [
        'flight cancelled',
        'airline nightmare',
        'lost luggage',
        'flight delayed hours',
        'worst airline'
    ]
}


def collect_trends_for_metric(pytrends, metric_name, terms):
    """Collect Google Trends data for a set of terms."""
    print(f"\n{'='*60}")
    print(f"Collecting: {metric_name.upper().replace('_', ' ')}")
    print(f"{'='*60}")

    all_data = []

    for term in terms:
        print(f"  Searching: '{term}'...")
        try:
            # Build payload - US only, past 12 months
            pytrends.build_payload([term], cat=0, timeframe='today 12-m', geo='US')

            # Get interest over time
            interest = pytrends.interest_over_time()

            if not interest.empty:
                # Get the average interest score
                avg_interest = interest[term].mean()
                max_interest = interest[term].max()
                recent_interest = interest[term].iloc[-4:].mean()  # Last month avg

                print(f"    Avg: {avg_interest:.1f}, Max: {max_interest}, Recent: {recent_interest:.1f}")

                all_data.append({
                    'metric': metric_name,
                    'term': term,
                    'avg_interest': round(avg_interest, 2),
                    'max_interest': int(max_interest),
                    'recent_interest': round(recent_interest, 2),
                    'trend': 'rising' if recent_interest > avg_interest else 'falling',
                    'collected_date': datetime.now().strftime('%Y-%m-%d')
                })
            else:
                print(f"    No data returned")

            # Rate limiting - Google Trends is sensitive
            time.sleep(2)

        except Exception as e:
            print(f"    Error: {e}")
            time.sleep(5)  # Longer wait on error

    return all_data


def calculate_metric_trend_score(data):
    """Calculate an overall trend score for a metric (0-100)."""
    if not data:
        return 0

    # Weight recent interest more heavily
    total_score = 0
    for item in data:
        # Normalize to 0-100 and weight by recency
        score = (item['recent_interest'] * 0.6) + (item['avg_interest'] * 0.4)
        total_score += score

    return round(total_score / len(data), 2)


def main():
    print("=" * 80)
    print("GOOGLE TRENDS DATA COLLECTION")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Initialize pytrends
    pytrends = TrendReq(hl='en-US', tz=360)

    all_results = []
    metric_scores = {}

    for metric_name, terms in METRIC_TERMS.items():
        data = collect_trends_for_metric(pytrends, metric_name, terms)
        all_results.extend(data)

        # Calculate metric score
        score = calculate_metric_trend_score(data)
        metric_scores[metric_name] = score
        print(f"\n  {metric_name} Trend Score: {score}")

        # Longer pause between metrics
        time.sleep(5)

    # Save results
    if all_results:
        df = pd.DataFrame(all_results)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'collected-data/google_trends_{timestamp}.csv'
        df.to_csv(output_file, index=False)
        print(f"\n{'='*80}")
        print(f"COLLECTION COMPLETE")
        print(f"{'='*80}")
        print(f"Total terms collected: {len(all_results)}")
        print(f"Saved to: {output_file}")

        print(f"\n{'='*80}")
        print(f"METRIC TREND SCORES")
        print(f"{'='*80}")
        for metric, score in sorted(metric_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"  {metric.replace('_', ' ').title():25} {score:5.1f}")
    else:
        print("\nNo data collected!")


if __name__ == '__main__':
    main()
