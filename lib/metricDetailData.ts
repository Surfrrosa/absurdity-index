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
    score: 44.22,
    label: "Prior Authorization Purgatory",
    trend: "neutral",
    officialScore: 56.30,
    crisisRatio: 42.56,
    levelDistribution: {
      level1: 790,
      level2: 114,
      level3: 65,
      total: 971
    },
    sampleData: [
      {
        content: "Insurance Denied a Life-Saving Transplant—A seven-year-old child Died Waiting",
        platform: "youtube",
        level: 3,
        date: "2026-05-01",
        url: "https://www.youtube.com/watch?v=Cn1SN0RA5Ug",
        videoId: "Cn1SN0RA5Ug",
        viewCount: 247164,
        commentCount: 0
      },
      {
        content: "$97,000 for ONE Twin?! Insurance Split the Bill",
        platform: "youtube",
        level: 3,
        date: "2026-04-19",
        url: "https://www.youtube.com/watch?v=Vngx_ExMc-A",
        videoId: "Vngx_ExMc-A",
        viewCount: 96503,
        commentCount: 0
      },
      {
        content: "Medicare Advantage is a Scam: My experience almost a decade in the Healthcare industry",
        platform: "reddit",
        level: 1,
        date: "2026-04-14",
        url: "https://www.reddit.com/r/HealthInsurance/comments/1sl2x0z/medicare_advantage_is_a_scam_my_experience_almost/"
      },
      {
        content: "Insurance won't cover accident due to Undisclosed Household Member",
        platform: "reddit",
        level: 2,
        date: "2026-04-10",
        url: "https://www.reddit.com/r/Insurance/comments/1si0dz2/insurance_wont_cover_accident_due_to_undisclosed/"
      },
      {
        content: "Health Insurance is a Nightmare",
        platform: "tiktok",
        level: 3,
        date: "2024-03-11",
        url: "https://www.youtube.com/watch?v=-lgzaL1zans",
        videoId: "-lgzaL1zans",
        viewCount: 195045,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 150,
        target: 160,
        percentage: 100
      },
      {
        platform: "Reddit",
        current: 150,
        target: 200,
        percentage: 67
      },
      {
        platform: "TikTok",
        current: 86,
        target: 120,
        percentage: 71
      },
      {
        platform: "CFPB",
        current: 100,
        target: 120,
        percentage: 83
      }
    ],
    dataSources: [
      "KFF (Kaiser Family Foundation): Premium increase data, coverage statistics, uninsured rate",
      "U.S. Census Bureau: Medical debt and bankruptcy statistics",
      "JAMA Network: Claim denial rates and prior authorization burden research",
      "YouTube: 150 videos analyzing healthcare system failures",
      "Reddit: 150 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 86 videos via YouTube compilations",
      "CFPB: 100 complaints (medical debt, billing disputes)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Sources include YouTube, Reddit, TikTok, and CFPB consumer complaints. Content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement. Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "May 4, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 33.41,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "neutral",
    officialScore: 12.5,
    crisisRatio: 47.34,
    levelDistribution: {
      level1: 743,
      level2: 36,
      level3: 72,
      total: 851
    },
    sampleData: [
      {
        content: "Addicted To Her AI Boyfriend",
        platform: "youtube",
        level: 3,
        date: "2026-04-01",
        url: "https://www.youtube.com/watch?v=0WS68I6PY-4",
        videoId: "0WS68I6PY-4",
        viewCount: 3389839,
        commentCount: 0
      },
      {
        content: "Why people are falling in love with A.I. companions | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-05-04",
        url: "https://www.youtube.com/watch?v=_d08BZmdZu8",
        videoId: "_d08BZmdZu8",
        viewCount: 1965206,
        commentCount: 0
      },
      {
        content: "i started talking to Claude like a caveman. my credits lasted 3x longer. i'm not joking.",
        platform: "reddit",
        level: 1,
        date: "2026-04-23",
        url: "https://www.reddit.com/r/ChatGPT/comments/1stdot6/i_started_talking_to_claude_like_a_caveman_my/"
      },
      {
        content: "RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison).",
        platform: "reddit",
        level: 2,
        date: "2026-04-14",
        url: "https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/"
      },
      {
        content: "Ask HN: Have top AI research institutions just given up on the idea of safety?",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://news.ycombinator.com/item?id=47152355"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 134,
        target: 160,
        percentage: 84
      },
      {
        platform: "Reddit",
        current: 152,
        target: 290,
        percentage: 100
      },
      {
        platform: "TikTok",
        current: 59,
        target: 120,
        percentage: 49
      },
      {
        platform: "Hacker News",
        current: 119,
        target: 150,
        percentage: 79
      }
    ],
    dataSources: [
      "YouTube: 134 videos analyzing AI companion usage and addiction",
      "Reddit: 152 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 59 videos via YouTube compilations",
      "Hacker News: 119 stories about AI risks and companion addiction"
    ],
    methodology: "Systematic collection from multiple platforms including YouTube, Reddit, TikTok, and Hacker News. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official data (40% weight).",
    lastUpdated: "May 4, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 40.3,
    label: "Quarterly Purge Required",
    trend: "neutral",
    officialScore: 45.2,
    crisisRatio: 37.03,
    levelDistribution: {
      level1: 725,
      level2: 73,
      level3: 4,
      total: 802
    },
    sampleData: [
      {
        content: "The Subscription Trap Keeps Getting Worse",
        platform: "youtube",
        level: 2,
        date: "2026-04-14",
        url: "https://www.youtube.com/watch?v=A3VPOXtADyQ",
        videoId: "A3VPOXtADyQ",
        viewCount: 236,
        commentCount: 0
      },
      {
        content: "What is a monthly subscription/service you ACTUALLY consider worth paying for?",
        platform: "reddit",
        level: 1,
        date: "2026-02-20",
        url: "https://www.reddit.com/r/Frugal/comments/1radc5q/what_is_a_monthly_subscriptionservice_you/"
      },
      {
        content: "Cancel the subscriptions you like, too",
        platform: "reddit",
        level: 1,
        date: "2026-03-19",
        url: "https://www.reddit.com/r/Frugal/comments/1ryfsu7/cancel_the_subscriptions_you_like_too/"
      },
      {
        content: "Maryland to ban A.I.-driven price increases in grocery stores",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://www.nytimes.com/2026/05/01/business/surveillance-pricing-groceries-maryland.html"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 150,
        target: 160,
        percentage: 100
      },
      {
        platform: "Hacker News",
        current: 133,
        target: 150,
        percentage: 88
      },
      {
        platform: "TikTok",
        current: 29,
        target: 120,
        percentage: 24
      },
      {
        platform: "Reddit",
        current: 128,
        target: 200,
        percentage: 6
      }
    ],
    dataSources: [
      "Consumer Reports: Average subscriptions per household, spending trends",
      "Streaming service pricing data: All major platforms tracked",
      "Industry reports: Annual subscription price increase trends",
      "YouTube: 150 videos analyzing subscription fatigue",
      "Hacker News: 133 stories about subscription fatigue and pricing",
      "TikTok: 29 videos via YouTube compilations",
      "Reddit: 128 posts from r/Frugal, r/personalfinance, r/povertyfinance"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment from YouTube, Hacker News, TikTok, and Reddit (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "May 4, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 42.51,
    label: "Paycheck-to-Paycheck Normal",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 39.85,
    levelDistribution: {
      level1: 572,
      level2: 129,
      level3: 10,
      total: 711
    },
    sampleData: [
      {
        content: "Woman says most people are living paycheck to paycheck, and being evicted, homeless is expensive",
        platform: "youtube",
        level: 3,
        date: "2026-05-02",
        url: "https://www.youtube.com/watch?v=G0xvoxprVuw",
        videoId: "G0xvoxprVuw",
        viewCount: 33752,
        commentCount: 0
      },
      {
        content: "40% of Americans Can’t Afford Rent — The Middle Class Collapse Fueling RV Homelessness (2026)",
        platform: "youtube",
        level: 3,
        date: "2026-02-17",
        url: "https://www.youtube.com/watch?v=eSly44yD8lU",
        videoId: "eSly44yD8lU",
        viewCount: 5712,
        commentCount: 0
      },
      {
        content: "The recruiter called my salary expectations \"cute.\" I ended the Zoom call right there. Did I overrea",
        platform: "reddit",
        level: 1,
        date: "2026-04-21",
        url: "https://www.reddit.com/r/jobs/comments/1sroszd/the_recruiter_called_my_salary_expectations_cute/"
      },
      {
        content: "Hard on the Poor Soft on the Rich",
        platform: "reddit",
        level: 1,
        date: "2026-04-12",
        url: "https://www.reddit.com/r/antiwork/comments/1sja0nn/hard_on_the_poor_soft_on_the_rich/"
      },
      {
        content: "Cory Doctorow on the High Cost of Living with the Ultra-Rich",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://www.newyorker.com/books/book-currents/cory-doctorow-on-the-high-cost-of-living-with-the-ultra-rich"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 77,
        target: 100,
        percentage: 88
      },
      {
        platform: "Reddit",
        current: 223,
        target: 200,
        percentage: 39
      },
      {
        platform: "Hacker News",
        current: 32,
        target: 100,
        percentage: 32
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: CEO-to-worker pay ratio tracking",
      "YouTube: 77 videos about wage stagnation and financial stress",
      "Reddit: 223 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "Hacker News: 32 stories about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "May 4, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 47.61,
    label: "Multiple Organs Required",
    trend: "neutral",
    officialScore: 37.6,
    crisisRatio: 47.61,
    levelDistribution: {
      level1: 573,
      level2: 168,
      level3: 122,
      total: 863
    },
    sampleData: [
      {
        content: "The $20 Sleep Setup That Keeps Homeless Van Dwellers Warm All Winter",
        platform: "youtube",
        level: 3,
        date: "2026-02-24",
        url: "https://www.youtube.com/watch?v=b78Pmm73nVg",
        videoId: "b78Pmm73nVg",
        viewCount: 146319,
        commentCount: 0
      },
      {
        content: "Young People Will Never Own a Home",
        platform: "youtube",
        level: 3,
        date: "2026-05-03",
        url: "https://www.youtube.com/watch?v=87FyEW8x_B0",
        videoId: "87FyEW8x_B0",
        viewCount: 138776,
        commentCount: 0
      },
      {
        content: "Housing crisis pending",
        platform: "reddit",
        level: 1,
        date: "2026-04-13",
        url: "https://www.reddit.com/r/LateStageCapitalism/comments/1skszm8/housing_crisis_pending/"
      },
      {
        content: "Want to buy a house? Get a boyfriend.",
        platform: "reddit",
        level: 1,
        date: "2026-04-16",
        url: "https://www.reddit.com/r/povertyfinance/comments/1sn9kjj/want_to_buy_a_house_get_a_boyfriend/"
      },
      {
        content: "'Can't sell house' searches are higher now than during the 2008 housing crisis",
        platform: "hackernews",
        level: 3,
        date: "",
        url: "https://www.morningstar.com/news/marketwatch/20260228147/cant-sell-house-searches-are-higher-now-than-during-the-2008-housing-crisis"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 114,
        target: 160,
        percentage: 86
      },
      {
        platform: "Reddit",
        current: 176,
        target: 200,
        percentage: 93
      },
      {
        platform: "CFPB",
        current: 100,
        target: 120,
        percentage: 83
      },
      {
        platform: "Hacker News",
        current: 80,
        target: 120,
        percentage: 66
      }
    ],
    dataSources: [
      "Redfin: Median home price tracking",
      "Zillow Rent Index: National median rent trends",
      "Census Bureau: Rent burden data by generation",
      "YouTube: 114 videos about housing crisis and homeownership despair",
      "Reddit: 176 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "Hacker News: 80 stories about housing affordability crisis",
      "CFPB: 100 complaints (mortgages, housing finance)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, Hacker News, and CFPB complaints (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "May 4, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 43.68,
    label: "Expect Delays",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 58.79,
    levelDistribution: {
      level1: 248,
      level2: 235,
      level3: 102,
      total: 585
    },
    sampleData: [
      {
        content: "Frustration grows at Hartsfield-Jackson amid flight cancellations, delay",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=5Q3jMGUm8Xw",
        videoId: "5Q3jMGUm8Xw",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "Strikes in Iran lead to Middle East AIRPORT CLOSURES, leaving AMERICANS stranded",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=qldByQOIpCI",
        videoId: "qldByQOIpCI",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "A cancelled flight changed my mind about Istanbul",
        platform: "reddit",
        level: 1,
        date: "2026-04-19",
        url: "https://www.reddit.com/r/travel/comments/1sq0p2m/a_cancelled_flight_changed_my_mind_about_istanbul/"
      },
      {
        content: "Jordan Travel",
        platform: "reddit",
        level: 1,
        date: "2026-04-11",
        url: "https://www.reddit.com/r/travel/comments/1siesc4/jordan_travel/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 87,
        target: 160,
        percentage: 61
      },
      {
        platform: "Reddit",
        current: 107,
        target: 200,
        percentage: 66
      }
    ],
    dataSources: [
      "Bureau of Transportation Statistics: Flight delay and cancellation rates",
      "ACSI satisfaction scores: Airline service quality tracking",
      "FAA safety incident data: Emergency landings, equipment failures",
      "YouTube: 87 videos about airline chaos and travel nightmares",
      "Reddit: 107 posts from r/travel, r/flights, r/delta, r/americanairlines"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "May 4, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 28.18,
    label: "Swipe Fatigue Setting In",
    trend: "neutral",
    officialScore: 8.5,
    crisisRatio: 41.3,
    levelDistribution: {
      level1: 336,
      level2: 128,
      level3: 13,
      total: 477
    },
    sampleData: [
      {
        content: "People Are Finally Quitting Dating Apps",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=XW2vA0DGXuc",
        videoId: "XW2vA0DGXuc",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "80% of Men Quit Dating Apps… Now Women Are Panicking — “They Stopped Approaching Now This”",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=N6454XfxtrI",
        videoId: "N6454XfxtrI",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "How I cracked the dating app algorithm (A strategy for average guys)",
        platform: "reddit",
        level: 1,
        date: "2026-04-24",
        url: "https://www.reddit.com/r/dating_advice/comments/1suanax/how_i_cracked_the_dating_app_algorithm_a_strategy/"
      },
      {
        content: "Your person is so close, I promise you. This is your sign not to give up on love.",
        platform: "reddit",
        level: 1,
        date: "2026-04-18",
        url: "https://www.reddit.com/r/dating/comments/1spb0ev/your_person_is_so_close_i_promise_you_this_is/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 106,
        target: 160,
        percentage: 82
      },
      {
        platform: "Reddit",
        current: 164,
        target: 200,
        percentage: 70
      }
    ],
    dataSources: [
      "Pew Research: Dating app frustration and burnout survey data",
      "YouTube: 106 videos about dating app burnout and despair",
      "Reddit: 164 posts from r/dating, r/Tinder, r/Bumble"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "May 4, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 35.76,
    label: "Resume At The Ready",
    trend: "improving",
    officialScore: 76.5,
    crisisRatio: 47.01,
    levelDistribution: {
      level1: 498,
      level2: 265,
      level3: 14,
      total: 777
    },
    sampleData: [
      {
        content: "The Job Market is Officially Broken in 2026",
        platform: "youtube",
        level: 2,
        date: "2026-03-23",
        url: "https://www.youtube.com/watch?v=MFzuybsykKI",
        videoId: "MFzuybsykKI",
        viewCount: 5488,
        commentCount: 0
      },
      {
        content: "Job Hunting & Job Interviews Have Become A NIGHTMARE- Looking For Work Has Become A Game Of WIPE",
        platform: "youtube",
        level: 2,
        date: "2026-03-19",
        url: "https://www.youtube.com/watch?v=T2KLEGmGzBk",
        videoId: "T2KLEGmGzBk",
        viewCount: 974,
        commentCount: 0
      },
      {
        content: "Recruiter treated me like shit. 3 months later, karma had a full circle moment.",
        platform: "reddit",
        level: 1,
        date: "2026-04-09",
        url: "https://www.reddit.com/r/recruitinghell/comments/1sgfdi3/recruiter_treated_me_like_shit_3_months_later/"
      },
      {
        content: "Dying man loses life insurance due to layoff",
        platform: "reddit",
        level: 1,
        date: "2026-03-29",
        url: "https://www.reddit.com/r/Layoffs/comments/1s6veca/dying_man_loses_life_insurance_due_to_layoff/"
      },
      {
        content: "2026 tech layoffs reach 45,000 in March",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://technode.global/2026/03/09/2026-tech-layoffs-reach-45000-in-march-more-than-9200-due-to-ai-and-automation-rationalfx/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 62,
        target: 100,
        percentage: 74
      },
      {
        platform: "Reddit",
        current: 304,
        target: 300,
        percentage: 94
      },
      {
        platform: "Hacker News",
        current: 150,
        target: 150,
        percentage: 100
      }
    ],
    dataSources: [
      "Layoffs.fyi: Tech layoff tracking data",
      "YouTube: 62 videos about layoffs and job search struggles",
      "Reddit: 304 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "Hacker News: 150 stories about tech layoffs and job market"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "May 4, 2026"
  }
};

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

/**
 * Calculate the Overall Absurdity Score
 * Equal-weight average of all metric final scores
 */
export function calculateOverallScore(): number {
  const metrics = Object.values(metricDetails);
  const scores = metrics.map(m => m.score);
  const sum = scores.reduce((a, b) => a + b, 0);
  return sum / scores.length;
}

/**
 * Get the dynamic label for the overall absurdity score
 */
export function getOverallLabel(score: number): string {
  if (score < 20) return "SURPRISINGLY FUNCTIONAL";
  if (score < 30) return "MINOR TURBULENCE";
  if (score < 40) return "FLYING TOO CLOSE TO THE SUN";
  if (score < 50) return "ICARUS HAS ENTERED THE CHAT";
  if (score < 60) return "THE WHEELS ARE COMING OFF";
  if (score < 70) return "ACTIVELY ON FIRE";
  if (score < 80) return "WE'VE REACHED PEAK CIVILIZATION";
  if (score < 90) return "REALITY.EXE HAS STOPPED WORKING";
  return "THE GODS ARE LAUGHING AT US";
}

/**
 * Get the most recent lastUpdated date from all metrics
 * Returns formatted string like "JAN 2026"
 */
export function getLatestUpdateDate(): string {
  const metrics = Object.values(metricDetails);

  // Parse dates and find the most recent
  const dates = metrics.map(m => {
    const parsed = new Date(m.lastUpdated);
    return isNaN(parsed.getTime()) ? new Date(0) : parsed;
  });

  const latestDate = new Date(Math.max(...dates.map(d => d.getTime())));

  // Format as "JAN 2026"
  const month = latestDate.toLocaleString('en-US', { month: 'short' }).toUpperCase();
  const year = latestDate.getFullYear();

  return `${month} ${year}`;
}
