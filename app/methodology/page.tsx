import Link from 'next/link';
import { metricDetails, getLatestUpdateDate } from '@/lib/metricDetailData';

// Order metrics by total entries (descending) for the table
function getSortedMetrics() {
  return Object.entries(metricDetails)
    .map(([name, data]) => {
      const youtube = data.collectionProgress.find(p => p.platform === 'YouTube');
      const reddit = data.collectionProgress.find(p => p.platform === 'Reddit');
      // Sum all non-YouTube/Reddit platforms (TikTok, Hacker News, CFPB, Bluesky, etc.)
      const other = data.collectionProgress
        .filter(p => p.platform !== 'YouTube' && p.platform !== 'Reddit')
        .reduce((sum, p) => sum + p.current, 0);
      const platforms = data.collectionProgress.length;
      return {
        name,
        youtube: youtube?.current ?? 0,
        reddit: reddit?.current ?? 0,
        other,
        platforms,
        total: data.levelDistribution.total,
        dataSources: data.dataSources,
        methodology: data.methodology,
      };
    })
    .sort((a, b) => b.total - a.total);
}

export default function Methodology() {
  const metrics = getSortedMetrics();
  const updateDate = getLatestUpdateDate();

  const totals = metrics.reduce(
    (acc, m) => ({
      youtube: acc.youtube + m.youtube,
      reddit: acc.reddit + m.reddit,
      other: acc.other + m.other,
      total: acc.total + m.total,
    }),
    { youtube: 0, reddit: 0, other: 0, total: 0 }
  );

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
                Data is collected from official sources (BLS, Census, BTS, FRED, CFPB) and public platforms without cherry-picking.
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

        {/* Data Sources - dynamically generated */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Data Sources by Metric
          </h2>

          <div className="space-y-6">
            {metrics.map((metric) => (
              <div key={metric.name} className="bg-red-700 border-4 border-black p-6">
                <h3 className="text-2xl font-black text-white mb-4 uppercase">{metric.name}</h3>
                <div className="space-y-2 text-white font-bold mono text-sm">
                  {metric.dataSources.map((source, i) => (
                    <p key={i}>{source}</p>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Sample Size Standards - dynamically generated */}
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
                  <th className="text-left py-3 px-2 text-black">OTHER</th>
                  <th className="text-left py-3 px-2 text-black">TOTAL</th>
                </tr>
              </thead>
              <tbody className="text-black">
                {metrics.map((metric) => (
                  <tr key={metric.name} className="border-b-2 border-black/20">
                    <td className="py-3 px-2 font-black">{metric.name.toUpperCase()}</td>
                    <td className="py-3 px-2">{metric.youtube}</td>
                    <td className="py-3 px-2">{metric.reddit}</td>
                    <td className="py-3 px-2">{metric.other}</td>
                    <td className="py-3 px-2 text-green-700 font-black">{metric.total.toLocaleString()}</td>
                  </tr>
                ))}
                <tr className="border-t-4 border-black">
                  <td className="py-3 px-2 font-black">TOTAL</td>
                  <td className="py-3 px-2 font-black">{totals.youtube.toLocaleString()}</td>
                  <td className="py-3 px-2 font-black">{totals.reddit.toLocaleString()}</td>
                  <td className="py-3 px-2 font-black">{totals.other.toLocaleString()}</td>
                  <td className="py-3 px-2 text-green-700 font-black">{totals.total.toLocaleString()}</td>
                </tr>
              </tbody>
            </table>
            <p className="text-black/60 font-bold text-xs mono mt-3">
              OTHER includes TikTok, Hacker News, CFPB complaints, and Bluesky where available per metric.
            </p>
          </div>
        </div>

        {/* Bias Mitigation */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Bias Mitigation
          </h2>

          <div className="bg-white border-4 border-black p-6">
            <p className="text-black font-bold mb-4">
              Data is collected from up to 7 platforms (YouTube, Reddit, TikTok, Hacker News, CFPB, Bluesky, and FRED) to avoid single-source bias. Content is sampled systematically via keyword search, not cherry-picked. Keyword-based severity categorization reduces subjective judgment.
            </p>
            <p className="text-black font-bold">
              Government and industry data provides the foundation (40% weight). Social sentiment data spans multiple platform demographics. Incomplete metrics are clearly labeled with collection percentages.
            </p>
          </div>
        </div>

        {/* Update Schedule */}
        <div className="mb-12">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Update Schedule
          </h2>

          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-3 uppercase">Weekly (Automated)</h3>
              <p className="text-black font-bold text-sm mono">
                YouTube, TikTok, Hacker News, CFPB complaints, Bluesky. Scores recalculated and dashboard updated automatically every Monday.
              </p>
            </div>
            <div className="bg-white border-4 border-black p-6">
              <h3 className="text-xl font-black text-black mb-3 uppercase">Periodic (Manual)</h3>
              <p className="text-black font-bold text-sm mono">
                Reddit collection (blocked from CI, run locally). FRED economic data (wage growth, housing prices, unemployment claims). Official score baselines.
              </p>
            </div>
          </div>
          <p className="text-white font-bold text-sm mono mt-4">
            LAST DATA: {updateDate} | AUTOMATED WEEKLY PIPELINE VIA GITHUB ACTIONS
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
              Platform demographics skew young and online. Social media users don't represent the general population. People experiencing crisis are more likely to post about it, creating self-selection bias. Hacker News skews toward tech workers. CFPB complaints skew toward motivated filers.
            </p>
            <p className="text-black font-bold text-sm mono">
              Some metrics are preliminary and require more research. Scores are relative indicators, not absolute measures. All data is collected from public sources only.
            </p>
          </div>
        </div>

        {/* Footer */}
        <div className="border-t-4 border-white pt-8">
          <p className="text-white font-black text-sm mono mb-4">
            LAST UPDATED: {updateDate} | {totals.total.toLocaleString()} TOTAL DATA POINTS
          </p>
          <Link
            href="/"
            className="inline-block px-8 py-4 bg-red-700 text-white font-black hover:bg-white hover:text-black transition-colors border-4 border-white text-lg uppercase tracking-wide"
          >
            BACK TO DASHBOARD
          </Link>
        </div>

      </div>
    </main>
  );
}
