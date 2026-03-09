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
    score: 48.8,
    label: "Prior Authorization Purgatory",
    trend: "neutral",
    officialScore: 56.30,
    crisisRatio: 43.79,
    levelDistribution: {
      level1: 353,
      level2: 61,
      level3: 35,
      total: 449
    },
    sampleData: [
      {
        content: "7 Years In Bankruptcy: What Went Wrong? | On The Red Dot",
        platform: "youtube",
        level: 3,
        date: "2026-03-03",
        url: "https://www.youtube.com/watch?v=V5BPOKtssgQ",
        videoId: "V5BPOKtssgQ",
        viewCount: 115232,
        commentCount: 0
      },
      {
        content: "$2 million gene therapy could save her baby's life. But insurance wouldn't pay.",
        platform: "youtube",
        level: 3,
        date: "2025-12-15",
        url: "https://www.youtube.com/watch?v=5qkDS7b37PI",
        videoId: "5qkDS7b37PI",
        viewCount: 33439,
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
        viewCount: 101872,
        commentCount: 0
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 134,
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
        current: 83,
        target: 120,
        percentage: 69
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
      "YouTube: 134 videos analyzing healthcare system failures",
      "Reddit: 132 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 83 videos via YouTube compilations",
      "CFPB: 100 complaints (medical debt, billing disputes)"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Sources include YouTube, Reddit, TikTok, and CFPB consumer complaints. Content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement. Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "March 9, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 35.7,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "neutral",
    officialScore: 12.5,
    crisisRatio: 51.16,
    levelDistribution: {
      level1: 454,
      level2: 64,
      level3: 106,
      total: 624
    },
    sampleData: [
      {
        content: "Why people are falling in love with A.I. companions | 60 Minutes Australia",
        platform: "youtube",
        level: 3,
        date: "2025-05-04",
        url: "https://www.youtube.com/watch?v=_d08BZmdZu8",
        videoId: "_d08BZmdZu8",
        viewCount: 1765990,
        commentCount: 0
      },
      {
        content: "New Rule: In Love with A.I. | Real Time with Bill Maher (HBO)",
        platform: "youtube",
        level: 3,
        date: "2025-02-15",
        url: "https://www.youtube.com/watch?v=fDKaoUNLNLc",
        videoId: "fDKaoUNLNLc",
        viewCount: 956787,
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
        viewCount: 5822128,
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
        current: 142,
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
        current: 69,
        target: 120,
        percentage: 57
      },
      {
        platform: "Hacker News",
        current: 124,
        target: 150,
        percentage: 82
      }
    ],
    dataSources: [
      "YouTube: 142 videos analyzing AI companion usage and addiction",
      "Reddit: 289 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 69 videos via YouTube compilations",
      "Hacker News: 124 stories about AI risks and companion addiction"
    ],
    methodology: "Systematic collection from multiple platforms including YouTube, Reddit, TikTok, and Hacker News. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official data (40% weight).",
    lastUpdated: "March 9, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 40.61,
    label: "Quarterly Purge Required",
    trend: "neutral",
    officialScore: 45.2,
    crisisRatio: 37.56,
    levelDistribution: {
      level1: 328,
      level2: 12,
      level3: 7,
      total: 348
    },
    sampleData: [
      {
        content: "Piracy Has Won The War. Streaming Lost.",
        platform: "youtube",
        level: 3,
        date: "2026-03-06",
        url: "https://www.youtube.com/watch?v=WBqy9CTQvO0",
        videoId: "WBqy9CTQvO0",
        viewCount: 34,
        commentCount: 0
      },
      {
        content: "Subscriptions Are Getting Out of Control",
        platform: "youtube",
        level: 2,
        date: "2026-01-31",
        url: "https://www.youtube.com/watch?v=jRcqJkW44Lc",
        videoId: "jRcqJkW44Lc",
        viewCount: 581818,
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
        viewCount: 3149281,
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
        current: 180,
        target: 160,
        percentage: 100
      },
      {
        platform: "Hacker News",
        current: 142,
        target: 150,
        percentage: 94
      },
      {
        platform: "TikTok",
        current: 14,
        target: 120,
        percentage: 11
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
      "YouTube: 180 videos analyzing subscription fatigue",
      "Hacker News: 142 stories about subscription fatigue and pricing",
      "TikTok: 14 videos via YouTube compilations",
      "Reddit: 12 posts from r/Frugal, r/personalfinance, r/povertyfinance"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment from YouTube, Hacker News, TikTok, and Reddit (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "March 9, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 37.25,
    label: "Paycheck-to-Paycheck Normal",
    trend: "improving",
    officialScore: 38.4,
    crisisRatio: 36.48,
    levelDistribution: {
      level1: 205,
      level2: 24,
      level3: 3,
      total: 232
    },
    sampleData: [
      {
        content: "Billionaires Want Us Homeless",
        platform: "youtube",
        level: 3,
        date: "2026-03-08",
        url: "https://www.youtube.com/watch?v=ANuGHbXa9QE",
        videoId: "ANuGHbXa9QE",
        viewCount: 110751,
        commentCount: 0
      },
      {
        content: "Living Paycheck to Paycheck Be Like",
        platform: "youtube",
        level: 2,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=K5uRsKyyNHY",
        videoId: "K5uRsKyyNHY",
        viewCount: 73777,
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
        content: "The new breed of 'zero bills' homes where you pay nothing for your energy",
        platform: "hackernews",
        level: 1,
        date: "",
        url: "https://news.sky.com/story/what-cost-of-living-crisis-why-elliott-pays-absolutely-nothing-to-power-his-home-13496916"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 116,
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
        current: 40,
        target: 100,
        percentage: 40
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: CEO-to-worker pay ratio tracking",
      "YouTube: 116 videos about wage stagnation and financial stress",
      "Reddit: 76 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "Hacker News: 40 stories about wage stagnation and financial stress"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 9, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 43.13,
    label: "Multiple Organs Required",
    trend: "neutral",
    officialScore: 37.6,
    crisisRatio: 46.81,
    levelDistribution: {
      level1: 373,
      level2: 56,
      level3: 63,
      total: 492
    },
    sampleData: [
      {
        content: "How Homeless People Sleep In A Car Without Heating",
        platform: "youtube",
        level: 3,
        date: "2026-01-17",
        url: "https://www.youtube.com/watch?v=awmWY5q1U1A",
        videoId: "awmWY5q1U1A",
        viewCount: 1504027,
        commentCount: 0
      },
      {
        content: "How Homeless People Turn a Van Into a Comfortable Home",
        platform: "youtube",
        level: 3,
        date: "2026-02-01",
        url: "https://www.youtube.com/watch?v=aX7Tpu19QfU",
        videoId: "aX7Tpu19QfU",
        viewCount: 812868,
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
        current: 109,
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
        current: 99,
        target: 120,
        percentage: 82
      }
    ],
    dataSources: [
      "Redfin: Median home price tracking",
      "Zillow Rent Index: National median rent trends",
      "Census Bureau: Rent burden data by generation",
      "YouTube: 109 videos about housing crisis and homeownership despair",
      "Reddit: 184 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "Hacker News: 99 stories about housing affordability crisis",
      "CFPB: 100 complaints (mortgages, housing finance)"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, Hacker News, and CFPB complaints (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 9, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 35.09,
    label: "Expect Delays",
    trend: "neutral",
    officialScore: 21.0,
    crisisRatio: 44.48,
    levelDistribution: {
      level1: 163,
      level2: 45,
      level3: 16,
      total: 224
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
        content: "Dubai Airport Shutdown Leaves Tourists Stranded As Gulf Flights Collapse Amid Regional Crisis",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=w7pQa-8khEQ",
        videoId: "w7pQa-8khEQ",
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
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 92,
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
      "YouTube: 92 videos about airline chaos and travel nightmares",
      "Reddit: 132 posts from r/travel, r/flights, r/delta, r/americanairlines"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 9, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 28.58,
    label: "Swipe Fatigue Setting In",
    trend: "neutral",
    officialScore: 8.5,
    crisisRatio: 41.97,
    levelDistribution: {
      level1: 187,
      level2: 46,
      level3: 11,
      total: 244
    },
    sampleData: [
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
        content: "Women Are STRUGGLING Now That Men Have Quit Dating",
        platform: "youtube",
        level: 3,
        date: "",
        url: "https://www.youtube.com/watch?v=ezL7Iw1TaYE",
        videoId: "ezL7Iw1TaYE",
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
        current: 105,
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
      "YouTube: 105 videos about dating app burnout and despair",
      "Reddit: 139 posts from r/dating, r/Tinder, r/Bumble"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 9, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 57.91,
    label: "Resume At The Ready",
    trend: "neutral",
    officialScore: 76.5,
    crisisRatio: 45.52,
    levelDistribution: {
      level1: 307,
      level2: 160,
      level3: 9,
      total: 476
    },
    sampleData: [
      {
        content: "You're not broken. The job market is. | It's Been A Minute",
        platform: "youtube",
        level: 2,
        date: "2026-01-26",
        url: "https://www.youtube.com/watch?v=vfi47X6dJzU",
        videoId: "vfi47X6dJzU",
        viewCount: 19138,
        commentCount: 0
      },
      {
        content: "The 2026 Job Market is DOOMED — People Can't Get Hired",
        platform: "youtube",
        level: 2,
        date: "2026-01-21",
        url: "https://www.youtube.com/watch?v=NhPvAieny9Y",
        videoId: "NhPvAieny9Y",
        viewCount: 13101,
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
        current: 56,
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
        current: 141,
        target: 150,
        percentage: 94
      }
    ],
    dataSources: [
      "Layoffs.fyi: Tech layoff tracking data",
      "YouTube: 56 videos about layoffs and job search struggles",
      "Reddit: 279 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "Hacker News: 141 stories about tech layoffs and job market"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment from YouTube, Reddit, and Hacker News (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "March 9, 2026"
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
