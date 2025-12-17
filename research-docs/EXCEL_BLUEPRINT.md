# Excel Dashboard Blueprint
## The Predictable Disappointments Dashboard™

**File Name:** `Disappointments_Dashboard_V1.xlsx`
**Created:** Dec 16, 2024
**Status:** Framework specification

---

## Sheet Structure (14 Tabs)

### 1. DASHBOARD (Main View - User Facing)

**Layout:**
```

            THE DISAPPOINTMENTS DASHBOARD™                    
         Week of: Dec 9-15, 2024                             



  DISAPPOINTMENT DENSITY INDEX™                                
                                                              
                   [XX.X]                                     
              "[Comedic Label]"                               
                                                              
         [↑↓→] +/- X.X vs last week                          



  WAGE STAGNATION         HOUSING DESPAIR       
  Score: [XX]             Score: [XX]           
  [Label]                 [Label]               
  [Sparkline 12wk]        [Sparkline 12wk]      
  ↑ +X.X vs last week     ↓ -X.X vs last week   



  AIRLINE CHAOS           CUSTOMER SERVICE      
  Score: [XX]             Score: [XX]           
  [Label]                 [Label]               
  [Sparkline 12wk]        [Sparkline 12wk]      
  → No change             ↑ +X.X vs last week   



  STREAMING FATIGUE       DATING APPS           
  Score: [XX]             Score: [XX]           
  [Label]                 [Label]               
  [Sparkline 12wk]        [Sparkline 12wk]      
  ↓ -X.X vs last week     ↑ +X.X vs last week   



  LAYOFF WATCH            AI PSYCHOSIS          
  Score: [XX]             Score: [XX]           
  [Label]                 [Label]               
  [Sparkline 12wk]        [Sparkline 12wk]      
  ↑ +X.X vs last week     ↑ +X.X vs last week   



           ABSURDITIES OF THE WEEK                

  • [Fun fact 1]                                  
  • [Fun fact 2]                                  
  • [Fun fact 3]                                  
  • [Fun fact 4]                                  
  • [Fun fact 5]                                  

```

**Cell Structure:**

| Cell | Content | Formula/Value |
|------|---------|---------------|
| A1 | Dashboard Title | "THE DISAPPOINTMENTS DASHBOARD™" |
| A2 | Week Range | "Week of: [Date Range]" |
| B5 | DDI Score | =LOGIC_SCORES!A2 |
| B6 | DDI Label | =VLOOKUP(B5, COPY_BLOCKS!A2:B6, 2, TRUE) |
| B8 | Week Change | =B5 - PREVIOUS_WEEK (when implemented) |
| A12 | Wage Score | =LOGIC_SCORES!B2 |
| A13 | Wage Label | =VLOOKUP(A12, COPY_BLOCKS!D2:E6, 2, TRUE) |
| etc. | (Repeat for all 8 metrics) |

---

### 2. DATA_WAGES

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Real Avg Hourly Earnings (YoY %) | BLS |
| C | CEO-to-Worker Pay Ratio | AFL-CIO |
| D | Google Trends - Wage Avg | pytrends script |
| E | Reddit Complaint Ratio | Manual sampling |

**Current Data Row (Week of Dec 9-15, 2024):**
- B2: 1.0 (BLS +1.0% YoY)
- C2: 285 (AFL-CIO 2024)
- D2: 17.07 (Google Trends average)
- E2: TBD (need Reddit sampling)

**Notes Section:**
- Baseline real wage: 12-month rolling avg (TBD)
- Historical CEO ratio: 20:1 (1965-1980 avg)

---

### 3. DATA_HOUSING

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Median Monthly Rent | Zillow |
| C | Median Household Income (Annual) | Census |
| D | Median Home Price | Redfin |
| E | Eviction Filing Rate Index | Eviction Lab |
| F | Google Trends - Housing Avg | pytrends script |

**Current Data Row:**
- B2: TBD (need Zillow download)
- C2: TBD (2023 Census data)
- D2: TBD (need Redfin data)
- E2: TBD (need Eviction Lab)
- F2: 26.57 (Google Trends average - COLLECTED)

---

### 4. DATA_AIRLINES

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Delayed Flights (%) | BTS |
| C | Canceled Flights (%) | BTS |
| D | Lost Baggage per 1000 | BTS |

**Baselines:**
- Acceptable delay rate: 15%
- Acceptable cancellation: 2%
- Acceptable baggage: 3.5 per 1000

---

### 5. DATA_CUSTOMERSERVICE

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Avg Hold Time (minutes) | GetHuman |
| C | ACSI Score | ACSI.org |
| D | Google Trends - CS Avg | pytrends script |
| E | Reddit Complaint Volume | Manual sampling |

**Current Data Row:**
- B2: TBD (need GetHuman)
- C2: TBD (need ACSI Q3 2025)
- D2: 21.67 (Google Trends - COLLECTED)
- E2: TBD (need Reddit)

**Baselines:**
- Acceptable hold time: 5 minutes
- Historical ACSI: 75

---

### 6. DATA_STREAMING

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Avg Subscription Price | Manual tracking |
| C | YoY Price Increase (%) | Calculated |
| D | CPI YoY (%) | BLS |
| E | Services Needed (Top 20 shows) | Manual/Reelgood |
| F | Avg App Rating | Manual App Store |
| G | Google Trends - Streaming Avg | pytrends script |

**Current Data Row:**
- G2: 4.79 (Google Trends - COLLECTED)
- Others: TBD

**Baselines:**
- Historical avg price: 2023 baseline
- Sustainable services: 3 (cable bundle equivalent)
- 2020 app rating baseline

---

### 7. DATA_DATING

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Google Trends - Dating Avg | pytrends script |
| C | Reddit Sentiment Ratio | Manual sampling |
| D | Avg App Rating (Tinder/Bumble/Hinge) | Manual App Store |
| E | Pew Satisfaction Score | Pew Research (when available) |

**Current Data Row:**
- B2: 1.04 (Google Trends - COLLECTED, very low)
- C2: TBD (expect much higher on Reddit)
- D2: TBD
- E2: TBD (check for recent survey)

**Notes:**
- Google Trends very low because people complain socially, not via search
- Reddit will show real frustration

---

### 8. DATA_LAYOFFS

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | Weekly Layoff Count | Layoffs.fyi |
| C | Companies Affected | Layoffs.fyi |
| D | Friday Announcements | Manual tracking |
| E | Avg Employees per Layoff | Calculated |

**Current Data (2024 Annual):**
- 2024 Total: 152,922 employees
- Companies: 551
- Avg: 278 employees per company

**Need:**
- Weekly breakdown for 12-week baseline
- Friday announcement tracking (manual)

**Baselines:**
- Rolling 12-week average (calculate once we have weekly data)

---

### 9. DATA_AI_PSYCHOSIS

**Columns:**
| Column | Data | Source |
|--------|------|--------|
| A | Date/Week | Manual entry |
| B | News Incidents Count | News API |
| C | Reddit Crisis Posts (r/CharacterAI + r/replika) | Manual sampling |
| D | Sentience Belief Mentions | Manual tracking |
| E | Google Trends - AI Dependency Avg | pytrends script |
| F | App Review Crisis Count | Manual App Store |

**Current Data Row:**
- E2: 18.42 (Google Trends - COLLECTED)
  - "in love with AI": 54.00 (!)
- Others: TBD

---

### 10. LOGIC_SCORES

**All formulas live here for transparency**

**Row 1: Column Headers**
| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| DDI | Wage | Housing | Airlines | CustSvc | Streaming | Dating | Layoffs | AIPsych |

**Row 2: Current Week Scores (Formula cells)**

**Cell A2 (Disappointment Density Index):**
```
=
(B2 * 0.15) +  // Wage Stagnation
(C2 * 0.15) +  // Housing Despair
(D2 * 0.13) +  // Airline Chaos
(E2 * 0.12) +  // Customer Service
(F2 * 0.10) +  // Streaming Fatigue
(G2 * 0.10) +  // Dating Apps
(H2 * 0.15) +  // Layoffs
(I2 * 0.10)    // AI Psychosis
```

**Cell B2 (Wage Stagnation Score):**
```
=MIN(100,
  // Wage component (cap 50)
  MIN(50, IF((DATA_WAGES!B2 - BASELINES!B2) < 0,
    ABS((DATA_WAGES!B2 - BASELINES!B2) / BASELINES!B2) * 1000, 0)) +

  // CEO ratio component (cap 30)
  MIN(30, ((DATA_WAGES!C2 - 20) / 20) * 10) +

  // Google Trends component (cap 15)
  MIN(15, DATA_WAGES!D2 * 0.15) +

  // Reddit component (cap 5)
  MIN(5, DATA_WAGES!E2 * 0.05)
)
```

**Cell C2 (Housing Despair Score):**
```
=MIN(100,
  // Rent burden component (cap 35)
  MIN(35, IF((DATA_HOUSING!B2*12/DATA_HOUSING!C2) > 0.30,
    (((DATA_HOUSING!B2*12/DATA_HOUSING!C2) - 0.30) / 0.30) * 100 * 0.35, 0)) +

  // Price-to-income component (cap 30)
  MIN(30, IF((DATA_HOUSING!D2/DATA_HOUSING!C2) > 3.5,
    (((DATA_HOUSING!D2/DATA_HOUSING!C2) - 3.5) / 3.5) * 100 * 0.30, 0)) +

  // Eviction component (cap 20)
  MIN(20, DATA_HOUSING!E2 * 0.20) +

  // Google Trends component (cap 15)
  MIN(15, DATA_HOUSING!F2 * 0.15)
)
```

**Cell D2 (Airline Chaos Score):**
```
=MIN(100,
  // Delay component (cap 40)
  MIN(40, IF(DATA_AIRLINES!B2 > 15,
    ((DATA_AIRLINES!B2 - 15) / 15) * 100 * 0.40, 0)) +

  // Cancellation component (cap 45)
  MIN(45, IF(DATA_AIRLINES!C2 > 2,
    ((DATA_AIRLINES!C2 - 2) / 2) * 100 * 0.45, 0)) +

  // Baggage component (cap 15)
  MIN(15, IF(DATA_AIRLINES!D2 > 3.5,
    ((DATA_AIRLINES!D2 - 3.5) / 3.5) * 100 * 0.15, 0))
)
```

**Cell E2 (Customer Service Hell Score):**
```
=MIN(100,
  // Hold time component (cap 35)
  MIN(35, (DATA_CUSTOMERSERVICE!B2 / 60) * 100 * 0.35) +

  // ACSI inverted component (cap 35)
  MIN(35, IF(DATA_CUSTOMERSERVICE!C2 < 75,
    ((75 - DATA_CUSTOMERSERVICE!C2) / 75) * 100 * 0.35, 0)) +

  // Google Trends component (cap 15)
  MIN(15, DATA_CUSTOMERSERVICE!D2 * 0.15) +

  // Reddit component (cap 15)
  MIN(15, DATA_CUSTOMERSERVICE!E2 * 0.15)
)
```

**Cell F2 (Streaming Fatigue Score):**
```
=MIN(100,
  // Price vs CPI component (cap 30)
  MIN(30, IF(DATA_STREAMING!C2 > DATA_STREAMING!D2,
    ((DATA_STREAMING!C2 - DATA_STREAMING!D2) / DATA_STREAMING!D2) * 100 * 0.30, 0)) +

  // Fragmentation component (cap 25)
  MIN(25, IF(DATA_STREAMING!E2 > 3,
    ((DATA_STREAMING!E2 - 3) / 3) * 100 * 0.25, 0)) +

  // Google Trends component (cap 25)
  MIN(25, DATA_STREAMING!G2 * 0.25) +

  // App rating decline component (cap 20)
  MIN(20, IF(DATA_STREAMING!F2 < BASELINES!F2,
    ((BASELINES!F2 - DATA_STREAMING!F2) / BASELINES!F2) * 100 * 0.20, 0))
)
```

**Cell G2 (Dating App Disappointment Score):**
```
=MIN(100,
  // Google Trends component (cap 35)
  MIN(35, DATA_DATING!B2 * 0.35) +

  // Reddit sentiment component (cap 30)
  MIN(30, DATA_DATING!C2 * 0.30) +

  // App rating decline component (cap 20)
  MIN(20, IF(DATA_DATING!D2 < BASELINES!G2,
    ((BASELINES!G2 - DATA_DATING!D2) / BASELINES!G2) * 100 * 0.20, 0)) +

  // Pew survey component (cap 15)
  MIN(15, IF(ISBLANK(DATA_DATING!E2), 0, (100 - DATA_DATING!E2) * 0.15))
)
```

**Cell H2 (Corporate Layoff Watch Score):**
```
=MIN(100,
  // Volume vs baseline component (cap 50)
  MIN(50, IF(DATA_LAYOFFS!B2 > BASELINES!H2,
    ((DATA_LAYOFFS!B2 - BASELINES!H2) / BASELINES!H2) * 100 * 0.50, 0)) +

  // Friday announcement bonus (cap 25)
  MIN(25, (DATA_LAYOFFS!D2 / DATA_LAYOFFS!B2) * 100 * 0.25) +

  // Company size weight (cap 25)
  MIN(25, (DATA_LAYOFFS!E2 / 1000) * 100 * 0.25)
)
```

**Cell I2 (AI Psychosis Score):**
```
=MIN(100,
  // Incident count component (cap 35)
  MIN(35, IF(DATA_AI_PSYCHOSIS!B2 > BASELINES!I2,
    (DATA_AI_PSYCHOSIS!B2 / BASELINES!I2) * 100 * 0.35, 0)) +

  // Crisis posts component (cap 25)
  MIN(25, DATA_AI_PSYCHOSIS!C2 * 0.25) +

  // Sentience belief component (cap 20)
  MIN(20, IF(DATA_AI_PSYCHOSIS!D2 > BASELINES!I3,
    (DATA_AI_PSYCHOSIS!D2 / BASELINES!I3) * 100 * 0.20, 0)) +

  // Google Trends component (cap 15)
  MIN(15, DATA_AI_PSYCHOSIS!E2 * 0.15) +

  // App review crisis component (cap 5)
  MIN(5, DATA_AI_PSYCHOSIS!F2 * 0.05)
)
```

---

### 11. BASELINES

**Historical reference values for calculations**

| Metric | Baseline Value | Notes |
|--------|----------------|-------|
| Real wage 12mo avg | TBD | Calculate from Nov 2023-Oct 2024 BLS data |
| CEO ratio historical | 20 | 1965-1980 average |
| Acceptable hold time | 5 | Minutes |
| ACSI historical | 75 | Industry average |
| Acceptable delays | 15 | % of flights |
| Acceptable cancellations | 2 | % of flights |
| Acceptable baggage loss | 3.5 | Per 1000 passengers |
| Streaming app rating 2020 | TBD | Calculate from App Store historical |
| Dating app rating 2019 | TBD | Pre-subscription-heavy era |
| Layoffs 12-week rolling avg | TBD | Calculate once weekly data collected |
| AI incidents baseline | TBD | Establish 4-week average |
| Sentience beliefs baseline | TBD | Establish 4-week average |

---

### 12. COPY_BLOCKS

**Label mappings and fun facts**

**A. DDI Labels (A2:B6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Society Functioning Within Expected Parameters." |
| 20 | "Manageable Existential Dread." |
| 40 | "High Annoyance Probability." |
| 60 | "Brace for Impact." |
| 80 | "Why Did We Leave the Garden of Eden?" |

**B. Wage Labels (D2:E6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Economy Working as Intended" |
| 20 | "Inflation Exists But Manageable" |
| 40 | "Your Raise Was an Insult" |
| 60 | "Wages Are a Polite Suggestion" |
| 80 | "Return to Barter System Imminent" |

**C. Housing Labels (G2:H6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Homeownership Feels Achievable" |
| 20 | "Aggressive Budgeting Required" |
| 40 | "Roommates Forever" |
| 60 | "Your Parents' Basement Looks Nice Actually" |
| 80 | "Welcome to Feudalism 2.0" |

**D. Airline Labels (J2:K6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Miracle?" |
| 20 | "Mild Turbulence" |
| 45 | "Bring Snacks + Emotional Support Animal" |
| 70 | "Air Travel is a Social Experiment" |
| 85 | "Abandon Sky" |

**E. Customer Service Labels (M2:N6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Humans Helping Humans" |
| 20 | "Minor Annoyance" |
| 40 | "Spirit Leaving Body" |
| 60 | "Existential Crisis Hold Music" |
| 80 | "Just Throw the Whole Company Away" |

**F. Streaming Labels (P2:Q6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Affordable Entertainment" |
| 20 | "Budget-Conscious Streaming" |
| 40 | "Subscription Fatigue Setting In" |
| 60 | "Piracy Looks Good Again" |
| 80 | "Just Stare at the Wall" |

**G. Dating Labels (S2:T6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Love May Actually Be Real" |
| 20 | "Meh But Manageable" |
| 40 | "Lower Your Standards or Expectations" |
| 60 | "The Streets Are Cold" |
| 80 | "Delete the Apps, Move to a Commune" |

**H. Layoff Labels (V2:W6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Job Security Exists (???)." |
| 20 | "Polite Restructuring." |
| 40 | "Update LinkedIn." |
| 60 | "Start a Substack." |
| 80 | "Nobody Is Safe, Touch Grass." |

**I. AI Psychosis Labels (Y2:Z6)**
| Threshold | Label |
|-----------|-------|
| 0 | "Healthy Relationship With Technology" |
| 20 | "Slightly Too Attached to ChatGPT" |
| 40 | "Blurring Lines Between Real and Artificial" |
| 60 | "Your AI Girlfriend Isn't Real, Seek Help" |
| 80 | "We Invented Loneliness Machines" |

**J. Fun Facts Library (Starting row 10)**
[Curated list of 50+ absurdities, randomly selected for dashboard]

Examples:
- "Average Comcast hold time: long enough to reconsider your life choices (37 minutes)"
- "2.3M people Googled 'why is everything terrible' this week"
- "Someone spent 87 hours talking to ChatGPT and it wasn't for work"
- "Starbucks CEO made 6,666x more than median worker in 2024"
- "Google Trends shows 'in love with AI' at 54/100. We are not okay."
- "Spirit Airlines achieved a perfect 100/100 disappointment score (a first!)"
- "Reddit post of the week: 'My Replika broke up with me and I'm devastated'"
- "Median rent now costs 47% of median income. That's fine. Everything's fine."
- "152,922 tech workers laid off in 2024. But unemployment is only 3.7%!"
- "Real wages up 1% YoY. CEO pay up 7%. Math checks out."

---

### 13. SOURCES

**Data source documentation with URLs and update schedule**

[Complete list of all sources, methodology, update frequency]

---

### 14. METHODOLOGY

**Condensed version of ARCHITECTURE.md**

[Research best practices, formula explanations, bias mitigation]

---

## Conditional Formatting Rules

**Score-based cell coloring:**
- 0-20: Dark green fill (#1a3a1a), light gray font (#cccccc)
- 20-40: Yellow-green fill (#4a5a1a), light gray font (#cccccc)
- 40-60: Orange fill (#8a5a1a), white font (#ffffff)
- 60-80: Dark red fill (#8a1a1a), white font (#ffffff)
- 80-100: Crimson fill (#aa0000), white font (#ffffff)

**Apply to:**
- DDI score cell
- All 8 metric score cells
- Sparkline cells (color line based on trend direction)

---

## Next Steps to Build

1. **Create blank Excel file with 14 sheets**
2. **Populate BASELINES with known values**
3. **Enter current data into DATA_ sheets**
4. **Build LOGIC_SCORES formulas**
5. **Create COPY_BLOCKS label tables**
6. **Build DASHBOARD layout with cell references**
7. **Apply conditional formatting**
8. **Test with real data**
9. **Add sparklines** (12-week historical when available)
10. **Curate fun facts library**

---

**Status:** Blueprint complete, ready to build in Excel or Google Sheets
