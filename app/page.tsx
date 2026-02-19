'use client';

import { useState } from 'react';
import MetricCard from '@/components/MetricCard';
import Header from '@/components/Header';
import AbsurdityScore from '@/components/AbsurdityScore';
import MetricDetail from '@/components/MetricDetail';
import { getAllMetricsWithLabels, getLatestUpdateDate } from '@/lib/metricDetailData';

export default function Home() {
  const [selectedMetric, setSelectedMetric] = useState<string | null>(null);
  const metricsWithLabels = getAllMetricsWithLabels();
  const updateDate = getLatestUpdateDate();

  return (
    <main className="min-h-screen bg-black">
      <a
        href="#metrics"
        className="sr-only focus:not-sr-only focus:absolute focus:z-50 focus:top-4 focus:left-4 focus:bg-white focus:text-black focus:px-4 focus:py-2 focus:font-black focus:border-4 focus:border-black"
      >
        Skip to metrics
      </a>
      <Header />

      {selectedMetric && metricsWithLabels[selectedMetric] && (
        <MetricDetail
          data={metricsWithLabels[selectedMetric]}
          onClose={() => setSelectedMetric(null)}
        />
      )}

      {/* Bosch-inspired banner with classical absurdist art */}
      <div className="border-b-4 border-white relative overflow-hidden" style={{ backgroundColor: '#5f0f0f' }}>
        {/* Background image - Bosch middle panel zoomed in */}
        <div
          className="absolute inset-0 opacity-45"
          style={{
            backgroundImage: "url('https://upload.wikimedia.org/wikipedia/commons/a/ae/El_jard%C3%ADn_de_las_Delicias%2C_de_El_Bosco.jpg')",
            backgroundSize: '280%',
            backgroundPosition: '50% 30%',
            backgroundRepeat: 'no-repeat',
            filter: 'grayscale(5%) contrast(140%) brightness(65%)',
            mixBlendMode: 'overlay'
          }}
        />

        <div className="container mx-auto px-4 md:px-6 py-12 md:py-20 text-center relative z-10">
          <p className="text-white text-xl sm:text-2xl md:text-3xl font-black uppercase tracking-tight drop-shadow-[0_4px_12px_rgba(0,0,0,0.8)] leading-tight max-w-4xl mx-auto px-2">
            "One must imagine Sisyphus checking his email"
          </p>
          <p className="text-white text-sm md:text-base font-bold mt-3 md:mt-4 mono drop-shadow-[0_2px_8px_rgba(0,0,0,0.9)]">
            — Albert Camus-ish
          </p>
        </div>
      </div>

      <div className="container mx-auto px-4 md:px-6 py-8 md:py-12">
        <AbsurdityScore />

        <div id="metrics" className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mt-6 md:mt-8">
          {Object.entries(metricsWithLabels).map(([name, metric], index) => (
            <div
              key={name}
              className="animate-fadeInUp"
              style={{ animationDelay: `${(index + 1) * 100}ms` }}
            >
              <MetricCard
                title={metric.title}
                score={metric.score}
                label={metric.label}
                trend={metric.trend}
                data={{
                  // Create summary from data sources with ellipsis if truncated
                  source1: metric.dataSources[0]
                    ? (metric.dataSources[0].length > 50 ? metric.dataSources[0].substring(0, 50) + ".." : metric.dataSources[0])
                    : "",
                  source2: metric.dataSources[1]
                    ? (metric.dataSources[1].length > 50 ? metric.dataSources[1].substring(0, 50) + ".." : metric.dataSources[1])
                    : "",
                  source3: metric.dataSources[2]
                    ? (metric.dataSources[2].length > 50 ? metric.dataSources[2].substring(0, 50) + ".." : metric.dataSources[2])
                    : ""
                }}
                onClick={() => setSelectedMetric(name)}
                entryCount={metric.levelDistribution.total}
                lastUpdated={metric.lastUpdated}
              />
            </div>
          ))}
        </div>

        <footer className="mt-16 text-center text-white pb-12 border-t-4 border-white pt-8">
          <p className="font-black text-2xl uppercase">THE ABSURDITY INDEX</p>
          <p className="mt-4 mono font-bold text-sm">DATA: {updateDate} | UPDATES: WEEKLY</p>
          <p className="mt-2 mono font-bold text-sm">CREATED BY SHAINA PAULEY</p>
          <p className="mt-3 mono font-bold text-sm">
            <a
              href="https://buymeacoffee.com/shainapauley"
              target="_blank"
              rel="noopener noreferrer"
              className="border-b-2 border-white hover:border-red-600 hover:text-red-600 transition-colors"
            >
              ♡ SUPPORT THIS PROJECT
            </a>
          </p>
        </footer>
      </div>
    </main>
  );
}
