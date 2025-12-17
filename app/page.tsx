'use client';

import { useState } from 'react';
import MetricCard from '@/components/MetricCard';
import Header from '@/components/Header';
import AbsurdityScore from '@/components/AbsurdityScore';
import MetricDetail from '@/components/MetricDetail';
import { metricDetails } from '@/lib/metricDetailData';

export default function Home() {
  const [selectedMetric, setSelectedMetric] = useState<string | null>(null);

  return (
    <main className="min-h-screen bg-black">
      <Header />

      {selectedMetric && metricDetails[selectedMetric] && (
        <MetricDetail
          data={metricDetails[selectedMetric]}
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

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mt-6 md:mt-8">
          <MetricCard
            title="Wage Stagnation"
            score={32.56}
            label="Inflation Exists But Manageable"
            trend="neutral"
            data={{
              wagegrowth: "+1.0% YoY (Dec 2025)",
              inflation: "Real wages barely keeping pace",
              ceoRatio: "285:1 CEO-to-worker pay"
            }}
            onClick={() => setSelectedMetric("Wage Stagnation")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="Housing Despair"
            score={50.85}
            label="Multiple Organs Required"
            trend="worsening"
            data={{
              genZRentBurden: "58.2% rent-burdened",
              medianPrice: "$383,725",
              priceToIncome: "4.6x ratio"
            }}
            onClick={() => setSelectedMetric("Housing Despair")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="Airline Chaos"
            score={18.67}
            label="Mild Turbulence"
            trend="neutral"
            data={{
              delays: "22% delayed (Dec 2025)",
              satisfaction: "Declining trends",
              complaints: "Rising consumer frustration"
            }}
            onClick={() => setSelectedMetric("Airline Chaos")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="What Healthcare?"
            score={72.34}
            label="Prior Authorization Purgatory"
            trend="worsening"
            data={{
              premiumIncrease: "+7% avg annual increase",
              denialRate: "~18% claims denied initially",
              medicalDebt: "41% adults have medical debt"
            }}
            onClick={() => setSelectedMetric("What Healthcare?")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="Subscription Overload"
            score={58.99}
            label="Quarterly Purge Required"
            trend="worsening"
            data={{
              avgSubscriptions: "12 per household",
              avgSpending: "$273/month",
              priceIncreases: "73% raised prices in 2025"
            }}
            onClick={() => setSelectedMetric("Subscription Overload")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="Dating App Despair"
            score={0.36}
            label="Love May Actually Be Real"
            trend="improving"
            data={{
              trends: "Low search volume",
              sentiment: "Stable",
              projection: "Expected 25-45 with full data"
            }}
            onClick={() => setSelectedMetric("Dating App Despair")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="Layoff Watch"
            score={48.48}
            label="Resume At The Ready"
            trend="worsening"
            data={{
              u6Unemployment: "7.5% (vs 3.7% U-3)",
              techLayoffs: "152,922 in 2024",
              jobSearchReality: "6+ month searches"
            }}
            onClick={() => setSelectedMetric("Layoff Watch")}
            entryCount={0}
            lastUpdated="Dec 17, 2024"
          />

          <MetricCard
            title="AI Psychosis"
            score={18.05}
            label="Digital Stockholm Syndrome Setting In"
            trend="worsening"
            data={{
              youtube: "37.0% crisis ratio (146 videos)",
              reddit: "4.0% crisis ratio (200 posts)",
              completion: "72% data collected"
            }}
            onClick={() => setSelectedMetric("AI Psychosis")}
            entryCount={346}
            lastUpdated="Dec 16, 2024"
          />
        </div>

        <footer className="mt-16 text-center text-white pb-12 border-t-4 border-white pt-8">
          <p className="font-black text-2xl uppercase">THE ABSURDITY INDEX</p>
          <p className="mt-4 mono font-bold text-sm">DATA: DEC 2025 | UPDATES: WEEKLY</p>
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
