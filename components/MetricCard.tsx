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
      className={`${bgColor} border-4 border-black p-4 md:p-6 transition-all duration-300 ease-out ${
        onClick
          ? 'cursor-pointer hover:border-red-600 hover:shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:translate-x-[-2px] active:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:translate-y-0 active:translate-x-0'
          : ''
      }`}
      onClick={onClick}
      role={onClick ? 'button' : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={onClick ? (e) => e.key === 'Enter' && onClick() : undefined}
    >
      <div className="flex justify-between items-start mb-3 md:mb-4">
        <h3 className={`text-lg md:text-xl font-black ${textColor} uppercase tracking-tight leading-tight`}>
          {title}
        </h3>
        <span className={`text-2xl md:text-3xl font-black ${textColor}`}>
          {trendIcons[trend]}
        </span>
      </div>

      <div className={`text-5xl md:text-6xl font-black ${textColor} mb-2 md:mb-3 mono`}>
        {score.toFixed(2)}
      </div>

      <div className={`text-xs ${textColor} font-bold mb-3 md:mb-4 uppercase leading-tight min-h-[2.5rem] flex items-center`}>
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
          <div key={key} className={`text-xs ${textColor} font-bold mono break-words whitespace-normal`}>
            {value}
          </div>
        ))}
      </div>

      {/* Data collection status */}
      {(lastUpdated || entryCount !== undefined) && (
        <div className={`mt-4 pt-3 border-t-2 ${textColor === 'text-black' ? 'border-gray-300' : 'border-gray-600'}`}>
          {entryCount !== undefined && (
            <div className={`text-xs ${textColor} font-bold mono break-words whitespace-normal`}>
              {entryCount} entries
            </div>
          )}
          {lastUpdated && (
            <div className={`text-xs ${textColor} opacity-70 font-bold mono mt-1 break-words whitespace-normal`}>
              {lastUpdated}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
