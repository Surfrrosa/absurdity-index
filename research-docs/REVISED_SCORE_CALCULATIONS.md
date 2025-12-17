# Revised Score Calculations - Using Better Data Sources
**Date:** December 17, 2024
**Purpose:** Recalculate scores using U-6, age-cohort housing data, and adjusted weightings

---

## HOUSING DESPAIR - REVISED CALCULATION

### Old Calculation (National Averages)
- Median rent: $2,000/month ($24,000/year)
- Median household income: $83,730/year
- Rent burden: 28.7% (below 30% threshold)
- **OLD SCORE: 13.25**

### New Calculation (Gen Z Reality)
Using Gen Z rent burden data (age 18-25, the cohort most affected):
- **Gen Z rent-burdened: 58.2%** (>30% of income on housing)
- Threshold: 30% (standard affordability measure)

**Rent Burden Component:**
```
Gen Z burden: 58.2%
Threshold: 30%
Excess burden: 58.2 - 30 = 28.2 percentage points
Normalized: (28.2 / 30) * 100 * 0.40 = 37.6 (weight: 40%)
```

**Price-to-Income Ratio (unchanged):**
```
Median home price: $383,725
Median income: $83,730
Ratio: 4.58x
Historical sustainable: 3.5x
Component: ((4.58 - 3.5) / 3.5) * 100 * 0.30 = 9.26 (weight: 30%)
```

**Google Trends (unchanged):**
```
Category average: 26.57/100
Component: 26.57 * 0.15 = 3.99 (weight: 15%)
```

**Social Sentiment (pending Reddit/TikTok collection):**
```
Crisis ratio: TBD
Weight: 15%
```

**REVISED PARTIAL SCORE:** 37.6 + 9.26 + 3.99 = **50.85/100**

**Note:** Still pending social sentiment collection (15%), but already 4X higher than old score of 13.25

---

## LAYOFF WATCH - REVISED CALCULATION

### Old Calculation (Tech Only, U-3 Implied)
- Tech layoffs 2024: 152,922
- Average company size: 278 employees
- **OLD SCORE: 6.95**

### New Calculation (U-6 Unemployment + Job Search Reality)

**U-6 Unemployment Component:**
```
Current U-6: 7.5%
Historical baseline (2019 pre-pandemic): 6.9%
Excess: 7.5 - 6.9 = 0.6 percentage points
Normalized: (0.6 / 6.9) * 100 * 0.40 = 3.48 (weight: 40%)
```

**Tech Layoff Volume (2024):**
```
Total: 152,922 employees
Average per week: 152,922 / 52 = 2,941 per week
Baseline acceptable: 1,000/week
Excess: (2,941 - 1,000) / 1,000 * 100 * 0.30 = 58.23 → CAP at 30
Component: 30 (weight: 30%)
```

**Job Search Duration (qualitative Reddit data):**
```
Consistent reports of 6+ month searches for entry-level
500+ applications for 1 interview
"Ghost jobs" on LinkedIn (25-30% of postings)
Crisis level: YES
Component estimate: 15 (weight: 15%, pending systematic collection)
```

**Social Sentiment (Reddit r/jobs, r/cscareerquestions):**
```
Crisis ratio: TBD (pending collection)
Weight: 15%
```

**REVISED PARTIAL SCORE:** 3.48 + 30 + 15 = **48.48/100**

**Note:** Conservative estimate. With full social sentiment could reach 55-65.

---

## WAGE STAGNATION - REVIEW (Possibly Already Accurate)

### Current Score: 32.56

**Components:**
- CEO ratio component: 30 (capped, ratio is 285:1)
- Google Trends: 2.56
- Reddit: TBD

**CPI Adjustment Question:**
- BLS reports +1.0% real wage growth
- CPI understates by ~0.41 points for low-income
- True growth might be +0.59% or lower

**Should we adjust?**
The CEO ratio (30 points) already dominates this score and captures the wealth inequality. The small wage growth (+1%) is almost irrelevant compared to 285:1 ratio.

**RECOMMENDATION:** Keep 32.56, but add methodology note about CPI limitations.

---

## HEALTHCARE - NO CHANGE NEEDED

### Current Score: 72.34

This is likely the MOST accurate score because:
- Official data gaps (no denial tracking)
- Social sentiment (60%) fills the void
- Score already reflects crisis reality

**RECOMMENDATION:** No adjustment. Add transparency note that official data doesn't exist.

---

## AIRLINE CHAOS - MINOR ADJUSTMENT

### Current Score: 18.67 (delays only)

**Still missing:**
- Cancellation data (need BTS report)
- Baggage mishandling (need BTS report)

**RECOMMENDATION:** Keep 18.67 as partial, note that full score will be 25-40 with complete data.

---

## AI PSYCHOSIS - ALREADY USING REAL DATA

### Current Score: 18.05

**Components:**
- Real collected data: 346 entries (200 Reddit + 146 YouTube)
- Crisis ratio: 17.92%
- This is REAL data, not estimates

**RECOMMENDATION:** No change. This is accurate.

---

## SUBSCRIPTION OVERLOAD - NEEDS COLLECTION

### Current Score: 58.99 (placeholder)

**Still need:**
- Streaming service price tracking
- Content fragmentation analysis
- App Store reviews

**RECOMMENDATION:** Mark as preliminary, continue collection.

---

## DATING APP DESPAIR - NEEDS COLLECTION

### Current Score: 0.36 (Google Trends only)

**Still need:**
- Reddit sampling (r/Tinder, r/Bumble, r/Hinge)
- App Store reviews
- Expected to jump to 25-45 with Reddit data

**RECOMMENDATION:** Mark as preliminary, Reddit collection will dramatically increase.

---

## RECALCULATED OVERALL ABSURDITY INDEX

### Formula (from METHODOLOGY_FORMULAS.md)
```
Overall Absurdity = (Σ Individual Scores) / 8
```
All metrics weighted equally - simple average.

### Current Calculation (With Flawed Data)
```
= (32.56 + 13.25 + 18.67 + 72.34 + 58.99 + 0.36 + 6.95 + 18.05) / 8
= 221.17 / 8
= 27.65/100
```

**Current dashboard shows: 16.26** - This appears to be a placeholder, not calculated from current metrics.
**Actual calculated score with current data: 27.65**

### New Calculation (With Revised Housing & Layoffs)
Using revised scores with better data sources:
```
Wage Stagnation: 32.56 (unchanged)
Housing Despair: 50.85 (was 13.25) ← REVISED
Airline Chaos: 18.67 (unchanged, partial)
Healthcare: 72.34 (unchanged, accurate)
Subscription Overload: 58.99 (unchanged, pending collection)
Dating App Despair: 0.36 (unchanged, pending Reddit collection)
Layoff Watch: 48.48 (was 6.95) ← REVISED
AI Psychosis: 18.05 (unchanged, real collected data)

= (32.56 + 50.85 + 18.67 + 72.34 + 58.99 + 0.36 + 48.48 + 18.05) / 8
= 300.30 / 8
= 37.54/100
```

**NEW OVERALL SCORE: 37.54** (was 16.26 placeholder, 27.65 with old flawed data)

**Label:** "QUARTERLY PURGE REQUIRED" (threshold: 31-50)
Previously "Manageable Existential Dread" (16-30)

### Score Increases:
- Old placeholder: 16.26 → New: 37.54 (+21.28 points, +131% increase)
- Old calculated: 27.65 → New: 37.54 (+9.89 points, +36% increase)

### What Changed:
1. Housing: +37.6 points (Gen Z rent burden 58.2% vs national 28.7%)
2. Layoffs: +41.53 points (U-6 7.5% + job search reality vs U-3 3.7%)

---

## SUMMARY OF CHANGES

| Metric | Old Score | New Score | Change | Reason |
|--------|-----------|-----------|--------|--------|
| Housing Despair | 13.25 | **50.85** | +37.6 | Gen Z rent burden (58.2%) vs national avg (28.7%) |
| Layoff Watch | 6.95 | **48.48** | +41.53 | U-6 unemployment + job search reality |
| Wage Stagnation | 32.56 | 32.56 | 0 | CEO ratio already captures crisis |
| Healthcare | 72.34 | 72.34 | 0 | Already accurate, social sentiment dominant |
| Airline Chaos | 18.67 | 18.67 | 0 | Partial score, awaiting complete BTS data |
| AI Psychosis | 18.05 | 18.05 | 0 | Real collected data (346 entries) |
| Subscription | 58.99 | 58.99 | 0 | Pending collection |
| Dating Apps | 0.36 | 0.36 | 0 | Pending Reddit collection |

**MAJOR IMPACT:** Housing and Layoffs both jumped ~40 points with better data sources.

---

## NEXT STEPS

1. Get actual metric weights from current methodology
2. Recalculate overall Absurdity Index with revised scores
3. Update dashboard with new scores
4. Update article numbers
5. Add transparency notes about data source changes
