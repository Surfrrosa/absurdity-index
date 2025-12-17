export default function Methodology() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-lg p-8">
          <h1 className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400 mb-6">
            Methodology & Data Transparency
          </h1>

          <div className="prose prose-invert prose-purple max-w-none">
            <p className="text-slate-300 text-lg mb-8">
              The Absurdity Index quantifies the absurdity of modern existence through rigorous data collection
              and research-grade methodology. All data sources, calculations, and sampling methods are documented below.
            </p>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Core Principles</h2>
              <div className="space-y-4 text-slate-300">
                <div className="bg-slate-900/50 p-4 rounded-lg border border-purple-500/20">
                  <h3 className="text-lg font-medium text-purple-200 mb-2">1. Objectivity</h3>
                  <p>Data is collected from official sources (BLS, Census, BTS) and public platforms without cherry-picking.
                  All sampling is systematic and documented.</p>
                </div>

                <div className="bg-slate-900/50 p-4 rounded-lg border border-purple-500/20">
                  <h3 className="text-lg font-medium text-purple-200 mb-2">2. Transparency</h3>
                  <p>Every data source is cited. All formulas are public. Sample sizes and collection methods are disclosed.
                  Limitations and data gaps are acknowledged.</p>
                </div>

                <div className="bg-slate-900/50 p-4 rounded-lg border border-purple-500/20">
                  <h3 className="text-lg font-medium text-purple-200 mb-2">3. Reproducibility</h3>
                  <p>All data collection scripts are available. Anyone can verify the results by following the same methodology.</p>
                </div>

                <div className="bg-slate-900/50 p-4 rounded-lg border border-purple-500/20">
                  <h3 className="text-lg font-medium text-purple-200 mb-2">4. Statistical Rigor</h3>
                  <p>Sample sizes meet research standards (minimum 100-200 per category). Multiple platforms are sampled
                  to avoid single-source bias.</p>
                </div>
              </div>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Data Sources by Metric</h2>

              <div className="space-y-6">
                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">Wage Stagnation</h3>
                  <ul className="list-disc list-inside space-y-2 text-slate-300">
                    <li><strong>BLS Employment Cost Index:</strong> Official wage growth data (Dec 2025)</li>
                    <li><strong>AFL-CIO CEO Pay Database:</strong> Executive compensation ratios</li>
                    <li><strong>Google Trends:</strong> Search volume for "wage stagnation", "cost of living"</li>
                    <li><strong>Sample size:</strong> Official government data (complete population)</li>
                  </ul>
                </div>

                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">Housing Despair</h3>
                  <ul className="list-disc list-inside space-y-2 text-slate-300">
                    <li><strong>Redfin Housing Market Data:</strong> Median home prices nationally</li>
                    <li><strong>Zillow Rent Index:</strong> Median rent by metro area</li>
                    <li><strong>Census Bureau:</strong> Median household income</li>
                    <li><strong>Google Trends:</strong> Housing crisis sentiment</li>
                  </ul>
                </div>

                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">AI Psychosis</h3>
                  <ul className="list-disc list-inside space-y-2 text-slate-300">
                    <li><strong>YouTube Data API v3:</strong> 146 videos analyzed (54.8% crisis ratio)</li>
                    <li><strong>Reddit JSON Feeds:</strong> 200 posts from r/replika + r/CharacterAI (15.0% crisis ratio)</li>
                    <li><strong>Google Trends:</strong> Search volume for AI companion terms</li>
                    <li><strong>App Store Reviews:</strong> Manual sampling from Replika, Character.AI (in progress)</li>
                    <li><strong>Categorization Framework:</strong>
                      <ul className="ml-6 mt-2">
                        <li>Level 3 (Crisis): Intense attachment, parasocial breakdown, "wife/husband" language</li>
                        <li>Level 2 (Dependent): Emotional attachment, relationship language</li>
                        <li>Level 1 (Casual): Informational, comedy, no emotional investment</li>
                      </ul>
                    </li>
                  </ul>
                </div>

                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">Subscription Overload</h3>
                  <ul className="list-disc list-inside space-y-2 text-slate-300">
                    <li><strong>Consumer Reports Survey:</strong> Average subscriptions per household (12)</li>
                    <li><strong>Streaming Service Pricing:</strong> All major platforms tracked</li>
                    <li><strong>Google Trends:</strong> "Cancel subscriptions", "subscription fatigue"</li>
                    <li><strong>Industry Reports:</strong> Price increase data (73% raised prices in 2025)</li>
                  </ul>
                </div>

                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">Airline Chaos</h3>
                  <ul className="list-disc list-inside space-y-2 text-slate-300">
                    <li><strong>Bureau of Transportation Statistics:</strong> Official delay/cancellation data</li>
                    <li><strong>ACSI Airline Satisfaction:</strong> Consumer satisfaction scores</li>
                    <li><strong>DOT Consumer Complaints:</strong> Complaint volume trends</li>
                  </ul>
                </div>

                <div className="bg-slate-900/50 p-6 rounded-lg border border-purple-500/20">
                  <h3 className="text-xl font-semibold text-pink-300 mb-3">Other Metrics</h3>
                  <p className="text-slate-300">
                    Customer Service Hell, Dating App Despair, and Layoff Watch use similar multi-source approaches combining
                    official data (ACSI, Layoffs.fyi), Google Trends sentiment, and platform-specific metrics.
                  </p>
                </div>
              </div>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Bias Mitigation Strategies</h2>
              <div className="space-y-3 text-slate-300">
                <div className="flex items-start">
                  <span className="text-purple-400 mr-3">•</span>
                  <p><strong>Multi-platform sampling:</strong> Data is collected from multiple sources (YouTube, Reddit, official statistics)
                  to avoid platform-specific bias</p>
                </div>
                <div className="flex items-start">
                  <span className="text-purple-400 mr-3">•</span>
                  <p><strong>Systematic sampling:</strong> Top/hot posts are sampled systematically, not selectively chosen to support
                  a narrative</p>
                </div>
                <div className="flex items-start">
                  <span className="text-purple-400 mr-3">•</span>
                  <p><strong>Automated categorization:</strong> Where possible, keyword-based categorization is used to reduce
                  subjective judgment</p>
                </div>
                <div className="flex items-start">
                  <span className="text-purple-400 mr-3">•</span>
                  <p><strong>Official sources prioritized:</strong> Government and industry data is used as the foundation,
                  supplemented by sentiment analysis</p>
                </div>
                <div className="flex items-start">
                  <span className="text-purple-400 mr-3">•</span>
                  <p><strong>Data gaps acknowledged:</strong> Incomplete metrics are clearly labeled with completion percentages</p>
                </div>
              </div>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Update Schedule</h2>
              <p className="text-slate-300 mb-4">
                Metrics are updated on different schedules based on data availability:
              </p>
              <ul className="list-disc list-inside space-y-2 text-slate-300">
                <li><strong>Weekly:</strong> Google Trends, social media sentiment, layoff tracking</li>
                <li><strong>Monthly:</strong> Housing prices, airline statistics, subscription trends</li>
                <li><strong>Quarterly:</strong> Wage data, CEO pay ratios, ACSI scores</li>
              </ul>
              <p className="text-slate-400 text-sm mt-4">
                Current baseline: December 2025. Full automated updates launching Q1 2026.
              </p>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Limitations & Ethical Considerations</h2>
              <div className="space-y-3 text-slate-300">
                <p>
                  This dashboard is designed to quantify cultural sentiment and economic trends, not to make clinical
                  diagnoses or policy recommendations. Specific limitations include:
                </p>
                <ul className="list-disc list-inside space-y-2 ml-4">
                  <li>Platform demographics may not represent general population</li>
                  <li>Self-reported sentiment may differ from actual behavior</li>
                  <li>Some metrics (AI Psychosis) are preliminary and require more research</li>
                  <li>Scores are relative indicators, not absolute measures</li>
                </ul>
                <p className="mt-4">
                  Data is collected from public sources only. No private information is accessed or stored.
                </p>
              </div>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Sample Size Standards</h2>
              <div className="bg-slate-900/50 p-4 rounded-lg border border-purple-500/20">
                <table className="w-full text-slate-300">
                  <thead>
                    <tr className="border-b border-purple-500/20">
                      <th className="text-left py-2">Component</th>
                      <th className="text-left py-2">Target Sample</th>
                      <th className="text-left py-2">Current Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr className="border-b border-slate-700/50">
                      <td className="py-2">YouTube Videos</td>
                      <td>120-160</td>
                      <td className="text-green-400">146 (Complete)</td>
                    </tr>
                    <tr className="border-b border-slate-700/50">
                      <td className="py-2">Reddit Posts</td>
                      <td>200</td>
                      <td className="text-green-400">200 (Complete)</td>
                    </tr>
                    <tr className="border-b border-slate-700/50">
                      <td className="py-2">App Store Reviews</td>
                      <td>200</td>
                      <td className="text-yellow-400">20 (10%, In Progress)</td>
                    </tr>
                    <tr className="border-b border-slate-700/50">
                      <td className="py-2">TikTok Videos</td>
                      <td>120</td>
                      <td className="text-slate-500">0 (Pending)</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </section>

            <section className="mb-8">
              <h2 className="text-2xl font-semibold text-purple-300 mb-4">Open Source & Verification</h2>
              <p className="text-slate-300">
                All data collection scripts, formulas, and raw data will be available on GitHub. Anyone can verify the
                methodology, reproduce the results, or suggest improvements.
              </p>
              <p className="text-slate-400 text-sm mt-3">
                GitHub repository: Coming soon | Contact: shaina@shainapauley.com
              </p>
            </section>

            <div className="mt-12 pt-8 border-t border-purple-500/20">
              <p className="text-slate-400 text-sm">
                Last updated: December 16, 2025 | Methodology version 1.0
              </p>
              <a
                href="/"
                className="inline-block mt-4 px-6 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg transition-colors"
              >
                Back to Dashboard
              </a>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
