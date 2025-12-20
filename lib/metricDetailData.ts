// Sample detailed data for metrics
// In production, this would be loaded from the data collection JSON files

export interface DataPoint {
  content: string;
  platform: string;
  level: number;
  date: string;
  url?: string;
  viewCount?: number;
  videoId?: string;
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
    crisisRatio: 17.92,
    levelDistribution: {
      level1: 236,
      level2: 48,
      level3: 62,
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
      "YouTube: 146 videos analyzing AI companion usage (37.0% crisis ratio)",
      "Reddit: 200 posts from r/replika, r/CharacterAI (4.0% crisis ratio)",
      "App Store: 0 reviews collected (pending)",
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
    score: 19.74,
    label: "Inflation Exists But Manageable",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 7.3,
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
        viewCount: 909737
      },
      {
        content: "3 Jobs Still Homeless: The Reality of Working America",
        platform: "youtube",
        level: 3,
        date: "2025-10-22",
        url: "https://www.youtube.com/watch?v=NN3zMclcIVs",
        videoId: "NN3zMclcIVs",
        viewCount: 1176
      },
      {
        content: "I STOPPED Living Paycheck to Paycheck After Learning This One Rule",
        platform: "youtube",
        level: 2,
        date: "2025-11-29",
        url: "https://www.youtube.com/watch?v=_6v1VMlkfrc",
        videoId: "_6v1VMlkfrc",
        viewCount: 33655
      },
      {
        content: "Working Full-Time and Still Can't Eat",
        platform: "youtube",
        level: 1,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=aBw582ctvOA",
        videoId: "aBw582ctvOA",
        viewCount: 495317
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
      "YouTube: 96 videos about wage stagnation and financial stress (7.3% crisis ratio)"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with social sentiment about financial stress (60% weight). Content categorized as Level 3 (working poor/homeless despite employment), Level 2 (living paycheck to paycheck), Level 1 (general awareness of wage issues).",
    lastUpdated: "December 17, 2025"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 50.88,
    label: "Multiple Organs Required",
    trend: "worsening",
    officialScore: 37.6,
    crisisRatio: 22.1,
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
        viewCount: 62827
      },
      {
        content: "YOU WILL NEVER OWN A HOME, AMERICANS HAVE LOST HOPE, THEY ILL EVER BE ABLE TO AFFORD TO BUY A HOMR",
        platform: "youtube",
        level: 3,
        date: "2025-12-07",
        url: "https://www.youtube.com/watch?v=BdN7wVBgd6Y",
        videoId: "BdN7wVBgd6Y",
        viewCount: 4061
      },
      {
        content: "The Housing Market Scam: Why You Will Never Own a Home 🏠📉",
        platform: "youtube",
        level: 3,
        date: "2025-11-27",
        url: "https://www.youtube.com/watch?v=GrF1MDQ-T0g",
        videoId: "GrF1MDQ-T0g",
        viewCount: 42
      },
      {
        content: "Why Nobody Can Afford a Home Anymore",
        platform: "youtube",
        level: 1,
        date: "2025-10-26",
        url: "https://www.youtube.com/watch?v=bqdPtjxzQaE",
        videoId: "bqdPtjxzQaE",
        viewCount: 397548
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
      "YouTube: 122 videos about housing crisis and homeownership despair (22.1% crisis ratio)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with social sentiment about housing crisis (60% weight). Content categorized as Level 3 (housing insecurity/homelessness/gave up on ownership), Level 2 (rent increases/struggling to afford), Level 1 (general housing concerns).",
    lastUpdated: "December 19, 2025"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 16.38,
    label: "Mild Turbulence",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 13.3,
    levelDistribution: {
      level1: 76,
      level2: 15,
      level3: 14,
      total: 105
    },
    sampleData: [
      {
        content: "Stranded For 10+ hours, Fliers Demand Action From Indigo Airlines For Cancelled Flights",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=rxXzYPDl5jc",
        videoId: "rxXzYPDl5jc"
      },
      {
        content: "I was stranded at the airport with my newborn baby, begging for help after my flight got...",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=-NJwQ_I1Y_4",
        videoId: "-NJwQ_I1Y_4"
      },
      {
        content: "Black Soldier Ignored At The Airport—Then The Flight Got Delayed For Him",
        platform: "youtube",
        level: 2,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=gzBWU8ICkOA",
        videoId: "gzBWU8ICkOA"
      },
      {
        content: "Flight Delays, Fees & Fights: Is Flying Getting Worse?",
        platform: "youtube",
        level: 1,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=X-ElLs6Xo-c",
        videoId: "X-ElLs6Xo-c"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 105,
        target: 160,
        percentage: 66
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
      "YouTube: 105 videos about airline chaos and travel nightmares (13.3% crisis ratio)"
    ],
    methodology: "Official delay/safety data (40% weight) combined with social sentiment about airline nightmares (60% weight). Content categorized as Level 3 (stranded for days/major disruption), Level 2 (delays/lost luggage), Level 1 (general complaints).",
    lastUpdated: "December 17, 2025"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 13.9,
    label: "Love May Actually Be Real",
    trend: "improving",
    officialScore: 8.5,
    crisisRatio: 17.5,
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
        videoId: "OdjIW8IdbIM"
      },
      {
        content: "Dating App Fatigue & Mental Health",
        platform: "youtube",
        level: 3,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=ygRO028UQUU",
        videoId: "ygRO028UQUU"
      },
      {
        content: "Dating Apps Are Exhausting: Here's What's Happening",
        platform: "youtube",
        level: 2,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=fLYKy51jIVc",
        videoId: "fLYKy51jIVc"
      },
      {
        content: "The Gen Z Dating Apocalypse",
        platform: "youtube",
        level: 1,
        date: "2025-12-17",
        url: "https://www.youtube.com/watch?v=dxxbcEGKs-c",
        videoId: "dxxbcEGKs-c"
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
      "YouTube: 114 videos about dating app burnout and despair (17.5% crisis ratio)"
    ],
    methodology: "Google Trends data (40% weight) combined with social sentiment analysis (60% weight). Content categorized as Level 3 (gave up/mental health impact), Level 2 (burnout/exhaustion), Level 1 (general frustration).",
    lastUpdated: "December 17, 2025"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 31.44,
    label: "Resume At The Ready",
    trend: "worsening",
    officialScore: 76.5,
    crisisRatio: 1.4,
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
        viewCount: 698
      },
      {
        content: "International students — 😓 200+ Job Applications, But No Response?",
        platform: "youtube",
        level: 2,
        date: "2025-10-17",
        url: "https://www.youtube.com/watch?v=Xe-dHYhBwVk",
        videoId: "Xe-dHYhBwVk",
        viewCount: 780
      },
      {
        content: "Unemployed @ 50 & was told I was overqualified",
        platform: "youtube",
        level: 2,
        date: "2025-09-26",
        url: "https://www.youtube.com/watch?v=4-UsaQaRiyA",
        videoId: "4-UsaQaRiyA",
        viewCount: 436
      },
      {
        content: "Why are Tech Layoffs Still Happening?",
        platform: "youtube",
        level: 1,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=XerzK0QNhnM",
        videoId: "XerzK0QNhnM",
        viewCount: 45923
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
      "YouTube: 74 videos about layoffs and job search struggles (1.4% crisis ratio)"
    ],
    methodology: "Official layoff numbers (40% weight) combined with social sentiment about job search struggles and layoff fear (60% weight). Content categorized as Level 3 (financial crisis/months unemployed), Level 2 (hundreds of applications/no response), Level 1 (general job market awareness).",
    lastUpdated: "December 17, 2025"
  }
};
