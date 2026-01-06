# The Absurdity Index

**A data-driven dashboard quantifying the absurdity of modern existence.**

Live at: [absurdity-index.vercel.app](https://absurdity-index.vercel.app) *(coming soon)*

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

- **Next.js 15** with App Router
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
    ├── COLLECTION_QUICKSTART.md        # Data collection guide
    ├── healthcare-collector.py         # What Healthcare? data script
    ├── dating-app-despair-collector.py # Dating App Despair script
    ├── airline-chaos-collector.py      # Airline Chaos script
    ├── wage-stagnation-collector.py    # Wage Stagnation script
    ├── housing-despair-collector.py    # Housing Despair script
    └── layoff-watch-collector.py       # Layoff Watch script
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

Each metric has a dedicated Python collection script in `/data-collection/`.

### Quick Start

1. Install Python 3
2. Navigate to data collection directory:
   ```bash
   cd "absurdity-index/data-collection"
   ```
3. Run a collector script:
   ```bash
   python3 healthcare-collector.py
   ```
4. Add entries following the documented format
5. Export to JSON
6. Update `/lib/metricDetailData.ts` with collected data

See `/data-collection/COLLECTION_QUICKSTART.md` for detailed instructions.

---

## Deployment

This project is optimized for deployment on Vercel:

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

## Policy Change Monitoring

The Absurdity Index tracks major policy changes affecting metrics. When policy changes occur, baselines are recalculated and documented with effective dates.

Healthcare (ACA modifications, Medicare/Medicaid changes, prior authorization rules), Wage & Labor (minimum wage legislation, NLRB rulings, tax policy), Housing (interest rates, zoning reform, rent control, tenant protections), Airlines (DOT passenger rights, FAA safety regulations, merger approvals), Tech & AI (AI safety regulations, antitrust enforcement, privacy laws), Labor Market (unemployment insurance, job training, WARN Act enforcement).

---

## Contributing

This is a personal research project by Shaina Pauley. Data collection contributions are welcome:

1. Follow the methodology in `/data-collection/METHODOLOGY_FORMULAS.md`
2. Use provided Python scripts for categorization
3. Include verifiable URLs for all data points
4. Submit pull requests with documented sources

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
