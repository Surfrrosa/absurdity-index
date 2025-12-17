#!/usr/bin/env python3
"""
Wage Stagnation Data Collection Script
Systematic collection of financial stress and wage inadequacy sentiment
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
    "living paycheck to paycheck",
    "can't afford rent on my salary",
    "wages too low",
    "can't make ends meet",
    "working full time still poor",
    "two jobs still struggling",
    "inflation eating my paycheck",
    "cost of living crisis",
    "can't afford groceries",
    "financial stress burnout"
]

REDDIT_SUBREDDITS = [
    "r/povertyfinance",
    "r/antiwork",
    "r/WorkReform",
    "r/personalfinance",
    "r/LateStageCapitalism",
    "r/lostgeneration"
]

REDDIT_SEARCH_QUERIES = [
    "paycheck to paycheck",
    "can't afford rent",
    "wages too low",
    "can't save money",
    "broke despite working",
    "cost of living",
    "inflation killing me",
    "working poor"
]

TIKTOK_HASHTAGS = [
    "#paychecktopaycheck",
    "#broke",
    "#cantaffordrent",
    "#workingpoor",
    "#wageslavery",
    "#costofliving",
    "#inflation",
    "#financialstress"
]

# Official data sources to track
OFFICIAL_METRICS = {
    "real_wage_growth": 1.0,  # % YoY real wage growth (Dec 2025)
    "ceo_to_worker_ratio": 285,  # CEO-to-worker pay ratio
    "median_income": 74580,  # US median household income
    "inflation_rate": 3.1  # Current inflation rate %
}

# Categorization criteria
LEVEL_3_KEYWORDS = [
    # Financial crisis
    "can't afford rent", "eviction", "homeless", "living in car",
    "skipping meals", "can't afford food", "food bank", "food stamps",
    "can't pay bills", "utilities shut off", "choosing between",
    "medical debt", "can't afford medication", "bankruptcy",
    "three jobs", "working 80 hours", "no savings", "zero savings",
    "emergency fund empty", "one paycheck from homeless",
    "can't afford childcare", "kids going hungry", "sleeping in office",

    # Mental health crisis
    "suicidal", "want to die", "can't take it anymore",
    "breaking point", "mental breakdown", "severe anxiety",
    "panic attacks about money"
]

LEVEL_2_KEYWORDS = [
    # Paycheck to paycheck
    "paycheck to paycheck", "living paycheck", "no emergency fund",
    "can't save", "saving impossible", "zero left over",

    # Multiple jobs/long hours
    "two jobs", "side hustle", "gig economy", "working weekends",
    "no days off", "60 hour weeks", "exhausted",

    # Cutting back
    "can't afford", "stopped going out", "cancel subscriptions",
    "cutting back", "eating ramen", "cheap food", "thrift store",
    "can't buy new clothes", "same shoes for years",

    # Stress
    "constant stress", "always worried about money", "anxiety about bills",
    "can't sleep worrying", "stressed about finances"
]

LEVEL_1_KEYWORDS = [
    "budget tight", "watching spending", "being careful",
    "prices going up", "more expensive", "noticing inflation",
    "wish I made more", "could use a raise", "frustrated with pay"
]


class WageStagnationEntry:
    """Single data point for wage stagnation analysis"""

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
        """Categorize content based on keywords (1=Mild, 2=Struggling, 3=Crisis)"""
        text = (self.title + " " + self.content).lower()

        # Check Level 3 (Crisis) first
        level_3_matches = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
        if level_3_matches >= 2:
            return 3

        # Check Level 2 (Struggling)
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


class WageStagnationCollector:
    """Manages wage stagnation data collection and scoring"""

    def __init__(self):
        self.entries: List[WageStagnationEntry] = []

    def add_entry(self, entry: WageStagnationEntry):
        self.entries.append(entry)

    def calculate_official_score(self) -> float:
        """
        Calculate official data component (0-100 scale)
        Formula: ((CEO Ratio / 400) + ((100 - Real Wage Growth) / 2) + (Inflation Rate × 10)) / 3 × 100
        """
        ceo_component = OFFICIAL_METRICS["ceo_to_worker_ratio"] / 400
        wage_component = (100 - OFFICIAL_METRICS["real_wage_growth"]) / 2
        inflation_component = OFFICIAL_METRICS["inflation_rate"] * 10

        official_score = ((ceo_component + wage_component + inflation_component) / 3) * 100
        return round(official_score, 2)

    def calculate_crisis_ratio(self) -> float:
        """Calculate percentage of Level 3 (crisis) entries"""
        if not self.entries:
            return 0.0

        level_3_count = sum(1 for entry in self.entries if entry.level == 3)
        crisis_ratio = (level_3_count / len(self.entries)) * 100
        return round(crisis_ratio, 2)

    def calculate_final_score(self) -> float:
        """
        Calculate final absurdity score
        Formula: (Official × 0.4) + (Crisis Ratio × 0.6)
        """
        official = self.calculate_official_score()
        crisis = self.calculate_crisis_ratio()

        final_score = (official * 0.4) + (crisis * 0.6)
        return round(final_score, 2)

    def get_label(self, score: float) -> str:
        """Get descriptive label for score"""
        if score < 15:
            return "Living Wage Exists (???)"
        elif score < 30:
            return "Inflation Exists But Manageable"
        elif score < 50:
            return "Paycheck To Paycheck Normalized"
        elif score < 70:
            return "Financial Stress Pandemic"
        elif score < 85:
            return "Working Poor Majority"
        else:
            return "Late Stage Capitalism Achievement Unlocked"

    def get_stats(self) -> Dict:
        """Calculate comprehensive statistics"""
        total = len(self.entries)
        if total == 0:
            return {
                "total": 0,
                "level_1": 0,
                "level_2": 0,
                "level_3": 0,
                "crisis_ratio": 0,
                "official_score": self.calculate_official_score(),
                "final_score": 0,
                "label": "No Data"
            }

        level_counts = {1: 0, 2: 0, 3: 0}
        platform_counts = {}

        for entry in self.entries:
            level_counts[entry.level] += 1
            platform_counts[entry.platform] = platform_counts.get(entry.platform, 0) + 1

        crisis_ratio = self.calculate_crisis_ratio()
        final_score = self.calculate_final_score()

        return {
            "total": total,
            "level_1": level_counts[1],
            "level_2": level_counts[2],
            "level_3": level_counts[3],
            "crisis_ratio": crisis_ratio,
            "official_score": self.calculate_official_score(),
            "final_score": final_score,
            "label": self.get_label(final_score),
            "platforms": platform_counts,
            "official_metrics": OFFICIAL_METRICS
        }

    def export_csv(self, filename: str = "wage_stagnation_data.csv"):
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

    def export_json(self, filename: str = "wage_stagnation_data.json"):
        """Export collected data to JSON with scoring"""
        stats = self.get_stats()

        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "metric": "Wage Stagnation",
                "stats": stats
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(self.entries)} entries to {filename}")
        print(f"\nFINAL WAGE STAGNATION SCORE: {stats['final_score']}")
        print(f"Label: {stats['label']}")
        print(f"\nBreakdown:")
        print(f"  Official Score: {stats['official_score']}")
        print(f"  Crisis Ratio: {stats['crisis_ratio']}%")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("WAGE STAGNATION DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nOFFICIAL METRICS (baseline):")
    for metric, value in OFFICIAL_METRICS.items():
        print(f"  - {metric}: {value}")

    print("\n" + "=" * 80)
    print("TARGET SAMPLE SIZES:")
    print("=" * 80)
    print("  - YouTube: 80-100 videos")
    print("  - Reddit: 200 posts")
    print("  - TikTok: 100 videos")
    print("  - TOTAL: 380-400 data points")

    print("\n" + "=" * 80)
    print("YOUTUBE SEARCH QUERIES:")
    print("=" * 80)
    for i, query in enumerate(YOUTUBE_QUERIES, 1):
        print(f"  {i}. \"{query}\"")
        print(f"     Collect 8-10 videos per query")

    print("\n" + "=" * 80)
    print("REDDIT COLLECTION:")
    print("=" * 80)
    print("Subreddits to sample:")
    for sub in REDDIT_SUBREDDITS:
        print(f"  - {sub} (collect ~33 posts)")
    print("\nSearch within each subreddit for:")
    for query in REDDIT_SEARCH_QUERIES:
        print(f"  - \"{query}\"")

    print("\n" + "=" * 80)
    print("TIKTOK COLLECTION:")
    print("=" * 80)
    print("Hashtags to search:")
    for tag in TIKTOK_HASHTAGS:
        print(f"  - {tag} (collect ~12 videos each)")

    print("\n" + "=" * 80)
    print("CATEGORIZATION LEVELS:")
    print("=" * 80)
    print("LEVEL 3 (CRISIS - Can't meet basic needs):")
    print("  Can't afford rent/food, eviction risk, homeless, medical debt,")
    print("  working 3 jobs, zero savings, mental health crisis")

    print("\nLEVEL 2 (STRUGGLING - Paycheck to paycheck):")
    print("  Can't save, multiple jobs, cutting essentials, constant financial stress")

    print("\nLEVEL 1 (MILD - Budget awareness):")
    print("  Watching spending, noticing price increases, wish for higher pay")
    print("=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = WageStagnationCollector()

# Add entry
entry = WageStagnationEntry(
    platform="reddit",
    content_id="abc123",
    title="Working full time, can't afford rent",
    content="I work 40 hours a week and still can't make rent. Living paycheck to paycheck...",
    url="https://reddit.com/r/povertyfinance/comments/abc123",
    date="2025-12-10"
)
collector.add_entry(entry)

# View stats and export
print(collector.get_stats())
collector.export_json("wage_stagnation_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
