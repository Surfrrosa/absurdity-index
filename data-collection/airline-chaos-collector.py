#!/usr/bin/env python3
"""
Airline Chaos Data Collection Script
Systematic collection of airline safety incidents, service failures, and travel nightmares
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
    "plane emergency landing",
    "Boeing 737 max door blew out",
    "severe turbulence injuries",
    "emergency evacuation slides",
    "engine failure mid flight",
    "near crash",
    "flight cancelled stranded",
    "lost luggage horror story",
    "stuck on tarmac",
    "bumped from overbooked flight",
    "airline refused refund",
    "damaged wheelchair airline",
    "missed connection nightmare",
    "airline nightmare",
    "worst airline experience"
]

REDDIT_SUBREDDITS = [
    "r/travel",
    "r/aviation",
    "r/delta",
    "r/united",
    "r/Southwest",
    "r/AmericanAirlines",
    "r/mildlyinfuriating",
    "r/AdmiralCloudberg"
]

REDDIT_SEARCH_QUERIES = [
    "flight cancelled",
    "stranded",
    "lost luggage",
    "airline nightmare",
    "bumped from flight",
    "stuck on tarmac",
    "airline won't refund",
    "emergency landing",
    "turbulence injuries",
    "near miss"
]

TIKTOK_HASHTAGS = [
    "#airlinenightmare",
    "#flightcancelled",
    "#lostluggage",
    "#stuckonplane",
    "#airlinetravel",
    "#travelnightmare",
    "#airportstranded",
    "#emergencylanding",
    "#planescary"
]

# Official data sources to track
OFFICIAL_METRICS = {
    "delay_rate": 22.0,  # % of flights delayed (Dec 2025)
    "cancellation_rate": 2.5,  # % of flights cancelled
    "acsi_satisfaction": 77.0,  # Customer satisfaction score
    "on_time_rate": 78.0  # % of flights on time
}

# Categorization criteria
LEVEL_3_KEYWORDS = [
    # Safety incidents
    "crash", "near crash", "emergency landing", "engine failure",
    "depressurization", "emergency evacuation", "737 max", "door blew out",
    "severe turbulence", "injured", "hospitalized", "fire in cabin",
    "smoke in cabin", "thought we were going to die", "emergency descent",
    "oxygen masks deployed", "terrifying", "mechanical failure",
    "bird strike emergency", "lightning strike emergency",

    # Major life disruption
    "stranded for days", "stranded 24 hours", "no hotel voucher",
    "missed funeral", "missed wedding", "missed job interview",
    "lost medication", "lost medical device", "damaged wheelchair",
    "mobility device destroyed", "vacation ruined", "honeymoon ruined",
    "forcibly removed", "dragged off plane", "stuck on tarmac 3 hours",
    "stuck on tarmac 4 hours", "never got refund", "fighting for refund",
    "thousands of dollars", "had to buy new flight", "stranded in foreign country"
]

LEVEL_2_KEYWORDS = [
    "flight cancelled", "flight delayed", "missed connection",
    "lost luggage", "luggage delayed", "baggage claim nightmare",
    "overbooked", "bumped from flight", "involuntarily bumped",
    "no compensation", "terrible customer service", "no help from airline",
    "hidden fees", "charged for carry on", "charged for seat",
    "cramped", "no legroom", "uncomfortable", "declined service",
    "rude staff", "unhelpful", "couldn't reach customer service",
    "hours on hold", "no refund", "voucher instead of refund",
    "frequent flyer points worthless", "loyalty program devalued"
]

LEVEL_1_KEYWORDS = [
    "minor delay", "30 minute delay", "short delay",
    "uncomfortable seat", "small seat", "tight squeeze",
    "expensive airport food", "overpriced", "boarding chaos",
    "slow boarding", "general annoyance", "not great service",
    "could be better", "mildly frustrating"
]


class AirlineChaosEntry:
    """Single data point for airline chaos analysis"""

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

        # Check Level 3 (Crisis/Safety) first
        level_3_matches = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
        if level_3_matches >= 2:
            return 3

        # Check Level 2 (Significant Frustration)
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


class AirlineChaosCollector:
    """Manages airline chaos data collection and scoring"""

    def __init__(self):
        self.entries: List[AirlineChaosEntry] = []

    def add_entry(self, entry: AirlineChaosEntry):
        self.entries.append(entry)

    def calculate_official_score(self) -> float:
        """
        Calculate official data component (0-100 scale)
        Formula: ((Delay % × 2) + (Cancellation % × 3) + ((100 - ACSI) / 2)) / 3
        """
        delay_component = OFFICIAL_METRICS["delay_rate"] * 2
        cancellation_component = OFFICIAL_METRICS["cancellation_rate"] * 3
        satisfaction_component = (100 - OFFICIAL_METRICS["acsi_satisfaction"]) / 2

        official_score = (delay_component + cancellation_component + satisfaction_component) / 3
        return round(official_score, 2)

    def calculate_crisis_ratio(self) -> float:
        """Calculate percentage of Level 3 (crisis/safety) entries"""
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
            return "Smooth Skies Ahead"
        elif score < 30:
            return "Mild Turbulence"
        elif score < 50:
            return "Flight Attendants Nervous"
        elif score < 70:
            return "Oxygen Masks Deployed"
        elif score < 85:
            return "Emergency Landing Imminent"
        else:
            return "Brace For Impact"

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

    def export_csv(self, filename: str = "airline_chaos_data.csv"):
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

    def export_json(self, filename: str = "airline_chaos_data.json"):
        """Export collected data to JSON with scoring"""
        stats = self.get_stats()

        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "metric": "Airline Chaos",
                "stats": stats
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(self.entries)} entries to {filename}")
        print(f"\nFINAL AIRLINE CHAOS SCORE: {stats['final_score']}")
        print(f"Label: {stats['label']}")
        print(f"\nBreakdown:")
        print(f"  Official Score: {stats['official_score']}")
        print(f"  Crisis Ratio: {stats['crisis_ratio']}%")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("AIRLINE CHAOS DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nOFFICIAL METRICS (baseline):")
    for metric, value in OFFICIAL_METRICS.items():
        print(f"  - {metric}: {value}%")

    official_score = ((OFFICIAL_METRICS['delay_rate'] * 2 +
                      OFFICIAL_METRICS['cancellation_rate'] * 3 +
                      (100 - OFFICIAL_METRICS['acsi_satisfaction']) / 2) / 3)
    print(f"\nOFFICIAL SCORE: {official_score:.2f}")

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
        if i <= 10:
            print(f"     Collect 12-16 videos per query")

    print("\n" + "=" * 80)
    print("REDDIT COLLECTION:")
    print("=" * 80)
    print("Subreddits to sample:")
    for sub in REDDIT_SUBREDDITS:
        print(f"  - {sub} (collect ~25 posts)")
    print("\nSearch within each subreddit for:")
    for query in REDDIT_SEARCH_QUERIES:
        print(f"  - \"{query}\"")
    print("\nSampling method: Sort by 'hot' or 'top' (past month), take systematically")

    print("\n" + "=" * 80)
    print("TIKTOK COLLECTION:")
    print("=" * 80)
    print("Hashtags to search:")
    for tag in TIKTOK_HASHTAGS:
        print(f"  - {tag} (collect ~13 videos each)")

    print("\n" + "=" * 80)
    print("CATEGORIZATION LEVELS:")
    print("=" * 80)
    print("LEVEL 3 (CRISIS - Safety incidents/Major disruption):")
    print("  Safety: crash, near crash, emergency landing, engine failure, 737 Max,")
    print("          severe turbulence injuries, evacuation, fire/smoke in cabin")
    print("  Disruption: stranded 24+ hours, missed life events, lost critical luggage,")
    print("              damaged wheelchair, vacation ruined, refund battles")

    print("\nLEVEL 2 (SIGNIFICANT FRUSTRATION):")
    print("  Flight cancelled/delayed, missed connection, lost luggage, overbooked,")
    print("  no compensation, terrible service, hidden fees, cramped seats")

    print("\nLEVEL 1 (MILD ANNOYANCE):")
    print("  Minor delays, uncomfortable seats, expensive food, boarding chaos")

    print("\n" + "=" * 80)
    print("\nKEY ABSURDITY FACTORS:")
    print("  - Boeing safety failures (737 Max crashes, door blowout)")
    print("  - Wheelchair damage (disability rights violations)")
    print("  - Overbooking + forced removal (selling more tickets than seats)")
    print("  - Service shrinkflation (fees for everything, smaller seats)")
    print("  - Refund battles ('weather delay' excuses)")
    print("  - Zero passenger recourse when stranded")
    print("=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = AirlineChaosCollector()

# Add YouTube video entry (safety incident)
entry = AirlineChaosEntry(
    platform="youtube",
    content_id="abc123",
    title="Boeing 737 Max Door Blew Out Mid-Flight",
    content="Terrifying experience as cabin depressurized, oxygen masks deployed...",
    url="https://youtube.com/watch?v=abc123",
    date="2025-01-15"
)
collector.add_entry(entry)

# Add Reddit post entry (service failure)
entry = AirlineChaosEntry(
    platform="reddit",
    content_id="xyz789",
    title="Stranded in Chicago for 3 days, airline won't pay for hotel",
    content="Flight cancelled, next available flight in 72 hours, missed my sister's wedding...",
    url="https://reddit.com/r/travel/comments/xyz789",
    date="2025-12-05"
)
collector.add_entry(entry)

# View statistics and final score
print(collector.get_stats())

# Export data
collector.export_csv("airline_chaos_data.csv")
collector.export_json("airline_chaos_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
