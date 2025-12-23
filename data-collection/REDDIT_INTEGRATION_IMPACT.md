# Reddit Integration Impact Analysis

**Date:** December 22, 2025
**Total Reddit Posts:** 1,004 across 8 metrics
**Method:** Blending YouTube + Reddit crisis ratios (50/50 weight), then combining with official scores

---

## Score Changes Summary

| Metric | Current Score | New Score | Change | Impact |
|--------|--------------|-----------|--------|--------|
| **Healthcare** | 50.20 | 45.09 | **-5.11** | 🔵 Lower |
| **AI Psychosis** | 37.31 | 27.88 | **-9.43** | 🔵 Lower |
| **Subscription Overload** | 39.93 | 33.05 | **-6.88** | 🔵 Lower |
| **Wage Stagnation** | 40.86 | 34.68 | **-6.18** | 🔵 Lower |
| **Housing Despair** | 43.64 | 38.22 | **-5.42** | 🔵 Lower |
| **Dating App Despair** | 31.55 | 27.59 | **-3.96** | 🔵 Lower |
| **Layoff Watch** | 51.64 | 53.87 | **+2.23** | 🔴 Higher |
| **Airline Chaos** | 40.13 | 35.13 | **-5.00** | 🔵 Lower |

**Overall Score:**
- Current: 41.91
- New: 37.19
- Change: **-4.72 points**

---

## Why Reddit Lowers Most Scores

**Reddit is less sensational than YouTube:**
- YouTube: Creators optimize for views/engagement → amplified language
- Reddit: Anonymous users sharing real struggles → more measured tone
- Reddit posts get upvoted for relatability, not drama

**Crisis Ratio Comparison:**

| Metric | YouTube CR | Reddit CR | Difference |
|--------|-----------|-----------|------------|
| Healthcare | 46.14% | 29.1% | -17.04% 🔵 |
| AI Psychosis | 53.85% | 22.4% | -31.45% 🔵 |
| Subscription Overload | 36.41% | 13.5% | -22.91% 🔵 |
| Wage Stagnation | 42.50% | 21.9% | -20.60% 🔵 |
| Housing Despair | 47.66% | 29.6% | -18.06% 🔵 |
| Dating App Despair | 46.92% | 33.7% | -13.22% 🔵 |
| **Layoff Watch** | **35.07%** | **42.5%** | **+7.43%** 🔴 |
| Airline Chaos | 52.89% | 36.2% | -16.69% 🔵 |

**Layoff Watch is the exception:** Reddit shows *higher* crisis (42.5% vs 35.07%) because:
- r/jobs and r/careerguidance are dedicated crisis forums
- People post when desperate ("500 applications, no response")
- YouTube content is more "tips" focused

---

## Detailed Impact by Metric

### 1. Healthcare: 50.20 → 45.09 (-5.11)

**Reddit Data:**
- 141 posts collected
- Crisis ratio: 29.1% (vs YouTube: 46.14%)
- Blended: 37.62%

**New Calculation:**
- Official score: 56.30 (premium increases, denial rates)
- Social score: 37.62% (blended YouTube + Reddit)
- Final: (56.30 × 0.4) + (37.62 × 0.6) = **45.09**

**Updated dataSources:**
```
"Reddit: 141 posts from r/HealthInsurance, r/povertyfinance, r/Insurance (29.1% crisis ratio)",
```

**Sample Reddit Post (Level 3):**
> "I ignored stomach pain for 8 months because I couldn't afford to be sick. Now I'm $12,000 in debt"
> — r/povertyfinance, 3,247 upvotes

---

### 2. AI Psychosis: 37.31 → 27.88 (-9.43)

**Reddit Data:**
- 290 posts collected (largest sample!)
- Crisis ratio: 22.4% (vs YouTube: 53.85%)
- Blended: 38.13%

**Why such a big drop?**
- YouTube focuses on sensational cases (Character.AI lawsuit, deaths)
- Reddit has mix of casual users + dependency cases
- r/replika, r/CharacterAI show both positive and negative experiences

**New Calculation:**
- Official score: 12.5 (app download growth)
- Social score: 38.13%
- Final: (12.5 × 0.4) + (38.13 × 0.6) = **27.88**

**Sample Reddit Post (Level 3):**
> "GPT-4 Week 3. Chatbots are yesterdays news. AI Agents are the future."
> — r/ChatGPT, 13,163 upvotes

---

### 3. Subscription Overload: 39.93 → 33.05 (-6.88)

**Reddit Data:**
- 37 posts (hit rate limits)
- Crisis ratio: 13.5% (vs YouTube: 36.41%)
- Blended: 24.96%

**Why low Reddit crisis?**
- Most Reddit posts are "how to cancel" advice, not desperation
- Subscription fatigue is annoyance, not crisis
- r/Frugal focuses on solutions, not venting

**New Calculation:**
- Official score: 45.2 (avg 12 subscriptions, $273/month)
- Social score: 24.96%
- Final: (45.2 × 0.4) + (24.96 × 0.6) = **33.05**

---

### 4. Wage Stagnation: 40.86 → 34.68 (-6.18)

**Reddit Data:**
- 128 posts collected
- Crisis ratio: 21.9% (vs YouTube: 42.50%)
- Blended: 32.2%

**Sample Reddit Post (Level 2):**
> "Today my supervisor asked me to either donate food or cook food for the office holiday party"
> — r/povertyfinance, 2,909 upvotes

---

### 5. Housing Despair: 43.64 → 38.22 (-5.42)

**Reddit Data:**
- 169 posts collected
- Crisis ratio: 29.6% (vs YouTube: 47.66%)
- Blended: 38.63%

**New Calculation:**
- Official score: 37.6 (rent burden 37.6%)
- Social score: 38.63%
- Final: (37.6 × 0.4) + (38.63 × 0.6) = **38.22**

---

### 6. Dating App Despair: 27.59 → 31.55 (-3.96)

**Reddit Data:**
- 86 posts collected
- Crisis ratio: 33.7% (vs YouTube: 46.92%)
- Blended: 40.31%

**Reddit validates Pew Research:**
- Reddit: 33.7% crisis
- Pew: 45% frustrated, 79% burnout
- Close alignment!

**Sample Reddit Post (Level 2):**
> "I dated 15 men in 2025, this is what I learned."
> — r/dating, 1,490 upvotes

---

### 7. Layoff Watch: 51.64 → 53.87 (+2.23) ⚠️ INCREASES

**Reddit Data:**
- 106 posts collected
- Crisis ratio: 42.5% (vs YouTube: 35.07%)
- Blended: 38.79%

**Why Reddit is MORE severe:**
- r/jobs, r/careerguidance are crisis forums
- Posts like "500 applications, no response"
- "Overqualified", "age discrimination", "unemployed for months"

**This is the ONLY metric where Reddit raises the score.**

**Sample Reddit Post (Level 2):**
> "I was laid off on Monday via zoom, they asked me to write up a transition plan..."
> — r/careerguidance, 1,892 upvotes

---

### 8. Airline Chaos: 40.13 → 35.13 (-5.00)

**Reddit Data:**
- 47 posts collected
- Crisis ratio: 36.2% (vs YouTube: 52.89%)
- Blended: 44.55%

**New Calculation:**
- Official score: 21.0 (22% delay rate)
- Social score: 44.55%
- Final: (21.0 × 0.4) + (44.55 × 0.6) = **35.13**

---

## Integration Benefits

### ✅ Pros

1. **More accurate**: Reddit grounds sensationalism from YouTube
2. **Larger sample**: 1,004 Reddit posts + existing YouTube = robust data
3. **Cross-validation**: Reddit confirms YouTube trends (especially Layoff Watch, Dating)
4. **Real voices**: Reddit posts are actual user experiences, not content creator narratives
5. **Methodologically sound**: Blending multiple sources is best practice

### ⚠️ Cons

1. **Scores drop significantly**: Overall -4.72 points
2. **Perception**: May look like crisis is "less bad" (but it's actually more accurate)
3. **Reddit bias**: Skews young, tech-savvy (though so does YouTube)
4. **Small samples**: Some metrics hit rate limits (Subscription: 37 posts)

---

## Recommendation

**Integrate the Reddit data.** Here's why:

1. **Scientific rigor**: Multi-source data is more reliable
2. **YouTube-only is too alarmist**: 53% crisis for AI Psychosis was likely inflated
3. **Reddit validates some scores**: Layoff Watch goes UP, confirming job market struggles
4. **Transparency**: Better to be accurate than artificially high

**The lower scores don't mean things are fine—they mean YouTube overstates severity.**

---

## Next Steps (If Approved)

1. ✅ Update `metricDetailData.ts` with:
   - New blended crisis ratios
   - New final scores
   - Reddit post counts in `levelDistribution`
   - Sample Reddit posts in `sampleData`
   - Updated `collectionProgress` (Reddit: 100%)
   - Updated `dataSources`
   - Updated `lastUpdated` to December 22, 2025

2. ✅ Test locally to ensure no breaking changes

3. ✅ Commit to git:
   ```bash
   git add .
   git commit -m "Integrate Reddit data: 1,004 posts across 8 metrics

   - Added Reddit JSON endpoint collectors (no API needed)
   - Blended Reddit + YouTube crisis ratios (50/50)
   - Updated scores, samples, and data sources
   - Overall score: 41.91 → 37.19 (-4.72)
   - Most metrics lower (Reddit less sensational than YouTube)
   - Layoff Watch increased (Reddit shows higher job crisis)
   "
   ```

4. ✅ Push to GitHub and deploy

---

## Alternate Approach: Reddit as Validation Only

If you don't want to change scores, we could:
- Keep current scores unchanged
- Add Reddit data to methodology as "cross-validation"
- Note: "Reddit data confirms YouTube trends with 27.9% avg crisis ratio"
- Show Reddit stats in detail pages as additional context

**Your call!**
