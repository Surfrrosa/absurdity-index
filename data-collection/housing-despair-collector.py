#!/usr/bin/env python3
"""
Housing Despair Data Collection Script
Systematic collection of housing crisis and homeownership despair sentiment
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
    "never own a home",
    "priced out of housing market",
    "gave up on buying house",
    "rent is killing me",
    "can't afford down payment",
    "housing crisis",
    "landlord raised rent again",
    "kicked out of apartment",
    "housing unaffordable",
    "millennial homeownership"
]

REDDIT_SUBREDDITS = [
    "r/FirstTimeHomeBuyer",
    "r/RealEstate",
    "r/povertyfinance",
    "r/lostgeneration",
    "r/renters",
    "r/HousingCrisis"
]

REDDIT_SEARCH_QUERIES = [
    "can't afford house",
    "priced out",
    "gave up on homeownership",
    "rent increase",
    "landlord",
    "eviction",
    "down payment impossible",
    "housing crisis"
]

TIKTOK_HASHTAGS = [
    "#housingcrisis",
    "#cantaffordhouse",
    "#millennial",
    "#rentistoohigh",
    "#housingmarket",
    "#priceout",
    "#landlord",
    "#eviction"
]

# Official data sources to track
OFFICIAL_METRICS = {
    "median_home_price": 383725,  # US median home price
    "median_household_income": 74580,  # US median household income
    "price_to_income_ratio": 5.1,  # Median price / median income
    "median_rent": 2000,  # Median monthly rent
    "rent_percent_income": 30  # Median rent as % of median income
}

# Categorization criteria
LEVEL_3_KEYWORDS = [
    # Housing insecurity
    "evicted", "eviction notice", "homeless", "living in car",
    "couch surfing", "sleeping in", "lost apartment", "foreclosure",
    "can't pay rent", "behind on rent", "rent strike",

    # Gave up entirely
    "gave up on homeownership", "will never own", "homeownership impossible",
    "accepted I'll never", "dream is dead", "given up on buying",

    # Forced moves
    "had to move back", "living with parents", "multi-generational",
    "forced to relocate", "priced out of city", "left my hometown",
    "couldn't afford to stay",

    # Mental health
    "depressed about housing", "anxiety about rent", "panic attacks",
    "suicidal", "hopeless", "breaking point"
]

LEVEL_2_KEYWORDS = [
    # Can't buy
    "can't save for down payment", "down payment impossible",
    "can't afford house", "priced out", "outbid again",
    "lost another bidding war", "housing too expensive",

    # Rent struggles
    "rent increase", "rent went up", "landlord raised rent",
    "can't afford rent increase", "rent is 50% income",
    "paycheck goes to rent", "nothing left after rent",

    # Cutting back
    "smaller apartment", "worse neighborhood", "longer commute",
    "roommates at 30", "roommates at 40", "shared housing",

    # Frustration
    "housing market broken", "system is rigged", "investors ruining",
    "corporations buying homes", "private equity", "Wall Street landlords"
]

LEVEL_1_KEYWORDS = [
    "housing expensive", "prices high", "tough market",
    "competitive", "saving for down payment", "looking to buy",
    "frustrating but trying", "still hopeful"
]


class HousingDespairEntry:
    """Single data point for housing despair analysis"""

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


class HousingDespairCollector:
    """Manages housing despair data collection and scoring"""

    def __init__(self):
        self.entries: List[HousingDespairEntry] = []

    def add_entry(self, entry: HousingDespairEntry):
        self.entries.append(entry)

    def calculate_official_score(self) -> float:
        """
        Calculate official data component (0-100 scale)
        Formula: ((Price-to-Income Ratio / 10) + (Rent % Income / 2)) × 10
        """
        price_income_component = OFFICIAL_METRICS["price_to_income_ratio"] / 10
        rent_component = OFFICIAL_METRICS["rent_percent_income"] / 2

        official_score = (price_income_component + rent_component) * 10
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
            return "Homeownership Feels Achievable"
        elif score < 30:
            return "Starter Home Exists (Somewhere)"
        elif score < 50:
            return "Landlord's Retirement Fund"
        elif score < 70:
            return "Generational Wealth Gap Locked In"
        elif score < 85:
            return "Housing Is Human Right (Just Kidding)"
        else:
            return "Welcome To Neo-Feudalism"

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

    def export_csv(self, filename: str = "housing_despair_data.csv"):
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

    def export_json(self, filename: str = "housing_despair_data.json"):
        """Export collected data to JSON with scoring"""
        stats = self.get_stats()

        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "metric": "Housing Despair",
                "stats": stats
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(self.entries)} entries to {filename}")
        print(f"\nFINAL HOUSING DESPAIR SCORE: {stats['final_score']}")
        print(f"Label: {stats['label']}")
        print(f"\nBreakdown:")
        print(f"  Official Score: {stats['official_score']}")
        print(f"  Crisis Ratio: {stats['crisis_ratio']}%")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("HOUSING DESPAIR DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nOFFICIAL METRICS (baseline):")
    for metric, value in OFFICIAL_METRICS.items():
        print(f"  - {metric}: {value}")

    official_score = ((OFFICIAL_METRICS['price_to_income_ratio'] / 10 +
                      OFFICIAL_METRICS['rent_percent_income'] / 2) * 10)
    print(f"\nOFFICIAL SCORE: {official_score:.2f}")

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
    print("LEVEL 3 (CRISIS - Housing insecurity/Gave up):")
    print("  Eviction, homeless, living in car, gave up on homeownership,")
    print("  forced to move, multi-generational living, mental health crisis")

    print("\nLEVEL 2 (FRUSTRATED - Can't buy/Rent struggles):")
    print("  Can't save down payment, priced out, rent increases, nothing left after rent")

    print("\nLEVEL 1 (MILD - Market awareness):")
    print("  Prices high, competitive market, still trying")
    print("=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = HousingDespairCollector()

# Add entry
entry = HousingDespairEntry(
    platform="reddit",
    content_id="abc123",
    title="Gave up on ever owning a home",
    content="After 5 years of saving, I'm further from a down payment than ever. Prices went up faster than I could save...",
    url="https://reddit.com/r/FirstTimeHomeBuyer/comments/abc123",
    date="2025-12-10"
)
collector.add_entry(entry)

# View stats and export
print(collector.get_stats())
collector.export_json("housing_despair_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
