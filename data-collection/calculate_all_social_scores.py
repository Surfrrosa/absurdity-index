import csv
import math
import os

def calculate_social_score(csv_file):
    """Calculate engagement-weighted severity score."""
    severity_weights = {
        'LEVEL_1_AWARE': 0.33,
        'LEVEL_2_STRUGGLING': 0.67,
        'LEVEL_2_FRUSTRATED': 0.67,
        'LEVEL_3_CRISIS': 1.0
    }
    
    total_weighted_score = 0
    total_engagement = 0
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}
    total_videos = 0
    
    if not os.path.exists(csv_file):
        return None, None
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                total_videos += 1
                category = row.get('category', '')
                view_count = int(row.get('view_count', 0))
                
                # Count levels
                if 'LEVEL_1' in category:
                    level_counts['L1'] += 1
                elif 'LEVEL_2' in category:
                    level_counts['L2'] += 1
                elif 'LEVEL_3' in category:
                    level_counts['L3'] += 1
                
                # Get severity weight
                severity = severity_weights.get(category, 0.33)
                
                # Calculate engagement weight (logarithmic)
                engagement = math.log10(view_count + 1)
                
                # Add contribution
                total_weighted_score += severity * engagement
                total_engagement += engagement
        
        # Calculate final score (0-100 scale)
        if total_engagement == 0:
            social_score = 0
        else:
            social_score = (total_weighted_score / total_engagement) * 100
        
        return social_score, level_counts, total_videos
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")
        return None, None, None

# Metric configurations - Updated 2026-01-06
metrics = [
    {
        'name': 'What Healthcare?',
        'csvs': [
            'collected-data/healthcare_youtube_20260106_005130.csv',
            'collected-data/healthcare_reddit_20260106_010226.csv'
        ],
        'official_score': 56.30
    },
    {
        'name': 'AI Psychosis',
        'csvs': [
            'collected-data/ai_psychosis_youtube_20260106_005452.csv',
            'collected-data/ai_psychosis_reddit_20260106_010447.csv'
        ],
        'official_score': 12.5
    },
    {
        'name': 'Subscription Overload',
        'csvs': [
            'collected-data/subscription_overload_youtube_20260106_005535.csv',
            'collected-data/subscription_overload_reddit_20260106_010724.csv'
        ],
        'official_score': 45.2
    },
    {
        'name': 'Wage Stagnation',
        'csvs': [
            'collected-data/wage_stagnation_youtube_20260106_005618.csv',
            'collected-data/wage_stagnation_reddit_20260106_011040.csv'
        ],
        'official_score': 38.4
    },
    {
        'name': 'Housing Despair',
        'csvs': [
            'collected-data/housing_despair_youtube_20260106_005651.csv',
            'collected-data/housing_despair_reddit_20260106_011352.csv'
        ],
        'official_score': 37.6
    },
    {
        'name': 'Dating App Despair',
        'csvs': [
            'collected-data/dating_app_despair_youtube_20260106_005709.csv',
            'collected-data/dating_app_despair_reddit_20260106_011734.csv'
        ],
        'official_score': 8.5
    },
    {
        'name': 'Layoff Watch',
        'csvs': [
            'collected-data/layoff_watch_youtube_20260106_005728.csv',
            'collected-data/layoff_watch_reddit_20260106_012319.csv'
        ],
        'official_score': 76.5
    },
    {
        'name': 'Airline Chaos',
        'csvs': [
            'collected-data/airline_chaos_youtube_20260106_005738.csv',
            'collected-data/airline_chaos_reddit_20260106_012625.csv'
        ],
        'official_score': 21.0
    }
]

def calculate_combined_score(csv_files):
    """Calculate combined engagement-weighted severity score from multiple CSV files."""
    severity_weights = {
        'LEVEL_1_AWARE': 0.33,
        'LEVEL_1_CASUAL': 0.33,
        'LEVEL_2_STRUGGLING': 0.67,
        'LEVEL_2_FRUSTRATED': 0.67,
        'LEVEL_2_DEPENDENT': 0.67,
        'LEVEL_3_CRISIS': 1.0
    }

    total_weighted_score = 0
    total_engagement = 0
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}
    total_entries = 0

    for csv_file in csv_files:
        if not os.path.exists(csv_file):
            print(f"  Warning: {csv_file} not found")
            continue

        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    total_entries += 1
                    category = row.get('category', '')

                    # Get view count (YouTube) or score (Reddit)
                    view_count = int(row.get('view_count', 0) or 0)
                    score = int(row.get('score', 0) or 0)
                    engagement_value = max(view_count, score, 1)

                    # Count levels
                    if 'LEVEL_1' in category:
                        level_counts['L1'] += 1
                    elif 'LEVEL_2' in category:
                        level_counts['L2'] += 1
                    elif 'LEVEL_3' in category:
                        level_counts['L3'] += 1

                    # Get severity weight
                    severity = severity_weights.get(category, 0.33)

                    # Calculate engagement weight (logarithmic)
                    engagement = math.log10(engagement_value + 1)

                    # Add contribution
                    total_weighted_score += severity * engagement
                    total_engagement += engagement

        except Exception as e:
            print(f"  Error processing {csv_file}: {e}")

    # Calculate final score (0-100 scale)
    if total_engagement == 0:
        social_score = 0
    else:
        social_score = (total_weighted_score / total_engagement) * 100

    return social_score, level_counts, total_entries

print("=" * 100)
print("CALCULATING ALL SOCIAL SCORES (Engagement-Weighted Severity Formula)")
print("=" * 100)
print()

results = []

for metric in metrics:
    csv_files = metric.get('csvs', [metric.get('csv')])
    social_score, levels, total = calculate_combined_score(csv_files)

    if social_score is not None:
        final_score = (metric['official_score'] * 0.4) + (social_score * 0.6)

        print(f"{metric['name']}:")
        print(f"  Total entries: {total}")
        print(f"  Distribution: L1={levels['L1']}, L2={levels['L2']}, L3={levels['L3']}")
        print(f"  Official Score: {metric['official_score']:.2f}")
        print(f"  Social Score: {social_score:.2f}")
        print(f"  Final Score: {final_score:.2f}")
        print()

        results.append({
            'name': metric['name'],
            'official': metric['official_score'],
            'social': social_score,
            'final': final_score,
            'total': total,
            'levels': levels
        })

print("=" * 100)
print("SUMMARY FOR UPDATING metricDetailData.ts")
print("=" * 100)
print()

for r in results:
    print(f"{r['name']:25} → score: {r['final']:.2f}, crisisRatio: {r['social']:.2f}")

