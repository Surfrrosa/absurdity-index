import Link from 'next/link';

export default function Methodology() {
  return (
    <main className="min-h-screen bg-black">
      {/* Header */}
      <header className="bg-black border-b-4 border-white">
        <div className="container mx-auto px-6 py-8">
          <div className="flex justify-between items-start">
            <div>
              <h1 className="text-5xl font-black text-white tracking-tight leading-none mb-3">
                METHODOLOGY &<br/>DATA TRANSPARENCY
              </h1>
              <p className="text-white text-lg font-bold mono">
                HOW WE QUANTIFY THE ABSURD
              </p>
            </div>
            <Link
              href="/"
              className="px-6 py-3 bg-white text-black font-black hover:bg-red-600 hover:text-white transition-colors border-4 border-black hover:border-white text-sm uppercase tracking-wide"
            >
              BACK
            </Link>
          </div>
        </div>
        <div className="h-3 bg-red-600"></div>
      </header>

      <div className="container mx-auto px-6 py-12 max-w-5xl">

        {/* Intro */}
        <div className="bg-white border-4 border-black p-8 mb-8">
          <p className="text-black text-lg font-bold leading-relaxed">
            The Absurdity Index quantifies the absurdity of modern existence through rigorous data collection
            and research-grade methodology. All data sources, calculations, and sampling methods are documented below.
          </p>
        </div>

        {/* Core Principles */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Core Principles
          </h2>

          <div className="space-y-4">
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">1. Objectivity</h3>
              <p className="text-black font-bold">
                Data is collected from official sources (BLS, Census, BTS) and public platforms without cherry-picking.
                All sampling is systematic and documented.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">2. Transparency</h3>
              <p className="text-black font-bold">
                Every data source is cited. All formulas are public. Sample sizes and collection methods are disclosed.
                Limitations and data gaps are acknowledged.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">3. Reproducibility</h3>
              <p className="text-black font-bold">
                All data collection scripts are available. Anyone can verify the results by following the same methodology.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">4. Statistical Rigor</h3>
              <p className="text-black font-bold">
                Sample sizes meet research standards (minimum 100-200 per category). Multiple platforms are sampled
                to avoid single-source bias.
              </p>
            </div>
          </div>
        </div>

        {/* Data Sources */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Data Sources by Metric
          </h2>

          <div className="space-y-6">
            {/* AI Psychosis */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">AI Psychosis</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>YOUTUBE: 146 videos analyzed (54.8% crisis ratio)</p>
                <p>REDDIT: 200 posts from r/replika + r/CharacterAI (15.0% crisis ratio)</p>
                <p>GOOGLE TRENDS: Search volume for AI companion terms</p>
                <p>APP STORE: Manual sampling in progress</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Crisis), Level 2 (Dependent), Level 1 (Casual)
                </p>
              </div>
            </div>

            {/* Subscription Overload */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">Subscription Overload</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>CONSUMER REPORTS: Average 12 subscriptions per household</p>
                <p>STREAMING PRICING: All major platforms tracked</p>
                <p>GOOGLE TRENDS: "Cancel subscriptions", "subscription fatigue"</p>
                <p>INDUSTRY REPORTS: 73% raised prices in 2025</p>
              </div>
            </div>

            {/* Dating App Despair */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">Dating App Despair</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>YOUTUBE: 120-160 videos analyzing "quit dating apps" content</p>
                <p>REDDIT: 200 posts from r/dating, r/Tinder, r/Bumble, r/HingeApp</p>
                <p>TIKTOK: 120 videos with dating app complaint/burnout hashtags</p>
                <p>GOOGLE TRENDS: Baseline sentiment tracking</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Quit/Crisis), Level 2 (Frustrated/Exhausted), Level 1 (Mild Complaints)
                </p>
                <p>SEARCH TERMS: "quit dating apps", "dating app burnout", "dating app horror stories", "dating fatigue"</p>
              </div>
            </div>

            {/* What Healthcare? */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">What Healthcare?</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>KFF DATA: Premium increases, claim denial rates, coverage gaps</p>
                <p>CENSUS: Medical debt statistics, bankruptcy data</p>
                <p>YOUTUBE: 120-160 videos on denied claims, insurance nightmares</p>
                <p>REDDIT: 200 posts from r/HealthInsurance, r/Insurance, r/povertyfinance</p>
                <p>TIKTOK: 120 videos with healthcare crisis hashtags</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Medical debt/denied life-saving care), Level 2 (Can't afford treatment/high premiums), Level 1 (Billing confusion/delays)
                </p>
                <p>SEARCH TERMS: "insurance denied claim", "can't afford healthcare", "medical bankruptcy", "prior authorization nightmare"</p>
              </div>
            </div>

            {/* Other Metrics */}
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-2xl font-black text-black mb-4 uppercase">Other Metrics</h3>
              <div className="space-y-3 text-black font-bold text-sm">
                <p><strong className="mono">WAGE STAGNATION:</strong> BLS Employment Cost Index, AFL-CIO CEO Pay Database, social media financial stress analysis</p>
                <p><strong className="mono">HOUSING DESPAIR:</strong> Redfin, Zillow Rent Index, Census Bureau median income, social media housing crisis analysis</p>
                <p><strong className="mono">AIRLINE CHAOS:</strong> Bureau of Transportation Statistics, ACSI satisfaction scores, social media travel nightmare tracking</p>
                <p><strong className="mono">LAYOFF WATCH:</strong> Layoffs.fyi tracking (152,922 tech workers in 2025), social media job market despair analysis</p>
              </div>
            </div>
          </div>
        </div>

        {/* Sample Size Standards */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Sample Size Standards
          </h2>

          <div className="bg-white border-4 border-black p-6">
            <table className="w-full mono font-bold text-sm">
              <thead>
                <tr className="border-b-4 border-black">
                  <th className="text-left py-3 px-2">COMPONENT</th>
                  <th className="text-left py-3 px-2">TARGET</th>
                  <th className="text-left py-3 px-2">STATUS</th>
                </tr>
              </thead>
              <tbody>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-bold">AI PSYCHOSIS</td>
                  <td className="py-3 px-2"></td>
                  <td className="py-3 px-2"></td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">YouTube Videos</td>
                  <td className="py-3 px-2">120-160</td>
                  <td className="py-3 px-2 text-green-700">146 COMPLETE</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">Reddit Posts</td>
                  <td className="py-3 px-2">200</td>
                  <td className="py-3 px-2 text-green-700">200 COMPLETE</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">App Store Reviews</td>
                  <td className="py-3 px-2">200</td>
                  <td className="py-3 px-2 text-orange-700">20 (10%)</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">TikTok Videos</td>
                  <td className="py-3 px-2">120</td>
                  <td className="py-3 px-2 text-red-700">PENDING</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-bold">DATING APP DESPAIR</td>
                  <td className="py-3 px-2"></td>
                  <td className="py-3 px-2"></td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">YouTube Videos</td>
                  <td className="py-3 px-2">120-160</td>
                  <td className="py-3 px-2 text-red-700">PENDING</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 pl-6">Reddit Posts</td>
                  <td className="py-3 px-2">200</td>
                  <td className="py-3 px-2 text-red-700">PENDING</td>
                </tr>
                <tr>
                  <td className="py-3 px-2 pl-6">TikTok Videos</td>
                  <td className="py-3 px-2">120</td>
                  <td className="py-3 px-2 text-red-700">PENDING</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* Bias Mitigation */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Bias Mitigation Strategies
          </h2>

          <div className="bg-white border-4 border-black p-6">
            <ul className="space-y-3 text-black font-bold">
              <li className="flex items-start">
                <span className="text-red-600 mr-3 text-xl">▸</span>
                <span>MULTI-PLATFORM SAMPLING: Data from multiple sources to avoid platform-specific bias</span>
              </li>
              <li className="flex items-start">
                <span className="text-red-600 mr-3 text-xl">▸</span>
                <span>SYSTEMATIC SAMPLING: Top/hot posts sampled systematically, not cherry-picked</span>
              </li>
              <li className="flex items-start">
                <span className="text-red-600 mr-3 text-xl">▸</span>
                <span>AUTOMATED CATEGORIZATION: Keyword-based categorization reduces subjective judgment</span>
              </li>
              <li className="flex items-start">
                <span className="text-red-600 mr-3 text-xl">▸</span>
                <span>OFFICIAL SOURCES PRIORITIZED: Government and industry data as foundation</span>
              </li>
              <li className="flex items-start">
                <span className="text-red-600 mr-3 text-xl">▸</span>
                <span>DATA GAPS ACKNOWLEDGED: Incomplete metrics clearly labeled with completion percentages</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Update Schedule */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Update Schedule
          </h2>

          <div className="grid md:grid-cols-3 gap-4">
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-3 uppercase">Weekly</h3>
              <p className="text-black font-bold text-sm mono">
                Google Trends, social media sentiment, layoff tracking
              </p>
            </div>
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-3 uppercase">Monthly</h3>
              <p className="text-black font-bold text-sm mono">
                Housing prices, airline stats, subscription trends
              </p>
            </div>
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-3 uppercase">Quarterly</h3>
              <p className="text-black font-bold text-sm mono">
                Wage data, CEO pay ratios, ACSI scores
              </p>
            </div>
          </div>
          <p className="text-white font-bold text-sm mono mt-4">
            CURRENT BASELINE: DECEMBER 2025 | FULL AUTOMATION: Q1 2026
          </p>
        </div>

        {/* Limitations */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Limitations & Ethics
          </h2>

          <div className="bg-white border-4 border-black p-6">
            <p className="text-black font-bold mb-4">
              This dashboard quantifies cultural sentiment and economic trends, not clinical diagnoses or policy recommendations.
            </p>
            <ul className="space-y-2 text-black font-bold text-sm mono">
              <li>▸ Platform demographics may not represent general population</li>
              <li>▸ Self-reported sentiment may differ from actual behavior</li>
              <li>▸ Some metrics are preliminary and require more research</li>
              <li>▸ Scores are relative indicators, not absolute measures</li>
              <li>▸ Data collected from public sources only - no private information</li>
            </ul>
          </div>
        </div>

        {/* Footer */}
        <div className="border-t-4 border-white pt-8">
          <p className="text-white font-black text-sm mono mb-4">
            LAST UPDATED: DECEMBER 16, 2025 | VERSION 1.0
          </p>
          <Link
            href="/"
            className="inline-block px-8 py-4 bg-red-600 text-white font-black hover:bg-white hover:text-black transition-colors border-4 border-white text-lg uppercase tracking-wide"
          >
            BACK TO DASHBOARD
          </Link>
        </div>

      </div>
    </main>
  );
}
