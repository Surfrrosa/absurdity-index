# The Absurdity Index: Calculation Methodology

## Core Formula

Each metric combines **official data** (objective baseline) with **social sentiment analysis** (lived experience multiplier) to produce a comprehensive absurdity score.

```
Final Score = (Official Data Component × 0.4) + (Social Sentiment Component × 0.6)
```

### Why 40/60 weighting?

- **Official data (40%)**: Provides objective grounding but often lags reality or misses psychological impact
- **Social sentiment (60%)**: Captures lived experience, urgency, and emotional toll that stats alone miss
- This weighting reflects that absurdity is fundamentally about the GAP between what should be vs what is - which social sentiment reveals better than raw numbers

---

## Metric-Specific Formulas

### 1. AI Psychosis
**Official Data Component:**
- App download trends
- Market research on AI companion usage
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from multi-platform analysis (YouTube, Reddit, TikTok, App Store)
- Level 3 (Crisis): User describes dependency, mental health crisis, preference for AI over humans
- Level 2 (Dependent): Regular emotional reliance, significant time investment
- Level 1 (Casual): Curiosity, occasional use

```
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 440-480 data points (146 YouTube + 200 Reddit + 20 App Store + 120 TikTok target)

---

### 2. Subscription Overload
**Official Data Component:**
- Average subscriptions per household
- Average monthly spending
- Percentage of services raising prices
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from social media "cancel subscriptions," "subscription fatigue" content
- Level 3: Financial strain, canceling essentials, overwhelmed by tracking
- Level 2: Actively trying to reduce, frustrated by price increases
- Level 1: Mild annoyance, awareness of spending

```
Official Score = ((Avg Subs / 20) + (Avg Spend / 400) + (Price Increase % / 100)) × 33.3
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

---

### 3. Dating App Despair
**Official Data Component:**
- Google Trends volume for dating app frustration terms
- App store review sentiment analysis
- User retention rates (when available)
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from "quit dating apps," "dating burnout" content
- Level 3: Quit entirely, mental health impact, gave up on dating
- Level 2: Burnt out but still trying, frequent bad experiences, considering quitting
- Level 1: General complaints, still optimistic

```
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 440-480 data points (120-160 YouTube + 200 Reddit + 120 TikTok)

---

### 4. What Healthcare?
**Official Data Component:**
- Average annual premium increases
- Initial claim denial rates
- Percentage of adults with medical debt
- Medical bankruptcy rates
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from healthcare nightmare content
- Level 3: Medical debt/bankruptcy, denied life-saving treatment, can't afford necessary care
- Level 2: Can't afford treatment, struggling with high premiums, insurance battle stress
- Level 1: Billing confusion, minor coverage frustrations, admin hassles

```
Official Score = ((Premium Increase % × 10) + (Denial Rate %) + (Medical Debt % / 2)) / 3
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 440-480 data points (120-160 YouTube + 200 Reddit + 120 TikTok)

---

### 5. Wage Stagnation
**Official Data Component:**
- Real wage growth (adjusted for inflation)
- CEO-to-worker pay ratio (normalized)
- Google Trends for "can't afford" terms
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from "living paycheck to paycheck," "can't afford rent" content
- Level 3: Can't meet basic needs, housing insecurity, financial crisis
- Level 2: Paycheck to paycheck, cutting essentials, constant stress
- Level 1: Frustrated by prices, some cutbacks

```
Official Score = ((CEO Ratio / 400) + ((100 - Real Wage Growth) / 2) + Trends) / 3 × 100
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 300+ data points across platforms

---

### 6. Housing Despair
**Official Data Component:**
- Median home price to median income ratio
- Rent as percentage of median income
- Homeownership rate decline
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from "never own a home," "priced out" content
- Level 3: Gave up on homeownership, housing insecurity, forced to move
- Level 2: Can't save for down payment, rent increases forcing lifestyle cuts
- Level 1: Frustrated by prices, homeownership feels distant

```
Official Score = ((Price-to-Income Ratio / 10) + (Rent % Income / 2)) × 10
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 300+ data points across platforms

---

### 7. Airline Chaos
**Official Data Component:**
- Flight delay percentage
- Cancellation rates
- Customer satisfaction scores (inverted)
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from airline nightmare content
- Level 3: Stranded for days, lost critical luggage, major life disruption
- Level 2: Significant delays/cancellations, poor service, frequent issues
- Level 1: Minor delays, general complaints

```
Official Score = ((Delay % × 2) + (Cancellation % × 3) + ((100 - ACSI) / 2)) / 3
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 200+ data points across platforms

---

### 8. Layoff Watch
**Official Data Component:**
- Total layoffs (industry-specific)
- Percentage of workforce affected
- Job opening trends
- Normalized to 0-100 scale

**Social Sentiment Component:**
- Crisis ratio from layoff fear and job search despair content
- Level 3: Laid off and can't find work, financial crisis, industry collapse fear
- Level 2: Layoff fear, difficult job search, hundreds of applications
- Level 1: General job market concerns, awareness of layoffs

```
Official Score = (Layoff Count / Target × 100) capped at reasonable maximum
Crisis Ratio = (Level 3 count / Total count) × 100
Final Score = (Official × 0.4) + (Crisis Ratio × 0.6)
```

**Sample size:** 300+ data points across platforms

---

## Overall Absurdity Score

The headline Absurdity Score is the **weighted average** of all 8 metrics:

```
Overall Absurdity = (Σ Individual Scores) / 8
```

All metrics are weighted equally because each represents a distinct dimension of modern absurdity.

---

## Label Thresholds

Based on the Overall Absurdity Score:

- **0-15**: "Love May Actually Be Real" (minimal absurdity)
- **16-30**: "Manageable Existential Dread"
- **31-50**: "Quarterly Purge Required"
- **51-70**: "Digital Stockholm Syndrome Setting In"
- **71-85**: "Prior Authorization Purgatory"
- **86-100**: "The Void Stares Back"

---

## Bias Mitigation

### Multi-platform sampling
Data collected from YouTube, Reddit, TikTok, Twitter/X to avoid platform-specific bias

### Systematic collection
- Defined search terms
- Minimum sample sizes (200-480 per metric)
- Top/hot/recent sorting (not cherry-picked)

### Keyword-based categorization
- Reduces subjective judgment
- Reproducible by others
- Keywords documented and public

### Transparency
- All formulas public
- Sample sizes disclosed
- Limitations acknowledged
- Raw data exportable

### Official data anchoring
40% weight on official statistics prevents pure sentiment drift

---

## Limitations

1. **Platform demographics**: Reddit/TikTok users ≠ general population
2. **Self-selection bias**: People experiencing crisis more likely to post
3. **Temporal bias**: Viral events can spike sentiment temporarily
4. **Geographic bias**: US-focused data collection
5. **Keyword limitations**: Automated categorization may miss context

**These limitations are acknowledged and do not invalidate the methodology** - they are present in all sentiment research. Our multi-source, systematic approach with official data anchoring mitigates these effects.

---

## Policy Change Monitoring

The Absurdity Index tracks major policy changes that directly impact metric scores. When significant regulatory changes occur, we document the impact and adjust baselines accordingly.

### Healthcare Policy Tracking

**Federal Level:**
- Affordable Care Act (ACA) modifications or repeal attempts
- Medicare/Medicaid expansion or restriction
- Prescription drug price regulations
- Prior authorization rule changes (CMS regulations)

**State Level:**
- Medicaid expansion decisions
- State-level insurance marketplace changes
- Surprise billing protections

**Impact Protocol:** When healthcare policy changes, official score baseline is recalculated using new premium/denial/coverage data. Social sentiment data collection continues to capture lived experience under new policies.

---

### Wage & Labor Policy Tracking

**Federal Level:**
- Minimum wage legislation
- National Labor Relations Board (NLRB) rulings
- Federal labor law updates
- Tax policy affecting working class

**State/Local Level:**
- State minimum wage increases
- Living wage ordinances
- Right-to-work law changes

**Impact Protocol:** CEO pay ratio and real wage growth metrics updated quarterly. Policy changes noted in methodology with before/after comparison.

---

### Housing Policy Tracking

**Federal Level:**
- Federal Reserve interest rate changes (direct impact on mortgages)
- FHA loan requirement modifications
- First-time homebuyer programs

**State/Local Level:**
- Zoning reform (upzoning, density changes)
- Rent control legislation
- Tenant protection laws
- Housing development incentives

**Impact Protocol:** Price-to-income ratios updated monthly. Rent control markets tracked separately. Policy impact documented with effective dates.

---

### Transportation & Airline Policy Tracking

**Federal Level:**
- DOT passenger bill of rights updates
- FAA safety regulation changes
- Airline merger approvals/denials
- Consumer protection enforcement

**Impact Protocol:** Safety incident tracking continues regardless of policy. Service quality metrics (delays, cancellations) compared before/after policy implementation.

---

### Technology & AI Policy Tracking

**Federal Level:**
- AI safety regulations
- Tech antitrust enforcement
- Platform regulation
- Consumer privacy laws

**Impact Protocol:** AI Psychosis metric tracks policy implementation impact on user behavior. Subscription Overload tracks antitrust impact on bundling practices.

---

### Labor Market Policy Tracking

**Federal Level:**
- Unemployment insurance changes
- Job training program funding
- WARN Act enforcement (layoff notification requirements)

**Impact Protocol:** Layoff Watch tracks policy changes requiring advance notice. Unemployment benefit changes noted in context of job search despair data.

---

## Policy Impact Disclosure

When a significant policy change affects a metric:

1. **Baseline Recalculation:** Official score component updated with new data
2. **Historical Comparison:** Pre-policy vs post-policy scores documented
3. **Dashboard Notation:** Policy change flagged in methodology page with effective date
4. **Social Sentiment Tracking:** Continued collection to measure lived experience under new policy

**Example:** If Medicare negotiates prescription drug prices, healthcare official score would decrease (good), but social sentiment collection continues to verify if people actually experience relief or if insurers find new ways to deny coverage.

This approach ensures The Absurdity Index captures both regulatory changes AND whether those changes actually improve lived experience.

---

## Version History

**v1.0 (December 2025)**: Initial methodology
- Established 40/60 weighting
- 8 core metrics defined
- Sample size standards set
- Multi-platform collection implemented
- Policy change monitoring framework established

---

## Reproducibility

All data collection scripts are available in `/data-collection/` directory.
Anyone can verify results by following the same methodology with the documented search terms and sample sizes.

Policy changes are documented with sources and effective dates for independent verification.
