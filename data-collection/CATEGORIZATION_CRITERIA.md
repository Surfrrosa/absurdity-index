# Content Categorization Criteria

**Version:** 1.0
**Last Updated:** December 20, 2025

---

## Overview

All social media content (videos, posts, reviews) is categorized into three severity levels based on the impact described in the content. This document provides explicit criteria for consistent, reproducible categorization across all metrics.

---

## Universal Categorization Framework

### Level 3: CRISIS
**Definition**: Life-altering negative impact, severe consequences, abandonment of hope

**General Indicators**:
- Financial ruin or bankruptcy
- Severe mental health impact (depression, anxiety, suicidal ideation)
- Gave up entirely / lost all hope
- Life-threatening situations
- Irreversible losses (missed major life events, deaths)
- Multiple severe problems simultaneously
- Desperation and helplessness

**Technical Criteria**:
- 2+ Level 3 keywords present in title/description, OR
- 1 critical phrase from designated list

### Level 2: STRUGGLING / FRUSTRATED
**Definition**: Active struggle, repeated negative experiences, burnout

**General Indicators**:
- Ongoing frustration and stress
- Burnout or exhaustion
- Multiple failed attempts
- Significant time/money wasted
- Actively seeking solutions (considering quitting, taking breaks)
- Feeling stuck or trapped
- System exploitation awareness

**Technical Criteria**:
- 2+ Level 2 keywords present in title/description, OR
- 1 common frustration phrase from designated list

### Level 1: AWARE
**Definition**: Awareness without crisis, informational content, mild frustration

**General Indicators**:
- General awareness of issues
- Educational/informational content
- Mild annoyance or confusion
- Navigating systems successfully (but noting difficulty)
- Theoretical discussions

**Technical Criteria**:
- Content is relevant to metric topic
- Does not meet Level 2 or Level 3 criteria
- Default category for relevant content

---

## Metric-Specific Criteria

### What Healthcare?

**Relevance Filter**: Must mention healthcare, insurance, medical, hospital, claims, treatment, or related terms

**Level 3 - Crisis**:
- Keywords: `bankruptcy`, `collections`, `medical debt`, `going broke`, `can't afford treatment`, `life-saving`, `cancer treatment`, `dying`, `emergency`, `life or death`
- Examples:
  - "Filed for bankruptcy due to medical bills"
  - "Denied life-saving cancer treatment"
  - "Died because insurance wouldn't cover"

**Level 2 - Struggling**:
- Keywords: `denied`, `claim denied`, `rejected`, `appeal denied`, `won't cover`, `can't afford`, `prior authorization`
- Examples:
  - "Insurance denied my claim three times"
  - "Can't afford insulin even with insurance"
  - "Prior authorization nightmare for 6 months"

**Level 1 - Aware**:
- Examples:
  - "Understanding your medical bill"
  - "How insurance works (confusing!)"
  - "Billing confusion resolved after 2 calls"

---

### AI Psychosis

**Relevance Filter**: Must mention AI companions, chatbots, character.ai, replika, or similar platforms

**Level 3 - Crisis**:
- Keywords: `addicted`, `dependency`, `can't stop`, `replacing humans`, `lost touch with reality`, `prefer AI`, `only friend`, `isolation`, `mental health crisis`, `delusional`
- Examples:
  - "AI chatbot is my only friend"
  - "Addicted to Character.AI, can't function"
  - "Lost interest in real relationships"

**Level 2 - Struggling**:
- Keywords: `spending hours`, `daily use`, `emotional attachment`, `concerned`, `hard to stop`, `prefer chatting`, `avoiding people`
- Examples:
  - "Using AI companion daily for emotional support"
  - "Concerned about my attachment to Replika"
  - "Spending 4+ hours per day chatting"

**Level 1 - Aware**:
- Examples:
  - "Trying AI companions for the first time"
  - "AI chatbot technology explained"
  - "Casual use for entertainment"

---

### Subscription Overload

**Relevance Filter**: Must mention subscriptions, streaming, software-as-service, monthly payments, recurring charges

**Level 3 - Crisis**:
- Keywords: `can't cancel`, `trapped`, `financial stress`, `working to pay subscriptions`, `forgot what paying for`, `hundreds per month`, `out of control`, `subscription debt`
- Examples:
  - "Paying $800/month for subscriptions I don't use"
  - "Can't figure out how to cancel, customer service nightmare"
  - "Working overtime just to afford streaming services"

**Level 2 - Struggling**:
- Keywords: `too many`, `price increase`, `frustrated`, `quarterly purge`, `forgot about`, `adding up`, `need to cancel`, `subscription fatigue`
- Examples:
  - "Another price increase, considering canceling"
  - "Quarterly subscription audit reveals $200/month waste"
  - "Forgot about 5 subscriptions for months"

**Level 1 - Aware**:
- Examples:
  - "Comparing streaming service options"
  - "Managing subscriptions with an app"
  - "New subscription service launches"

---

### Wage Stagnation

**Relevance Filter**: Must mention wages, salary, inflation, cost of living, paycheck, working poor

**Level 3 - Crisis**:
- Keywords: `homeless despite working`, `food insecure`, `can't afford food`, `working poor`, `three jobs`, `living in car`, `choosing between`, `medical or food`, `working full-time homeless`
- Examples:
  - "Working full-time but homeless"
  - "Three jobs and still can't eat"
  - "Choosing between rent and food weekly"

**Level 2 - Struggling**:
- Keywords: `paycheck to paycheck`, `no savings`, `inflation hurting`, `wages not keeping up`, `side hustle required`, `struggling`, `barely surviving`
- Examples:
  - "Living paycheck to paycheck despite good job"
  - "Need 2 side hustles to afford basics"
  - "Wages haven't increased but everything costs more"

**Level 1 - Aware**:
- Examples:
  - "Understanding the inflation rate"
  - "Wage growth vs inflation explained"
  - "Budgeting tips for tight times"

---

### Housing Despair

**Relevance Filter**: Must mention housing, rent, mortgage, homeownership, property, apartment

**Level 3 - Crisis**:
- Keywords: `gave up on homeownership`, `will never own`, `accepting renting forever`, `priced out`, `homeless`, `evicted`, `housing insecurity`, `living with parents at 35`
- Examples:
  - "Accepted I'll never own a home"
  - "40 years old, still with parents, can't afford rent"
  - "Evicted despite paying on time"

**Level 2 - Struggling**:
- Keywords: `saving forever`, `deposit impossible`, `rent increase`, `unaffordable`, `bidding war`, `outbid`, `multiple offers`, `rejected application`
- Examples:
  - "Saving for 10 years, still can't afford deposit"
  - "Lost 15th bidding war this year"
  - "Rent increased $500, can barely afford"

**Level 1 - Aware**:
- Examples:
  - "Housing market trends 2025"
  - "First-time homebuyer guide"
  - "Rent vs buy calculator"

---

### Dating App Despair

**Relevance Filter**: Must mention dating apps, tinder, hinge, bumble, online dating, relationships, swiping

**Level 3 - Crisis**:
- Keywords: `quit`, `gave up`, `hopeless`, `will never find`, `mental health`, `depression`, `anxiety`, `self-esteem destroyed`, `confidence destroyed`, `therapy`, `emotional damage`, `trauma`
- Examples:
  - "Quit all dating apps, gave up entirely"
  - "Dating apps destroyed my mental health"
  - "In therapy because of dating app trauma"

**Level 2 - Struggling**:
- Keywords: `burnt out`, `burnout`, `exhausted`, `frustrated`, `waste of time`, `no matches`, `ghosted`, `breadcrumbing`, `endless swiping`, `algorithm rigged`, `considering quitting`
- Examples:
  - "Burnt out after 2 years of swiping"
  - "Ghosted 20 times this month"
  - "Exhausted, considering taking a break"

**Level 1 - Aware**:
- Examples:
  - "Dating app tips for beginners"
  - "Which dating app is right for you?"
  - "Profile optimization guide"

---

### Layoff Watch

**Relevance Filter**: Must mention layoffs, job loss, unemployment, job search, fired, applications

**Level 3 - Crisis**:
- Keywords: `months unemployed`, `500+ applications`, `financial crisis`, `losing home`, `can't find work`, `age discrimination`, `overqualified`, `giving up`, `desperate`
- Examples:
  - "8 months unemployed, 600 applications, 3 interviews"
  - "Lost home due to layoff, can't find work"
  - "Overqualified for everything, desperate"

**Level 2 - Struggling**:
- Keywords: `hundreds of applications`, `no response`, `ghosted by recruiters`, `months searching`, `resume anxiety`, `layoff fear`, `daily anxiety`, `job insecurity`
- Examples:
  - "200 applications, zero responses"
  - "Living in fear of layoffs daily"
  - "3 months searching, no offers"

**Level 1 - Aware**:
- Examples:
  - "Layoff news from tech company X"
  - "Job market trends 2025"
  - "Resume tips for job search"

---

### Airline Chaos

**Relevance Filter**: Must mention flight, airline, airport, travel, plane, cancelled, delayed, luggage

**Level 3 - Crisis**:
- Keywords: `stranded for days`, `missed funeral`, `missed wedding`, `lost all luggage`, `no compensation`, `no refund`, `sleeping at airport`, `abandoned`, `medical emergency`, `ruined vacation`
- Examples:
  - "Stranded 3 days, missed funeral, no help"
  - "Lost all luggage, zero compensation"
  - "Slept at airport 2 nights with newborn"

**Level 2 - Struggling**:
- Keywords: `hours delayed`, `cancelled twice`, `rebooked multiple times`, `missed connection`, `lost luggage`, `damaged luggage`, `rude staff`, `no help`, `terrible customer service`
- Examples:
  - "Flight delayed 8 hours, no meal vouchers"
  - "Lost luggage on 3 consecutive flights"
  - "Rebooked 4 times, still not home"

**Level 1 - Aware**:
- Examples:
  - "Flight delay statistics by airline"
  - "Passenger rights explained"
  - "Travel tips for busy season"

---

## Quality Assurance

### Inter-Coder Reliability
When multiple people categorize content:
- Agreement on Level 3 should be >90% (clear crisis indicators)
- Agreement on Level 2 should be >80% (some subjectivity in "struggling")
- Agreement on Level 1/2 boundary may be ~70% (most subjective)

### Edge Cases
**When content describes multiple levels**:
- Categorize based on the **highest severity** mentioned
- Example: "I was frustrated (L2) and almost gave up (L3)" → Level 3

**When content is ambiguous**:
- Default to **lower severity** to avoid inflating crisis ratios
- Document uncertainty for review

**When content is satirical/humorous**:
- Assess underlying message, not tone
- Absurdist humor about crisis → still Level 3 if describing real crisis
- Pure satire with no underlying struggle → Level 1

---

## Reproducibility

All categorization is:
1. **Rule-based**: Keyword matching with explicit thresholds
2. **Transparent**: All keywords documented above
3. **Auditable**: Original content title/description stored
4. **Updatable**: Criteria can evolve with version tracking

To verify categorization for any metric:
```bash
cd data-collection
python3 [metric]-youtube-collector.py
# Review collected data CSV with categories
```

---

## Version History

**v1.0 (Dec 20, 2025)**
- Initial documentation of criteria
- Extracted from existing collector implementations
- Standardized 3-level framework across all metrics
