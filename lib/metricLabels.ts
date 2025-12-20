/**
 * Dynamic labels for metrics based on score thresholds
 * Each metric has 5 labels corresponding to severity levels
 */

export interface LabelThreshold {
  max: number;
  label: string;
}

export interface MetricLabels {
  [metricName: string]: LabelThreshold[];
}

export const metricLabels: MetricLabels = {
  "What Healthcare?": [
    { max: 20, label: "Coverage Exists (Allegedly)" },
    { max: 40, label: "Navigating the Maze" },
    { max: 60, label: "Prior Authorization Purgatory" },
    { max: 80, label: "Medical Bankruptcy Pipeline" },
    { max: 100, label: "Die Quietly, Please" }
  ],

  "AI Psychosis": [
    { max: 20, label: "Chatbots Are Cute" },
    { max: 40, label: "Digital Stockholm Syndrome Setting In" },
    { max: 60, label: "My AI Is My Best Friend" },
    { max: 80, label: "Can't Tell Humans From Bots Anymore" },
    { max: 100, label: "Ready Player One Was A Warning" }
  ],

  "Subscription Overload": [
    { max: 20, label: "Affordable Convenience" },
    { max: 40, label: "Quarterly Purge Required" },
    { max: 60, label: "Forgot What I'm Paying For" },
    { max: 80, label: "Working to Pay Subscriptions" },
    { max: 100, label: "Subscription Serfdom Achieved" }
  ],

  "Wage Stagnation": [
    { max: 20, label: "Inflation Exists But Manageable" },
    { max: 40, label: "Paycheck Doesn't Go As Far" },
    { max: 60, label: "Living Paycheck to Paycheck" },
    { max: 80, label: "Full-Time Yet Food Insecure" },
    { max: 100, label: "Working Poor Is The New Normal" }
  ],

  "Housing Despair": [
    { max: 20, label: "Homeownership Is Possible" },
    { max: 40, label: "Saving For A Deposit (Forever)" },
    { max: 60, label: "Multiple Organs Required" },
    { max: 80, label: "Gave Up On Ownership Entirely" },
    { max: 100, label: "Welcome To Permanent Rentership" }
  ],

  "Dating App Despair": [
    { max: 20, label: "Love Is In The Air" },
    { max: 40, label: "Swiping Through The Void" },
    { max: 60, label: "Emotionally Exhausted, Still Trying" },
    { max: 80, label: "Gave Up, Got A Cat" },
    { max: 100, label: "Accepting Loneliness As Default" }
  ],

  "Layoff Watch": [
    { max: 20, label: "Job Security Intact" },
    { max: 40, label: "Resume At The Ready" },
    { max: 60, label: "Layoff Roulette Daily Anxiety" },
    { max: 80, label: "500 Applications, Zero Responses" },
    { max: 100, label: "Experience Is Now A Liability" }
  ],

  "Airline Chaos": [
    { max: 20, label: "Mild Turbulence" },
    { max: 40, label: "Delays Are The New Normal" },
    { max: 60, label: "Stranded Overnight Regularly" },
    { max: 80, label: "Travel Plans Are Suggestions" },
    { max: 100, label: "Airlines Are Scam Operations" }
  ]
};

/**
 * Get the appropriate label for a metric based on its score
 */
export function getMetricLabel(metricName: string, score: number): string {
  const labels = metricLabels[metricName];

  if (!labels) {
    console.warn(`No labels found for metric: ${metricName}`);
    return "Status Unknown";
  }

  // Find the first threshold that the score is less than or equal to
  for (const threshold of labels) {
    if (score <= threshold.max) {
      return threshold.label;
    }
  }

  // Fallback to the highest severity label
  return labels[labels.length - 1].label;
}
