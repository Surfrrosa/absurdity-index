// Sample detailed data for metrics
// In production, this would be loaded from the data collection JSON files

import { getMetricLabel } from './metricLabels';

export interface DataPoint {
  content: string;
  platform: string;
  level: number;
  date: string;
  url?: string;
  viewCount?: number;
  videoId?: string;
  commentCount?: number;
}

export interface CollectionProgress {
  platform: string;
  current: number;
  target: number;
  percentage: number;
}

export interface MetricDetailData {
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

export const metricDetails: Record<string, MetricDetailData> = {
  "What Healthcare?": {
    title: "What Healthcare?",
    score: 50.20,
    label: "Prior Authorization Purgatory",
    trend: "worsening",
    officialScore: 56.30,
    crisisRatio: 46.14,
    levelDistribution: {
      level1: 110,
      level2: 16,
      level3: 34,
      total: 160
    },
    sampleData: [
      {
        content: "One of the top reasons people go broke? Medical debt.",
        platform: "youtube",
        level: 3,
        date: "2025-10-31",
        url: "https://www.youtube.com/watch?v=BKxGsIbBhnI",
        videoId: "BKxGsIbBhnI",
        viewCount: 23263,
        commentCount: 274
      },
      {
        content: "Medical #Bankruptcy Is an American Problem #america #medicaldebt #medicalinsurance #healthcare",
        platform: "youtube",
        level: 3,
        date: "2025-11-25",
        url: "https://www.youtube.com/watch?v=9rJZ17vjSWc",
        videoId: "9rJZ17vjSWc",
        viewCount: 18233,
        commentCount: 61
      },
      {
        content: "11 Investigates local woman denied life-saving cancer treatment",
        platform: "youtube",
        level: 3,
        date: "2025-09-23",
        url: "https://www.youtube.com/watch?v=spA2CT97xpA",
        videoId: "spA2CT97xpA",
        viewCount: 1522,
        commentCount: 0
      },
      {
        content: "Medical Bills Are Still the #1 Cause of Bankruptcy- Here's Why Coverage Matters",
        platform: "youtube",
        level: 3,
        date: "2025-10-30",
        url: "https://www.youtube.com/watch?v=jguj_sabgBY",
        videoId: "jguj_sabgBY",
        viewCount: 1065,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 160,
        target: 160,
        percentage: 100
      },
      {
        platform: "Reddit",
        current: 200,
        target: 200,
        percentage: 100
      },
      {
        platform: "TikTok",
        current: 24,
        target: 120,
        percentage: 20
      }
    ],
    dataSources: [
      "KFF (Kaiser Family Foundation): Premium increase data, coverage statistics, uninsured rate",
      "U.S. Census Bureau: Medical debt and bankruptcy statistics",
      "JAMA Network: Claim denial rates and prior authorization burden research",
      "YouTube: 160 videos analyzing healthcare system failures (systematic sampling)",
      "Reddit: 200 posts from r/HealthInsurance, r/Insurance, r/povertyfinance (top posts, past 90 days)",
      "TikTok: 24 videos with healthcare crisis hashtags (ongoing collection)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Social media content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement (views). Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "December 20, 2025"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 37.31,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "worsening",
    officialScore: 12.5,
    crisisRatio: 53.85,
    levelDistribution: {
      level1: 66,
      level2: 26,
      level3: 54,
      total: 146
    },
    sampleData: [
      {
        content: "How Character.ai slowly destroys your mental health | The C.ai addiction iceberg",
        platform: "youtube",
        level: 3,
        date: "2024-12-25",
        url: "https://www.youtube.com/watch?v=12waK-aDHV0",
        videoId: "12waK-aDHV0",
        viewCount: 665497,
        commentCount: 6293
      },
      {
        content: "AI Made Him Delusional: The Case Nobody's Talking About",
        platform: "youtube",
        level: 3,
        date: "2025-12-19",
        url: "https://www.youtube.com/watch?v=TBD",
        videoId: "TBD",
        viewCount: 439,
        commentCount: 0
      },
      {
        content: "People Are Getting ADDICTED To AI Chatbot Lovers (2025)",
        platform: "youtube",
        level: 3,
        date: "2025-02-16",
        url: "https://www.youtube.com/watch?v=fsHcHr7OqI0",
        videoId: "fsHcHr7OqI0",
        viewCount: 173374,
        commentCount: 753
      },
      {
        content: "We Ignored Her's Warning About AI Loneliness | Replika Reality Check",
        platform: "youtube",
        level: 2,
        date: "2025-10-24",
        url: "https://www.youtube.com/watch?v=ftnbNaAMhYU",
        videoId: "ftnbNaAMhYU",
        viewCount: 944,
        commentCount: 18
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 146,
        target: 160,
        percentage: 91
      },
      {
        platform: "Reddit",
        current: 200,
        target: 200,
        percentage: 100
      },
      {
        platform: "App Store",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 120,
        percentage: 0
      }
    ],
    dataSources: [
      "YouTube: 146 videos analyzing AI companion usage",
      "Reddit: 200 posts from r/replika, r/CharacterAI (4.0% crisis ratio)",
      "App Store: 0 reviews collected (pending)",
      "TikTok: AI companion content analysis (pending)",
      "Google Trends: Search volume for AI companion terms"
    ],
    methodology: "Systematic collection from multiple platforms. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official app download data (40% weight).",
    lastUpdated: "December 20, 2025"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 39.93,
    label: "Quarterly Purge Required",
    trend: "worsening",
    officialScore: 45.2,
    crisisRatio: 36.41,
    levelDistribution: {
      level1: 139,
      level2: 9,
      level3: 2,
      total: 150
    },
    sampleData: [
      {
        content: "Microsoft f*cked up real bad..",
        platform: "youtube",
        level: 1,
        date: "2025-10-02",
        url: "https://www.youtube.com/watch?v=lxJG6FBo9h8",
        videoId: "lxJG6FBo9h8",
        viewCount: 2383779,
        commentCount: 12593
      },
      {
        content: "why I'm cancelling ALL my subscription services",
        platform: "youtube",
        level: 2,
        date: "2025-11-30",
        url: "https://www.youtube.com/watch?v=Xv6q3gcHro0",
        videoId: "Xv6q3gcHro0",
        viewCount: 9754,
        commentCount: 217
      },
      {
        content: "Subscription Fatigue Is Bleeding Americans Dry",
        platform: "youtube",
        level: 1,
        date: "2025-12-16",
        url: "https://www.youtube.com/watch?v=pc4MgspmiUs",
        videoId: "pc4MgspmiUs",
        viewCount: 8637,
        commentCount: 174
      },
      {
        content: "Streaming is OVERWHELMING! Why Netflix is LOSING Viewers! #shorts",
        platform: "youtube",
        level: 2,
        date: "2025-10-23",
        url: "https://www.youtube.com/watch?v=GZPr9fJG1wA",
        videoId: "GZPr9fJG1wA",
        viewCount: 1926,
        commentCount: 2
      }
    ],
    collectionProgress: [
      {
        platform: "Industry Reports",
        current: 100,
        target: 100,
        percentage: 100
      },
      {
        platform: "Social Media Sampling",
        current: 150,
        target: 300,
        percentage: 50
      }
    ],
    dataSources: [
      "Consumer Reports: Average 12 subscriptions per household",
      "Streaming service pricing data: All major platforms tracked",
      "Google Trends: Subscription fatigue search volume",
      "Industry reports: 73% of services raised prices in 2025",
      "YouTube: 150 videos analyzing subscription fatigue"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment analysis (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "December 20, 2025"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 40.86,
    label: "Inflation Exists But Manageable",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 42.50,
    levelDistribution: {
      level1: 73,
      level2: 16,
      level3: 7,
      total: 96
    },
    sampleData: [
      {
        content: "When the employed are pushed into homelessness",
        platform: "youtube",
        level: 3,
        date: "2025-11-16",
        url: "https://www.youtube.com/watch?v=4loulWBN5Nw",
        videoId: "4loulWBN5Nw",
        viewCount: 909737,
        commentCount: 7097
      },
      {
        content: "3 Jobs Still Homeless: The Reality of Working America",
        platform: "youtube",
        level: 3,
        date: "2025-10-22",
        url: "https://www.youtube.com/watch?v=NN3zMclcIVs",
        videoId: "NN3zMclcIVs",
        viewCount: 1176,
        commentCount: 1
      },
      {
        content: "I STOPPED Living Paycheck to Paycheck After Learning This One Rule",
        platform: "youtube",
        level: 2,
        date: "2025-11-29",
        url: "https://www.youtube.com/watch?v=_6v1VMlkfrc",
        videoId: "_6v1VMlkfrc",
        viewCount: 33655,
        commentCount: 18
      },
      {
        content: "Working Full-Time and Still Can't Eat",
        platform: "youtube",
        level: 1,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=aBw582ctvOA",
        videoId: "aBw582ctvOA",
        viewCount: 495317,
        commentCount: 2408
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 96,
        target: 100,
        percentage: 96
      },
      {
        platform: "Reddit",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 100,
        percentage: 0
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: 285:1 CEO-to-worker pay ratio",
      "Google Trends: Financial stress search volume",
      "YouTube: 96 videos about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "December 20, 2025"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 43.64,
    label: "Multiple Organs Required",
    trend: "worsening",
    officialScore: 37.6,
    crisisRatio: 47.66,
    levelDistribution: {
      level1: 91,
      level2: 4,
      level3: 27,
      total: 122
    },
    sampleData: [
      {
        content: "why i will never own a home (reality of being a gen Z)",
        platform: "youtube",
        level: 3,
        date: "2025-09-24",
        url: "https://www.youtube.com/watch?v=-w_kQ-4q8cc",
        videoId: "-w_kQ-4q8cc",
        viewCount: 62827,
        commentCount: 1253
      },
      {
        content: "YOU WILL NEVER OWN A HOME, AMERICANS HAVE LOST HOPE, THEY ILL EVER BE ABLE TO AFFORD TO BUY A HOMR",
        platform: "youtube",
        level: 3,
        date: "2025-12-07",
        url: "https://www.youtube.com/watch?v=BdN7wVBgd6Y",
        videoId: "BdN7wVBgd6Y",
        viewCount: 4061,
        commentCount: 130
      },
      {
        content: "The Housing Market Scam: Why You Will Never Own a Home 🏠📉",
        platform: "youtube",
        level: 3,
        date: "2025-11-27",
        url: "https://www.youtube.com/watch?v=GrF1MDQ-T0g",
        videoId: "GrF1MDQ-T0g",
        viewCount: 42,
        commentCount: 2
      },
      {
        content: "Why Nobody Can Afford a Home Anymore",
        platform: "youtube",
        level: 1,
        date: "2025-10-26",
        url: "https://www.youtube.com/watch?v=bqdPtjxzQaE",
        videoId: "bqdPtjxzQaE",
        viewCount: 397548,
        commentCount: 1896
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 122,
        target: 100,
        percentage: 122
      },
      {
        platform: "Reddit",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 100,
        percentage: 0
      }
    ],
    dataSources: [
      "Redfin: Median home price $383,725",
      "Zillow Rent Index: $2,000/month median rent",
      "Census Bureau: Gen Z rent burden data (37.6%)",
      "YouTube: 122 videos about housing crisis and homeownership despair"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "December 20, 2025"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 40.13,
    label: "Mild Turbulence",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 52.89,
    levelDistribution: {
      level1: 92,
      level2: 16,
      level3: 14,
      total: 122
    },
    sampleData: [
      {
        content: "Stranded For 10+ hours, Fliers Demand Action From Indigo Airlines For Cancelled Flights",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=rxXzYPDl5jc",
        videoId: "rxXzYPDl5jc",
        viewCount: 144801,
        commentCount: 98
      },
      {
        content: "I was stranded at the airport with my newborn baby, begging for help after my flight got...",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=-NJwQ_I1Y_4",
        videoId: "-NJwQ_I1Y_4",
        viewCount: 441045,
        commentCount: 84
      },
      {
        content: "Black Soldier Ignored At The Airport—Then The Flight Got Delayed For Him",
        platform: "youtube",
        level: 2,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=gzBWU8ICkOA",
        videoId: "gzBWU8ICkOA",
        viewCount: 4385,
        commentCount: 0
      },
      {
        content: "Flight Delays, Fees & Fights: Is Flying Getting Worse?",
        platform: "youtube",
        level: 1,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=X-ElLs6Xo-c",
        videoId: "X-ElLs6Xo-c",
        viewCount: 12,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 122,
        target: 160,
        percentage: 76
      },
      {
        platform: "Reddit",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 120,
        percentage: 0
      }
    ],
    dataSources: [
      "Bureau of Transportation Statistics: 22% flight delay rate",
      "ACSI satisfaction scores: Declining airline service quality",
      "FAA safety incident data: Emergency landings, equipment failures",
      "YouTube: 122 videos about airline chaos and travel nightmares"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "December 20, 2025"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 31.55,
    label: "Love May Actually Be Real",
    trend: "improving",
    officialScore: 8.5,
    crisisRatio: 46.92,
    levelDistribution: {
      level1: 84,
      level2: 10,
      level3: 20,
      total: 114
    },
    sampleData: [
      {
        content: "Why Gen Z is Quitting Dating Apps",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=OdjIW8IdbIM",
        videoId: "OdjIW8IdbIM",
        viewCount: 199804,
        commentCount: 994
      },
      {
        content: "Dating App Fatigue & Mental Health",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=ygRO028UQUU",
        videoId: "ygRO028UQUU",
        viewCount: 1683,
        commentCount: 77
      },
      {
        content: "Dating Apps Are Exhausting: Here's What's Happening",
        platform: "youtube",
        level: 2,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=fLYKy51jIVc",
        videoId: "fLYKy51jIVc",
        viewCount: 6,
        commentCount: 1
      },
      {
        content: "The Gen Z Dating Apocalypse",
        platform: "youtube",
        level: 1,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=dxxbcEGKs-c",
        videoId: "dxxbcEGKs-c",
        viewCount: 104738,
        commentCount: 585
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 114,
        target: 160,
        percentage: 71
      },
      {
        platform: "Reddit",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 120,
        percentage: 0
      }
    ],
    dataSources: [
      "Google Trends: Dating app search volume",
      "App store sentiment: Initial analysis",
      "YouTube: 114 videos about dating app burnout and despair"
    ],
    methodology: "Google Trends data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "December 20, 2025"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 51.64,
    label: "Resume At The Ready",
    trend: "worsening",
    officialScore: 76.5,
    crisisRatio: 35.07,
    levelDistribution: {
      level1: 65,
      level2: 8,
      level3: 1,
      total: 74
    },
    sampleData: [
      {
        content: "Job Search Nightmare: 1,000 Applications and Failure? #shorts",
        platform: "youtube",
        level: 3,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=-8rg1nPv-rc",
        videoId: "-8rg1nPv-rc",
        viewCount: 698,
        commentCount: 5
      },
      {
        content: "International students — 😓 200+ Job Applications, But No Response?",
        platform: "youtube",
        level: 2,
        date: "2025-10-17",
        url: "https://www.youtube.com/watch?v=Xe-dHYhBwVk",
        videoId: "Xe-dHYhBwVk",
        viewCount: 780,
        commentCount: 0
      },
      {
        content: "Unemployed @ 50 & was told I was overqualified",
        platform: "youtube",
        level: 2,
        date: "2025-09-26",
        url: "https://www.youtube.com/watch?v=4-UsaQaRiyA",
        videoId: "4-UsaQaRiyA",
        viewCount: 436,
        commentCount: 2
      },
      {
        content: "Why are Tech Layoffs Still Happening?",
        platform: "youtube",
        level: 1,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=XerzK0QNhnM",
        videoId: "XerzK0QNhnM",
        viewCount: 45923,
        commentCount: 184
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 74,
        target: 100,
        percentage: 74
      },
      {
        platform: "Reddit",
        current: 0,
        target: 200,
        percentage: 0
      },
      {
        platform: "TikTok",
        current: 0,
        target: 100,
        percentage: 0
      }
    ],
    dataSources: [
      "Layoffs.fyi: 152,922 tech workers laid off in 2025",
      "551 companies reported layoffs",
      "YouTube: 74 videos about layoffs and job search struggles"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "December 20, 2025"
  }
};

/**
 * Get a single metric with its dynamically calculated label
 */
export function getMetricWithLabel(metricName: string): MetricDetailData | undefined {
  const metric = metricDetails[metricName];
  if (!metric) return undefined;

  return {
    ...metric,
    label: getMetricLabel(metricName, metric.score)
  };
}

/**
 * Get all metrics with their dynamically calculated labels
 */
export function getAllMetricsWithLabels(): Record<string, MetricDetailData> {
  const metricsWithLabels: Record<string, MetricDetailData> = {};

  for (const [name, metric] of Object.entries(metricDetails)) {
    metricsWithLabels[name] = {
      ...metric,
      label: getMetricLabel(name, metric.score)
    };
  }

  return metricsWithLabels;
}
