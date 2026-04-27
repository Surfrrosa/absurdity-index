# The Absurdity Index

**A data-driven dashboard quantifying the absurdity of modern existence.**

Live at: [absurdity-index.vercel.app](https://absurdity-index.vercel.app)

---

## What Is This?

The Absurdity Index tracks 8 metrics of modern life through a combination of official statistics and social sentiment analysis. Each metric combines objective data (40% weight) with lived experience captured from social media (60% weight) to produce a single absurdity score.

### The 8 Metrics

1. **What Healthcare?** (Insurance denials, medical debt, prior authorization purgatory)
2. **Wage Stagnation** (Real wage growth vs. CEO pay ratios)
3. **Housing Despair** (Price-to-income ratios, rent burden, homeownership dreams)
4. **Subscription Overload** (Average subscriptions, monthly spending, price increases)
5. **Dating App Despair** (App burnout, mental health impact, quit rates)
6. **Airline Chaos** (Delays, cancellations, safety incidents, service quality)
7. **Layoff Watch** (Tech layoffs, job search despair, unemployment anxiety)
8. **AI Psychosis** (AI companion dependency, emotional reliance, digital relationships)

---

## Methodology

### Core Formula

```
Final Score = (Official Data × 0.4) + (Social Sentiment × 0.6)
```

**Why 40/60 weighting?**
- Official data (40%) provides objective grounding but often lags reality
- Social sentiment (60%) captures lived experience and emotional toll that stats alone miss

### Social Sentiment Collection

Each metric collects 380-480 data points from YouTube (80-160 videos), Reddit (200 posts), and TikTok (100-120 videos).

### Crisis Categorization

Content is categorized using keyword-based analysis into three levels:

**Level 1 (Mild)**: Awareness, minor frustrations
**Level 2 (Struggling)**: Significant impact, frequent challenges
**Level 3 (Crisis)**: Financial ruin, mental health crisis, life disruption

The crisis ratio is calculated as (Level 3 count / Total count) × 100.

### Data Transparency

- All data points include verifiable URLs
- Collection scripts are open-source
- Methodology fully documented in `/data-collection/METHODOLOGY_FORMULAS.md`
- No hallucinated or fabricated stories

---

## Tech Stack

- **Next.js 16** with App Router
- **React 19** with TypeScript
- **Tailwind CSS 4** for styling
- **Python 3** for data collection scripts

---

## Project Structure

```
absurdity-index/
├── app/
│   ├── page.tsx              # Main dashboard
│   ├── methodology/          # Methodology documentation page
│   └── layout.tsx            # Root layout
├── components/
│   ├── Header.tsx            # Site header
│   ├── MetricCard.tsx        # Individual metric cards
│   ├── MetricDetail.tsx      # Expandable metric details modal
│   └── AbsurdityScore.tsx    # Overall score component
├── lib/
│   └── metricDetailData.ts   # Detailed metric data and types
└── data-collection/
    ├── METHODOLOGY_FORMULAS.md         # Full methodology documentation
    ├── config.json                     # Centralized weights, severity, metric defs
    ├── run_weekly_update.py            # Master script: runs all collectors
    ├── *-youtube-collector.py          # 8 per-metric YouTube collectors
    ├── *-reddit-collector.py           # 8 per-metric Reddit collectors (local only)
    ├── reddit_collector_base.py        # Shared base class for Reddit collectors
    ├── bluesky-collector.py            # Bluesky (all metrics, AT Protocol)
    ├── cfpb-collector.py               # CFPB complaints (3 metrics)
    ├── fred-collector.py               # FRED official economic data
    ├── hackernews-collector.py         # Hacker News (Algolia API)
    ├── calculate_all_social_scores.py  # Score calculator
    └── update_metric_data.py           # Updates metricDetailData.ts
```

---

## Local Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view the dashboard.

---

## Data Collection

Per-source collectors run weekly via GitHub Actions and write CSVs to `data-collection/collected-data/`. Scoring runs after collection and updates `lib/metricDetailData.ts` automatically.

### Local Run

```bash
cd data-collection
pip install -r requirements.txt

# Set API keys in .env (see .env.example)
# YOUTUBE_API_KEY required for YouTube collectors
# FRED_API_KEY optional for FRED collector

# Run all collectors + scoring + TS update
python3 run_weekly_update.py

# Or run a single source
python3 hackernews-collector.py
python3 bluesky-collector.py
```

Reddit collectors only work locally (Reddit blocks datacenter IPs). All other sources work in CI. See `CLAUDE.md` for the full pipeline.

---

## Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/shainarazavi/absurdity-index)

### Manual Deployment

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts to deploy

---

## Design Philosophy

**Brutalist Aesthetic**
- Heavy black borders
- Bold typography
- Red/black/white color scheme
- Inspired by Hieronymus Bosch's "The Garden of Earthly Delights"

**Data-First Approach**
- No embellishment
- Direct confrontation with reality
- Transparency over polish
- Verifiable sources only

---

---

## Limitations

Platform demographics skew young and online. Reddit and TikTok users don't represent everyone. People in crisis are more likely to post about it. Viral events can spike sentiment temporarily. Data collection focuses on the US. Automated keyword categorization sometimes misses context or sarcasm.

We account for these through multi-source sampling and anchoring to official data.

---

## License

MIT License - See LICENSE file for details

---

## Contact

Created by **Shaina Pauley**

For questions about methodology or data collection, open an issue on GitHub.

---

**"One must imagine Sisyphus checking his email"** — Albert Camus-ish
