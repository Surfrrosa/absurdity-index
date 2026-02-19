import Link from 'next/link';
import { metricDetails, getLatestUpdateDate } from '@/lib/metricDetailData';

function getDaysSince(dateStr: string): number {
  const date = new Date(dateStr);
  if (isNaN(date.getTime())) return -1;
  const now = new Date();
  return Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24));
}

function getFreshnessClass(days: number): string {
  if (days < 0) return 'text-white/40';
  if (days <= 7) return 'text-green-500';
  if (days <= 14) return 'text-yellow-500';
  return 'text-red-500';
}

function getFreshnessLabel(days: number): string {
  if (days < 0) return 'UNKNOWN';
  if (days === 0) return 'TODAY';
  if (days === 1) return '1 DAY AGO';
  if (days <= 7) return `${days} DAYS AGO`;
  if (days <= 14) return `${days} DAYS AGO (STALE)`;
  return `${days} DAYS AGO (OUTDATED)`;
}

export default function Status() {
  const updateDate = getLatestUpdateDate();
  const metrics = Object.entries(metricDetails);

  const totalEntries = metrics.reduce(
    (sum, [, m]) => sum + m.levelDistribution.total,
    0
  );

  // Calculate platform health across all metrics
  const platformStats: Record<string, { collected: number; target: number }> = {};
  for (const [, metric] of metrics) {
    for (const progress of metric.collectionProgress) {
      if (!platformStats[progress.platform]) {
        platformStats[progress.platform] = { collected: 0, target: 0 };
      }
      platformStats[progress.platform].collected += progress.current;
      platformStats[progress.platform].target += progress.target;
    }
  }

  return (
    <main className="min-h-screen bg-black">
      <header className="bg-black border-b-4 border-white">
        <div className="container mx-auto px-6 py-8">
          <div className="flex justify-between items-start">
            <div>
              <h1 className="text-5xl font-black text-white tracking-tight leading-none mb-3">
                PIPELINE STATUS
              </h1>
              <p className="text-white text-lg font-bold mono">
                DATA COLLECTION HEALTH
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
      </header>

      <div className="container mx-auto px-6 py-12 max-w-5xl">

        {/* Overall Health */}
        <div className="bg-white border-4 border-black p-8 mb-8">
          <h2 className="text-3xl font-black text-black mb-6 uppercase">Overview</h2>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">TOTAL DATA POINTS</div>
              <div className="text-4xl font-black text-white mono">{totalEntries.toLocaleString()}</div>
            </div>
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">METRICS TRACKED</div>
              <div className="text-4xl font-black text-white mono">{metrics.length}</div>
            </div>
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">LAST UPDATE</div>
              <div className="text-2xl font-black text-white mono">{updateDate}</div>
            </div>
          </div>
        </div>

        {/* Platform Health */}
        <div className="bg-white border-4 border-black p-8 mb-8">
          <h2 className="text-3xl font-black text-black mb-6 uppercase">Platform Health</h2>
          <div className="space-y-4">
            {Object.entries(platformStats)
              .sort((a, b) => b[1].collected - a[1].collected)
              .map(([platform, stats]) => {
                const pct = stats.target > 0 ? Math.min(100, Math.round(stats.collected / stats.target * 100)) : 0;
                return (
                  <div key={platform}>
                    <div className="flex justify-between mb-2">
                      <span className="font-black text-black mono">{platform.toUpperCase()}</span>
                      <span className="font-black text-black mono">
                        {stats.collected.toLocaleString()} / {stats.target.toLocaleString()} ({pct}%)
                      </span>
                    </div>
                    <div className="w-full bg-black/10 h-6 border-4 border-black">
                      <div
                        className={`h-full ${pct >= 80 ? 'bg-green-600' : pct >= 40 ? 'bg-yellow-500' : 'bg-red-600'}`}
                        style={{ width: `${pct}%` }}
                      />
                    </div>
                  </div>
                );
              })}
          </div>
        </div>

        {/* Per-Metric Status */}
        <div className="mb-8">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-2">
            Metric Status
          </h2>
          <div className="space-y-4">
            {metrics.map(([name, metric]) => {
              const days = getDaysSince(metric.lastUpdated);
              const freshnessClass = getFreshnessClass(days);
              const freshnessLabel = getFreshnessLabel(days);
              const l3Pct = metric.levelDistribution.total > 0
                ? ((metric.levelDistribution.level3 / metric.levelDistribution.total) * 100).toFixed(1)
                : '0';

              return (
                <div key={name} className="bg-white border-4 border-black p-6">
                  <div className="flex flex-col md:flex-row md:justify-between md:items-start gap-4">
                    <div>
                      <h3 className="text-xl font-black text-black uppercase">{name}</h3>
                      <div className="text-sm font-bold mono text-black mt-2">
                        SCORE: {metric.score.toFixed(2)} | ENTRIES: {metric.levelDistribution.total} | L3: {l3Pct}%
                      </div>
                    </div>
                    <div className="text-right">
                      <div className={`font-black mono text-sm ${freshnessClass}`}>
                        {freshnessLabel}
                      </div>
                      <div className="text-xs font-bold mono text-black/60 mt-1">
                        {metric.lastUpdated}
                      </div>
                    </div>
                  </div>
                  <div className="mt-4 flex flex-wrap gap-3">
                    {metric.collectionProgress.map((p, i) => {
                      const color = p.percentage >= 80 ? 'border-green-600 text-green-700'
                        : p.percentage >= 40 ? 'border-yellow-500 text-yellow-600'
                        : 'border-red-600 text-red-700';
                      return (
                        <span key={i} className={`border-2 ${color} px-3 py-1 font-black mono text-xs`}>
                          {p.platform}: {p.current}/{p.target} ({p.percentage}%)
                        </span>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Footer */}
        <div className="border-t-4 border-white pt-8">
          <p className="text-white font-black text-sm mono mb-4">
            PIPELINE RUNS WEEKLY (MONDAYS 9AM UTC) | {updateDate}
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
