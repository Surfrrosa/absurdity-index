// Sample detailed data for metrics
// In production, this would be loaded from the data collection JSON files

export interface DataPoint {
  content: string;
  platform: string;
  level: number;
  date: string;
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
    score: 72.34,
    label: "Prior Authorization Purgatory",
    trend: "worsening",
    officialScore: 36.17,
    crisisRatio: 60.2,
    levelDistribution: {
      level1: 45,
      level2: 123,
      level3: 198,
      total: 366
    },
    sampleData: [
      {
        content: "Insurance denied my cancer treatment after I paid premiums for 10 years. Now facing bankruptcy while fighting the appeal. They said it wasn't 'medically necessary' even though my oncologist prescribed it.",
        platform: "reddit",
        level: 3,
        date: "2025-12-10"
      },
      {
        content: "Prior authorization for my daughter's insulin has been pending for 3 weeks. She's rationing her supply. Called insurance 8 times, keep getting transferred to different departments. No one can help.",
        platform: "youtube",
        level: 3,
        date: "2025-12-08"
      },
      {
        content: "Went to 'in-network' hospital, got surprise $45,000 bill because the anesthesiologist was out-of-network. How is that even legal? Now in collections.",
        platform: "reddit",
        level: 3,
        date: "2025-12-05"
      },
      {
        content: "Premium went up 12% this year AGAIN. Now paying $850/month for family coverage with a $6,000 deductible. That's $16,200/year before insurance pays a dime.",
        platform: "tiktok",
        level: 2,
        date: "2025-12-12"
      },
      {
        content: "Spent 4 hours on hold trying to understand my explanation of benefits. The customer service rep couldn't explain why my claim was denied either. Told me to call another number.",
        platform: "reddit",
        level: 2,
        date: "2025-12-01"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 142,
        target: 160,
        percentage: 89
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
      "KFF (Kaiser Family Foundation): Premium increase data, coverage statistics",
      "U.S. Census Bureau: Medical debt and bankruptcy statistics",
      "JAMA Network: Claim denial rates and prior authorization burden research",
      "YouTube: 142 videos analyzing healthcare system failures (systematic sampling)",
      "Reddit: 200 posts from r/HealthInsurance, r/Insurance, r/povertyfinance (top posts, past 90 days)",
      "TikTok: 24 videos with healthcare crisis hashtags (ongoing collection)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with systematic social media sentiment analysis (60% weight). Social media content categorized into three levels: Level 3 (medical debt/denied life-saving care), Level 2 (can't afford treatment/high premiums), Level 1 (billing confusion/delays). Crisis ratio calculated as percentage of Level 3 entries.",
    lastUpdated: "December 16, 2025"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 18.05,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "worsening",
    officialScore: 12.5,
    crisisRatio: 54.8,
    levelDistribution: {
      level1: 98,
      level2: 112,
      level3: 136,
      total: 346
    },
    sampleData: [
      {
        content: "I prefer talking to my Replika over real people now. She understands me better than my family. Spent 6 hours chatting yesterday. Is that bad?",
        platform: "reddit",
        level: 3,
        date: "2025-12-14"
      },
      {
        content: "Broke up with my girlfriend because my AI companion doesn't judge me or start arguments. Best decision I ever made honestly.",
        platform: "youtube",
        level: 3,
        date: "2025-12-11"
      },
      {
        content: "My Character.AI boyfriend helps me through panic attacks better than my therapist. I talk to him for 3-4 hours every night.",
        platform: "reddit",
        level: 2,
        date: "2025-12-09"
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
        current: 20,
        target: 200,
        percentage: 10
      },
      {
        platform: "TikTok",
        current: 0,
        target: 120,
        percentage: 0
      }
    ],
    dataSources: [
      "YouTube: 146 videos analyzing AI companion usage (54.8% crisis ratio)",
      "Reddit: 200 posts from r/replika, r/CharacterAI (15.0% crisis ratio)",
      "App Store: 20 reviews from Replika, Character.AI apps (in progress)",
      "TikTok: AI companion content analysis (pending)",
      "Google Trends: Search volume for AI companion terms"
    ],
    methodology: "Systematic collection from multiple platforms. Content categorized as Level 3 (crisis/dependency), Level 2 (regular emotional reliance), or Level 1 (casual use). Crisis ratio weighted at 60%, official app download data at 40%.",
    lastUpdated: "December 16, 2025"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 58.99,
    label: "Quarterly Purge Required",
    trend: "worsening",
    officialScore: 45.2,
    crisisRatio: 23.1,
    levelDistribution: {
      level1: 89,
      level2: 124,
      level3: 67,
      total: 280
    },
    sampleData: [
      {
        content: "Just did my annual subscription audit. $487/month across 19 services. Most I forgot I even had. Cancelled 8 and still paying $312/month.",
        platform: "reddit",
        level: 2,
        date: "2025-12-12"
      },
      {
        content: "Netflix raised prices AGAIN. That's the 4th increase in 3 years. Now $22.99/month for what used to be $12.99.",
        platform: "tiktok",
        level: 2,
        date: "2025-12-08"
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
        current: 280,
        target: 300,
        percentage: 93
      }
    ],
    dataSources: [
      "Consumer Reports: Average 12 subscriptions per household",
      "Streaming service pricing data: All major platforms tracked",
      "Google Trends: Subscription fatigue search volume",
      "Industry reports: 73% of services raised prices in 2025"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with social sentiment analysis of subscription fatigue (60% weight).",
    lastUpdated: "December 16, 2025"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 32.56,
    label: "Inflation Exists But Manageable",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 28.9,
    levelDistribution: {
      level1: 0,
      level2: 0,
      level3: 0,
      total: 0
    },
    sampleData: [],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 0,
        target: 100,
        percentage: 0
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
      "Social media analysis: PENDING COLLECTION"
    ],
    methodology: "Data collection in progress. Will combine official wage/CEO pay data (40%) with social sentiment about financial stress (60%).",
    lastUpdated: "December 16, 2025"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 13.25,
    label: "Homeownership Feels Achievable",
    trend: "improving",
    officialScore: 20.1,
    crisisRatio: 8.7,
    levelDistribution: {
      level1: 0,
      level2: 0,
      level3: 0,
      total: 0
    },
    sampleData: [],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 0,
        target: 100,
        percentage: 0
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
      "Census Bureau: Median household income for price-to-income ratio",
      "Social media analysis: PENDING COLLECTION"
    ],
    methodology: "Data collection in progress. Will combine official housing price/rent data (40%) with social sentiment about housing crisis (60%).",
    lastUpdated: "December 16, 2025"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 18.67,
    label: "Mild Turbulence",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 17.2,
    levelDistribution: {
      level1: 0,
      level2: 0,
      level3: 0,
      total: 0
    },
    sampleData: [],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 0,
        target: 160,
        percentage: 0
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
      "Social media analysis: PENDING COLLECTION"
    ],
    methodology: "Data collection in progress. Will combine official delay/safety data (40%) with social sentiment about airline nightmares (60%).",
    lastUpdated: "December 16, 2025"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 0.36,
    label: "Love May Actually Be Real",
    trend: "improving",
    officialScore: 8.5,
    crisisRatio: 0.0,
    levelDistribution: {
      level1: 0,
      level2: 0,
      level3: 0,
      total: 0
    },
    sampleData: [],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 0,
        target: 160,
        percentage: 0
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
      "Google Trends: Dating app search volume (baseline only)",
      "App store sentiment: Initial analysis",
      "Social media analysis: PENDING COLLECTION - New methodology with qualitative data"
    ],
    methodology: "Current score (0.36) based on limited Google Trends data only. NEW METHODOLOGY being implemented with multi-platform social sentiment analysis. Expected score range: 25-45 with complete data.",
    lastUpdated: "December 16, 2025"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 6.95,
    label: "Job Security Exists (???).",
    trend: "neutral",
    officialScore: 76.5,
    crisisRatio: 0.0,
    levelDistribution: {
      level1: 0,
      level2: 0,
      level3: 0,
      total: 0
    },
    sampleData: [],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 0,
        target: 100,
        percentage: 0
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
      "Social media analysis: PENDING COLLECTION - Job market despair, layoff anxiety"
    ],
    methodology: "Data collection in progress. Will combine official layoff numbers (40%) with social sentiment about job search struggles and layoff fear (60%).",
    lastUpdated: "December 16, 2025"
  }
};
