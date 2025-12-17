#!/usr/bin/env python3
"""
Dating App Despair Data Collection Script
Systematic collection and categorization of social media content about dating app experiences
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
    "I quit dating apps",
    "deleted tinder",
    "deleted hinge",
    "deleted bumble",
    "dating app burnout",
    "dating app horror stories",
    "worst dating app experience",
    "giving up on dating apps",
    "dating apps ruined dating",
    "dating app fatigue"
]

REDDIT_SUBREDDITS = [
    "r/dating",
    "r/Tinder",
    "r/Bumble",
    "r/HingeApp",
    "r/dating_advice",
    "r/OnlineDating"
]

REDDIT_SEARCH_QUERIES = [
    "quit dating apps",
    "deleted app",
    "burnout",
    "exhausted",
    "horror story",
    "worst experience",
    "giving up"
]

TIKTOK_HASHTAGS = [
    "#datingappburnout",
    "#quitdatingapps",
    "#datingappfails",
    "#deletedtinder",
    "#datingapphorrorstory",
    "#datingfatigue"
]

# Categorization criteria
LEVEL_3_KEYWORDS = [
    "deleted", "quit", "gave up", "mental health", "therapy", "depression",
    "anxiety", "exhausted", "can't do this", "done with", "never again",
    "ruined my", "destroyed", "worst decision"
]

LEVEL_2_KEYWORDS = [
    "frustrated", "tired", "burnout", "considering quitting", "taking a break",
    "so hard", "difficult", "draining", "waste of time", "fake profiles",
    "ghosting", "breadcrumbing", "terrible experience"
]

LEVEL_1_KEYWORDS = [
    "annoying", "minor complaint", "sometimes", "occasional", "not great",
    "could be better", "mildly frustrating"
]


class DatingAppDespairEntry:
    """Single data point for dating app despair analysis"""

    def __init__(self, platform: str, content_id: str, title: str,
                 content: str, url: str, date: str):
        self.platform = platform
        self.content_id = content_id
        self.title = title
        self.content = content
        self.url = url
        self.date = date
        self.level = self.categorize()
        self.collected_at = datetime.now().isoformat()

    def categorize(self) -> int:
        """Categorize content based on keywords (1=Mild, 2=Frustrated, 3=Crisis)"""
        text = (self.title + " " + self.content).lower()

        # Check Level 3 (Crisis) first
        level_3_matches = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
        if level_3_matches >= 2:
            return 3

        # Check Level 2 (Frustrated)
        level_2_matches = sum(1 for kw in LEVEL_2_KEYWORDS if kw in text)
        if level_2_matches >= 2:
            return 2

        # Default to Level 1 (Mild)
        return 1

    def to_dict(self) -> Dict:
        return {
            "platform": self.platform,
            "content_id": self.content_id,
            "title": self.title,
            "content": self.content,
            "url": self.url,
            "date": self.date,
            "level": self.level,
            "collected_at": self.collected_at
        }


class DataCollector:
    """Manages data collection and export"""

    def __init__(self):
        self.entries: List[DatingAppDespairEntry] = []

    def add_entry(self, entry: DatingAppDespairEntry):
        self.entries.append(entry)

    def get_stats(self) -> Dict:
        """Calculate collection statistics"""
        total = len(self.entries)
        if total == 0:
            return {"total": 0, "level_1": 0, "level_2": 0, "level_3": 0, "crisis_ratio": 0}

        level_counts = {1: 0, 2: 0, 3: 0}
        platform_counts = {}

        for entry in self.entries:
            level_counts[entry.level] += 1
            platform_counts[entry.platform] = platform_counts.get(entry.platform, 0) + 1

        crisis_ratio = (level_counts[3] / total) * 100

        return {
            "total": total,
            "level_1": level_counts[1],
            "level_2": level_counts[2],
            "level_3": level_counts[3],
            "crisis_ratio": round(crisis_ratio, 1),
            "platforms": platform_counts
        }

    def export_csv(self, filename: str = "dating_app_despair_data.csv"):
        """Export collected data to CSV"""
        if not self.entries:
            print("No data to export")
            return

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'platform', 'content_id', 'title', 'content', 'url',
                'date', 'level', 'collected_at'
            ])
            writer.writeheader()
            for entry in self.entries:
                writer.writerow(entry.to_dict())

        print(f"Exported {len(self.entries)} entries to {filename}")

    def export_json(self, filename: str = "dating_app_despair_data.json"):
        """Export collected data to JSON"""
        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "stats": self.get_stats()
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Exported {len(self.entries)} entries to {filename}")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("DATING APP DESPAIR DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nTARGET SAMPLE SIZES:")
    print("  - YouTube: 120-160 videos")
    print("  - Reddit: 200 posts")
    print("  - TikTok: 120 videos")
    print("  - TOTAL: 440-480 data points")
    print("\n" + "=" * 80)
    print("YOUTUBE SEARCH QUERIES:")
    print("=" * 80)
    for i, query in enumerate(YOUTUBE_QUERIES, 1):
        print(f"  {i}. \"{query}\"")
        print(f"     Collect 12-16 videos per query")

    print("\n" + "=" * 80)
    print("REDDIT COLLECTION:")
    print("=" * 80)
    print("Subreddits to sample:")
    for sub in REDDIT_SUBREDDITS:
        print(f"  - {sub} (collect ~33 posts)")
    print("\nSearch within each subreddit for:")
    for query in REDDIT_SEARCH_QUERIES:
        print(f"  - \"{query}\"")
    print("\nSampling method: Sort by 'hot' or 'top' (past month), take systematically")

    print("\n" + "=" * 80)
    print("TIKTOK COLLECTION:")
    print("=" * 80)
    print("Hashtags to search:")
    for tag in TIKTOK_HASHTAGS:
        print(f"  - {tag} (collect ~20 videos each)")

    print("\n" + "=" * 80)
    print("CATEGORIZATION LEVELS:")
    print("=" * 80)
    print("LEVEL 3 (CRISIS/QUIT):")
    print(f"  Keywords: {', '.join(LEVEL_3_KEYWORDS[:10])}...")
    print("\nLEVEL 2 (FRUSTRATED/EXHAUSTED):")
    print(f"  Keywords: {', '.join(LEVEL_2_KEYWORDS[:10])}...")
    print("\nLEVEL 1 (MILD COMPLAINTS):")
    print(f"  Keywords: {', '.join(LEVEL_1_KEYWORDS[:5])}...")
    print("\n" + "=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = DataCollector()

# Add YouTube video entry
entry = DatingAppDespairEntry(
    platform="youtube",
    content_id="abc123",
    title="I Quit All Dating Apps - Here's Why",
    content="After 3 years of burnout and anxiety, I deleted all my dating apps...",
    url="https://youtube.com/watch?v=abc123",
    date="2025-12-01"
)
collector.add_entry(entry)

# Add Reddit post entry
entry = DatingAppDespairEntry(
    platform="reddit",
    content_id="xyz789",
    title="Finally deleted Hinge after 2 years",
    content="The constant ghosting and fake profiles destroyed my mental health...",
    url="https://reddit.com/r/dating/comments/xyz789",
    date="2025-12-05"
)
collector.add_entry(entry)

# View statistics
print(collector.get_stats())

# Export data
collector.export_csv("dating_app_despair_data.csv")
collector.export_json("dating_app_despair_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
