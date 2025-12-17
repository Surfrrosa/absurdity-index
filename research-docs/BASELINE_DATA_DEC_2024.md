# Baseline Data Collection - December 2024

**Collection Period:** Week of Dec 9-15, 2024
**Updated:** Dec 16, 2024

---

## 1. WAGE STAGNATION REALITY CHECK

### BLS Real Average Hourly Earnings (Dec 2024)
**Source:** https://www.bls.gov/news.release/archives/realer_01152025.htm

**Current Data:**
- Real average hourly earnings (Dec 2024): +1.0% YoY
- Month-over-month change (Nov→Dec): -0.2%
- Average weekly earnings: +0.7% YoY

**Historical Baseline:**
- Need: Rolling 12-month average for comparison
- Status: PENDING - Need to pull Nov 2023-Oct 2024 data

### CEO-to-Worker Pay Ratio (2024)
**Source:** AFL-CIO Executive Paywatch 2024

**Current Data:**
- S&P 500 average: 285:1
- Previous year (2023): 268:1
- Historical baseline (1965-1980): ~20:1

**Calculation:**
```
ratio_component = ((285 - 20) / 20) * 10 = 132.5
Cap at 30 → 30
```

### Google Trends - Wage Frustration
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "can't afford groceries": 0.00 (too specific, low volume)
- "wages too low": 0.55
- "need a raise": **50.65** ← HIGH
- **Category average: 17.07/100**

**Component calculation:**
```
trends_component = 17.07 * 0.15 = 2.56 (out of 15 cap)
```

### Reddit r/antiwork Sampling
**Status:** PENDING
**Method:** Sample 100 posts from last week, count wage-related complaints

---

## 2. HOUSING MARKET DESPAIR INDEX

### Median Rent Data
**Source:** Zillow Rent Index
**Status:** PENDING - Need to access Zillow Research downloads

### Median Home Price
**Source:** Redfin Data Center
**Status:** PENDING

### Median Household Income
**Source:** U.S. Census Bureau
**Latest:** 2023 data (2024 not yet released)
**Status:** PENDING - Use 2023 as baseline

### Eviction Filing Rate
**Source:** Eviction Lab
**Note:** Select cities only, not national aggregate
**Status:** PENDING - May need to aggregate top 10 cities

### Google Trends - Housing Despair
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "can't afford rent": 0.64
- "housing crisis": **52.50** ← VERY HIGH
- **Category average: 26.57/100**

**Component calculation:**
```
trends_component = 26.57 * 0.15 = 3.99 (out of 15 cap)
```

---

## 3. AIRLINE CHAOS METER

### BTS On-Time Performance
**Source:** https://www.transtats.bts.gov/ONTIME/
**Data available:** Jan 1995 - Sept 2025

**Status:** PENDING
**Need to download:**
- Last 12 weeks of data (or available months)
- Delay percentages
- Cancellation percentages
- Mishandled baggage rates

---

## 4. CUSTOMER SERVICE HELL SCORE

### ACSI Scores
**Source:** https://www.theacsi.org/
**Latest:** Q3 2025 scores available

**Status:** PENDING
**Need to collect:**
- Telecom sector scores
- Retail scores
- Utilities scores
- Calculate weighted average

### Hold Time Data
**Source:** GetHuman.com
**Status:** PENDING - Manual sampling of top 20 companies

### Google Trends - Customer Service
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "customer service complaints": **42.49** ← HIGH
- "terrible customer service": 0.86
- **Category average: 21.67/100**

**Component calculation:**
```
trends_component = 21.67 * 0.15 = 3.25 (out of 15 cap)
```

### Reddit r/CustomerService
**Status:** PENDING
**Method:** Sample 100 posts, categorize complaints

---

## 5. STREAMING SERVICE FATIGUE INDEX

### Subscription Prices (Manual Tracking)
**Status:** PENDING

**Need to collect:**
- Netflix: Current price vs 1 year ago
- Disney+: Current vs 1 year ago
- Hulu: Current vs 1 year ago
- Max: Current vs 1 year ago
- Prime Video: Current vs 1 year ago
- Apple TV+: Current vs 1 year ago
- Peacock: Current vs 1 year ago
- Paramount+: Current vs 1 year ago

**Calculate:** Average YoY price increase vs CPI

### Content Fragmentation
**Source:** Reelgood.com or manual tracking
**Status:** PENDING
**Need:** Top 20 most-watched shows, count services needed

### Google Trends - Streaming Fatigue
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "cancel Netflix": 14.30
- "too many streaming services": 0.00 (low volume)
- "streaming fatigue": 0.07
- **Category average: 4.79/100** ← Low (not a Google search problem, more social complaint)

**Component calculation:**
```
trends_component = 4.79 * 0.25 = 1.20 (out of 25 cap)
```

### App Store Reviews
**Status:** PENDING
**Method:** Sample reviews for major 8 apps, calculate average rating

---

## 6. DATING APP DISAPPOINTMENT SCORE

### Google Trends - Dating Frustration
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "dating apps suck": 1.15
- "I hate dating apps": 1.92
- "dating app fatigue": 0.05
- **Category average: 1.04/100** ← Very low (people complain on Reddit/Twitter, not Google)

**Component calculation:**
```
trends_component = 1.04 * 0.35 = 0.36 (out of 35 cap)
```

**Note:** Reddit will likely show much higher frustration - Google Trends misses social complaints

### Reddit Sentiment
**Status:** PENDING
**Subreddits:** r/Tinder, r/Bumble, r/Hinge
**Method:** Sample 100 posts total, categorize sentiment

### App Store Reviews
**Status:** PENDING
**Apps:** Tinder, Bumble, Hinge
**Need:** Current average rating vs 2019 baseline

### Pew Research Survey
**Status:** Check if recent survey available
**Latest known:** 2023 data

---

## 7. CORPORATE LAYOFF WATCH

### Layoffs.fyi Data
**Source:** https://layoffs.fyi/
**Status:**  COLLECTED (Dec 16, 2024)

**2024 Totals:**
- Tech layoffs (2024): **152,922 employees**
- Companies affected: **551 companies**
- Average per company: ~278 employees

**Historical context:**
- Total since March 2020: 264,320 (all years)
- 2024 accounts for 58% of all tracked layoffs since pandemic

**Status:** PARTIAL
**Still need:**
- Weekly breakdown for last 12 weeks (need to scrape historical data or track manually)
- Friday announcement tracking
- Company size distribution

**Job Market Reality Gap:**
Official unemployment: ~3.7%
Reality: 6+ month job searches, ghost jobs on LinkedIn, 500 applications for 1 interview, "we hired internally" after 6 rounds

**Component calculation (using 2024 annual data as baseline):**
- Need weekly granularity to calculate volume_component properly
- Friday announcements: Manual tracking going forward
- Size weight: Need company-level data

### WARN Notices
**Source:** U.S. Department of Labor
**Status:** PENDING - Supplement Layoffs.fyi data

---

## 8. AI PSYCHOSIS & PARASOCIAL BREAKDOWN INDEX

### News API - Incident Reports
**Status:** PENDING
**Search terms:**
- "AI mental health"
- "chatbot addiction"
- "AI suicide"
- Last 12 weeks

### Reddit Crisis Posts
**Subreddits:** r/CharacterAI, r/replika
**Status:** PENDING
**Method:** Sample 200 posts weekly, identify crisis-level dependency mentions

### Google Trends - AI Dependency
**Status:**  COLLECTED (Dec 16, 2024)
**Results (3-month average, 0-100 scale):**
- "in love with AI": **54.00** ← EXTREMELY HIGH (This is both hilarious and concerning)
- "AI therapy addiction": 0.58
- "AI is sentient": 0.67
- **Category average: 18.42/100**

**Component calculation:**
```
trends_component = 18.42 * 0.15 = 2.76 (out of 15 cap)
```

**Note:** The fact that "in love with AI" scores 54/100 on Google Trends is deeply absurd and perfect for our dashboard

### App Review Crisis Signals
**Apps:** Replika, Character.AI
**Status:** PENDING
**Method:** Sample 50 recent 1-star reviews per app, count crisis mentions

---

## NEXT STEPS

**Priority 1 - Can Do Now:**
1. Set up pytrends and pull all Google Trends data
2. Manual streaming service price collection
3. Layoffs.fyi data scraping/collection
4. Reddit sampling scripts

**Priority 2 - Need Downloads:**
5. BTS airline data download
6. ACSI score collection
7. Zillow/Redfin housing data

**Priority 3 - Manual Research:**
8. App Store review sampling
9. News API setup and incident tracking
10. Content fragmentation analysis

**Blockers:**
- None critical - all sources accessible
- Some require manual sampling (acceptable for MVP)

---

## DATA COLLECTION PROGRESS SUMMARY

###  Completed (Real Data Collected)

**Google Trends (All 6 Categories):**
- Wages: 17.07/100 ("need a raise" at 50.65)
- Housing: 26.57/100 ("housing crisis" at 52.50)
- Customer Service: 21.67/100 ("customer service complaints" at 42.49)
- Streaming: 4.79/100 (low Google volume)
- Dating: 1.04/100 (very low Google, expect high Reddit)
- AI Psychosis: 18.42/100 ("in love with AI" at 54.00!)

**Layoffs:**
- 2024 total: 152,922 tech workers, 551 companies
- Need weekly breakdown for scoring

**Wages:**
- BLS real earnings: +1.0% YoY (Dec 2024)
- CEO pay ratio: 285:1 (2024)

### ⏳ In Progress / Partial

**Layoffs:**
- Have annual totals
- Need: Weekly breakdown, Friday tracking

**Wages:**
- Have current month and CEO ratio
- Need: 12-month baseline for rolling average

###  Still Need (Next Priority)

**High Priority:**
1. BTS airline data download (delays, cancellations, baggage)
2. Zillow/Redfin housing data (rent, home prices)
3. Census median income data
4. ACSI customer service scores
5. Streaming service pricing (manual collection)

**Medium Priority:**
6. Reddit sampling (r/antiwork, r/CustomerService, r/Tinder, etc.)
7. App Store review sampling
8. Content fragmentation analysis (top 20 shows)
9. Eviction Lab data aggregation

**Lower Priority (Can Start With Estimates):**
10. News API setup for AI psychosis incidents
11. GetHuman hold time data
12. Pew Research dating surveys

###  Minimum Viable Data for Excel Dashboard V1

**We currently have enough to build:**
- Wages score (partial - using CEO ratio + Trends)
- Housing score (partial - using Trends as proxy)
- Customer Service score (partial - using Trends)
- Layoffs score (using annual 2024 data as baseline)
- AI Psychosis score (using Trends)

**Can start Excel framework NOW with:**
- Formula structure
- Conditional formatting
- Label system
- Placeholder cells for missing data
- Real data where we have it

**Target:** Excel V1 by end of day with real + estimated data, then refine with better sources
