# The Absurdity Index: Complete Methodology & Formulas

**Version:** 1.0
**Last Updated:** December 20, 2025
**Status:** Living document - will be updated as methodology evolves

---

## Core Philosophy

### What Is Absurdity?

The Absurdity Index quantifies a subjective but widely-felt sense: that we live in an insane society actively causing its own misery. This is not a precise clinical term—it's the recognition that our systems produce outcomes that seem increasingly detached from human wellbeing.

### Methodological Approach

We combine two data sources to create more sound, relevant, and accurate measurements than either source alone:

1. **Official Statistics (40% weight):** Government reports, industry data, economic indicators
2. **Systematically Quantified Qualitative Data (60% weight):** Social media content categorized by severity

Official statistics tell you what's happening at the macro level. Systematically quantifying lived experiences tells you what's happening at the human level. Together, they provide a more complete and accurate picture than either source alone.

This is not about finding "gaps" or "discrepancies"—it's about enhancing the accuracy of our measurements by incorporating data from multiple sources.

### Transparency Over Perfection

This is an experimental methodology. We prioritize:
- Explicit documentation of all formulas
- Verifiable data sources
- Honest acknowledgment of limitations
- Reproducible processes

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

(Section 3 - To be added)

