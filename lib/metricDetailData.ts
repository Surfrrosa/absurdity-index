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
    score: 44.35,
    label: "Prior Authorization Purgatory",
    trend: "neutral",
    officialScore: 56.30,
    crisisRatio: 44.85,
    levelDistribution: {
      level1: 360,
      level2: 63,
      level3: 46,
      total: 469
    },
    sampleData: [
      {
        content: "7 Years In Bankruptcy: What Went Wrong? | On The Red Dot",
        platform: "youtube",
        level: 3,
        date: "2026-03-03",
        url: "https://www.youtube.com/watch?v=V5BPOKtssgQ",
        videoId: "V5BPOKtssgQ",
        viewCount: 146734,
        commentCount: 0
      },
      {
        content: "Insurance Denied a Life-Saving Stroke Treatment… for “Cost Optimization”",
        platform: "youtube",
        level: 3,
        date: "2026-02-24",
        url: "https://www.youtube.com/watch?v=WUujzQ_jMI8",
        videoId: "WUujzQ_jMI8",
        viewCount: 50126,
        commentCount: 0
      },
      {
        content: "Denied $11,000 ER claim for \"Panic Disorder\" when I thought I was having a heart attack. I’m terrifi",
        platform: "reddit",
        level: 2,
        date: "2026-03-14",
        url: "https://www.reddit.com/r/HealthInsurance/comments/1rtatb6/denied_11000_er_claim_for_panic_disorder_when_i/"
      },
      {
        content: "Anthem denied a 2-day ER admission after my wife lost consciousness — \"not medically necessary\"",
        platform: "reddit",
        level: 1,
        date: "2026-03-08",
        url: "https://www.reddit.com/r/HealthInsurance/comments/1roeq1f/anthem_denied_a_2day_er_admission_after_my_wife/"
      },
      {
        content: "Health Insurance is a Nightmare",
        platform: "tiktok",
        level: 3,
        date: "2024-03-11",
        url: "https://www.youtube.com/watch?v=-lgzaL1zans",
        videoId: "-lgzaL1zans",
        viewCount: 194901,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 158,
        target: 160,
        percentage: 100
      },
      {
        platform: "Reddit",
        current: 127,
        target: 200,
        percentage: 67
      },
      {
        platform: "TikTok",
        current: 84,
        target: 120,
        percentage: 70
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
      "YouTube: 158 videos analyzing healthcare system failures",
      "Reddit: 127 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 84 videos via YouTube compilations",
      "CFPB: 100 complaints (medical debt, billing disputes)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Sources include YouTube, Reddit, TikTok, and CFPB consumer complaints. Content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement. Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "March 23, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 35.55,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "improving",
    officialScore: 12.5,
    crisisRatio: 50.91,
    levelDistribution: {
      level1: 390,
      level2: 31,
      level3: 87,
      total: 508
    },
    sampleData: [
      {
        content: "Why people are falling in love with A.I. companions | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-05-04",
        url: "https://www.youtube.com/watch?v=_d08BZmdZu8",
        videoId: "_d08BZmdZu8",
        viewCount: 1808466,
        commentCount: 0
      },
      {
        content: "Grieving mum speaks out about teen son falling in love with an AI bot | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-12-07",
        url: "https://www.youtube.com/watch?v=yz4zfBnHksU",
        videoId: "yz4zfBnHksU",
        viewCount: 1020613,
        commentCount: 0
      },
      {
        content: "Time to cancel ChatGPT Plus after three Years. Anthropic got nuked for having ethics, and Sam Altman",
        platform: "reddit",
        level: 1,
        date: "2026-02-28",
        url: "https://www.reddit.com/r/ChatGPT/comments/1rgv7jx/time_to_cancel_chatgpt_plus_after_three_years/"
      },
      {
        content: "PEOPLE OF CHARACTER AI I COME WITH YOU WITH A STRAIGHT ANSWER ABT ADS IN CHAT. FINAL ANSWER IT’S A B",
        platform: "reddit",
        level: 1,
        date: "2026-02-26",
        url: "https://www.reddit.com/r/CharacterAI/comments/1rftiwb/people_of_character_ai_i_come_with_you_with_a/"
      },
      {
        content: "Trending chatgpt Prompts Photo Editing Prompts #shorts #viral #chatgpt #prompts",
        platform: "tiktok",
        level: 3,
        date: "2025-06-30",
        url: "https://www.youtube.com/watch?v=21EseaiPb38",
        videoId: "21EseaiPb38",
        viewCount: 5952625,
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
        current: 141,
        target: 160,
        percentage: 84
      },
      {
        platform: "Reddit",
        current: 145,
        target: 290,
        percentage: 100
      },
      {
        platform: "TikTok",
        current: 98,
        target: 120,
        percentage: 81
      },
      {
        platform: "Hacker News",
        current: 124,
        target: 150,
        percentage: 82
      }
    ],
    dataSources: [
      "YouTube: 141 videos analyzing AI companion usage and addiction",
      "Reddit: 145 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 98 videos via YouTube compilations",
      "Hacker News: 124 stories about AI risks and companion addiction"
    ],
    methodology: "Systematic collection from multiple platforms including YouTube, Reddit, TikTok, and Hacker News. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official data (40% weight).",
    lastUpdated: "March 23, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 40.29,
    label: "Quarterly Purge Required",
    trend: "neutral",
    officialScore: 45.2,
    crisisRatio: 37.02,
    levelDistribution: {
      level1: 396,
      level2: 24,
      level3: 4,
      total: 424
    },
    sampleData: [
      {
        content: "Subscriptions Are Getting Out of Control",
        platform: "youtube",
        level: 2,
        date: "2026-01-31",
        url: "https://www.youtube.com/watch?v=jRcqJkW44Lc",
        videoId: "jRcqJkW44Lc",
        viewCount: 588964,
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
        current: 160,
        target: 160,
        percentage: 100
      },
      {
        platform: "Hacker News",
        current: 136,
        target: 150,
        percentage: 90
      },
      {
        platform: "TikTok",
        current: 4,
        target: 120,
        percentage: 3
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
      "YouTube: 160 videos analyzing subscription fatigue",
      "Hacker News: 136 stories about subscription fatigue and pricing",
      "TikTok: 4 videos via YouTube compilations",
      "Reddit: 128 posts from r/Frugal, r/personalfinance, r/povertyfinance"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment from YouTube, Hacker News, TikTok, and Reddit (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "March 23, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 34.41,
    label: "Paycheck-to-Paycheck Normal",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 38.09,
    levelDistribution: {
      level1: 295,
      level2: 44,
      level3: 5,
      total: 344
    },
    sampleData: [
      {
        content: "How Homeless People Eat Three Meals A Day Without Spending Money",
        platform: "youtube",
        level: 3,
        date: "2026-03-18",
        url: "https://www.youtube.com/watch?v=LG_HDsvJ7uM",
        videoId: "LG_HDsvJ7uM",
        viewCount: 10086,
        commentCount: 0
      },
      {
        content: "Why Americans Are Working 3 Jobs and Still Poor",
        platform: "youtube",
        level: 3,
        date: "2026-01-11",
        url: "https://www.youtube.com/watch?v=bOopXHk6nT8",
        videoId: "bOopXHk6nT8",
        viewCount: 189,
        commentCount: 0
      },
      {
        content: "Trump’s shutdown now hurting workers with 'paycheck-to-paycheck' jobs",
        platform: "reddit",
        level: 1,
        date: "2026-03-13",
        url: "https://www.reddit.com/r/antiwork/comments/1rssdp5/trumps_shutdown_now_hurting_workers_with/"
      },
      {
        content: "Apparently some customer(s) found my jacket offensive, so I'm no longer allowed to wear it.",
        platform: "reddit",
        level: 1,
        date: "2026-03-19",
        url: "https://www.reddit.com/r/antiwork/comments/1rxs4dj/apparently_some_customers_found_my_jacket/"
      },
      {
        content: "Built a 1.3M-line agent-native OS in Rust while homeless. What now?",
        platform: "hackernews",
        level: 3,
        date: "",
        url: "https://news.ycombinator.com/item?id=47388478"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 93,
        target: 100,
        percentage: 88
      },
      {
        platform: "Reddit",
        current: 217,
        target: 200,
        percentage: 39
      },
      {
        platform: "Hacker News",
        current: 34,
        target: 100,
        percentage: 34
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: CEO-to-worker pay ratio tracking",
      "YouTube: 93 videos about wage stagnation and financial stress",
      "Reddit: 217 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "Hacker News: 34 stories about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 23, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 47.81,
    label: "Multiple Organs Required",
    trend: "neutral",
    officialScore: 37.6,
    crisisRatio: 47.95,
    levelDistribution: {
      level1: 368,
      level2: 60,
      level3: 58,
      total: 486
    },
    sampleData: [
      {
        content: "How Homeless People Sleep In A Car Without Heating",
        platform: "youtube",
        level: 3,
        date: "2026-01-17",
        url: "https://www.youtube.com/watch?v=awmWY5q1U1A",
        videoId: "awmWY5q1U1A",
        viewCount: 1539337,
        commentCount: 0
      },
      {
        content: "How Homeless People Turn a Van Into a Comfortable Home",
        platform: "youtube",
        level: 3,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=aX7Tpu19QfU",
        videoId: "aX7Tpu19QfU",
        viewCount: 837864,
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
        content: "My landlord is selling. Does he have any benefit of selling to me at a discount?",
        platform: "reddit",
        level: 1,
        date: "2026-03-20",
        url: "https://www.reddit.com/r/personalfinance/comments/1rz2not/my_landlord_is_selling_does_he_have_any_benefit/"
      },
      {
        content: "\"I Can't Afford My Mortgage\" Out Of Touch Influencers Are AT IT Again",
        platform: "tiktok",
        level: 3,
        date: "2025-10-31",
        url: "https://www.youtube.com/watch?v=j6wAu18vzvI",
        videoId: "j6wAu18vzvI",
        viewCount: 240584,
        commentCount: 0
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
        current: 108,
        target: 160,
        percentage: 86
      },
      {
        platform: "Reddit",
        current: 177,
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
        current: 86,
        target: 120,
        percentage: 71
      }
    ],
    dataSources: [
      "Redfin: Median home price tracking",
      "Zillow Rent Index: National median rent trends",
      "Census Bureau: Rent burden data by generation",
      "YouTube: 108 videos about housing crisis and homeownership despair",
      "Reddit: 177 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "Hacker News: 86 stories about housing affordability crisis",
      "CFPB: 100 complaints (mortgages, housing finance)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, Hacker News, and CFPB complaints (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 23, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 35.38,
    label: "Expect Delays",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 44.97,
    levelDistribution: {
      level1: 191,
      level2: 77,
      level3: 19,
      total: 287
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
        content: "Do not travel alone through Cairo Airport for a connecting flight",
        platform: "reddit",
        level: 1,
        date: "2026-03-14",
        url: "https://www.reddit.com/r/Flights/comments/1rtcy3l/do_not_travel_alone_through_cairo_airport_for_a/"
      },
      {
        content: "Friend cancelled last minute on a 100 day trip",
        platform: "reddit",
        level: 1,
        date: "2026-03-06",
        url: "https://www.reddit.com/r/travel/comments/1rmzfvs/friend_cancelled_last_minute_on_a_100_day_trip/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 105,
        target: 160,
        percentage: 61
      },
      {
        platform: "Reddit",
        current: 182,
        target: 200,
        percentage: 66
      }
    ],
    dataSources: [
      "Bureau of Transportation Statistics: Flight delay and cancellation rates",
      "ACSI satisfaction scores: Airline service quality tracking",
      "FAA safety incident data: Emergency landings, equipment failures",
      "YouTube: 105 videos about airline chaos and travel nightmares",
      "Reddit: 182 posts from r/travel, r/flights, r/delta, r/americanairlines"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 23, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 28.37,
    label: "Swipe Fatigue Setting In",
    trend: "neutral",
    officialScore: 8.5,
    crisisRatio: 41.62,
    levelDistribution: {
      level1: 223,
      level2: 47,
      level3: 15,
      total: 285
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
        content: "When You Quit All Dating Apps",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=Pl7FZr8AVgQ",
        videoId: "Pl7FZr8AVgQ",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "I don’t understand Muslim guys on dating apps",
        platform: "reddit",
        level: 1,
        date: "2026-03-09",
        url: "https://www.reddit.com/r/Bumble/comments/1rp1vuy/i_dont_understand_muslim_guys_on_dating_apps/"
      },
      {
        content: "She likes me. I like her. I swipe right. No match. What gives?",
        platform: "reddit",
        level: 1,
        date: "2026-03-20",
        url: "https://www.reddit.com/r/Tinder/comments/1rz07mq/she_likes_me_i_like_her_i_swipe_right_no_match/"
      },
      {
        content: "TikTok's Most INSANE Dating Account - Molly Rutter",
        platform: "tiktok",
        level: 3,
        date: "2024-11-19",
        url: "https://www.youtube.com/watch?v=c4QmlwM232Q",
        videoId: "c4QmlwM232Q",
        viewCount: 919037,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 100,
        target: 160,
        percentage: 82
      },
      {
        platform: "Reddit",
        current: 170,
        target: 200,
        percentage: 70
      }
    ],
    dataSources: [
      "Pew Research: Dating app frustration and burnout survey data",
      "YouTube: 100 videos about dating app burnout and despair",
      "Reddit: 170 posts from r/dating, r/Tinder, r/Bumble"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 23, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 36.89,
    label: "Resume At The Ready",
    trend: "neutral",
    officialScore: 76.5,
    crisisRatio: 46.14,
    levelDistribution: {
      level1: 331,
      level2: 161,
      level3: 11,
      total: 503
    },
    sampleData: [
      {
        content: "You're not broken. The job market is. | It's Been A Minute",
        platform: "youtube",
        level: 2,
        date: "2026-01-26",
        url: "https://www.youtube.com/watch?v=vfi47X6dJzU",
        videoId: "vfi47X6dJzU",
        viewCount: 19339,
        commentCount: 0
      },
      {
        content: "The 2026 Job Market is DOOMED — People Can't Get Hired",
        platform: "youtube",
        level: 2,
        date: "2026-01-21",
        url: "https://www.youtube.com/watch?v=NhPvAieny9Y",
        videoId: "NhPvAieny9Y",
        viewCount: 13567,
        commentCount: 0
      },
      {
        content: "Job search on LinkedIn",
        platform: "reddit",
        level: 1,
        date: "2026-03-14",
        url: "https://www.reddit.com/r/jobs/comments/1rtxijj/job_search_on_linkedin/"
      },
      {
        content: "Recruiter hung up on me because I didn’t “remember” the job I applied for??",
        platform: "reddit",
        level: 1,
        date: "2026-02-24",
        url: "https://www.reddit.com/r/recruitinghell/comments/1rdpu4e/recruiter_hung_up_on_me_because_i_didnt_remember/"
      },
      {
        content: "Laid Off After 25 Years in Tech:The Anxiety,Sacrifice,Reality No One Talks About [video]",
        platform: "hackernews",
        level: 2,
        date: "",
        url: "https://www.youtube.com/watch?v=VeMA9WGKxOg"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 53,
        target: 100,
        percentage: 74
      },
      {
        platform: "Reddit",
        current: 297,
        target: 300,
        percentage: 94
      },
      {
        platform: "Hacker News",
        current: 153,
        target: 150,
        percentage: 100
      }
    ],
    dataSources: [
      "Layoffs.fyi: Tech layoff tracking data",
      "YouTube: 53 videos about layoffs and job search struggles",
      "Reddit: 297 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "Hacker News: 153 stories about tech layoffs and job market"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 23, 2026"
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
