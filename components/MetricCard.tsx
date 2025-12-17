'use client';

interface MetricCardProps {
  title: string;
  score: number;
  label: string;
  trend: 'improving' | 'worsening' | 'neutral';
  data: Record<string, string>;
  onClick?: () => void;
  lastUpdated?: string;
  entryCount?: number;
}

export default function MetricCard({ title, score, label, trend, data, onClick, lastUpdated, entryCount }: MetricCardProps) {
  const trendIcons = {
    improving: '↓',
    worsening: '↑',
    neutral: '→'
  };

  const bgColor = score < 20 ? 'bg-white' : score < 40 ? 'bg-white' : score < 60 ? 'bg-red-600' : 'bg-red-600';
  const textColor = score < 60 ? 'text-black' : 'text-white';
  const barColor = score < 20 ? 'bg-black' : score < 60 ? 'bg-red-600' : 'bg-white';

  return (
    <div
      className={`${bgColor} border-4 border-black p-6 hover:border-red-600 transition-all ${onClick ? 'cursor-pointer hover:scale-105 active:scale-95' : ''}`}
      onClick={onClick}
      role={onClick ? 'button' : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={onClick ? (e) => e.key === 'Enter' && onClick() : undefined}
    >
      <div className="flex justify-between items-start mb-4">
        <h3 className={`text-xl font-black ${textColor} uppercase tracking-tight leading-tight`}>
          {title}
        </h3>
        <span className={`text-3xl font-black ${textColor}`}>
          {trendIcons[trend]}
        </span>
      </div>

      <div className={`text-6xl font-black ${textColor} mb-3 mono`}>
        {score.toFixed(2)}
      </div>

      <div className={`text-xs ${textColor} font-bold mb-4 uppercase leading-tight h-10 flex items-center`}>
        "{label}"
      </div>

      <div className={`w-full ${textColor === 'text-black' ? 'bg-black' : 'bg-white'} h-6 border-2 border-black mb-4`}>
        <div
          className={`h-full ${barColor} transition-all duration-1000`}
          style={{ width: `${Math.min(score, 100)}%` }}
        />
      </div>

      <div className="space-y-1">
        {Object.entries(data).map(([key, value]) => (
          <div key={key} className={`text-xs ${textColor} font-bold mono`}>
            {value}
          </div>
        ))}
      </div>

      {/* Data collection status */}
      {(lastUpdated || entryCount !== undefined) && (
        <div className={`mt-4 pt-3 border-t-2 ${textColor === 'text-black' ? 'border-gray-300' : 'border-gray-600'}`}>
          {entryCount !== undefined && (
            <div className={`text-xs ${entryCount === 0 ? 'text-gray-500' : textColor} font-bold uppercase tracking-wide`}>
              {entryCount === 0 ? (
                <span className="text-yellow-600">⚠️ No data collected</span>
              ) : entryCount < 100 ? (
                <span>📊 {entryCount} entries (Preliminary)</span>
              ) : (
                <span>✓ {entryCount} entries collected</span>
              )}
            </div>
          )}
          {lastUpdated && (
            <div className={`text-xs ${textColor} opacity-70 font-bold mono mt-1`}>
              Updated: {lastUpdated}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
