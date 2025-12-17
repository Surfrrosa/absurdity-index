import MetricCard from '@/components/MetricCard';
import Header from '@/components/Header';
import AbsurdityScore from '@/components/AbsurdityScore';

export default function Home() {
  return (
    <main className="min-h-screen bg-black">
      <Header />

      {/* Bosch-inspired banner with classical absurdist art */}
      <div className="bg-red-600 border-b-4 border-white py-20 relative overflow-hidden min-h-[280px]">
        {/* Background image - Bosch Garden of Earthly Delights (full triptych) */}
        <div
          className="absolute inset-0 opacity-50 bg-cover bg-center"
          style={{
            backgroundImage: "url('https://upload.wikimedia.org/wikipedia/commons/a/ae/El_jard%C3%ADn_de_las_Delicias%2C_de_El_Bosco.jpg')",
            filter: 'grayscale(10%) contrast(130%) brightness(70%)'
          }}
        />
        {/* Subtle dark overlay */}
        <div className="absolute inset-0 bg-black/10" />

        <div className="container mx-auto px-6 text-center relative z-10">
          <p className="text-white text-3xl font-black uppercase tracking-tight drop-shadow-[0_4px_12px_rgba(0,0,0,0.8)] leading-tight max-w-4xl mx-auto">
            "One must imagine Sisyphus checking his email"
          </p>
          <p className="text-white text-base font-bold mt-4 mono drop-shadow-[0_2px_8px_rgba(0,0,0,0.9)]">
            — Albert Camus-ish
          </p>
        </div>
      </div>

      <div className="container mx-auto px-6 py-12">
        <AbsurdityScore />

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
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
          />

          <MetricCard
            title="Housing Despair"
            score={13.25}
            label="Homeownership Feels Achievable"
            trend="improving"
            data={{
              medianPrice: "$383,725",
              medianRent: "$2,000/mo",
              priceToIncome: "4.6x ratio"
            }}
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
          />

          <MetricCard
            title="Customer Service Hell"
            score={5.12}
            label="Humans Helping Humans"
            trend="improving"
            data={{
              acsi: "77.3 overall satisfaction",
              telecom: "71 (lowest sector)",
              trends: "Moderate frustration"
            }}
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
          />

          <MetricCard
            title="Layoff Watch"
            score={6.95}
            label="Job Security Exists (???)."
            trend="neutral"
            data={{
              total2025: "152,922 tech workers",
              companies: "551 companies",
              trend: "Ongoing instability"
            }}
          />

          <MetricCard
            title="AI Psychosis"
            score={18.05}
            label="Digital Stockholm Syndrome Setting In"
            trend="worsening"
            data={{
              youtube: "54.8% crisis ratio (146 videos)",
              reddit: "15.0% crisis ratio (200 posts)",
              completion: "60% data collected"
            }}
          />
        </div>

        <footer className="mt-16 text-center text-white pb-12 border-t-4 border-white pt-8">
          <p className="font-black text-2xl uppercase">THE ABSURDITY INDEX</p>
          <p className="mt-4 mono font-bold text-sm">DATA: DEC 2025 | UPDATES: WEEKLY</p>
          <p className="mt-2 mono font-bold text-sm">BUILT BY SHAINA PAULEY</p>
        </footer>
      </div>
    </main>
  );
}
