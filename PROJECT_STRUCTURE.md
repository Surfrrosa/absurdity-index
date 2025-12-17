# Project Structure

## Folder Organization

### `/app`
Next.js 15 application pages
- `page.tsx` - Main dashboard
- `methodology/` - Methodology page
- `status/` - Data collection progress tracker
- `layout.tsx` - Root layout with metadata

### `/components`
React components
- `AbsurdityScore.tsx` - Overall score display
- `MetricCard.tsx` - Individual metric cards
- `MetricDetail.tsx` - Expandable detail modals
- `Header.tsx` - Site header

### `/lib`
Utility libraries
- `metricDetailData.ts` - Metric data and types

### `/data-collection`
Python collection scripts and collected data

#### **Collection Scripts:**
- `healthcare-collector.py` - What Healthcare? data
- `dating-app-despair-collector.py` - Dating App Despair data
- `airline-chaos-collector.py` - Airline Chaos data
- `wage-stagnation-collector.py` - Wage Stagnation data
- `housing-despair-collector.py` - Housing Despair data
- `layoff-watch-collector.py` - Layoff Watch data
- `ai-psychosis-reddit-collector.py` - AI Psychosis Reddit data
- `ai-psychosis-youtube-collector.py` - AI Psychosis YouTube data
- `ai-psychosis-appstore-collector.py` - AI Psychosis App Store data
- `pull_google_trends.py` - Google Trends baseline data

#### **Documentation:**
- `METHODOLOGY_FORMULAS.md` - All scoring formulas
- `COLLECTION_QUICKSTART.md` - How to collect data

#### **Collected Data (`collected-data/`):**
- ✅ `reddit_posts_collected_20251216.csv` - **355 AI Psychosis Reddit posts**
- ✅ `youtube_videos_collected_20251216.csv` - **147 AI Psychosis YouTube videos**
- ✅ `google_trends_*.csv` - Google Trends data for all metrics
- `APP_STORE_SAMPLING_TEMPLATE.csv` - Template for App Store reviews
- `TIKTOK_SAMPLING_TEMPLATE.csv` - Template for TikTok sampling

### `/research-docs`
Background research, methodology development, and findings

#### **Core Documentation:**
- `ARCHITECTURE.md` - Full technical architecture
- `EXCEL_BLUEPRINT.md` - Original Excel dashboard design
- `PROJECT_STATUS_DEC16.md` - Project status snapshot

#### **AI Psychosis Research:**
- `AI_PSYCHOSIS_METHODOLOGY.md` - Detailed methodology
- `AI_PSYCHOSIS_COLLECTION_PLAN.md` - Collection plan
- `PRELIMINARY_AI_PSYCHOSIS_DATA.md` - Initial findings
- `AI_PSYCHOSIS_ENHANCED_DISPLAY.md` - Display recommendations

#### **Data & Findings:**
- `BASELINE_DATA_DEC_2024.md` - Baseline official data
- `COLLECTED_BASELINE_DATA.md` - All baseline data collected
- `SUBSCRIPTION_OVERLOAD_DATA.md` - Subscription metric research
- `INTERESTING_FINDINGS.md` - 40+ shareable facts

#### **Setup Guides:**
- `REDDIT_API_SETUP.md` - Reddit API configuration
- `YOUTUBE_API_SETUP.md` - YouTube API configuration
- `TIKTOK_SAMPLING_GUIDE.md` - TikTok sampling methodology
- `FACEBOOK_SAMPLING_GUIDE.md` - Facebook sampling methodology

### **Root Files:**
- `README.md` - Project overview
- `ARTICLE_DRAFT.md` - Portfolio article draft
- `LICENSE` - MIT License
- `package.json` - Dependencies

---

## Merged from Original Project

This project consolidates two separate folders:
1. **Original research folder** - Data collection work, AI Psychosis focus
2. **Web deployment folder** - Live Next.js site

**What was merged:**
- 355 Reddit posts + 147 YouTube videos (AI Psychosis)
- Google Trends CSVs for all metrics
- AI Psychosis collection scripts (Reddit, YouTube, App Store)
- All research documentation and findings
- Architecture and methodology docs

---

## Data Status

### **Collected (Ready to Integrate):**
- AI Psychosis: 502 entries (355 Reddit + 147 YouTube)
- Google Trends: All 7 metrics baseline

### **In Progress:**
- What Healthcare?: 0/480 target
- Dating App Despair: 0/480 target
- Wage Stagnation: 0/400 target
- Housing Despair: 0/400 target
- Airline Chaos: 0/480 target
- Layoff Watch: 0/400 target

---

## Next Steps

1. Parse AI Psychosis CSVs and calculate real crisis ratio
2. Update dashboard with 502 real data points
3. Begin systematic collection for remaining metrics
4. Update `/status` page as data grows
