'use client';

import { useEffect, useRef, useCallback } from 'react';

interface DataPoint {
  content: string;
  platform: string;
  level: number;
  date: string;
  url?: string;
  viewCount?: number;
  videoId?: string;
  commentCount?: number;
}

interface CollectionProgress {
  platform: string;
  current: number;
  target: number;
  percentage: number;
}

interface MetricDetailData {
  title: string;
  score: number;
  label: string;
  trend: 'improving' | 'neutral' | 'worsening';
  officialScore: number;
  crisisRatio: number;
  levelDistribution: {
    level1: number;
    level2: number;
    level3: number;
    total: number;
  };
  sampleData: DataPoint[];
  collectionProgress: CollectionProgress[];
  dataSources: string[];
  methodology: string;
  lastUpdated: string;
}

interface MetricDetailProps {
  data: MetricDetailData;
  onClose: () => void;
}

export default function MetricDetail({ data, onClose }: MetricDetailProps) {
  const modalRef = useRef<HTMLDivElement>(null);
  const closeButtonRef = useRef<HTMLButtonElement>(null);

  // Focus trap: keep Tab cycling within the modal
  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      onClose();
      return;
    }

    if (e.key !== 'Tab') return;

    const modal = modalRef.current;
    if (!modal) return;

    const focusable = modal.querySelectorAll<HTMLElement>(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    if (focusable.length === 0) return;

    const first = focusable[0];
    const last = focusable[focusable.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }, [onClose]);

  // Set up keyboard handling and initial focus
  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown);
    closeButtonRef.current?.focus();
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  // Prevent body scroll when modal is open
  useEffect(() => {
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, []);

  const level1Percent = (data.levelDistribution.level1 / data.levelDistribution.total * 100).toFixed(1);
  const level2Percent = (data.levelDistribution.level2 / data.levelDistribution.total * 100).toFixed(1);
  const level3Percent = (data.levelDistribution.level3 / data.levelDistribution.total * 100).toFixed(1);

  return (
    <div
      className="fixed inset-0 bg-black/95 z-50 overflow-y-auto"
      role="dialog"
      aria-modal="true"
      aria-label={`${data.title} metric details`}
      onClick={onClose}
    >
      <div
        ref={modalRef}
        className="container mx-auto px-6 py-12 max-w-5xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close button */}
        <button
          ref={closeButtonRef}
          onClick={onClose}
          className="fixed top-8 right-8 text-white hover:text-red-600 transition-colors text-4xl font-black z-50"
          aria-label="Close metric details"
        >
          ×
        </button>

        {/* Header */}
        <div className="bg-white border-8 border-black p-10 mb-8">
          <h2 className="text-5xl font-black text-black uppercase tracking-tight mb-6">
            {data.title}
          </h2>

          <div className="grid md:grid-cols-3 gap-6 mb-6">
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">ABSURDITY SCORE</div>
              <div className="text-6xl font-black text-red-600 mono">{data.score.toFixed(2)}</div>
            </div>
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">STATUS</div>
              <div className="text-2xl font-black text-white uppercase leading-tight">{data.label}</div>
            </div>
            <div className="border-4 border-black p-6 bg-black">
              <div className="text-white text-sm font-bold mono mb-2">TREND</div>
              <div className={`text-2xl font-black uppercase ${
                data.trend === 'worsening' ? 'text-red-600' :
                data.trend === 'improving' ? 'text-green-600' :
                'text-white'
              }`}>
                {data.trend === 'worsening' ? '↑ WORSENING' :
                 data.trend === 'improving' ? '↓ IMPROVING' :
                 '→ NEUTRAL'}
              </div>
            </div>
          </div>

          <div className="text-black font-bold text-sm mono">
            LAST UPDATED: {data.lastUpdated}
          </div>
        </div>

        {/* Score Breakdown */}
        <div className="bg-red-700 border-8 border-black p-8 mb-8">
          <h3 className="text-3xl font-black text-white mb-6 uppercase">Score Breakdown</h3>
          <div className="grid md:grid-cols-2 gap-6">
            <div>
              <div className="text-white font-bold mono text-sm mb-2">OFFICIAL DATA (40% weight)</div>
              <div className="text-5xl font-black text-white mono">{data.officialScore.toFixed(2)}</div>
              <div className="text-white font-bold text-sm mt-2">Government stats, industry reports</div>
            </div>
            <div>
              <div className="text-white font-bold mono text-sm mb-2">CRISIS RATIO (60% weight)</div>
              <div className="text-5xl font-black text-white mono">{data.crisisRatio.toFixed(1)}%</div>
              <div className="text-white font-bold text-sm mt-2">Social media sentiment analysis</div>
            </div>
          </div>
          <div className="mt-6 pt-6 border-t-4 border-white/30">
            <div className="text-white font-bold mono text-sm">FORMULA:</div>
            <div className="text-white font-bold text-lg mt-2">
              ({data.officialScore.toFixed(2)} × 0.4) + ({data.crisisRatio.toFixed(1)}% × 0.6) = {data.score.toFixed(2)}
            </div>
          </div>
        </div>

        {/* Level Distribution */}
        <div className="bg-white border-8 border-black p-8 mb-8">
          <h3 className="text-3xl font-black text-black mb-6 uppercase">Sentiment Distribution</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-2">
                <span className="font-black text-black mono">LEVEL 3 (CRISIS)</span>
                <span className="font-black text-black mono">{data.levelDistribution.level3} entries ({level3Percent}%)</span>
              </div>
              <div className="w-full bg-black/10 h-8 border-4 border-black">
                <div
                  className="h-full bg-red-600"
                  style={{ width: `${level3Percent}%` }}
                ></div>
              </div>
            </div>
            <div>
              <div className="flex justify-between mb-2">
                <span className="font-black text-black mono">LEVEL 2 (FRUSTRATED)</span>
                <span className="font-black text-black mono">{data.levelDistribution.level2} entries ({level2Percent}%)</span>
              </div>
              <div className="w-full bg-black/10 h-8 border-4 border-black">
                <div
                  className="h-full bg-orange-500"
                  style={{ width: `${level2Percent}%` }}
                ></div>
              </div>
            </div>
            <div>
              <div className="flex justify-between mb-2">
                <span className="font-black text-black mono">LEVEL 1 (MILD)</span>
                <span className="font-black text-black mono">{data.levelDistribution.level1} entries ({level1Percent}%)</span>
              </div>
              <div className="w-full bg-black/10 h-8 border-4 border-black">
                <div
                  className="h-full bg-yellow-500"
                  style={{ width: `${level1Percent}%` }}
                ></div>
              </div>
            </div>
          </div>
          <div className="mt-6 pt-6 border-t-4 border-black">
            <div className="font-black text-black mono text-sm">
              TOTAL DATA POINTS: {data.levelDistribution.total}
            </div>
          </div>
        </div>

        {/* Sample Data Points */}
        <div className="bg-black border-8 border-white p-8 mb-8">
          <h3 className="text-3xl font-black text-white mb-6 uppercase">Real Stories From The Data</h3>
          <div className="space-y-4">
            {data.sampleData.map((point, i) => (
              <div key={i} className="border-4 border-white p-6 bg-black hover:border-red-600 transition-colors">
                <div className="flex justify-between items-start mb-3">
                  <span className={`font-black mono text-sm px-3 py-1 ${
                    point.level === 3 ? 'bg-red-600' :
                    point.level === 2 ? 'bg-orange-500' :
                    'bg-yellow-500'
                  } text-black`}>
                    LEVEL {point.level}
                  </span>
                  <span className="text-white/60 font-bold mono text-xs">
                    {point.platform.toUpperCase()} · {point.date}
                  </span>
                </div>
                {point.url ? (
                  <a
                    href={point.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block group"
                  >
                    <p className="text-white font-bold leading-relaxed group-hover:text-red-600 transition-colors">
                      "{point.content}"
                    </p>
                    {(point.viewCount !== undefined || point.commentCount !== undefined) && (
                      <div className="flex items-center gap-3 mt-3 pt-3 border-t-2 border-white/20">
                        {point.viewCount !== undefined && (
                          <span className="text-white/60 font-bold mono text-xs">
                            {point.viewCount.toLocaleString()} VIEWS
                          </span>
                        )}
                        {point.commentCount !== undefined && (
                          <span className="text-white/60 font-bold mono text-xs">
                            {point.commentCount.toLocaleString()} COMMENTS
                          </span>
                        )}
                        <span className="text-white/40 font-bold mono text-xs">
                          → Click to watch
                        </span>
                      </div>
                    )}
                  </a>
                ) : (
                  <p className="text-white font-bold leading-relaxed">
                    "{point.content}"
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Collection Progress */}
        <div className="bg-white border-8 border-black p-8 mb-8">
          <h3 className="text-3xl font-black text-black mb-6 uppercase">Data Collection Progress</h3>
          <div className="space-y-4">
            {data.collectionProgress.map((progress, i) => (
              <div key={i}>
                <div className="flex justify-between mb-2">
                  <span className="font-black text-black mono">{progress.platform.toUpperCase()}</span>
                  <span className="font-black text-black mono">
                    {progress.current}/{progress.target} ({progress.percentage}%)
                  </span>
                </div>
                <div className="w-full bg-black/10 h-6 border-4 border-black">
                  <div
                    className={`h-full ${progress.percentage === 100 ? 'bg-green-600' : progress.percentage > 0 ? 'bg-orange-500' : 'bg-red-600'}`}
                    style={{ width: `${progress.percentage}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Data Sources & Methodology */}
        <div className="bg-red-700 border-8 border-black p-8 mb-8">
          <h3 className="text-3xl font-black text-white mb-6 uppercase">Methodology & Sources</h3>
          <div className="mb-6">
            <div className="text-white font-bold mono text-sm mb-3">DATA SOURCES:</div>
            <ul className="space-y-2">
              {data.dataSources.map((source, i) => (
                <li key={i} className="text-white font-bold flex items-start">
                  <span className="text-white mr-3">▸</span>
                  <span>{source}</span>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <div className="text-white font-bold mono text-sm mb-3">COLLECTION METHOD:</div>
            <p className="text-white font-bold leading-relaxed">
              {data.methodology}
            </p>
          </div>
        </div>

        {/* Close button at bottom */}
        <div className="text-center">
          <button
            onClick={onClose}
            className="px-12 py-6 bg-white text-black font-black hover:bg-red-600 hover:text-white transition-colors border-8 border-black text-2xl uppercase tracking-wide"
          >
            CLOSE
          </button>
        </div>
      </div>
    </div>
  );
}
