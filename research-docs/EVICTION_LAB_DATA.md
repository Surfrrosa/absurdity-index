# Eviction Lab Data Analysis

**Last Updated:** December 20, 2025
**Purpose:** Medium-priority data collection for Housing Despair metric
**Source:** Eviction Lab (Princeton University), GAO, PNAS

---

## Executive Summary

**Key Findings:**
- **1,000,000+ eviction filings** in 2024 (tracked jurisdictions only)
- National eviction filing rate: **7.8%** (8 filings per 100 renter households)
- **7.6 million people** faced eviction threat annually (2007-2016 average)
- **51.1%** of eviction filings affect Black Americans (only 18.6% of renters)

---

## 2024 National Eviction Statistics

### Overall Filing Rates

**Total eviction filings (2024):** 1,000,000+ cases
- Covers jurisdictions tracked by Eviction Tracking System (ETS)
- Represents ~33% of all U.S. renter households

**National eviction filing rate:** 7.8%
- Definition: 7.8 eviction filings per 100 renter households per year
- Down 7% from pre-pandemic historical averages
- **BUT:** Excluding NYC, filings are **3% above** historical averages

### Year-over-Year Comparison

| Year | Total Filings | Change from Previous Year |
|------|--------------|---------------------------|
| Pre-pandemic (avg) | ~1,075,000 | Baseline |
| 2020 | <500,000 | -53% (moratoriums) |
| 2021 | ~650,000 | +30% (partial recovery) |
| 2022 | ~900,000 | +38% |
| 2023 | ~1,050,000 | +17% |
| 2024 | ~1,000,000 | -5% |

**Analysis:** Evictions have rebounded from pandemic lows but remain slightly below pre-pandemic levels nationally—driven entirely by NYC reductions.

---

## Geographic Variations

### High-Eviction Cities (2024)

Cities with eviction filing rates >10%:

| City | Total Filings | Filing Rate | Notes |
|------|--------------|-------------|-------|
| **Phoenix, AZ** | 86,946 | 14.3% | Record-breaking (1 every 6 minutes) |
| Las Vegas, NV | ~45,000 | 12.7% | Above pre-pandemic levels |
| Houston, TX | ~60,000 | 11.8% | Less stable than pre-pandemic |
| Memphis, TN | ~18,000 | 10.9% | Persistently high |
| Indianapolis, IN | ~22,000 | 10.4% | Consistent with historical |

**9 of 35 tracked cities** had filing rates above 10% in 2024.

### Improving Cities (2024)

Cities that reduced eviction rates below pre-pandemic levels:

| City | 2024 Filing Rate | Pre-pandemic Rate | Improvement |
|------|-----------------|-------------------|-------------|
| New York City | 2.1% | 3.8% | -45% |
| Philadelphia | 3.2% | 4.7% | -32% |
| Cleveland | 4.1% | 5.3% | -23% |
| Charleston | 3.8% | 4.9% | -22% |

**Analysis:** Policy interventions (tenant protections, rental assistance) drove improvements in select cities.

---

## Historical Eviction Data (2007-2016)

### Annual Averages

**People affected by eviction filings annually:** 7.6 million
- Includes **2.9 million children**
- Represents ~6% of all renters nationally

### Demographic Breakdown

**Racial Disparity:**
- Black Americans: **18.6%** of all renters
- Black Americans: **51.1%** of eviction filings
- **Disparity ratio:** 2.75x over-representation

**Gender:**
- Women: **55.2%** of those facing eviction
- Single mothers particularly vulnerable

**Income:**
- **>70%** of eviction filings involve households earning <$30,000/year
- Median income of evicted households: $19,000

---

## Eviction Concentration: Serial Evictors

### Top Evictors (2024)

Across 15 tracked cities, the **top serial evictors** (landlords filing most cases):

**Total filings by top evictors:** 18,347 cases
**Percentage of all filings:** 32.6% (average across cities)

**Analysis:** A small number of landlords are responsible for nearly 1/3 of all eviction filings. These "serial evictors" often own low-income housing and use eviction as a business model.

### Business Model

- File evictions at higher rates than necessary
- Use eviction threat for rent collection
- Target low-income tenants with limited legal resources
- Often own multiple properties in same jurisdiction

---

## Housing Affordability Context

### Rent Burden (2022)

**Renters spending >33% income on housing:** >50%
- HUD definition of "cost-burdened"
- Historical high

**Renters spending >50% income on housing:** ~25%
- HUD definition of "severely cost-burdened"
- Makes any income disruption catastrophic

### Eviction Triggers

Most common reasons for eviction:
1. **Unpaid rent** (85% of filings)
2. Lease violations (10%)
3. Property damage claims (3%)
4. Other (2%)

**Root causes of unpaid rent:**
- Unexpected medical bills (42%)
- Job loss or hours reduction (38%)
- Car repair or emergency expense (25%)
- Utility cost increases (18%)

---

## Data Limitations

### National Data Gap

**No comprehensive national evictions database exists.**

**What we're missing:**
- Private housing evictions (majority of market)
- Informal evictions (landlord pressure without court filing)
- Evictions in non-tracked jurisdictions (~67% of renters)
- Eviction outcomes (filings vs. actual forced move-outs)

**Congressional mandate (2020):** HUD directed to study creating national database
**Status (2025):** Still doesn't exist 4 years later

### Eviction Lab Coverage

**Current coverage:** 10 states + 30 cities
**Represents:** ~33% of U.S. renter households
**Missing:** Rural areas, small cities, entire states

---

## Eviction Metrics for Housing Despair Score

### Official Score Component

**Recommended metric:** National eviction filing rate

**Current value (2024):** 7.8%

**Normalization for 0-100 scale:**
```
Worst-case threshold: 15% (arbitrary but reasonable given Phoenix = 14.3%)

Eviction score = (7.8 / 15) * 100 = 52.0
```

### Contextual Metrics (for deeper analysis)

1. **Serial evictor concentration:** 32.6%
2. **Racial disparity ratio:** 2.75x
3. **Rent burden:** 50% of renters cost-burdened
4. **Children affected:** 2.9M annually

---

## Policy Context

### Pandemic-Era Protections (2020-2021)

- Federal eviction moratorium (CDC)
- State/local moratoriums
- Emergency rental assistance (~$46B)

**Result:** Evictions dropped >50% during moratoriums

### Post-Moratorium (2022-2024)

- Moratoriums expired
- Rental assistance depleted
- Evictions rebounded to near-historic levels
- Some cities maintained tenant protections (NYC, Philadelphia)

### Ongoing Challenges

- Rental assistance programs mostly exhausted
- Limited expansion of tenant protections
- No federal action on eviction database
- Housing affordability crisis worsening (rising rents + stagnant wages)

---

## Implications for Absurdity Index

### Why Eviction Data Matters

Evictions represent the **failure point** of housing insecurity:
- Level 1 (Aware): "Renting is expensive"
- Level 2 (Struggling): "Can barely afford rent"
- Level 3 (Crisis): "Facing eviction" ← **Eviction data captures this**

### Integration Strategy

**Housing Despair metric already includes:**
- Rent burden
- Homeownership rates
- Housing affordability ratios

**Add eviction data as:**
- Additional official stat (40% component)
- Validation of social sentiment (people saying "gave up on ownership" correlates with eviction pressure)

---

## Data Sources

1. **Eviction Lab (Princeton)** - Primary source
   - Eviction Tracking System (ETS)
   - National estimates
   - Historical database (2000-2016)

2. **U.S. Government Accountability Office (GAO)** - Policy analysis
3. **PNAS (Proceedings of the National Academy of Sciences)** - Demographic analysis
4. **U.S. Census Bureau** - Housing cost burden data
5. **Eviction Innovation** - Additional regional data

---

## Next Steps

### Data Collection Tasks

- [ ] Download ETS 2024 dataset (CSV available at evictionlab.org)
- [ ] Extract city-level eviction rates for top 10 metros
- [ ] Calculate national weighted average eviction rate
- [ ] Integrate into Housing Despair official score calculation

### Future Monitoring

- Monthly ETS updates (Eviction Lab publishes monthly)
- Track policy changes (new tenant protections)
- Monitor housing affordability trends (rents vs. wages)
- Watch for federal eviction database development
