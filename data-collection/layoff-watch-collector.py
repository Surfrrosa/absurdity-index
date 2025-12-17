#!/usr/bin/env python3
"""
Layoff Watch Data Collection Script
Systematic collection of layoff anxiety and job market despair sentiment
"""

import csv
import json
from datetime import datetime
from typing import List, Dict

# Search queries for systematic data collection
YOUTUBE_QUERIES = [
    "laid off can't find job",
    "applied to 500 jobs",
    "job search depression",
    "scared of layoffs",
    "layoff anxiety",
    "tech layoffs 2025",
    "mass layoffs",
    "job market terrible",
    "overqualified unemployed",
    "ghosted by recruiters"
]

REDDIT_SUBREDDITS = [
    "r/jobs",
    "r/cscareerquestions",
    "r/layoffs",
    "r/careerguidance",
    "r/unemployed",
    "r/jobsearchhacks"
]

REDDIT_SEARCH_QUERIES = [
    "laid off",
    "can't find job",
    "applied to hundreds",
    "scared of layoffs",
    "job search exhausting",
    "no interviews",
    "ghosted by companies",
    "overqualified"
]

TIKTOK_HASHTAGS = [
    "#laidoff",
    "#jobsearch",
    "#unemployed",
    "#layoffs",
    "#jobmarket",
    "#techlayoffs",
    "#careeradvice",
    "#jobhunting"
]

# Official data sources to track
OFFICIAL_METRICS = {
    "tech_layoffs_2025": 152922,  # Total tech workers laid off in 2025
    "companies_layoffs": 551,  # Number of companies with layoffs
    "unemployment_rate": 4.2,  # Current unemployment rate %
    "job_openings": 7440000  # Current job openings (JOLTS)
}

# Categorization criteria
LEVEL_3_KEYWORDS = [
    # Long-term unemployment crisis
    "can't find job", "no job offers", "applied to 500", "applied to 1000",
    "6 months unemployed", "year unemployed", "gave up looking",
    "stopped applying", "lost hope",

    # Financial crisis
    "running out of savings", "can't pay rent", "about to be homeless",
    "lost health insurance", "can't afford", "bankruptcy",
    "moving back with parents", "depleted savings",

    # Mental health crisis
    "suicidal", "depressed", "severe anxiety", "panic attacks",
    "crying every day", "mental breakdown", "therapy",
    "losing my mind", "can't take it anymore",

    # Laid off with severe impact
    "laid off with family", "laid off pregnant", "laid off medical condition",
    "visa expiring", "have to leave country",

    # Industry collapse fears
    "entire industry dying", "career is over", "skills obsolete",
    "AI taking jobs", "outsourced"
]

LEVEL_2_KEYWORDS = [
    # Active job search struggles
    "applied to hundreds", "no responses", "no interviews",
    "ghosted", "rejected", "overqualified", "underqualified",
    "entry level requires 5 years",

    # Layoff fear at current job
    "worried about layoffs", "company struggling", "rumors of layoffs",
    "updating resume", "looking for exit", "scared", "anxious",

    # Recently laid off
    "laid off last month", "laid off", "let go", "downsized",
    "position eliminated", "restructuring",

    # Job market frustration
    "terrible job market", "hundreds of applicants", "competition insane",
    "lowball offers", "temp jobs only", "contract work only",
    "companies not hiring"
]

LEVEL_1_KEYWORDS = [
    "job market tough", "competitive", "keeping eye on market",
    "updating LinkedIn", "networking", "brushing up resume",
    "considering options", "aware of layoffs"
]


class LayoffWatchEntry:
    """Single data point for layoff watch analysis"""

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
        """Categorize content based on keywords (1=Mild, 2=Anxious, 3=Crisis)"""
        text = (self.title + " " + self.content).lower()

        # Check Level 3 (Crisis) first
        level_3_matches = sum(1 for kw in LEVEL_3_KEYWORDS if kw in text)
        if level_3_matches >= 2:
            return 3

        # Check Level 2 (Anxious/Struggling)
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


class LayoffWatchCollector:
    """Manages layoff watch data collection and scoring"""

    def __init__(self):
        self.entries: List[LayoffWatchEntry] = []

    def add_entry(self, entry: LayoffWatchEntry):
        self.entries.append(entry)

    def calculate_official_score(self) -> float:
        """
        Calculate official data component (0-100 scale)
        Formula: (Layoff Count / 200000) × 100, capped at reasonable maximum
        """
        # Normalize layoff count to 0-100 scale
        # 200,000 layoffs = 100 score (very high)
        layoff_score = min((OFFICIAL_METRICS["tech_layoffs_2025"] / 200000) * 100, 100)

        return round(layoff_score, 2)

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
            return "Job Security Exists (???)"
        elif score < 30:
            return "Resume Updated Just In Case"
        elif score < 50:
            return "LinkedIn Learning Panic Mode"
        elif score < 70:
            return "Applied To 500 Jobs Achievement"
        elif score < 85:
            return "Industry-Wide Existential Crisis"
        else:
            return "Welcome To The Gig Economy Hellscape"

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

    def export_csv(self, filename: str = "layoff_watch_data.csv"):
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

    def export_json(self, filename: str = "layoff_watch_data.json"):
        """Export collected data to JSON with scoring"""
        stats = self.get_stats()

        data = {
            "metadata": {
                "collected_at": datetime.now().isoformat(),
                "metric": "Layoff Watch",
                "stats": stats
            },
            "entries": [entry.to_dict() for entry in self.entries]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(self.entries)} entries to {filename}")
        print(f"\nFINAL LAYOFF WATCH SCORE: {stats['final_score']}")
        print(f"Label: {stats['label']}")
        print(f"\nBreakdown:")
        print(f"  Official Score: {stats['official_score']}")
        print(f"  Crisis Ratio: {stats['crisis_ratio']}%")


def print_collection_guide():
    """Print systematic collection instructions"""
    print("=" * 80)
    print("LAYOFF WATCH DATA COLLECTION GUIDE")
    print("=" * 80)
    print("\nOFFICIAL METRICS (baseline):")
    for metric, value in OFFICIAL_METRICS.items():
        print(f"  - {metric}: {value}")

    official_score = min((OFFICIAL_METRICS["tech_layoffs_2025"] / 200000) * 100, 100)
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
    print("LEVEL 3 (CRISIS - Long-term unemployment/Financial crisis):")
    print("  Can't find job after months, applied to 500+, financial ruin,")
    print("  mental health crisis, visa issues, industry collapse fears")

    print("\nLEVEL 2 (ANXIOUS - Job search struggles/Layoff fear):")
    print("  Applied to hundreds, ghosted, overqualified, recently laid off,")
    print("  worried about layoffs at current job, terrible market")

    print("\nLEVEL 1 (MILD - Market awareness):")
    print("  Monitoring market, updating resume, aware of challenges")
    print("=" * 80)


def example_usage():
    """Example of how to use the collector"""
    print("\n" + "=" * 80)
    print("EXAMPLE USAGE:")
    print("=" * 80)
    print("""
# Initialize collector
collector = LayoffWatchCollector()

# Add entry
entry = LayoffWatchEntry(
    platform="reddit",
    content_id="abc123",
    title="Applied to 500 jobs, got 3 interviews",
    content="Been laid off for 8 months. Applied to over 500 positions, heard back from maybe 20, got 3 interviews, zero offers...",
    url="https://reddit.com/r/jobs/comments/abc123",
    date="2025-12-10"
)
collector.add_entry(entry)

# View stats and export
print(collector.get_stats())
collector.export_json("layoff_watch_data.json")
    """)
    print("=" * 80)


if __name__ == "__main__":
    print_collection_guide()
    example_usage()
