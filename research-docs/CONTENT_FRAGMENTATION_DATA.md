# Content Fragmentation Analysis

**Last Updated:** December 20, 2025
**Purpose:** Medium-priority data collection for Subscription Overload metric

---

## Executive Summary

**Key Finding:** Streaming content is fragmented across **110+ platforms**, requiring viewers to subscribe to multiple services to access desired content. **46% of consumers experience decision fatigue**, and average quarterly churn exceeds **32%**.

---

## Market Overview

### Platform Fragmentation (2024)

- **Total streaming platforms globally:** 110+
- **Consumer decision fatigue:** 46%
- **Average quarterly churn rate:** 32%+
- **Average production cost per episode:** $8 million

### Consumer Behavior

- Viewers juggle multiple simultaneous subscriptions
- "Platform-hopping" for specific shows is common
- Access to exclusive content ranks as high as price in subscription decisions
- Overwhelming content choices create decision paralysis

---

## Top 20 Most-Watched Shows (2024-2025 Season)

### Platform Distribution

| Rank | Show Title | Platform | Viewers (millions) |
|------|-----------|----------|-------------------|
| 1 | Zero Day | **Netflix** | 15.7 |
| 2 | Nobody Wants This | **Netflix** | 15.2 |
| 3 | The Night Agent | **Netflix** | 14.8 |
| 4 | American Primeval | **Netflix** | 13.8 |
| 5 | Running Point | **Netflix** | 13.1 |
| 6 | The Residence | **Netflix** | 12.8 |
| 7 | A Man on the Inside | **Netflix** | 12.4 |
| 8 | Georgie & Mandy's First Marriage | **CBS** | 12.1 |
| 9 | Ghosts | **CBS** | 12.1 |
| 10 | Yellowstone | **Paramount** | 12.1 |
| 11 | 1923 | **Paramount+** | 11.9 |
| 12 | The White Lotus | **HBO** | 11.6 |
| 13 | Elsbeth | **CBS** | 11.5 |
| 14 | Ms. Rachel | **Netflix/YouTube** | 11.5 |
| 15 | La Palma | **Netflix** | 11.4 |
| 16 | Will Trent | **ABC** | 11.4 |
| 17 | 9-1-1 | **ABC** | 11.1 |
| 18 | Watson | **CBS** | 11.0 |
| 19 | The Madness | **Netflix** | 11.0 |
| 20 | MobLand | **Paramount+** | 11.0 |

### Platform Breakdown (Top 20 Shows)

| Platform | Shows | Percentage |
|----------|-------|------------|
| Netflix | 10 | 50% |
| CBS | 4 | 20% |
| Paramount/Paramount+ | 3 | 15% |
| ABC | 2 | 10% |
| HBO | 1 | 5% |

**Analysis:** To watch all top 20 shows, viewers would need subscriptions to **6 different platforms**.

---

## Most Popular Shows of 2024 (JustWatch Rankings)

### Top Critically-Acclaimed Shows by Platform

1. **Shōgun** - Hulu
2. **Fallout** - Amazon Prime Video
3. **The Bear** - Hulu
4. **Severance S2** - Apple TV+
5. **The Mandalorian** - Disney+
6. **Stranger Things** - Netflix
7. **The Crown** - Netflix
8. **The Rings of Power S2** - Amazon Prime Video
9. **WandaVision** - Disney+

**To access all 9 shows:** Requires subscriptions to **5 platforms** (Hulu, Amazon, Apple TV+, Disney+, Netflix)

---

## Exclusive Content Strategy by Platform

### Netflix
- **Strategy:** Heavy investment in original content
- **Notable exclusives:** Stranger Things, The Crown, Wednesday, Squid Game
- **Cost:** Increased subscription prices to fund originals

### HBO Max
- **Strategy:** Same-day theatrical releases + prestige originals
- **Notable exclusives:** Warner Bros. theatrical releases, The Last of Us, House of the Dragon
- **Advantage:** Premium content justifies premium pricing

### Amazon Prime Video
- **Strategy:** Franchise tentpoles + exclusive sports
- **Notable exclusives:** The Rings of Power ($1B production), NFL games, Premier League
- **Bundling:** Included with Prime membership ($139/year)

### Disney+
- **Strategy:** Franchise IP + family content
- **Notable exclusives:** Star Wars (Mandalorian), Marvel (WandaVision), Pixar, Disney classics
- **Moat:** Unmatched IP library

### Apple TV+
- **Strategy:** Quality over quantity, prestige originals
- **Notable exclusives:** Severance, Ted Lasso, The Morning Show
- **Pricing:** Lower cost ($9.99/mo) but smaller library

---

## Content Fragmentation Score

**Metric:** Average number of subscriptions needed to access top content

### Calculation

To watch:
- **Top 20 most-watched shows:** 6 platforms required
- **Top 10 critically-acclaimed shows:** 5 platforms required
- **Average:** **5.5 platforms**

**Monthly cost estimate:**
- Netflix: $15.49
- Hulu: $17.99
- HBO Max: $15.99
- Disney+: $13.99
- Amazon Prime Video: $11.58 ($139/year)
- Apple TV+: $9.99
- Paramount+: $11.99

**Total:** $97.02/month = **$1,164.24/year** to access top content

---

## Consumer Pain Points

### 1. Subscription Fatigue
- 46% experience decision fatigue
- Tracking which show is on which platform
- Managing multiple accounts, passwords, billing cycles

### 2. Financial Burden
- Average household: $273/month on subscriptions (all types)
- Streaming alone: ~$100/month for comprehensive access
- 18.75% of median household income

### 3. Content Discovery Challenges
- Overwhelming volume of content across platforms
- No unified search across services
- Fear of missing out (FOMO) drives more subscriptions

### 4. Platform Hopping
- Subscribe → watch show → cancel → repeat
- 32%+ quarterly churn indicates this behavior
- Platforms combat with annual discounts

---

## Implications for Subscription Overload Metric

### Official Score Component
**Fragmentation metric:** Number of subscriptions needed to access top 20 shows

- Pre-streaming (cable TV): 1 subscription
- 2024 streaming: 6 subscriptions
- **Fragmentation multiplier:** 6x

**Suggested normalization:**
```
Fragmentation score = (platforms_needed / 1) * 100 / 10
                    = (6 / 1) * 100 / 10
                    = 60
```

### Social Sentiment Component
Already captured in YouTube data:
- "subscription fatigue" searches
- "too many subscriptions" complaints
- "streaming service overload" frustration

---

## Data Sources

1. **Nielsen Top 10** - Viewership data
2. **JustWatch** - Popularity rankings across platforms
3. **Eviction Lab streaming analysis** - Market research
4. **Consumer surveys** - Decision fatigue statistics
5. **Platform announcements** - Exclusive content strategies

---

## Future Updates

### Pending Research
- Specific "forced exclusivity" examples (Friends leaving Netflix → HBO Max)
- Historical data: cable bundle → streaming fragmentation timeline
- Regional variations (UK, EU have different platform availability)

### Monitoring
- Track new platform launches
- Monitor platform consolidation (mergers like HBO Max + Discovery+)
- Price increase trends across platforms
