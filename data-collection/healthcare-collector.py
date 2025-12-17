#!/usr/bin/env python3
"""
What Healthcare? Data Collection Script
Systematic collection and categorization of healthcare system absurdity
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
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

REDDIT_SUBREDDITS = [
    "r/HealthInsurance",
    "r/Insurance",
    "r/povertyfinance",
    "r/ChronicIllness",
    "r/diabetes",
    "r/cancer"
]

REDDIT_SEARCH_QUERIES = [
    "claim denied",
    "can't afford",
    "prior authorization",
    "medical debt",
    "insurance won't cover",
    "appeal denied",
    "out of network",
    "surprise bill"
]

TIKTOK_HASHTAGS = [
    "#medicaldebt",
    "#healthinsurance",
    "#claimdenied",
    "#cantaffordhealthcare",
    "#medicalbankruptcy",
    "#priorauthorization",
    "#healthcaresystem",
    "#insurancenightmare"
]

# Official data sources to track
OFFICIAL_METRICS = {
    "premium_increase_yoy": 7.0,  # Average annual increase %
    "initial_denial_rate": 18.0,  # % of claims denied initially
    "adults_medical_debt": 41.0,  # % of adults with medical debt
    "medical_bankruptcies": 66.5  # % of bankruptcies with medical component
}

# Categorization criteria
LEVEL_3_KEYWORDS = [
    "bankruptcy", "collections", "can't afford", "denied life-saving",
    "denied cancer treatment", "denied surgery", "going to die",
    "choose between", "ration", "can't afford medication",
    "homeless due to medical", "lost everything", "medical debt",
    "selling", "gofundme", "crowdfunding medical"
]

LEVEL_2_KEYWORDS = [
    "can't afford treatment", "skipping medication", "delaying care",
    "prior authorization hell", "fighting insurance", "appeal",
    "high deductible", "out of pocket", "premium too high",
    "can't afford premium", "struggling to pay", "payment plan",
    "stress", "anxiety about medical bills"
]

LEVEL_1_KEYWORDS = [
    "billing confusion", "admin hassle", "paperwork nightmare",
    "customer service runaround", "confusing explanation of benefits",
    "minor delay", "annoying but manageable", "bureaucracy"
]


class HealthcareEntry:
    """Single data point for healthcare system analysis"""

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


class HealthcareDataCollector:
    """Manages healthcare data collection and scoring"""

    def __init__(self):
        self.entries: List[HealthcareEntry] = []

    def add_entry(self, entry: HealthcareEntry):
        self.entries.append(entry)

    def calculate_official_score(self) -> float:
        """
        Calculate official data component (0-100 scale)
        Formula: ((Premium Increase % × 10) + (Denial Rate %) + (Medical Debt % / 2)) / 3
        """
        premium = OFFICIAL_METRICS["premium_increase_yoy"] * 10
        denial = OFFICIAL_METRICS["initial_denial_rate"]
        debt = OFFICIAL_METRICS["adults_medical_debt"] / 2

        official_score = (premium + denial + debt) / 3
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
            return "Affordable Care Exists (???)"
        elif score < 30:
            return "Minor Medical Anxiety"
        elif score < 50:
            return "Quarterly Health Crisis"
        elif score < 70:
            return "Prior Authorization Purgatory"
        elif score < 85:
            return "Medical Bankruptcy Imminent"
        else:
            return "Healthcare Is A Right (In Other Countries)"

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

    def export_csv(self, filename: str = "healthcare_data.csv"):
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

    def export_json(self, filename: str = "healthcare_data.json"):
        """Export collected data to JSON with scoring"""
        stats = self.get_stats()

        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "metric": "What Healthcare?",
                "stats": stats
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(self.entries)} entries to {filename}")
        print(f"\nFINAL HEALTHCARE ABSURDITY SCORE: {stats['final_score']}")
        print(f"Label: {stats['label']}")
        print(f"\nBreakdown:")
        print(f"  Official Score: {stats['official_score']}")
        print(f"  Crisis Ratio: {stats['crisis_ratio']}%")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("WHAT HEALTHCARE? DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nOFFICIAL METRICS (baseline):")
    for metric, value in OFFICIAL_METRICS.items():
        print(f"  - {metric}: {value}%")

    print(f"\nOFFICIAL SCORE: {((OFFICIAL_METRICS['premium_increase_yoy'] * 10 + OFFICIAL_METRICS['initial_denial_rate'] + OFFICIAL_METRICS['adults_medical_debt'] / 2) / 3):.2f}")

    print("\n" + "=" * 80)
    print("TARGET SAMPLE SIZES:")
    print("=" * 80)
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
        print(f"  - {tag} (collect ~15 videos each)")

    print("\n" + "=" * 80)
    print("CATEGORIZATION LEVELS:")
    print("=" * 80)
    print("LEVEL 3 (CRISIS - Medical debt/denied life-saving care):")
    print(f"  Keywords: {', '.join(LEVEL_3_KEYWORDS[:8])}...")
    print("\nLEVEL 2 (STRUGGLING - Can't afford treatment/high premiums):")
    print(f"  Keywords: {', '.join(LEVEL_2_KEYWORDS[:8])}...")
    print("\nLEVEL 1 (MILD - Billing confusion/delays):")
    print(f"  Keywords: {', '.join(LEVEL_1_KEYWORDS[:5])}...")
    print("\n" + "=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = HealthcareDataCollector()

# Add YouTube video entry
entry = HealthcareEntry(
    platform="youtube",
    content_id="abc123",
    title="Insurance Denied My Cancer Treatment",
    content="After paying premiums for 10 years, my claim was denied. Now facing bankruptcy...",
    url="https://youtube.com/watch?v=abc123",
    date="2025-12-01"
)
collector.add_entry(entry)

# Add Reddit post entry
entry = HealthcareEntry(
    platform="reddit",
    content_id="xyz789",
    title="Prior authorization taking 3 weeks while I'm in pain",
    content="Doctor prescribed medication months ago but insurance requires prior auth...",
    url="https://reddit.com/r/HealthInsurance/comments/xyz789",
    date="2025-12-05"
)
collector.add_entry(entry)

# View statistics and final score
print(collector.get_stats())

# Export data
collector.export_csv("healthcare_data.csv")
collector.export_json("healthcare_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
