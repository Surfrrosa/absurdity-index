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
    score: 50.41,
    label: "Prior Authorization Purgatory",
    trend: "neutral",
    officialScore: 56.30,
    crisisRatio: 46.48,
    levelDistribution: {
      level1: 359,
      level2: 57,
      level3: 56,
      total: 472
    },
    sampleData: [
      {
        content: "7 Years In Bankruptcy: What Went Wrong? | On The Red Dot",
        platform: "youtube",
        level: 3,
        date: "2026-03-03",
        url: "https://www.youtube.com/watch?v=V5BPOKtssgQ",
        videoId: "V5BPOKtssgQ",
        viewCount: 137676,
        commentCount: 0
      },
      {
        content: "Insurance Denied a Life-Saving Stroke Treatment… for “Cost Optimization”",
        platform: "youtube",
        level: 3,
        date: "2026-02-24",
        url: "https://www.youtube.com/watch?v=WUujzQ_jMI8",
        videoId: "WUujzQ_jMI8",
        viewCount: 49983,
        commentCount: 0
      },
      {
        content: "Drowning in huge medical bills after suicide attempt(s)",
        platform: "reddit",
        level: 1,
        date: "2025-12-26",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pw6u3e/drowning_in_huge_medical_bills_after_suicide/"
      },
      {
        content: "I can’t afford to live anymore after cancer",
        platform: "reddit",
        level: 1,
        date: "2025-12-18",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pq13yz/i_cant_afford_to_live_anymore_after_cancer/"
      },
      {
        content: "Healthcare NIGHTMARE As Nurses QUIT By The Thousands - THE SHOCKING TRUTH",
        platform: "tiktok",
        level: 3,
        date: "2025-03-24",
        url: "https://www.youtube.com/watch?v=fkoV5wA4pUc",
        videoId: "fkoV5wA4pUc",
        viewCount: 102093,
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
        current: 132,
        target: 200,
        percentage: 67
      },
      {
        platform: "TikTok",
        current: 80,
        target: 120,
        percentage: 66
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
      "YouTube: 160 videos analyzing healthcare system failures",
      "Reddit: 132 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 80 videos via YouTube compilations",
      "CFPB: 100 complaints (medical debt, billing disputes)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Sources include YouTube, Reddit, TikTok, and CFPB consumer complaints. Content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement. Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "March 16, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 36.19,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "neutral",
    officialScore: 12.5,
    crisisRatio: 51.98,
    levelDistribution: {
      level1: 431,
      level2: 58,
      level3: 106,
      total: 595
    },
    sampleData: [
      {
        content: "Why people are falling in love with A.I. companions | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-05-04",
        url: "https://www.youtube.com/watch?v=_d08BZmdZu8",
        videoId: "_d08BZmdZu8",
        viewCount: 1789602,
        commentCount: 0
      },
      {
        content: "Grieving mum speaks out about teen son falling in love with an AI bot | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-12-07",
        url: "https://www.youtube.com/watch?v=yz4zfBnHksU",
        videoId: "yz4zfBnHksU",
        viewCount: 983053,
        commentCount: 0
      },
      {
        content: "Rap battling ChatGPT is my new favorite sport.",
        platform: "reddit",
        level: 1,
        date: "2023-03-26",
        url: "https://www.reddit.com/r/ChatGPT/comments/122zfa6/rap_battling_chatgpt_is_my_new_favorite_sport/"
      },
      {
        content: "Accused of using AI generation on my midterm, I didn’t and now my future is at stake",
        platform: "reddit",
        level: 1,
        date: "2024-01-07",
        url: "https://www.reddit.com/r/ChatGPT/comments/190kndt/accused_of_using_ai_generation_on_my_midterm_i/"
      },
      {
        content: "Trending chatgpt Prompts Photo Editing Prompts #shorts #viral #chatgpt #prompts",
        platform: "tiktok",
        level: 3,
        date: "2025-06-30",
        url: "https://www.youtube.com/watch?v=21EseaiPb38",
        videoId: "21EseaiPb38",
        viewCount: 5886834,
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
        current: 135,
        target: 160,
        percentage: 84
      },
      {
        platform: "Reddit",
        current: 289,
        target: 290,
        percentage: 100
      },
      {
        platform: "TikTok",
        current: 45,
        target: 120,
        percentage: 37
      },
      {
        platform: "Hacker News",
        current: 126,
        target: 150,
        percentage: 84
      }
    ],
    dataSources: [
      "YouTube: 135 videos analyzing AI companion usage and addiction",
      "Reddit: 289 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 45 videos via YouTube compilations",
      "Hacker News: 126 stories about AI risks and companion addiction"
    ],
    methodology: "Systematic collection from multiple platforms including YouTube, Reddit, TikTok, and Hacker News. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official data (40% weight).",
    lastUpdated: "March 16, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 39.91,
    label: "Quarterly Purge Required",
    trend: "neutral",
    officialScore: 45.2,
    crisisRatio: 36.39,
    levelDistribution: {
      level1: 293,
      level2: 12,
      level3: 2,
      total: 307
    },
    sampleData: [
      {
        content: "Subscriptions Are Getting Out of Control",
        platform: "youtube",
        level: 2,
        date: "2026-01-31",
        url: "https://www.youtube.com/watch?v=jRcqJkW44Lc",
        videoId: "jRcqJkW44Lc",
        viewCount: 586486,
        commentCount: 0
      },
      {
        content: "Did a subscription audit. Just gave myself a $2,058/year raise going into 2026",
        platform: "reddit",
        level: 1,
        date: "2025-12-23",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pu5xpw/did_a_subscription_audit_just_gave_myself_a/"
      },
      {
        content: "Subscriptions that offer discounts when you go to cancel pt 2",
        platform: "reddit",
        level: 1,
        date: "2025-12-06",
        url: "https://www.reddit.com/r/Frugal/comments/1pg6kk8/subscriptions_that_offer_discounts_when_you_go_to/"
      },
      {
        content: "Subscriptions Are Ruining Our Lives. Here's Why They're Everywhere Now.",
        platform: "tiktok",
        level: 1,
        date: "2024-10-24",
        url: "https://www.youtube.com/watch?v=zptP3GiaulE",
        videoId: "zptP3GiaulE",
        viewCount: 3156992,
        commentCount: 0
      },
      {
        content: "GitHub Actions for self-hosted runners price increase postponed",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://pricetimeline.com/news/189"
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
        current: 141,
        target: 150,
        percentage: 94
      },
      {
        platform: "TikTok",
        current: 4,
        target: 120,
        percentage: 3
      },
      {
        platform: "Reddit",
        current: 12,
        target: 200,
        percentage: 6
      }
    ],
    dataSources: [
      "Consumer Reports: Average subscriptions per household, spending trends",
      "Streaming service pricing data: All major platforms tracked",
      "Industry reports: Annual subscription price increase trends",
      "YouTube: 150 videos analyzing subscription fatigue",
      "Hacker News: 141 stories about subscription fatigue and pricing",
      "TikTok: 4 videos via YouTube compilations",
      "Reddit: 12 posts from r/Frugal, r/personalfinance, r/povertyfinance"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment from YouTube, Hacker News, TikTok, and Reddit (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "March 16, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 38.75,
    label: "Paycheck-to-Paycheck Normal",
    trend: "neutral",
    officialScore: 38.4,
    crisisRatio: 38.99,
    levelDistribution: {
      level1: 175,
      level2: 36,
      level3: 3,
      total: 214
    },
    sampleData: [
      {
        content: "Why Many Americans Are Living Paycheck To Paycheck",
        platform: "youtube",
        level: 2,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=d0cdsKE5-d4",
        videoId: "d0cdsKE5-d4",
        viewCount: 273535,
        commentCount: 0
      },
      {
        content: "Living Paycheck to Paycheck Be Like",
        platform: "youtube",
        level: 2,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=K5uRsKyyNHY",
        videoId: "K5uRsKyyNHY",
        viewCount: 87519,
        commentCount: 0
      },
      {
        content: "If you are broke, it’s almost impossible to get a job",
        platform: "reddit",
        level: 1,
        date: "2025-12-17",
        url: "https://www.reddit.com/r/jobs/comments/1pp7xkk/if_you_are_broke_its_almost_impossible_to_get_a/"
      },
      {
        content: "The poorest 50% in China is richer than the poorest 50% in USA (adjusted by buying power)",
        platform: "reddit",
        level: 1,
        date: "2025-12-28",
        url: "https://www.reddit.com/r/economy/comments/1py0099/the_poorest_50_in_china_is_richer_than_the/"
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
        current: 101,
        target: 100,
        percentage: 88
      },
      {
        platform: "Reddit",
        current: 76,
        target: 200,
        percentage: 39
      },
      {
        platform: "Hacker News",
        current: 37,
        target: 100,
        percentage: 37
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: CEO-to-worker pay ratio tracking",
      "YouTube: 101 videos about wage stagnation and financial stress",
      "Reddit: 76 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "Hacker News: 37 stories about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 16, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 44.38,
    label: "Multiple Organs Required",
    trend: "neutral",
    officialScore: 37.6,
    crisisRatio: 48.9,
    levelDistribution: {
      level1: 351,
      level2: 65,
      level3: 69,
      total: 485
    },
    sampleData: [
      {
        content: "How Homeless People Sleep In A Car Without Heating",
        platform: "youtube",
        level: 3,
        date: "2026-01-17",
        url: "https://www.youtube.com/watch?v=awmWY5q1U1A",
        videoId: "awmWY5q1U1A",
        viewCount: 1525746,
        commentCount: 0
      },
      {
        content: "How Homeless People Turn a Van Into a Comfortable Home",
        platform: "youtube",
        level: 3,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=aX7Tpu19QfU",
        videoId: "aX7Tpu19QfU",
        viewCount: 823329,
        commentCount: 0
      },
      {
        content: "I am officially done with \"Starter Homes.\" It’s not an investment; it’s a bailout for the previous g",
        platform: "reddit",
        level: 1,
        date: "2025-12-12",
        url: "https://www.reddit.com/r/FirstTimeHomeBuyer/comments/1pkvxta/i_am_officially_done_with_starter_homes_its_not/"
      },
      {
        content: "I work in an apartment complex and 62.2% of the residents are late on rent and I’m so sad about it.",
        platform: "reddit",
        level: 1,
        date: "2025-12-09",
        url: "https://www.reddit.com/r/povertyfinance/comments/1piheez/i_work_in_an_apartment_complex_and_622_of_the/"
      },
      {
        content: "Grocery Prices OUT OF CONTROL, People Can't Afford to Eat | TikTok Rant on America’s Grocery Crisis",
        platform: "tiktok",
        level: 3,
        date: "2025-04-23",
        url: "https://www.youtube.com/watch?v=W4CxBZnzfao",
        videoId: "W4CxBZnzfao",
        viewCount: 353,
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
        current: 107,
        target: 160,
        percentage: 86
      },
      {
        platform: "Reddit",
        current: 184,
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
        current: 79,
        target: 120,
        percentage: 65
      }
    ],
    dataSources: [
      "Redfin: Median home price tracking",
      "Zillow Rent Index: National median rent trends",
      "Census Bureau: Rent burden data by generation",
      "YouTube: 107 videos about housing crisis and homeownership despair",
      "Reddit: 184 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "Hacker News: 79 stories about housing affordability crisis",
      "CFPB: 100 complaints (mortgages, housing finance)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, Hacker News, and CFPB complaints (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 16, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 33.52,
    label: "Expect Delays",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 41.87,
    levelDistribution: {
      level1: 184,
      level2: 48,
      level3: 21,
      total: 253
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
        content: "Some flights resume in Qatar after thousands stranded",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=eXGSd0TBtYA",
        videoId: "eXGSd0TBtYA",
        viewCount: 0,
        commentCount: 0
      },
      {
        content: "Anyone headed through DFW today? Need cat food after cancelled flight...",
        platform: "reddit",
        level: 1,
        date: "2026-01-01",
        url: "https://www.reddit.com/r/americanairlines/comments/1q175vd/anyone_headed_through_dfw_today_need_cat_food/"
      },
      {
        content: "Delta One fail.",
        platform: "reddit",
        level: 1,
        date: "2025-12-13",
        url: "https://www.reddit.com/r/delta/comments/1pm0f7y/delta_one_fail/"
      },
      {
        content: "At the airport, my flight got delayed… #fyp #viral #relatable #tiktok #trending #funny #music",
        platform: "tiktok",
        level: 3,
        date: "2024-03-23",
        url: "https://www.youtube.com/watch?v=rxUwl2nMz7U",
        videoId: "rxUwl2nMz7U",
        viewCount: 554,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 106,
        target: 160,
        percentage: 61
      },
      {
        platform: "Reddit",
        current: 132,
        target: 200,
        percentage: 66
      }
    ],
    dataSources: [
      "Bureau of Transportation Statistics: Flight delay and cancellation rates",
      "ACSI satisfaction scores: Airline service quality tracking",
      "FAA safety incident data: Emergency landings, equipment failures",
      "YouTube: 106 videos about airline chaos and travel nightmares",
      "Reddit: 132 posts from r/travel, r/flights, r/delta, r/americanairlines"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 16, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 28.56,
    label: "Swipe Fatigue Setting In",
    trend: "neutral",
    officialScore: 8.5,
    crisisRatio: 41.93,
    levelDistribution: {
      level1: 195,
      level2: 45,
      level3: 12,
      total: 252
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
        content: "Dating a girl with severe hygiene issues (bad smell, hasn't showered in 6 days). How do I break up w",
        platform: "reddit",
        level: 1,
        date: "2025-12-23",
        url: "https://www.reddit.com/r/dating_advice/comments/1ptoziu/dating_a_girl_with_severe_hygiene_issues_bad/"
      },
      {
        content: "I deleted dating apps & approached 30 women (this is what happened)",
        platform: "reddit",
        level: 1,
        date: "2025-12-13",
        url: "https://www.reddit.com/r/dating_advice/comments/1plo95q/i_deleted_dating_apps_approached_30_women_this_is/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 113,
        target: 160,
        percentage: 82
      },
      {
        platform: "Reddit",
        current: 139,
        target: 200,
        percentage: 70
      }
    ],
    dataSources: [
      "Pew Research: Dating app frustration and burnout survey data",
      "YouTube: 113 videos about dating app burnout and despair",
      "Reddit: 139 posts from r/dating, r/Tinder, r/Bumble"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 16, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 57.79,
    label: "Resume At The Ready",
    trend: "neutral",
    officialScore: 76.5,
    crisisRatio: 45.32,
    levelDistribution: {
      level1: 315,
      level2: 164,
      level3: 10,
      total: 489
    },
    sampleData: [
      {
        content: "You're not broken. The job market is. | It's Been A Minute",
        platform: "youtube",
        level: 2,
        date: "2026-01-26",
        url: "https://www.youtube.com/watch?v=vfi47X6dJzU",
        videoId: "vfi47X6dJzU",
        viewCount: 19233,
        commentCount: 0
      },
      {
        content: "The 2026 Job Market is DOOMED — People Can't Get Hired",
        platform: "youtube",
        level: 2,
        date: "2026-01-21",
        url: "https://www.youtube.com/watch?v=NhPvAieny9Y",
        videoId: "NhPvAieny9Y",
        viewCount: 13323,
        commentCount: 0
      },
      {
        content: "Recruitment in 2025: you applied for 1000 jobs and none of them were actually hiring!",
        platform: "reddit",
        level: 1,
        date: "2025-12-24",
        url: "https://www.reddit.com/r/recruitinghell/comments/1pusdk7/recruitment_in_2025_you_applied_for_1000_jobs_and/"
      },
      {
        content: "As a job seeker, I don’t think there’s a “talent shortage.” I think hiring is broken.",
        platform: "reddit",
        level: 1,
        date: "2025-12-15",
        url: "https://www.reddit.com/r/recruitinghell/comments/1pn5wrn/as_a_job_seeker_i_dont_think_theres_a_talent/"
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
        current: 65,
        target: 100,
        percentage: 74
      },
      {
        platform: "Reddit",
        current: 279,
        target: 300,
        percentage: 94
      },
      {
        platform: "Hacker News",
        current: 145,
        target: 150,
        percentage: 96
      }
    ],
    dataSources: [
      "Layoffs.fyi: Tech layoff tracking data",
      "YouTube: 65 videos about layoffs and job search struggles",
      "Reddit: 279 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "Hacker News: 145 stories about tech layoffs and job market"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 16, 2026"
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
