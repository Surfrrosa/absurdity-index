import Link from 'next/link';

export default function DataCollectionStatus() {
  const metrics = [
    {
      name: "What Healthcare?",
      target: 480,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "Dating App Despair",
      target: 480,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "AI Psychosis",
      target: 400,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "App Store, TikTok"
    },
    {
      name: "Wage Stagnation",
      target: 400,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "Housing Despair",
      target: 400,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "Airline Chaos",
      target: 480,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "Layoff Watch",
      target: 400,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    },
    {
      name: "Subscription Overload",
      target: 400,
      collected: 0,
      lastUpdated: "Dec 17, 2024",
      platforms: "Reddit, YouTube, TikTok"
    }
  ];

  const totalTarget = metrics.reduce((sum, m) => sum + m.target, 0);
  const totalCollected = metrics.reduce((sum, m) => sum + m.collected, 0);
  const overallProgress = (totalCollected / totalTarget) * 100;

  const getStatusColor = (collected: number, target: number) => {
    const percentage = (collected / target) * 100;
    if (percentage === 0) return "bg-gray-700";
    if (percentage < 25) return "bg-red-600";
    if (percentage < 70) return "bg-yellow-500";
    return "bg-green-500";
  };

  const getStatusLabel = (collected: number, target: number) => {
    const percentage = (collected / target) * 100;
    if (percentage === 0) return "Not Started";
    if (percentage < 25) return "Just Started";
    if (percentage < 70) return "In Progress";
    return "Near Complete";
  };

  return (
    <main className="min-h-screen bg-black">
      {/* Header */}
      <header className="bg-black border-b-4 border-white">
        <div className="container mx-auto px-6 py-8">
          <div className="flex justify-between items-start">
            <div>
              <h1 className="text-5xl font-black text-white tracking-tight leading-none mb-3">
                DATA COLLECTION<br/>STATUS
              </h1>
              <p className="text-white text-lg font-bold mono">
                TRACKING PROGRESS ACROSS 8 METRICS
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

      <div className="container mx-auto px-6 py-12 max-w-6xl">
        {/* Overall Progress */}
        <div className="bg-white border-8 border-black p-8 mb-12">
          <div className="text-center border-4 border-black p-8 bg-black">
            <h2 className="text-2xl font-black text-white mb-4 uppercase tracking-tight">
              Overall Collection Progress
            </h2>
            <div className="text-6xl font-black text-red-600 my-6 mono">
              {totalCollected} / {totalTarget}
            </div>
            <div className="text-lg text-white font-bold mb-6">
              {overallProgress.toFixed(1)}% COMPLETE
            </div>
            <div className="w-full bg-white h-8 border-4 border-white">
              <div
                className="h-full bg-red-600 transition-all duration-1000"
                style={{ width: `${overallProgress}%` }}
              />
            </div>
            <p className="text-gray-400 mt-4 text-sm font-bold uppercase">
              Target: 3,440 total entries across all metrics
            </p>
          </div>
        </div>

        {/* Individual Metric Progress */}
        <div className="space-y-6">
          <h2 className="text-3xl font-black text-white mb-6 uppercase border-b-4 border-white pb-3">
            Metric-by-Metric Breakdown
          </h2>

          {metrics.map((metric) => {
            const percentage = (metric.collected / metric.target) * 100;
            const statusColor = getStatusColor(metric.collected, metric.target);
            const statusLabel = getStatusLabel(metric.collected, metric.target);

            return (
              <div
                key={metric.name}
                className="bg-white border-4 border-black p-6"
              >
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="text-2xl font-black text-black uppercase">
                      {metric.name}
                    </h3>
                    <p className="text-sm font-bold text-gray-600 mt-1 uppercase">
                      {metric.platforms}
                    </p>
                  </div>
                  <div className="text-right">
                    <div className={`inline-block px-3 py-1 ${statusColor} text-white font-black text-xs uppercase`}>
                      {statusLabel}
                    </div>
                    <p className="text-xs font-bold text-gray-600 mt-2 mono">
                      Updated: {metric.lastUpdated}
                    </p>
                  </div>
                </div>

                <div className="mb-3">
                  <div className="flex justify-between text-sm font-black text-black mb-2">
                    <span>{metric.collected} collected</span>
                    <span>{metric.target} target</span>
                  </div>
                  <div className="w-full bg-gray-200 h-6 border-2 border-black">
                    <div
                      className={`h-full ${statusColor} transition-all duration-1000`}
                      style={{ width: `${Math.min(percentage, 100)}%` }}
                    />
                  </div>
                </div>

                <div className="text-xl font-black text-black mono">
                  {percentage.toFixed(1)}% complete
                </div>
              </div>
            );
          })}
        </div>

        {/* Footer Info */}
        <div className="mt-12 bg-red-600 border-4 border-white p-8 text-white">
          <h3 className="text-2xl font-black uppercase mb-4">About This Data</h3>
          <div className="space-y-3 font-bold">
            <p>
              ✓ All entries include <strong>verifiable URLs</strong> to original sources
            </p>
            <p>
              ✓ Content categorized using <strong>keyword-based analysis</strong> (Level 1-3)
            </p>
            <p>
              ✓ Collection methodology documented in{' '}
              <Link href="/methodology" className="underline hover:text-black">
                /methodology
              </Link>
            </p>
            <p>
              ✓ Updated <strong>weekly</strong> as new data is collected
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}
