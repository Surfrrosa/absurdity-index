# The Predictable Disappointments Dashboard

**"A weekly index of everything that reliably sucks."**

---

## Project Overview

**What:** A data-backed weekly index quantifying everyday American frustrations

**Why:** Part satire, part social commentary, all signal

**Tone:** Dark, deadpan, devastatingly accurate

**Methodology:** Real data, transparent sources, minimal bias, reproducible results

**Portfolio Positioning:**
- Unique (not another B2B dashboard)
- Shareable (people will actually send this around)
- Real data with documented methodology
- Demonstrates analytical rigor + cultural intelligence + humor
- Shows you can make data engaging without sacrificing accuracy

---

## The 8 Core Metrics

### TIER 1: ECONOMIC BRUTALITY

---

### 1. Wage Stagnation Reality Check (0-100)

**What it measures:** The gap between wage growth and actual purchasing power

**Data Sources:**
- U.S. Bureau of Labor Statistics (BLS) - Real Average Hourly Earnings (https://www.bls.gov/data/)
- Consumer Price Index (CPI) - BLS (updated monthly)
- AFL-CIO Executive Paywatch - CEO-to-worker pay ratio (annual)
- Google Trends API - "can't afford groceries", "wages too low", "need a raise"
- Reddit r/antiwork - wage complaint volume (manual sampling, n=100 posts/week)

**Methodology:**

**Step 1: Real Wage Change**
```
real_wage_change = ((current_real_wage - baseline_real_wage) / baseline_real_wage) * 100
baseline = rolling 12-month average

If real_wage_change < 0: wage_component = abs(real_wage_change) * 10
If real_wage_change >= 0: wage_component = 0
Cap at 50 (prevents single month from dominating)
```

**Step 2: CEO Pay Ratio Component**
```
Historical baseline (1965-1980 avg): ~20:1
Current ratio: ~300:1+

ratio_component = ((current_ratio - 20) / 20) * 10
Cap at 30
```

**Step 3: Google Trends Component**
```
Normalized index (0-100 from Google)
trends_component = avg("can't afford groceries", "wages too low") * 0.15
Cap at 15
```

**Step 4: Reddit Sentiment**
```
Sample 100 posts from r/antiwork weekly
complaint_ratio = (posts mentioning wage frustration / 100) * 100 * 0.05
Cap at 5
```

**Final Score:**
```
wage_stagnation_score = wage_component + ratio_component + trends_component + complaint_ratio
Range: 0-100
```

**Thresholds:**
- 0-20: "Economy Working as Intended"
- 20-40: "Inflation Exists But Manageable"
- 40-60: "Your Raise Was an Insult"
- 60-80: "Wages Are a Polite Suggestion"
- 80-100: "Return to Barter System Imminent"

**Bias Mitigation:**
- Use BLS data (peer-reviewed, government source)
- Rolling averages prevent single-month spikes
- Multiple data sources prevent single-point failure
- Reddit sampling randomized by day/time
- Document any manual adjustments

---

### 2. Housing Market Despair Index (0-100)

**What it measures:** Housing affordability crisis and rental market dysfunction

**Data Sources:**
- Zillow Rent Index API (https://www.zillow.com/research/data/)
- U.S. Census Bureau - Median household income (annual)
- National Association of Realtors (NAR) - Housing Affordability Index (monthly)
- Eviction Lab - Princeton University (https://evictionlab.org/)
- Google Trends - "can't afford rent", "housing crisis"
- Redfin Data Center - Median home prices (https://www.redfin.com/news/data-center/)

**Methodology:**

**Step 1: Rent Burden Ratio**
```
Standard: Rent should be ≤30% of gross income
Current median rent: From Zillow Rent Index
Current median income: From Census Bureau

rent_burden = (median_monthly_rent * 12) / median_household_income
If rent_burden > 0.30:
  rent_component = ((rent_burden - 0.30) / 0.30) * 100 * 0.35
Cap at 35
```

**Step 2: Home Price to Income Ratio**
```
Historical sustainable ratio: ~3.5x annual income
Current ratio: median_home_price / median_household_income

If current_ratio > 3.5:
  price_component = ((current_ratio - 3.5) / 3.5) * 100 * 0.30
Cap at 30
```

**Step 3: Eviction Filing Rate**
```
Baseline: Pre-pandemic eviction filing rate (2019)
Current: Eviction Lab weekly data

eviction_component = ((current_rate - baseline_rate) / baseline_rate) * 100 * 0.20
Cap at 20
```

**Step 4: Housing Despair Trends**
```
Google Trends normalized index
trends_component = avg("can't afford rent", "housing crisis") * 0.15
Cap at 15
```

**Final Score:**
```
housing_despair_score = rent_component + price_component + eviction_component + trends_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Homeownership Feels Achievable"
- 20-40: "Aggressive Budgeting Required"
- 40-60: "Roommates Forever"
- 60-80: "Your Parents' Basement Looks Nice Actually"
- 80-100: "Welcome to Feudalism 2.0"

**Bias Mitigation:**
- Use only national medians (not cherry-picked cities)
- Compare to historical sustainable ratios (not arbitrary)
- Eviction data from academic source (peer-reviewed)
- Document geographic limitations (national vs regional)

---

### TIER 2: DAILY GRIND / MODERN LIFE DISAPPOINTMENT

---

### 3. Airline Chaos Meter (0-100)

**What it measures:** Flight reliability and passenger experience quality

**Data Sources:**
- Bureau of Transportation Statistics (BTS) On-Time Performance (https://www.transtats.bts.gov/)
- BTS Air Travel Consumer Report - Mishandled Baggage
- FlightAware API (optional supplementary data)

**Methodology:**

**Step 1: Delayed Flights**
```
Baseline acceptable: 15% delayed flights (industry standard)
Current: BTS on-time performance data

If current_delayed_pct > 15:
  delay_component = ((current_delayed_pct - 15) / 15) * 100 * 0.40
Else:
  delay_component = 0
Cap at 40
```

**Step 2: Canceled Flights**
```
Baseline acceptable: 2% cancellations
Current: BTS cancellation data

If current_canceled_pct > 2:
  cancel_component = ((current_canceled_pct - 2) / 2) * 100 * 0.45
Else:
  cancel_component = 0
Cap at 45
```

**Step 3: Lost/Mishandled Baggage**
```
Baseline: 3.5 per 1,000 passengers (historical average)
Current: BTS mishandled baggage reports

If current_rate > 3.5:
  baggage_component = ((current_rate - 3.5) / 3.5) * 100 * 0.15
Else:
  baggage_component = 0
Cap at 15
```

**Final Score:**
```
airline_chaos_score = delay_component + cancel_component + baggage_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Miracle?"
- 20-45: "Mild Turbulence"
- 45-70: "Bring Snacks + Emotional Support Animal"
- 70-85: "Air Travel is a Social Experiment"
- 85-100: "Abandon Sky"

**Bias Mitigation:**
- Use only BTS data (comprehensive, government source)
- National aggregates (not cherry-picked airlines or routes)
- Compare to historical industry standards
- Account for seasonal variation (use same-month YoY comparison)

---

### 4. Customer Service Hell Score (0-100)

**What it measures:** Customer service quality and accessibility

**Data Sources:**
- American Customer Satisfaction Index (ACSI) - Quarterly reports (https://www.theacsi.org/)
- GetHuman.com - Crowdsourced average hold times
- Reddit r/CustomerService - Complaint volume sampling
- Google Trends - "customer service complaints", "terrible customer service"

**Methodology:**

**Step 1: Hold Time Component**
```
Baseline acceptable: 5 minutes average hold time
Current: GetHuman.com aggregated data for top 20 companies

hold_time_component = (avg_hold_minutes / 60) * 100 * 0.35
If > 35: cap at 35
```

**Step 2: ACSI Score (Inverted)**
```
ACSI scores range 0-100 (higher = better satisfaction)
Industry baseline: 75 (historical average)

If current_acsi < 75:
  acsi_component = ((75 - current_acsi) / 75) * 100 * 0.35
Else:
  acsi_component = 0
Cap at 35
```

**Step 3: Reddit Complaint Sampling**
```
Sample 100 posts from r/CustomerService weekly
Baseline: Establish 4-week average complaint ratio

complaint_component = (current_week_ratio / baseline_ratio) * 100 * 0.15
Cap at 15
```

**Step 4: Google Trends**
```
Normalized search volume for customer service frustration

trends_component = avg("customer service complaints", "terrible customer service") * 0.15
Cap at 15
```

**Final Score:**
```
customer_service_score = hold_time_component + acsi_component + complaint_component + trends_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Humans Helping Humans"
- 20-40: "Minor Annoyance"
- 40-60: "Spirit Leaving Body"
- 60-80: "Existential Crisis Hold Music"
- 80-100: "Just Throw the Whole Company Away"

**Bias Mitigation:**
- Use ACSI (academically rigorous, third-party)
- GetHuman data is crowdsourced but large sample
- Reddit sampling randomized
- Compare to historical baselines, not arbitrary thresholds

---

### 5. Streaming Service Fatigue Index (0-100)

**What it measures:** Streaming subscription burden and content fragmentation

**Data Sources:**
- Manual tracking: Netflix, Disney+, Hulu, Max, Prime, Apple TV+, Peacock, Paramount+ pricing
- Reelgood.com - Content distribution data (which shows are on which platforms)
- Google Trends - "cancel Netflix", "too many streaming services", "streaming fatigue"
- App Store/Google Play - Review scores for major streaming apps
- Reddit r/cordcutters, r/Piracy - Sentiment sampling

**Methodology:**

**Step 1: Price Increase Rate**
```
Baseline: CPI inflation rate (general price increases)
Current: Average YoY price increase across major 8 platforms

price_component = ((streaming_increase_pct - cpi_increase_pct) / cpi_increase_pct) * 100 * 0.30
If negative (prices decreased): component = 0
Cap at 30
```

**Step 2: Fragmentation Index**
```
Sample top 20 most-watched shows (Nielsen or Reelgood data)
Count: How many different services needed to watch all 20

Baseline: 3 services (historical bundled cable equivalent)

fragmentation_component = ((services_needed - 3) / 3) * 100 * 0.25
Cap at 25
```

**Step 3: Cancellation Intent Trends**
```
Google Trends for cancellation-related searches

trends_component = avg("cancel Netflix", "too many streaming services") * 0.25
Cap at 25
```

**Step 4: App Review Score Decline**
```
Baseline: Average app rating from 2020 (pre-price-hike era)
Current: Average rating across major 8 apps

If current_avg < baseline_avg:
  review_component = ((baseline_avg - current_avg) / baseline_avg) * 100 * 0.20
Else:
  review_component = 0
Cap at 20
```

**Final Score:**
```
streaming_fatigue_score = price_component + fragmentation_component + trends_component + review_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Affordable Entertainment"
- 20-40: "Budget-Conscious Streaming"
- 40-60: "Subscription Fatigue Setting In"
- 60-80: "Piracy Looks Good Again"
- 80-100: "Just Stare at the Wall"

**Bias Mitigation:**
- Compare price increases to CPI (context matters)
- Use top 20 shows (not cherry-picked content)
- App review baselines prevent single bad week from skewing
- Multiple independent data sources

---

### 6. Dating App Disappointment Score (0-100)

**What it measures:** Dating app user satisfaction and frustration levels

**Data Sources:**
- Google Trends - "dating apps suck", "I hate dating apps", "dating app fatigue"
- Pew Research Center - Online dating surveys (periodic)
- Reddit r/Tinder, r/Bumble, r/Hinge - Sentiment sampling
- App Store/Google Play - Review scores for Tinder, Bumble, Hinge
- Academic research - Match-to-date conversion rates (published papers)

**Methodology:**

**Step 1: Google Trends Frustration Index**
```
Aggregate search volume for negative dating app queries

trends_component = avg("dating apps suck", "I hate dating apps", "dating app fatigue") * 0.35
Cap at 35
```

**Step 2: Reddit Sentiment Ratio**
```
Sample 100 posts weekly from r/Tinder, r/Bumble, r/Hinge combined
Categorize: Positive, Neutral, Negative

complaint_ratio = (negative_posts / total_posts) * 100 * 0.30
Cap at 30
```

**Step 3: App Review Score Decline**
```
Baseline: Average app rating from 2019 (pre-subscription-heavy era)
Current: Average rating across Tinder, Bumble, Hinge

If current_avg < baseline_avg:
  review_component = ((baseline_avg - current_avg) / baseline_avg) * 100 * 0.20
Else:
  review_component = 0
Cap at 20
```

**Step 4: Survey Data (When Available)**
```
Pew Research satisfaction scores (if recent survey available)
Convert satisfaction score to disappointment score

survey_component = (100 - satisfaction_pct) * 0.15
Cap at 15
```

**Final Score:**
```
dating_app_score = trends_component + complaint_ratio + review_component + survey_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Love May Actually Be Real"
- 20-40: "Meh But Manageable"
- 40-60: "Lower Your Standards or Expectations"
- 60-80: "The Streets Are Cold"
- 80-100: "Delete the Apps, Move to a Commune"

**Bias Mitigation:**
- Reddit sampling stratified across multiple subreddits
- Compare to historical baselines (not arbitrary)
- Use Pew Research when available (peer-reviewed)
- Multiple independent frustration signals

---

### TIER 3: EXISTENTIAL NIGHTMARE

---

### 7. Corporate Layoff Watch (0-100)

**What it measures:** Job security and corporate workforce reduction trends

**Data Sources:**
- Layoffs.fyi - Tech layoffs database (https://layoffs.fyi/)
- U.S. Department of Labor WARN notices (https://www.dol.gov/agencies/eta/layoffs/warn)
- Bureau of Labor Statistics - Mass layoff statistics
- LinkedIn - Layoff announcement tracking (manual)
- TechCrunch, The Verge - News RSS feeds for layoff headlines

**Methodology:**

**Step 1: Weekly Layoff Volume vs Baseline**
```
Calculate rolling 12-week average layoff count (baseline)
Current week layoff count from Layoffs.fyi + WARN notices

If current_week > baseline:
  volume_component = ((current_week - baseline) / baseline) * 100 * 0.50
Else:
  volume_component = 0
Cap at 50
```

**Step 2: Surprise Friday Announcement Bonus**
```
Industry pattern: Friday layoffs are often rushed/poorly handled
Track: What % of weekly layoffs announced on Friday

friday_bonus = (friday_layoffs / total_layoffs) * 100 * 0.25
Cap at 25
```

**Step 3: Company Size Weight**
```
Larger layoffs = bigger social impact
Weight by employee count affected

size_weight = (avg_employees_per_layoff / 1000) * 100 * 0.25
Cap at 25
```

**Final Score:**
```
layoff_watch_score = volume_component + friday_bonus + size_weight
Range: 0-100
```

**Thresholds:**
- 0-20: "Job Security Exists (???)."
- 20-40: "Polite Restructuring."
- 40-60: "Update LinkedIn."
- 60-80: "Start a Substack."
- 80-100: "Nobody Is Safe, Touch Grass."

**Bias Mitigation:**
- Use rolling baseline (accounts for seasonal trends)
- Combine multiple sources (Layoffs.fyi + WARN + BLS)
- Weight by impact (not just raw count)
- Document tech sector bias (Layoffs.fyi is tech-heavy)

---

### 8. AI Psychosis & Parasocial Breakdown Index (0-100)

**What it measures:** AI-related mental health incidents and parasocial dependency

**Data Sources:**
- News API - AI mental health incident reports
- Reddit r/CharacterAI, r/replika - Crisis post tracking
- Google Trends - "in love with AI", "AI therapy addiction", "AI is sentient"
- App Store/Google Play - Replika, Character.AI crisis reviews (1-star mentioning harm/dependency)
- Academic papers - AI-related mental health case studies (PubMed, arXiv)

**Methodology:**

**Step 1: Reported Incident Count**
```
Track verified news reports of AI-related mental health crises
Sources: News API search for "AI mental health", "chatbot addiction", "AI suicide"

Baseline: Establish 4-week rolling average
incident_component = (current_week_incidents / baseline) * 100 * 0.35
Cap at 35
```

**Step 2: Parasocial Crisis Posts**
```
Sample 200 posts weekly from r/CharacterAI, r/replika
Categorize: Crisis-level dependency (mentions of harm, can't stop, replacing real relationships)

crisis_ratio = (crisis_posts / 200) * 100 * 0.25
Cap at 25
```

**Step 3: Sentience Belief Tracking**
```
Count posts/comments claiming AI is sentient or has feelings (unironic)
Reddit, Twitter sampling

belief_component = (sentience_belief_mentions / baseline) * 100 * 0.20
Cap at 20
```

**Step 4: Google Trends Dependency Signals**
```
Search volume for AI addiction/dependency terms

trends_component = avg("in love with AI", "AI therapy addiction") * 0.15
Cap at 15
```

**Step 5: App Review Crisis Signals**
```
1-star reviews mentioning "addicted", "can't stop", "replacing real people", "depressed"
Sample 50 recent reviews per app (Replika, Character.AI)

crisis_review_component = (crisis_reviews / total_sampled) * 100 * 0.05
Cap at 5
```

**Final Score:**
```
ai_psychosis_score = incident_component + crisis_ratio + belief_component + trends_component + crisis_review_component
Range: 0-100
```

**Thresholds:**
- 0-20: "Healthy Relationship With Technology"
- 20-40: "Slightly Too Attached to ChatGPT"
- 40-60: "Blurring Lines Between Real and Artificial"
- 60-80: "Your AI Girlfriend Isn't Real, Seek Help"
- 80-100: "We Invented Loneliness Machines"

**Bias Mitigation:**
- Use only verified news reports (not rumors)
- Reddit sampling stratified by day/time
- Define "crisis" clearly (mentions of harm, not just heavy use)
- Rolling baselines prevent single incident from skewing
- **Ethical note:** This metric critiques the technology/companies, not the individuals suffering

---

## The Composite Score: Disappointment Density Index

**Formula:**
```
Disappointment Density Index =
  (WageStagnation * 0.15) +
  (Housing * 0.15) +
  (Airlines * 0.13) +
  (CustomerService * 0.12) +
  (Streaming * 0.10) +
  (Dating * 0.10) +
  (Layoffs * 0.15) +
  (AIPsychosis * 0.10)

Total weights = 1.00 (100%)
Range: 0-100
```

**Weighting Rationale:**
- **Economic pain** (Wages, Housing): 30% combined - Most impactful to daily life
- **Job security** (Layoffs): 15% - Existential threat to livelihood
- **Service quality** (Airlines, Customer Service): 25% combined - Universal frequent frustrations
- **Modern life** (Streaming, Dating): 20% combined - Cultural zeitgeist, less severe impact
- **Emerging risk** (AI Psychosis): 10% - Novel threat, smaller current population affected

**Thresholds:**
- 0-20: "Society Functioning Within Expected Parameters."
- 20-40: "Manageable Existential Dread."
- 40-60: "High Annoyance Probability."
- 60-80: "Brace for Impact."
- 80-100: "Why Did We Leave the Garden of Eden?"

**Validation Checks:**
- All weights sum to 1.00
- All component scores capped at stated maximums
- Rolling baselines updated weekly
- Historical comparison data documented

---

## Data Collection Standards

### General Principles

1. **Transparency:** All data sources publicly documented
2. **Reproducibility:** Anyone should be able to recreate scores with same inputs
3. **Consistency:** Same methodology applied week-over-week
4. **Validation:** Cross-reference multiple sources when possible
5. **Baseline Integrity:** Use historical data, not arbitrary thresholds
6. **Bias Documentation:** Note limitations and potential biases

### Data Quality Checklist

**For each metric:**
- [ ] Primary source is authoritative (government, academic, or industry standard)
- [ ] Backup sources available if primary fails
- [ ] Baseline period clearly defined (typically 12-month rolling average)
- [ ] Normalization method documented
- [ ] Caps prevent single outliers from dominating
- [ ] Manual data collection process is randomized/stratified
- [ ] Seasonal adjustments noted where relevant

### Update Schedule

**Weekly (Every Monday 9am):**
- BTS airline data (updated weekly)
- Layoffs.fyi scraping
- Google Trends pulls
- Reddit sentiment sampling
- News API queries
- App review sampling

**Monthly:**
- BLS wage data (updated monthly)
- ACSI scores (updated quarterly, check monthly)
- Zillow Rent Index
- NAR housing data

**Quarterly:**
- Pew Research survey checks
- Academic paper reviews
- Methodology review and refinement

**Annual:**
- CEO pay ratio update
- Historical baseline recalculation
- Formula weight review

---

## Research Best Practices

### Avoiding Common Biases

**Selection Bias:**
- Use national aggregates, not cherry-picked cities/companies
- Sample Reddit posts randomly (not just "hot" or "top")
- Include full week of data (not just bad days)

**Confirmation Bias:**
- Let data determine scores (don't adjust to make things look worse)
- Document when scores are LOW (good weeks happen)
- Include offsetting factors (e.g., compare streaming prices to CPI)

**Recency Bias:**
- Use rolling averages (not single data points)
- Compare to same period prior year (account for seasonality)
- Weight recent data appropriately but not exclusively

**Measurement Bias:**
- Define categories clearly before sampling (not after)
- Use consistent categorization rules
- Inter-rater reliability for manual sampling (if multiple people involved)

### Data Source Hierarchy

**Tier 1 (Highest reliability):**
- Government sources (BLS, BTS, Census)
- Academic institutions (Pew, Eviction Lab)
- Industry standards (ACSI, NAR)

**Tier 2 (Reliable with documentation):**
- Established data providers (Zillow, Redfin)
- News API aggregates
- Google Trends (directional, not absolute)

**Tier 3 (Supplementary):**
- Reddit sampling (subjective but real signal)
- App reviews (self-selected but valuable)
- Manual news tracking

**Never use:**
- Single anecdotes without verification
- Unverified social media claims
- Data sources with undisclosed methodology

### Validation Methods

**Internal Consistency:**
- Do component scores align logically?
- Are there unexpected correlations?
- Document and investigate anomalies

**External Validation:**
- Do scores match general sentiment/news?
- Cross-check with other indices when available
- Note when dashboard diverges from conventional wisdom (and why)

**Sensitivity Analysis:**
- How much do scores change if one data source is removed?
- What if weights are adjusted ±5%?
- Document fragility of conclusions

---

## Dashboard Layout

### 4x2 Grid Structure

```

 WAGE STAGNATION      HOUSING DESPAIR     
 Score: [XX]          Score: [XX]         
 [Label]              [Label]             
 [12-week sparkline]  [12-week sparkline] 
 ↑ +X vs last week    ↓ -X vs last week   



 AIRLINE CHAOS        CUSTOMER SERVICE    
 Score: [XX]          Score: [XX]         
 [Label]              [Label]             
 [12-week sparkline]  [12-week sparkline] 
 ↑ +X vs last week    → No change         



 STREAMING FATIGUE    DATING APPS         
 Score: [XX]          Score: [XX]         
 [Label]              [Label]             
 [12-week sparkline]  [12-week sparkline] 
 ↓ -X vs last week    ↑ +X vs last week   



 LAYOFF WATCH         AI PSYCHOSIS        
 Score: [XX]          Score: [XX]         
 [Label]              [Label]             
 [12-week sparkline]  [12-week sparkline] 
 ↑ +X vs last week    ↑ +X vs last week   

```

**Top Banner:**
```

  DISAPPOINTMENT DENSITY INDEX™: [XX.X]
  "[Label]"
  Week of: [Date Range]
  Trend: [↑↓→] [+/-X.X] vs last week

```

**Bottom Section - Fun Facts:**
```

 ABSURDITIES OF THE WEEK                       

 • [Fact 1]                                    
 • [Fact 2]                                    
 • [Fact 3]                                    
 • [Fact 4]                                    
 • [Fact 5]                                    

```

### Visual Design Principles

**Color Coding:**
- 0-20: Dark green (#1a3a1a)
- 20-40: Yellow-green (#4a5a1a)
- 40-60: Orange (#8a5a1a)
- 60-80: Dark red (#8a1a1a)
- 80-100: Crimson (#aa0000)

**Typography:**
- Monospace font for numbers (terminal aesthetic)
- Sans-serif for labels
- Dark charcoal background (#1a1a1a)
- Light gray text (#cccccc)

**Aesthetic:**
- Minimal, brutalist design
- No cheerful colors
- No rounded corners
- Terminal/dashboard vibe
- Information density over decoration

---

## Excel Implementation

### Sheet Structure

1. **DASHBOARD** - Public-facing view (the main attraction)
2. **DATA_WAGES** - BLS data, CEO ratios, calculations
3. **DATA_HOUSING** - Zillow, Census, evictions
4. **DATA_AIRLINES** - BTS stats, delays, cancellations
5. **DATA_CUSTOMERSERVICE** - ACSI, hold times, complaints
6. **DATA_STREAMING** - Pricing, fragmentation, sentiment
7. **DATA_DATING** - Trends, Reddit, app reviews
8. **DATA_LAYOFFS** - Layoffs.fyi weekly tracking
9. **DATA_AI_PSYCHOSIS** - Incident tracking, crisis posts
10. **LOGIC_SCORES** - All formulas live here
11. **BASELINES** - Historical averages and reference points
12. **COPY_BLOCKS** - Label mappings, fun facts library
13. **SOURCES** - Data source documentation, URLs
14. **METHODOLOGY** - This document, condensed

### Formula Implementation

**Example: Wage Stagnation in Excel**

```excel
// Cell references
current_real_wage = DATA_WAGES!B2
baseline_real_wage = BASELINES!B2
current_ceo_ratio = DATA_WAGES!C2
baseline_ceo_ratio = BASELINES!C2
google_trends_avg = DATA_WAGES!D2
reddit_ratio = DATA_WAGES!E2

// Wage component
=MIN(50, IF((current_real_wage - baseline_real_wage)/baseline_real_wage < 0,
    ABS((current_real_wage - baseline_real_wage)/baseline_real_wage) * 100 * 10,
    0))

// CEO ratio component
=MIN(30, ((current_ceo_ratio - baseline_ceo_ratio) / baseline_ceo_ratio) * 10)

// Google Trends component
=MIN(15, google_trends_avg * 0.15)

// Reddit component
=MIN(5, reddit_ratio * 100 * 0.05)

// Final score
=wage_component + ceo_component + trends_component + reddit_component
```

**All formulas follow this pattern:**
- Clear cell references
- MIN() caps to prevent overflow
- IF() statements for conditional logic
- Component-based addition for transparency

### Conditional Formatting

**Score-based cell coloring:**
```
0-20: Fill #1a3a1a, Font #cccccc
20-40: Fill #4a5a1a, Font #cccccc
40-60: Fill #8a5a1a, Font #ffffff
60-80: Fill #8a1a1a, Font #ffffff
80-100: Fill #aa0000, Font #ffffff
```

**Label lookup:**
```excel
=VLOOKUP(score, label_table, 2, TRUE)

Label table:
0   | "Label for 0-20"
20  | "Label for 20-40"
40  | "Label for 40-60"
60  | "Label for 60-80"
80  | "Label for 80-100"
```

### Sparklines

**12-week historical trend:**
```excel
=SPARKLINE(OFFSET(current_cell, 0, -11, 1, 12), {"charttype", "line"; "linewidth", 2; "color", "#888888"})
```

---

## Web Version (Phase 2)

### Tech Stack

**Frontend:**
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS + custom dark theme
- Recharts (sparklines, detailed charts)
- Framer Motion (subtle animations)
- shadcn/ui components

**Backend:**
- Next.js API routes
- Python scripts for data collection
- Node.js for API integrations
- Vercel Postgres or JSON files for storage

**Data Pipeline:**
- GitHub Actions cron (runs every Monday 9am)
- Python scripts hit APIs, scrape data
- Store results in database or JSON
- Dashboard reads from latest data file
- Historical data archived for trends

**APIs to Integrate:**
- BLS API (official)
- Google Trends (pytrends library)
- News API (newsapi.org)
- Reddit API (PRAW library)
- Zillow API (if available) or scraping
- BTS data downloads (manual or automated)

### Deployment

**Hosting:** Vercel (free tier sufficient for MVP)

**Domain:** shainapauley.com/disappointments

**Update Schedule:**
- Cron job runs Monday 9am EST
- Data collection takes ~30 minutes
- Dashboard updates automatically
- Historical data preserved

**Performance:**
- Static generation where possible
- Client-side data fetching for real-time
- CDN caching for assets
- Optimize for mobile

---

## Portfolio Case Study

### Structure

**Title:** The Predictable Disappointments Dashboard

**Subtitle:** A weekly data-backed index quantifying the everyday frustrations Americans reliably endure

**The Problem:**
Modern life feels increasingly frustrating: wages stagnate while costs rise, customer service deteriorates, streaming services multiply, and we're forming parasocial relationships with chatbots. But frustration without measurement is just noise. What if we could quantify collective disappointment with the same rigor typically reserved for stock markets or economic indicators?

**The Solution:**
Built a composite scoring system across 8 categories that transforms scattered cultural frustration into trackable metrics. Part satire, part social commentary, entirely backed by real data from government sources, academic research, and public sentiment tracking.

**The Approach:**

**1. Identified Universal Pain Points**
- Researched what consistently frustrates Americans across economic, service quality, and cultural dimensions
- Selected 8 categories with publicly available, verifiable data sources
- Organized into tiers: Economic Brutality → Daily Grind → Existential Nightmare

**2. Built Research-Grade Methodology**
- Designed weighted scoring formulas with documented rationale
- Used government sources (BLS, BTS, Census) as primary data
- Implemented rolling baselines to avoid cherry-picking
- Created bias mitigation protocols
- Made all methodology transparent and reproducible

**3. Balanced Rigor and Humor**
- Let the data speak (reality is bleak enough)
- Added deadpan comedic labels without manipulating scores
- Designed dark aesthetic matching content tone
- Made complex data accessible and shareable

**4. Built Automated Data Pipeline**
- Integrated 10+ data sources via APIs and web scraping
- Created weekly update automation (GitHub Actions cron)
- Archived historical data for trend analysis
- Documented data collection process for reproducibility

**5. Designed for Engagement**
- Dashboard layout optimized for quick comprehension
- Individual metrics are independently shareable
- Fun facts add human element without sacrificing credibility
- Weekly updates create return visit incentive

**The Impact:**
[After launch:]
- [X] visitors in first month
- [X] social media shares
- Featured in [publications]
- Demonstrates ability to make data both rigorous and engaging
- Shows cultural intelligence and timing
- Real data builds credibility over typical portfolio mock data

**Skills Showcased:**
- Data modeling & statistical methodology
- Multi-source API integration & web scraping
- Dashboard design (Excel → Web)
- Automation & data pipeline engineering
- Research best practices & bias mitigation
- Storytelling through data
- Cultural awareness & comedic timing
- TypeScript, Next.js, Python
- Formula design & validation

**What I Learned:**
- How to balance analytical rigor with accessibility
- Importance of transparent methodology for credibility
- Sourcing and validating diverse data streams
- Building maintainable weekly automation
- Making depressing data oddly compelling
- The power of deadpan humor in data presentation

**Data Sources:**
[Full list of 15+ sources with citations]

**View Live:** shainapauley.com/disappointments

**GitHub:** github.com/shainapauley/disappointments-dashboard

---

## Build Timeline

### Phase 1: Research & Excel (Week 1-2)

**Week 1: Data Foundation**
- Day 1-2: Validate all data sources, document APIs
- Day 3-4: Collect 8-12 weeks historical baseline data
- Day 5: Set up Excel structure, build formula framework

**Week 2: Excel Dashboard**
- Day 1-2: Implement all scoring formulas with validation
- Day 3: Design dashboard layout, conditional formatting
- Day 4: Build fun facts system, polish visual design
- Day 5: Write methodology documentation, take screenshots

### Phase 2: Web Version (Week 3-4)

**Week 3: Development**
- Day 1-2: Next.js setup, component architecture, dark theme
- Day 3-4: Data pipeline scripts (Python + Node.js)
- Day 5: Connect dashboard UI to data, build metric details

**Week 4: Launch**
- Day 1-2: GitHub Actions automation, testing
- Day 3: Deploy to production, test weekly update
- Day 4: Write case study, prepare launch materials
- Day 5: Public launch, monitor and iterate

---

## Success Metrics

**Portfolio Impact:**
- Unique, memorable project
- Shows range beyond typical B2B work
- Demonstrates research rigor + humor
- Real data = credibility
- Conversation starter in interviews

**Public Launch (if applicable):**
- Weekly unique visitors
- Social media shares
- Press mentions
- Return visitor rate
- Time on site
- GitHub stars

**Interview Value:**
- "Walk me through your methodology"
- "How did you handle bias?"
- "What was your data validation process?"
- "How did you balance humor with accuracy?"

---

## Risk Mitigation

**Data source failure:**
- Document 2-3 backup sources per metric
- Build graceful degradation (dashboard shows "data unavailable" vs breaking)

**Methodology criticism:**
- Full transparency in documentation
- Cite academic standards
- Welcome feedback and iteration

**Tone misses the mark:**
- Beta test with diverse audience
- Adjust labels based on feedback
- Ensure humor punches up (at systems) not down (at people)

**Maintenance burden:**
- Automate everything possible
- Document manual processes clearly
- Set realistic update schedule (weekly, not daily)

**Legal/ethical:**
- Use only public data
- Respect ToS and robots.txt
- Cite all sources
- Note when tracking sensitive topics (AI psychosis)

---

## Next Steps

1. Review and approve final architecture
2. Validate all 8 data sources
3. Collect baseline historical data (8-12 weeks)
4. Build Excel dashboard with formulas
5. Test scoring system with real data
6. Polish visual design
7. Write portfolio case study
8. Build web version
9. Deploy and launch
10. Iterate based on feedback

---

**Let's build something darkly beautiful with flawless methodology.**
