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
            and transparent methodology. All data sources, calculations, and sampling methods are documented below.
          </p>
        </div>

        {/* Core Principles */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Core Principles
          </h2>

          <div className="space-y-4">
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">Objectivity</h3>
              <p className="text-black font-bold">
                Data is collected from official sources (BLS, Census, BTS) and public platforms without cherry-picking.
                All sampling is systematic and documented.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">Transparency</h3>
              <p className="text-black font-bold">
                Every data source is cited. All formulas are public. Sample sizes and collection methods are disclosed.
                Limitations and data gaps are acknowledged.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">Reproducibility</h3>
              <p className="text-black font-bold">
                All data collection scripts are available. Anyone can verify the results by following the same methodology.
              </p>
            </div>

            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-2 uppercase">Statistical Rigor</h3>
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
                <p>YOUTUBE: 135 videos analyzed</p>
                <p>REDDIT: 289 posts from r/replika + r/CharacterAI</p>
                <p>TIKTOK: 88 videos via YouTube compilations</p>
                <p>GOOGLE TRENDS: Search volume for AI companion terms</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Crisis), Level 2 (Dependent), Level 1 (Casual)
                </p>
              </div>
            </div>

            {/* Subscription Overload */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">Subscription Overload</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>YOUTUBE: 160 videos analyzed</p>
                <p>REDDIT: 12 posts from subscription-related subreddits</p>
                <p>TIKTOK: 58 videos via YouTube compilations</p>
                <p>CONSUMER REPORTS: Average 12 subscriptions per household</p>
                <p>INDUSTRY REPORTS: 73% raised prices in 2025</p>
              </div>
            </div>

            {/* Dating App Despair */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">Dating App Despair</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>YOUTUBE: 131 videos analyzed</p>
                <p>REDDIT: 139 posts from r/dating, r/Tinder, r/Bumble, r/HingeApp</p>
                <p>TIKTOK: 83 videos via YouTube compilations</p>
                <p>GOOGLE TRENDS: Baseline sentiment tracking</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Quit/Crisis), Level 2 (Frustrated/Exhausted), Level 1 (Mild Complaints)
                </p>
              </div>
            </div>

            {/* What Healthcare? */}
            <div className="bg-red-600 border-4 border-black p-6">
              <h3 className="text-2xl font-black text-white mb-4 uppercase">What Healthcare?</h3>
              <div className="space-y-2 text-white font-bold mono text-sm">
                <p>YOUTUBE: 170 videos analyzed</p>
                <p>REDDIT: 134 posts from r/HealthInsurance, r/Insurance, r/povertyfinance</p>
                <p>TIKTOK: 88 videos via YouTube compilations</p>
                <p>KFF DATA: Premium increases, claim denial rates, coverage gaps</p>
                <p>CENSUS: Medical debt statistics, bankruptcy data</p>
                <p className="pt-2 border-t-2 border-white/30">
                  CATEGORIZATION: Level 3 (Medical debt/denied life-saving care), Level 2 (Can't afford treatment/high premiums), Level 1 (Billing confusion/delays)
                </p>
              </div>
            </div>

            {/* Other Metrics */}
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-2xl font-black text-black mb-4 uppercase">Other Metrics</h3>
              <div className="space-y-3 text-black font-bold text-sm">
                <p><strong className="mono">WAGE STAGNATION:</strong> YouTube (88), Reddit (78), TikTok (82) + BLS Employment Cost Index, AFL-CIO CEO Pay Database</p>
                <p><strong className="mono">HOUSING DESPAIR:</strong> YouTube (137), Reddit (185), TikTok (91) + Redfin, Zillow Rent Index, Census Bureau</p>
                <p><strong className="mono">AIRLINE CHAOS:</strong> YouTube (98), Reddit (132), TikTok (83) + Bureau of Transportation Statistics, ACSI scores</p>
                <p><strong className="mono">LAYOFF WATCH:</strong> YouTube (74), Reddit (282), TikTok (74) + Layoffs.fyi tracking</p>
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
            <table className="w-full mono font-bold text-sm text-black">
              <thead>
                <tr className="border-b-4 border-black">
                  <th className="text-left py-3 px-2 text-black">METRIC</th>
                  <th className="text-left py-3 px-2 text-black">YOUTUBE</th>
                  <th className="text-left py-3 px-2 text-black">REDDIT</th>
                  <th className="text-left py-3 px-2 text-black">TIKTOK</th>
                  <th className="text-left py-3 px-2 text-black">TOTAL</th>
                </tr>
              </thead>
              <tbody className="text-black">
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">AI PSYCHOSIS</td>
                  <td className="py-3 px-2">135</td>
                  <td className="py-3 px-2">289</td>
                  <td className="py-3 px-2">88</td>
                  <td className="py-3 px-2 text-green-700 font-black">512</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">LAYOFF WATCH</td>
                  <td className="py-3 px-2">74</td>
                  <td className="py-3 px-2">282</td>
                  <td className="py-3 px-2">74</td>
                  <td className="py-3 px-2 text-green-700 font-black">430</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">HOUSING DESPAIR</td>
                  <td className="py-3 px-2">137</td>
                  <td className="py-3 px-2">185</td>
                  <td className="py-3 px-2">91</td>
                  <td className="py-3 px-2 text-green-700 font-black">413</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">HEALTHCARE</td>
                  <td className="py-3 px-2">170</td>
                  <td className="py-3 px-2">134</td>
                  <td className="py-3 px-2">88</td>
                  <td className="py-3 px-2 text-green-700 font-black">392</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">DATING APP DESPAIR</td>
                  <td className="py-3 px-2">131</td>
                  <td className="py-3 px-2">139</td>
                  <td className="py-3 px-2">83</td>
                  <td className="py-3 px-2 text-green-700 font-black">353</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">AIRLINE CHAOS</td>
                  <td className="py-3 px-2">98</td>
                  <td className="py-3 px-2">132</td>
                  <td className="py-3 px-2">83</td>
                  <td className="py-3 px-2 text-green-700 font-black">313</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">WAGE STAGNATION</td>
                  <td className="py-3 px-2">88</td>
                  <td className="py-3 px-2">78</td>
                  <td className="py-3 px-2">82</td>
                  <td className="py-3 px-2 text-green-700 font-black">248</td>
                </tr>
                <tr className="border-b-2 border-black/20">
                  <td className="py-3 px-2 font-black">SUBSCRIPTION OVERLOAD</td>
                  <td className="py-3 px-2">160</td>
                  <td className="py-3 px-2">12</td>
                  <td className="py-3 px-2">58</td>
                  <td className="py-3 px-2 text-green-700 font-black">230</td>
                </tr>
                <tr className="border-t-4 border-black">
                  <td className="py-3 px-2 font-black">TOTAL</td>
                  <td className="py-3 px-2 font-black">993</td>
                  <td className="py-3 px-2 font-black">1,251</td>
                  <td className="py-3 px-2 font-black">647</td>
                  <td className="py-3 px-2 text-green-700 font-black">2,891</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* Bias Mitigation */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Bias Mitigation
          </h2>

          <div className="bg-white border-4 border-black p-6">
            <p className="text-black font-bold mb-4">
              Data is collected from multiple platforms to avoid platform-specific bias. Top and hot posts are sampled systematically (not cherry-picked). Keyword-based categorization reduces subjective judgment.
            </p>
            <p className="text-black font-bold">
              Government and industry data provides the foundation. Incomplete metrics are clearly labeled with completion percentages.
            </p>
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
            CURRENT BASELINE: JANUARY 2026 | AUTOMATED WEEKLY UPDATES ENABLED
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
            <p className="text-black font-bold text-sm mono mb-3">
              Platform demographics skew young and online. Reddit and TikTok users don't represent the general population. People experiencing crisis are more likely to post about it, creating self-selection bias.
            </p>
            <p className="text-black font-bold text-sm mono">
              Some metrics are preliminary and require more research. Scores are relative indicators, not absolute measures. All data is collected from public sources only.
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="border-t-4 border-white pt-8">
          <p className="text-white font-black text-sm mono mb-4">
            LAST UPDATED: JANUARY 10, 2026 | VERSION 1.2
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
