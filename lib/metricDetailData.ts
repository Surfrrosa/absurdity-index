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
    score: 43.77,
    label: "Prior Authorization Purgatory",
    trend: "neutral",
    officialScore: 56.30,
    crisisRatio: 41.82,
    levelDistribution: {
      level1: 799,
      level2: 120,
      level3: 57,
      total: 976
    },
    sampleData: [
      {
        content: "“They Called FDA-Approved Cancer Treatment ‘Experimental’… Then Denied It.”",
        platform: "youtube",
        level: 3,
        date: "2026-04-18",
        url: "https://www.youtube.com/watch?v=JioBoGBSHCg",
        videoId: "JioBoGBSHCg",
        viewCount: 162973,
        commentCount: 0
      },
      {
        content: "$97,000 for ONE Twin?! Insurance Split the Bill",
        platform: "youtube",
        level: 3,
        date: "2026-04-19",
        url: "https://www.youtube.com/watch?v=Vngx_ExMc-A",
        videoId: "Vngx_ExMc-A",
        viewCount: 67536,
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
        content: "Republican House Speaker PANICS Over Healthcare Nightmare As Shutdown Backlash Grows",
        platform: "tiktok",
        level: 3,
        date: "2025-10-17",
        url: "https://www.youtube.com/watch?v=u35OGnaKhi4",
        videoId: "u35OGnaKhi4",
        viewCount: 20739,
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
        current: 154,
        target: 200,
        percentage: 67
      },
      {
        platform: "TikTok",
        current: 87,
        target: 120,
        percentage: 72
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
      "Reddit: 154 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 87 videos via YouTube compilations",
      "CFPB: 100 complaints (medical debt, billing disputes)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Sources include YouTube, Reddit, TikTok, and CFPB consumer complaints. Content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement. Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "April 27, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 34.35,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "neutral",
    officialScore: 12.5,
    crisisRatio: 48.91,
    levelDistribution: {
      level1: 732,
      level2: 36,
      level3: 82,
      total: 850
    },
    sampleData: [
      {
        content: "Addicted To Her AI Boyfriend",
        platform: "youtube",
        level: 3,
        date: "2026-04-01",
        url: "https://www.youtube.com/watch?v=0WS68I6PY-4",
        videoId: "0WS68I6PY-4",
        viewCount: 3294118,
        commentCount: 0
      },
      {
        content: "Why people are falling in love with A.I. companions | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-05-04",
        url: "https://www.youtube.com/watch?v=_d08BZmdZu8",
        videoId: "_d08BZmdZu8",
        viewCount: 1929828,
        commentCount: 0
      },
      {
        content: "I would like to DEEPLY apologise for slandering the good name of character.ai",
        platform: "reddit",
        level: 1,
        date: "2026-03-24",
        url: "https://www.reddit.com/r/CharacterAI/comments/1s27qwk/i_would_like_to_deeply_apologise_for_slandering/"
      },
      {
        content: "RED ALERT: Tennessee is about to make building chatbots a Class A felony (15-25 years in prison).",
        platform: "reddit",
        level: 2,
        date: "2026-04-14",
        url: "https://www.reddit.com/r/artificial/comments/1slu23a/red_alert_tennessee_is_about_to_make_building/"
      },
      {
        content: "Trending chatgpt Prompts Photo Editing Prompts #shorts #viral #chatgpt #prompts",
        platform: "tiktok",
        level: 3,
        date: "2025-06-30",
        url: "https://www.youtube.com/watch?v=21EseaiPb38",
        videoId: "21EseaiPb38",
        viewCount: 6252900,
        commentCount: 0
      },
      {
        content: "Show HN: I built an AI companion to stop doomscrolling and regulate anxiety",
        platform: "hackernews",
        level: 2,
        date: "",
        url: "https://mynomie.com/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 132,
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
      "YouTube: 132 videos analyzing AI companion usage and addiction",
      "Reddit: 152 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 59 videos via YouTube compilations",
      "Hacker News: 119 stories about AI risks and companion addiction"
    ],
    methodology: "Systematic collection from multiple platforms including YouTube, Reddit, TikTok, and Hacker News. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official data (40% weight).",
    lastUpdated: "April 27, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 41.08,
    label: "Quarterly Purge Required",
    trend: "neutral",
    officialScore: 45.2,
    crisisRatio: 38.33,
    levelDistribution: {
      level1: 712,
      level2: 91,
      level3: 4,
      total: 807
    },
    sampleData: [
      {
        content: "Subscriptions Are Getting Out of Control",
        platform: "youtube",
        level: 2,
        date: "2026-01-31",
        url: "https://www.youtube.com/watch?v=jRcqJkW44Lc",
        videoId: "jRcqJkW44Lc",
        viewCount: 606047,
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
        content: "Covering electricity price increases from our data centers",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://www.anthropic.com/news/covering-electricity-price-increases"
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
        current: 138,
        target: 150,
        percentage: 92
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
      "Hacker News: 138 stories about subscription fatigue and pricing",
      "TikTok: 29 videos via YouTube compilations",
      "Reddit: 128 posts from r/Frugal, r/personalfinance, r/povertyfinance"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment from YouTube, Hacker News, TikTok, and Reddit (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "April 27, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 42.09,
    label: "Paycheck-to-Paycheck Normal",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 39.15,
    levelDistribution: {
      level1: 585,
      level2: 124,
      level3: 7,
      total: 716
    },
    sampleData: [
      {
        content: "Living Paycheck to Paycheck Be Like",
        platform: "youtube",
        level: 2,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=K5uRsKyyNHY",
        videoId: "K5uRsKyyNHY",
        viewCount: 119366,
        commentCount: 0
      },
      {
        content: "WARNING! The TRUTH About Living Paycheck To Paycheck",
        platform: "youtube",
        level: 2,
        date: "2026-03-09",
        url: "https://www.youtube.com/watch?v=TDELR2fLn8I",
        videoId: "TDELR2fLn8I",
        viewCount: 88454,
        commentCount: 0
      },
      {
        content: "No longer homeless.",
        platform: "reddit",
        level: 1,
        date: "2026-04-10",
        url: "https://www.reddit.com/r/povertyfinance/comments/1shf29z/no_longer_homeless/"
      },
      {
        content: "How to cope with poor parents",
        platform: "reddit",
        level: 3,
        date: "2026-04-10",
        url: "https://www.reddit.com/r/povertyfinance/comments/1shparv/how_to_cope_with_poor_parents/"
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
        current: 76,
        target: 100,
        percentage: 88
      },
      {
        platform: "Reddit",
        current: 228,
        target: 200,
        percentage: 39
      },
      {
        platform: "Hacker News",
        current: 27,
        target: 100,
        percentage: 27
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: CEO-to-worker pay ratio tracking",
      "YouTube: 76 videos about wage stagnation and financial stress",
      "Reddit: 228 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "Hacker News: 27 stories about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "April 27, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 48.74,
    label: "Multiple Organs Required",
    trend: "neutral",
    officialScore: 37.6,
    crisisRatio: 49.5,
    levelDistribution: {
      level1: 548,
      level2: 181,
      level3: 129,
      total: 858
    },
    sampleData: [
      {
        content: "How Homeless People Turn a Van Into a Comfortable Home",
        platform: "youtube",
        level: 3,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=aX7Tpu19QfU",
        videoId: "aX7Tpu19QfU",
        viewCount: 857856,
        commentCount: 0
      },
      {
        content: "The $20 Sleep Setup That Keeps Homeless Van Dwellers Warm All Winter",
        platform: "youtube",
        level: 3,
        date: "2026-02-24",
        url: "https://www.youtube.com/watch?v=b78Pmm73nVg",
        videoId: "b78Pmm73nVg",
        viewCount: 146052,
        commentCount: 0
      },
      {
        content: "First in my family to own a home. 27M Upstate NY 160k 5.25",
        platform: "reddit",
        level: 2,
        date: "2026-03-21",
        url: "https://www.reddit.com/r/FirstTimeHomeBuyer/comments/1s08pfu/first_in_my_family_to_own_a_home_27m_upstate_ny/"
      },
      {
        content: "Just won a housing lottery unit in NYC ($975 rent, but it increases yearly) — I make ~$785/week afte",
        platform: "reddit",
        level: 1,
        date: "2026-03-24",
        url: "https://www.reddit.com/r/povertyfinance/comments/1s2lv64/just_won_a_housing_lottery_unit_in_nyc_975_rent/"
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
        current: 113,
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
        current: 75,
        target: 120,
        percentage: 62
      }
    ],
    dataSources: [
      "Redfin: Median home price tracking",
      "Zillow Rent Index: National median rent trends",
      "Census Bureau: Rent burden data by generation",
      "YouTube: 113 videos about housing crisis and homeownership despair",
      "Reddit: 176 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "Hacker News: 75 stories about housing affordability crisis",
      "CFPB: 100 complaints (mortgages, housing finance)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, Hacker News, and CFPB complaints (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "April 27, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 44.03,
    label: "Expect Delays",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 59.38,
    levelDistribution: {
      level1: 251,
      level2: 240,
      level3: 99,
      total: 590
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
        content: "Flight Chaos: AI Can't Solve Our Family Travel Nightmare! #shorts",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=IheEmuwnzRI",
        videoId: "IheEmuwnzRI",
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
        content: "Delta-",
        platform: "reddit",
        level: 1,
        date: "2026-04-06",
        url: "https://www.reddit.com/r/delta/comments/1sehdod/delta/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 89,
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
      "YouTube: 89 videos about airline chaos and travel nightmares",
      "Reddit: 107 posts from r/travel, r/flights, r/delta, r/americanairlines"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "April 27, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 28.16,
    label: "Swipe Fatigue Setting In",
    trend: "neutral",
    officialScore: 8.5,
    crisisRatio: 41.27,
    levelDistribution: {
      level1: 335,
      level2: 127,
      level3: 13,
      total: 475
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
        content: "why i quit dating apps",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=SpUJUnKN7As",
        videoId: "SpUJUnKN7As",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "Did I match with someone completely insane?",
        platform: "reddit",
        level: 1,
        date: "2026-03-25",
        url: "https://www.reddit.com/r/Tinder/comments/1s30cr3/did_i_match_with_someone_completely_insane/"
      },
      {
        content: "She likes me. I like her. I swipe right. No match. What gives?",
        platform: "reddit",
        level: 1,
        date: "2026-03-20",
        url: "https://www.reddit.com/r/Tinder/comments/1rz07mq/she_likes_me_i_like_her_i_swipe_right_no_match/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 103,
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
      "YouTube: 103 videos about dating app burnout and despair",
      "Reddit: 164 posts from r/dating, r/Tinder, r/Bumble"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "April 27, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 39.43,
    label: "Resume At The Ready",
    trend: "neutral",
    officialScore: 76.5,
    crisisRatio: 46.79,
    levelDistribution: {
      level1: 493,
      level2: 270,
      level3: 13,
      total: 776
    },
    sampleData: [
      {
        content: "The Job Market is Officially Broken in 2026",
        platform: "youtube",
        level: 2,
        date: "2026-03-23",
        url: "https://www.youtube.com/watch?v=MFzuybsykKI",
        videoId: "MFzuybsykKI",
        viewCount: 5355,
        commentCount: 0
      },
      {
        content: "Job Hunting & Job Interviews Have Become A NIGHTMARE- Looking For Work Has Become A Game Of WIPE",
        platform: "youtube",
        level: 2,
        date: "2026-03-19",
        url: "https://www.youtube.com/watch?v=T2KLEGmGzBk",
        videoId: "T2KLEGmGzBk",
        viewCount: 960,
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
        content: "Ask HN: How are you dealing with anxiety with layoffs?",
        platform: "hackernews",
        level: 2,
        date: "",
        url: "https://news.ycombinator.com/item?id=46848912"
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
        current: 305,
        target: 300,
        percentage: 94
      },
      {
        platform: "Hacker News",
        current: 147,
        target: 150,
        percentage: 98
      }
    ],
    dataSources: [
      "Layoffs.fyi: Tech layoff tracking data",
      "YouTube: 62 videos about layoffs and job search struggles",
      "Reddit: 305 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "Hacker News: 147 stories about tech layoffs and job market"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "April 27, 2026"
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
