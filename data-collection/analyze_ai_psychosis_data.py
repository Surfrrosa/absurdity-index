#!/usr/bin/env python3
"""
Analyze AI Psychosis collected data and calculate crisis ratio
"""
import csv
from pathlib import Path
from collections import Counter

def analyze_csv(filepath, source_name):
    """Analyze a CSV file and return statistics"""
    print(f"\n{'='*60}")
    print(f"Analyzing {source_name}")
    print(f"{'='*60}")

    categories = Counter()
    total = 0
    entries = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            category = row.get('category', '').strip()
            categories[category] += 1
            entries.append({
                'url': row.get('url', ''),
                'title': row.get('title', ''),
                'category': category
            })

    print(f"Total entries: {total}")
    print(f"\nCategory breakdown:")
    for category, count in sorted(categories.items()):
        percentage = (count / total * 100) if total > 0 else 0
        print(f"  {category}: {count} ({percentage:.1f}%)")

    return {
        'total': total,
        'categories': dict(categories),
        'entries': entries
    }

def main():
    base_path = Path(__file__).parent / "collected-data"

    # Analyze Reddit data
    reddit_file = base_path / "reddit_posts_collected_20251216.csv"
    reddit_stats = analyze_csv(reddit_file, "Reddit Posts")

    # Analyze YouTube data
    youtube_file = base_path / "youtube_videos_collected_20251216.csv"
    youtube_stats = analyze_csv(youtube_file, "YouTube Videos")

    # Combined statistics
    print(f"\n{'='*60}")
    print("COMBINED STATISTICS")
    print(f"{'='*60}")

    total_entries = reddit_stats['total'] + youtube_stats['total']
    print(f"Total entries: {total_entries}")
    print(f"  Reddit: {reddit_stats['total']}")
    print(f"  YouTube: {youtube_stats['total']}")

    # Combine categories
    combined_categories = Counter()
    for category, count in reddit_stats['categories'].items():
        combined_categories[category] += count
    for category, count in youtube_stats['categories'].items():
        combined_categories[category] += count

    print(f"\nCombined category breakdown:")
    for category, count in sorted(combined_categories.items()):
        percentage = (count / total_entries * 100) if total_entries > 0 else 0
        print(f"  {category}: {count} ({percentage:.1f}%)")

    # Calculate crisis ratio (LEVEL_3_CRISIS / Total)
    crisis_count = combined_categories.get('LEVEL_3_CRISIS', 0)
    crisis_ratio = (crisis_count / total_entries * 100) if total_entries > 0 else 0

    print(f"\n{'='*60}")
    print(f"CRISIS RATIO: {crisis_ratio:.2f}%")
    print(f"{'='*60}")
    print(f"Level 3 (Crisis) entries: {crisis_count}")
    print(f"Total entries: {total_entries}")
    print(f"Crisis ratio: {crisis_count}/{total_entries} = {crisis_ratio:.2f}%")

    # Show some example entries from each category
    print(f"\n{'='*60}")
    print("SAMPLE ENTRIES")
    print(f"{'='*60}")

    all_entries = reddit_stats['entries'] + youtube_stats['entries']

    for category in ['LEVEL_1_CASUAL', 'LEVEL_2_DEPENDENT', 'LEVEL_3_CRISIS']:
        category_entries = [e for e in all_entries if e['category'] == category]
        if category_entries:
            print(f"\n{category} (showing first 3):")
            for i, entry in enumerate(category_entries[:3], 1):
                title = entry['title'][:80] + "..." if len(entry['title']) > 80 else entry['title']
                print(f"  {i}. {title}")

if __name__ == "__main__":
    main()
