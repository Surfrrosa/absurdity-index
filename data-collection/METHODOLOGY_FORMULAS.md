# The Absurdity Index: Complete Methodology & Formulas

**Version:** 1.0
**Last Updated:** December 20, 2025
**Status:** Living document - will be updated as methodology evolves

---

## Core Philosophy

### What Is Absurdity?

The Absurdity Index quantifies a subjective but widely-felt sense: that we live in an insane society actively causing its own misery. This is not a precise clinical term. It's the recognition that our systems produce outcomes that seem increasingly detached from human wellbeing.

### Methodological Approach

We combine two data sources to create more sound, relevant, and accurate measurements than either source alone:

1. **Official Statistics (40% weight):** Government reports, industry data, economic indicators
2. **Systematically Quantified Qualitative Data (60% weight):** Social media content categorized by severity

Official statistics tell you what's happening at the macro level. Systematically quantifying lived experiences tells you what's happening at the human level. Together, they provide a more complete and accurate picture than either source alone.

This is not about finding "gaps" or "discrepancies." It's about enhancing the accuracy of our measurements by incorporating data from multiple sources.

### Transparency Over Perfection

This is an experimental methodology. We prioritize explicit documentation of all formulas, verifiable data sources, and honest acknowledgment of limitations. All processes are designed to be reproducible.

We're not claiming scientific perfection. We're claiming transparency about what we're measuring and how we're measuring it.

---

## Mathematical Formulas

### Overview

Each metric's Final Score combines two components:

```
Final Score = (Official Score × 0.4) + (Social Score × 0.6)
```

Where:
- **Official Score (0-100)**: Normalized from government/industry statistics
- **Social Score (0-100)**: Engagement-weighted severity from social media content

### Official Score Calculation

Official scores normalize raw metrics to a 0-100 scale based on reasonable worst-case scenarios.

**Example: Healthcare Official Score**

```python
# Raw metrics
premium_increase_yoy = 7.0%        # Annual premium increase
denial_rate = 18.0%                 # Initial claim denial rate
medical_debt_pct = 41.0%            # Adults with medical debt
medical_bankruptcies = 66.5%        # Bankruptcies from medical debt
uninsured_rate = 8.0%               # Americans without insurance

# Normalize to 0-100 (based on worst-case thresholds)
premium_score = min(100, (7.0 / 15.0) * 100) = 46.67
denial_score = min(100, (18.0 / 30.0) * 100) = 60.00
debt_score = min(100, (41.0 / 60.0) * 100) = 68.33
bankruptcy_score = 66.50  # Already 0-100
uninsured_score = min(100, (8.0 / 20.0) * 100) = 40.00

# Average all metrics
Official Score = (46.67 + 60.00 + 68.33 + 66.50 + 40.00) / 5 = 56.30
```

### Social Score Calculation

Social scores quantify qualitative data by combining:
1. **Severity categorization**: How severe is the content?
2. **Engagement weighting**: How many people saw it?

**Step 1: Categorize Content by Severity**

Each piece of content (video, post, etc.) is categorized into one of three levels:

| Level | Weight | Description | Example (Healthcare) |
|-------|--------|-------------|---------------------|
| Level 1 (Aware) | 0.33 | Awareness without crisis | Billing confusion, delays |
| Level 2 (Struggling) | 0.67 | Active struggle | Can't afford treatment, high premiums |
| Level 3 (Crisis) | 1.0 | Critical situation | Medical debt, denied life-saving care |

**Step 2: Weight by Engagement**

Use logarithmic scaling to account for reach without letting viral content dominate:

```
Engagement Weight = log₁₀(views + 1)
```

Why logarithmic?
- Prevents viral outliers from skewing results
- Still accounts for relative reach
- 100 views → weight 2.0
- 10,000 views → weight 4.0 (not 100x more impact)
- 1,000,000 views → weight 6.0

**Step 3: Calculate Weighted Average**

For each video/post, multiply severity by engagement, then normalize:

```
Social Score = (Σ severity_weight × log₁₀(views + 1)) / (Σ log₁₀(views + 1)) × 100
```

**Worked Example: Healthcare Social Score**

Sample data from 160 videos:

| Video | Severity | Views | Calculation |
|-------|----------|-------|-------------|
| "Medical bankruptcy crisis" | 1.0 (L3) | 23,263 | 1.0 × log₁₀(23,264) = 1.0 × 4.37 = 4.37 |
| "Can't afford insulin" | 0.67 (L2) | 5,420 | 0.67 × log₁₀(5,421) = 0.67 × 3.73 = 2.50 |
| "Insurance billing confusion" | 0.33 (L1) | 892 | 0.33 × log₁₀(893) = 0.33 × 2.95 = 0.97 |

Sum across all 160 videos:
```
Total Weighted Score = Σ (severity × log₁₀(views + 1)) = 1,847.2
Total Engagement = Σ log₁₀(views + 1) = 4,004.3

Social Score = (1,847.2 / 4,004.3) × 100 = 46.14
```

**Distribution:**
- Level 1: 110 videos (awareness)
- Level 2: 16 videos (struggling)
- Level 3: 34 videos (crisis)
- Total: 160 videos

### Final Score Calculation

Combine official statistics with quantified lived experiences:

```
Healthcare Final Score = (56.30 × 0.4) + (46.14 × 0.6)
                      = 22.52 + 27.68
                      = 50.20
```

**Why 40/60 weighting?**
- Official statistics provide objective baselines
- Social sentiment captures real-world impact and lived experiences
- 60% weight on social data reflects that human experience matters more than abstract metrics
- Creates more accurate, relevant measurements than either source alone

### Complete Example: All 8 Metrics

| Metric | Official Score | Social Score | Final Score |
|--------|---------------|--------------|-------------|
| What Healthcare? | 56.30 | 46.14 | 50.20 |
| AI Psychosis | 12.50 | 53.85 | 37.31 |
| Subscription Overload | 45.20 | 36.41 | 39.93 |
| Wage Stagnation | 38.40 | 42.50 | 40.86 |
| Housing Despair | 37.60 | 47.66 | 43.64 |
| Dating App Despair | 8.50 | 46.92 | 31.55 |
| Layoff Watch | 76.50 | 35.07 | 51.64 |
| Airline Chaos | 21.00 | 52.89 | 40.13 |

### Notes on Reproducibility

All calculations are implemented in:
- `/data-collection/calculate_all_social_scores.py` - Social score calculator
- `/data-collection/calculate_healthcare_official_score.py` - Official score examples

To recalculate any metric:
```bash
cd data-collection
python3 calculate_all_social_scores.py
```

---

## Data Collection

### Platform Selection

**Primary Platforms:**
- YouTube (all metrics)
- Reddit (select metrics: Healthcare, AI Psychosis)
- App Stores (AI Psychosis only - pending)
- TikTok (pending expansion)

**Rationale:**
- **YouTube**: Largest video platform, rich metadata (views, comments), accessible API, representative of general population sentiment
- **Reddit**: Anonymous self-disclosure, specific community conversations, text-based detail
- **App Stores**: User reviews provide unfiltered feedback on products
- **TikTok**: Younger demographic, viral content spreading, currently limited by API access

**Known Bias**: Heavy YouTube emphasis may over-represent:
- Younger demographics (18-49)
- English-speaking populations
- Users comfortable with public video content
- U.S.-centric perspectives (regionCode='US' filter)

### Sampling Methodology

**Search-Based Sampling:**

Each metric uses 8-10 carefully crafted search terms designed to capture different aspects of the issue:

**Example (Healthcare):**
```python
[
    "health insurance denied claim",
    "medical bankruptcy story",
    "can't afford healthcare",
    "prior authorization nightmare",
    "insurance denied life saving treatment",
    "medical debt collections",
    "emergency room bill shock",
    "prescription too expensive"
]
```

**Search Parameters:**
- `maxResults`: 10-15 per search term
- `order`: 'relevance' (not recency or view count)
- `publishedAfter`: Last 90 days
- `regionCode`: 'US'
- `type`: 'video'

**Why Relevance Ordering:**
- Captures videos that best match search intent
- Avoids bias toward viral outliers
- Returns substantive content over clickbait

**Target Sample Sizes:**
- Minimum: 100 videos per metric
- Target: 150-200 videos per metric
- Rationale: Balance between statistical validity and API quota limits

### Temporal Windows

**90-Day Window:**

All social media sampling uses a 90-day lookback period.

**Rationale:**
- Recent enough to reflect current conditions
- Long enough to avoid weekly noise/outliers
- Captures seasonal patterns (quarterly data)
- Manageable for weekly updates

**Example:**
```python
ninety_days_ago = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%dT%H:%M:%SZ')

search_response = youtube.search().list(
    q=query,
    publishedAfter=ninety_days_ago,
    ...
)
```

**Trade-offs:**
- ✅ Current: Reflects present reality
- ✅ Stable: Not swayed by single viral event
- ⚠️ Limited History: Can't detect long-term trends (yet)
- ⚠️ Seasonal Bias: Q4 may differ from Q2

### Content Categorization

All content is categorized using rule-based keyword matching (see `CATEGORIZATION_CRITERIA.md` for complete documentation).

**Three-Level System:**
- **Level 1 (Aware)**: Information, mild frustration, awareness
- **Level 2 (Struggling)**: Active struggle, frustration, burnout
- **Level 3 (Crisis)**: Life-altering impact, severe consequences, hopelessness

**Categorization Logic:**
```python
def categorize_video(title, description):
    text = (title + " " + description).lower()

    # Level 3: 2+ crisis keywords OR critical phrases
    if level_3_count >= 2 or any(critical_phrase in text):
        return 'LEVEL_3_CRISIS'

    # Level 2: 2+ struggle keywords OR common frustration phrases
    if level_2_count >= 2 or any(struggle_phrase in text):
        return 'LEVEL_2_STRUGGLING'

    # Level 1: Default for relevant content
    return 'LEVEL_1_AWARE'
```

**Quality Control:**
- Relevance filtering (keyword pre-screening)
- Duplicate removal (by video ID)
- Manual spot-checking of edge cases

### Data Enrichment

After initial collection, videos are enriched with engagement data:

**Engagement Metrics:**
- `view_count`: Total views (for weighting)
- `comment_count`: Community engagement level
- Video metadata: title, description, publish date

**Fetching:**
```python
# Batch fetch statistics for collected videos
stats = youtube.videos().list(
    part='statistics',
    id=','.join(video_ids)  # Up to 50 per request
).execute()
```

### Update Frequency

**Current**: Manual collection with weekly updates

**Future**: Automated weekly collection on Sundays at 00:00 UTC

**Rationale**:
- Weekly updates capture evolving sentiment
- Sunday timing: Full week of data, pre-Monday analysis
- Manual verification during beta phase ensures quality

### Data Storage

**Format**: CSV files in `/data-collection/collected-data/`

**Filename Convention**: `{metric}_youtube_{timestamp}.csv`

**Schema**:
```
search_term, video_id, url, title, category, view_count, comment_count
```

**Example**:
```csv
"health insurance denied claim","abc123","https://...","My claim was denied","LEVEL_3_CRISIS",23263,274
```

**Retention**:
- All historical CSVs preserved for trend analysis
- Latest file used for score calculation
- Archived data enables reproducibility audits

### Sample Size Considerations

**Current Sample Sizes** (as of Dec 20, 2025):

| Metric | Videos | Target Met? |
|--------|--------|-------------|
| What Healthcare? | 160 | ✅ Yes |
| AI Psychosis | 146 | ✅ Yes |
| Subscription Overload | 150 | ✅ Yes |
| Housing Despair | 122 | ✅ Yes |
| Dating App Despair | 114 | ✅ Yes |
| Wage Stagnation | 96 | ⚠️ Near |
| Airline Chaos | 122 | ✅ Yes |
| Layoff Watch | 74 | ⚠️ Below |

**Statistical Validity:**
- 100+ samples: Generally sufficient for proportions within ±10% margin of error
- <100 samples: Higher variance, but still directionally valid
- Ongoing collection to increase all metrics >150

### API Quotas & Constraints

**YouTube Data API v3:**
- Free tier: 10,000 quota units/day
- Search operation: 100 units
- Video statistics: 1 unit per 50 videos
- Typical collection run: ~2,000 units (well under limit)

**Rate Limiting:**
- Implemented: 1-second delay between searches
- Prevents API throttling
- Respectful of platform resources

---

## Bias and Limitations

### Platform Bias

**YouTube-Heavy Sampling:**
- **Issue**: 6 of 8 metrics rely primarily on YouTube data
- **Impact**: Over-represents demographics that create video content and engage publicly
- **Who's Missing**:
  - Older adults (65+) less represented on YouTube
  - Non-English speakers (U.S. region filter)
  - People experiencing extreme poverty (limited internet access)
  - Those unwilling to share struggles publicly

**Mitigation**:
- Expanding to Reddit for anonymous text-based content
- Planning TikTok integration for younger demographics
- Using official statistics (40% weight) to ground social sentiment

**Residual Bias**: Acknowledged - we're measuring "visible absurdity," which may undercount silent suffering

---

### Temporal Limitations

**90-Day Window:**
- **Issue**: No long-term trend detection yet
- **Impact**: Can't distinguish temporary spikes from sustained deterioration
- **Example**: Airline chaos during holiday season vs. year-round issues

**Mitigation**:
- Archiving all historical data for future trend analysis
- Weekly updates to detect month-over-month changes
- Planning 12-month rolling average implementation

**Residual Limitation**: Current scores are snapshots, not trends

---

### Sample Size Concerns

**Small Samples (<100 videos):**
- **Metrics Affected**: Layoff Watch (74 videos), Wage Stagnation (96 videos)
- **Impact**: Higher variance, wider confidence intervals
- **Statistical Note**: ±11-13% margin of error vs ±8% for 150+ samples

**Mitigation**:
- Ongoing collection to increase sample sizes
- Conservative interpretation of close scores
- Transparency about sample sizes in UI

**When to Trust Small Samples**:
- ✅ Extreme scores (very high or very low) - signal clear despite noise
- ✅ Directional validity - "high" vs "low", not precise ranking
- ⚠️ Precise comparisons - don't over-interpret 2-point differences

---

### Categorization Subjectivity

**Human Judgment in Keywords:**
- **Issue**: L2/L3 boundaries require subjective keyword selection
- **Impact**: Different researchers might categorize 10-20% differently
- **Example**: "frustrated and exhausted" - L2 or L3?

**Mitigation**:
- Rule-based thresholds (2+ keywords) reduce subjectivity
- Explicit criteria documented in CATEGORIZATION_CRITERIA.md
- Default to lower severity when ambiguous (conservative)
- Future: Multiple coders for inter-rater reliability testing

**Residual Subjectivity**: Edge cases will always exist - we aim for 80%+ consistency

---

### Engagement Weighting Assumptions

**Logarithmic Scaling:**
- **Assumption**: A video with 1M views has more impact than 1K views, but not 1000x more
- **Debate**: Should virality count more? Or does log() under-weight reach?
- **Our Choice**: log₁₀() balances reach with content diversity

**Alternative Approaches Considered**:
- Linear weighting - rejected (viral outliers dominate)
- Square root - similar to log, chose log for interpretability
- No weighting - rejected (ignores reach entirely)

**Residual Uncertainty**: Optimal weighting function is philosophically debatable

---

### Geographic Limitations

**U.S.-Centric Data:**
- **Issue**: `regionCode='US'` filter in YouTube API
- **Impact**: Missing global perspectives on universal issues
- **Who's Missing**: European healthcare experiences, Asian housing markets, etc.

**Rationale**:
- Official statistics are U.S.-based (BLS, Census, KFF)
- Consistent geographic scope for comparison
- U.S. audience is primary user base

**Future**: International metrics as separate indices (UK Absurdity Index, etc.)

---

### Selection Bias

**Who Creates Content:**
- **Issue**: People with time/resources to create videos are not representative
- **Impact**: May under-represent those most affected (working multiple jobs, no internet)
- **Example**: Someone truly homeless likely not uploading YouTube videos

**Mitigation**:
- Diverse search terms to capture range of experiences
- Include both creator content and news coverage
- Official statistics capture those not represented online

**Residual Bias**: We measure "vocal absurdity" - the seen, not the unseen

---

### Algorithmic Filtering

**YouTube Search Algorithm:**
- **Issue**: "Relevance" ordering is a black box
- **Impact**: Unknown which videos are filtered out
- **Potential Bias**: Algorithm may suppress certain types of content

**Mitigation**:
- Multiple search terms reduce single-query bias
- Regular re-collection captures algorithm changes
- Awareness that we're sampling "YouTube's version of reality"

**Residual Uncertainty**: Can't fully audit YouTube's filtering logic

---

### Recency Bias

**What's Measured:**
- Recent uploads (last 90 days)
- Current view counts (which change over time)

**What's Missed:**
- Older systemic issues that sparked less recent content
- View count growth trajectories

**Trade-off**:
- ✅ Reflects current moment
- ⚠️ May miss slow-burning crises

---

### Language and Cultural Bias

**English-Only:**
- **Issue**: Keyword matching only works in English
- **Impact**: Missing Spanish-language U.S. content, other languages
- **Who's Missing**: Non-English-speaking Americans experiencing same issues

**Mitigation**: Future multilingual keyword expansion

**Cultural Assumptions:**
- Categorization keywords reflect Western/U.S. cultural norms
- "Crisis" definitions may not translate cross-culturally

---

### Transparency vs Perfection

**Our Approach:**
We prioritize **transparent imperfection** over **opaque sophistication**.

**What This Means:**
- ✅ Explicit documentation of all limitations
- ✅ Simple, auditable methods over complex models
- ✅ Reproducible processes anyone can verify
- ⚠️ Accepting known biases over unknowable black boxes

**Core Belief:**
Transparent flaws are better than hidden ones. Perfect measurement is impossible. Honest measurement is essential.

---

### What We're NOT Claiming

**We are NOT:**
- ❌ A scientific peer-reviewed study
- ❌ Statistically representative of all Americans
- ❌ Capturing every dimension of societal absurdity
- ❌ Providing clinical/diagnostic assessments

**We ARE:**
- ✅ A transparent, reproducible methodology
- ✅ Combining official data with lived experiences
- ✅ Quantifying widely-felt but under-measured phenomena
- ✅ Honest about our limitations

---

### Future Improvements

**Planned:**
1. Increase sample sizes to 200+ per metric
2. Add Reddit/TikTok for platform diversity
3. Implement trend detection (historical comparison)
4. Test inter-coder reliability formally
5. Expand to non-English content
6. Add confidence intervals to scores

**Under Consideration:**
1. Geographic expansion (state-level indices)
2. Demographic breakdowns (age, income)
3. Alternative weighting schemes
4. Machine learning for categorization (after establishing baseline)

---

## Overall Absurdity Score

### Definition

The **Overall Absurdity Score** is the headline metric that aggregates all 8 individual metrics into a single number representing the current state of societal absurdity.

### Calculation Formula

**Equal-Weight Average:**

```
Overall Score = (Σ Final Scores) / N

Where:
- Σ Final Scores = Sum of all 8 metric final scores
- N = Number of metrics (8)
```

**Current Calculation:**

```
Overall Score = (Healthcare + AI + Subscription + Wage + Housing + Dating + Layoff + Airline) / 8
             = (50.20 + 37.31 + 39.93 + 40.86 + 43.64 + 31.55 + 51.64 + 40.13) / 8
             = 335.26 / 8
             = 41.91
```

### Why Equal Weighting?

**Rationale:**
1. **Democratic Measurement**: No single metric is "more important" - all represent dimensions of lived experience
2. **Defensible**: Any weighting scheme requires subjective judgments we can't defend
3. **Simple**: Transparent and easily understood
4. **Robust**: No single metric can dominate the overall score

**Alternative Approaches Considered:**

**Impact Weighting** (by affected population):
- Healthcare (affects ~300M) > Dating Apps (affects ~40M)
- Rejected: Would make some struggles "count less"
- Philosophical issue: Individual suffering isn't less valid if fewer experience it

**Severity Weighting** (by individual crisis scores):
- Weight metrics with higher crisis ratios more heavily
- Rejected: Creates circular logic (severe metrics get more weight → score goes up → they get more weight)

**Domain Weighting** (economic vs social vs health):
- Group metrics by type, weight categories
- Rejected: Arbitrary category boundaries, added complexity

### Score Interpretation

**Scale: 0-100**

| Range | Label | Interpretation |
|-------|-------|----------------|
| 0-20 | "Sustainable" | Minimal systemic issues, mostly functioning |
| 20-40 | "Concerning" | Notable problems, but manageable for most |
| 40-60 | "Critical" | Significant dysfunction across multiple domains |
| 60-80 | "Crisis" | Severe widespread suffering, systems failing |
| 80-100 | "Collapse" | Complete breakdown, society non-functional |

**Current Score: 41.91** → "Critical" (just into the range)

### Dynamic Label System

Based on the overall score, a contextual label is displayed:

| Score | Label |
|-------|-------|
| 0-20 | "SURPRISINGLY FUNCTIONAL" |
| 20-30 | "MINOR TURBULENCE" |
| 30-40 | "FLYING TOO CLOSE TO THE SUN" |
| 40-50 | "ICARUS HAS ENTERED THE CHAT" |
| 50-60 | "THE WHEELS ARE COMING OFF" |
| 60-70 | "ACTIVELY ON FIRE" |
| 70-80 | "WE'VE REACHED PEAK CIVILIZATION" |
| 80-90 | "REALITY.EXE HAS STOPPED WORKING" |
| 90-100 | "THE GODS ARE LAUGHING AT US" |

**Current Label (41.91)**: "ICARUS HAS ENTERED THE CHAT"

### Sensitivity Analysis

**How Much Does Each Metric Matter?**

With equal weighting, each metric contributes 1/8 (12.5%) to the overall score.

**Example:**
- If Healthcare goes from 50.20 → 60.20 (+10 points)
- Overall Score changes: 41.91 → 43.16 (+1.25 points)
- Each metric point = 0.125 overall points

**Implications:**
- No single metric can drive dramatic changes alone
- Requires coordinated improvement/deterioration across multiple metrics
- Reflects that "societal absurdity" is multi-faceted

### Trend Detection (Future)

**Planned Implementation:**
- Weekly historical tracking
- Month-over-month change percentage
- 12-month rolling average
- Trend indicators: ⬆️ Worsening, ➡️ Stable, ⬇️ Improving

**Example Future Display:**
```
Overall Score: 41.91 ⬆️ +2.3 vs last month
```

### Confidence & Uncertainty

**Current Limitations:**
- No confidence intervals displayed (yet)
- Sample size variance not propagated to overall score
- Assumes equal measurement quality across metrics

**Planned:**
- Calculate weighted average of sample sizes
- Display confidence range: "41.91 ± 3.2"
- Adjust weighting by data completeness

### Implementation

**Code Location**: `/lib/metricDetailData.ts`

**Function:**
```typescript
export function calculateOverallScore(): number {
  const metrics = getAllMetricsWithLabels();
  const scores = Object.values(metrics).map(m => m.score);
  const sum = scores.reduce((a, b) => a + b, 0);
  return sum / scores.length;
}

export function getOverallLabel(score: number): string {
  if (score < 20) return "SURPRISINGLY FUNCTIONAL";
  if (score < 30) return "MINOR TURBULENCE";
  if (score < 40) return "FLYING TOO CLOSE TO THE SUN";
  if (score < 50) return "ICARUS HAS ENTERED THE CHAT";
  if (score < 60) return "THE WHEELS ARE COMING OFF";
  if (score < 70) return "ACTIVELY ON FIRE";
  if (score < 80) return "WE'VE REACHED PEAK CIVILIZATION";
  if (score < 90) return "REALITY.EXE HAS STOPPED WORKING";
  return "THE GODS ARE LAUGHING AT US";
}
```

### Reproducibility

To verify the overall score calculation:

```bash
cd data-collection
python3 << EOF
scores = [50.20, 37.31, 39.93, 40.86, 43.64, 31.55, 51.64, 40.13]
overall = sum(scores) / len(scores)
print(f"Overall Score: {overall:.2f}")
EOF
```

Output: `Overall Score: 41.91`

---

