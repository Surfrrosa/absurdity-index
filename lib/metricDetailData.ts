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
    score: 51.84,
    label: "Prior Authorization Purgatory",
    trend: "worsening",
    officialScore: 56.30,
    crisisRatio: 48.87,
    levelDistribution: {
      level1: 167,
      level2: 18,
      level3: 50,
      total: 235
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
      },
      {
        content: "I ignored stomach pain for 8 months because I couldn't afford to be sick. Now I'm $12,000 in debt an",
        platform: "reddit",
        level: 3,
        date: "2025-12-15",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pndd3k/i_ignored_stomach_pain_for_8_months_because_i/"
      },
      {
        content: "My Dad doesn't understand how poor I am.",
        platform: "reddit",
        level: 2,
        date: "2025-12-10",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pjgumo/my_dad_doesnt_understand_how_poor_i_am/"
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
        current: 132,
        target: 200,
        percentage: 67
      },
      {
        platform: "TikTok",
        current: 85,
        target: 120,
        percentage: 70
      }
    ],
    dataSources: [
      "KFF (Kaiser Family Foundation): Premium increase data, coverage statistics, uninsured rate",
      "U.S. Census Bureau: Medical debt and bankruptcy statistics",
      "JAMA Network: Claim denial rates and prior authorization burden research",
      "YouTube: 150 videos analyzing healthcare system failures",
      "Reddit: 132 posts from r/HealthInsurance, r/povertyfinance, r/Insurance",
      "TikTok: 85 videos via YouTube compilations"
    ],
    methodology: "Multi-source data collection combining official healthcare statistics (40% weight) with engagement-weighted social media sentiment analysis (60% weight). Social media content categorized into three severity levels (L1=0.33, L2=0.67, L3=1.0) and weighted by logarithmic engagement (views). Final social score combines severity and reach to quantify lived experiences.",
    lastUpdated: "February 19, 2026"
  },
  "AI Psychosis": {
    title: "AI Psychosis",
    score: 37.51,
    label: "Digital Stockholm Syndrome Setting In",
    trend: "worsening",
    officialScore: 12.5,
    crisisRatio: 54.18,
    levelDistribution: {
      level1: 125,
      level2: 29,
      level3: 64,
      total: 218
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
      },
      {
        content: "GPT-4 Week 3. Chatbots are yesterdays news. AI Agents are the future. The beginning of the proto-agi",
        platform: "reddit",
        level: 3,
        date: "2023-04-06",
        url: "https://www.reddit.com/r/ChatGPT/comments/12diapw/gpt4_week_3_chatbots_are_yesterdays_news_ai/"
      },
      {
        content: "PSA: CHAT GPT IS A TOOL. NOT YOUR FRIEND.",
        platform: "reddit",
        level: 2,
        date: "2025-03-03",
        url: "https://www.reddit.com/r/ChatGPT/comments/1j2lebf/psa_chat_gpt_is_a_tool_not_your_friend/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 140,
        target: 160,
        percentage: 84
      },
      {
        platform: "Reddit",
        current: 290,
        target: 290,
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
        current: 78,
        target: 120,
        percentage: 65
      }
    ],
    dataSources: [
      "YouTube: 140 videos analyzing AI companion usage and addiction",
      "Reddit: 290 posts from r/replika, r/CharacterAI, r/ChatGPT",
      "TikTok: 78 videos via YouTube compilations",
      "App Store: 0 reviews collected (pending)",
      "Google Trends: Search volume for AI companion terms"
    ],
    methodology: "Systematic collection from multiple platforms. Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by engagement. Social score (60% weight) combined with official app download data (40% weight).",
    lastUpdated: "February 19, 2026"
  },
  "Subscription Overload": {
    title: "Subscription Overload",
    score: 41.55,
    label: "Quarterly Purge Required",
    trend: "worsening",
    officialScore: 45.2,
    crisisRatio: 39.12,
    levelDistribution: {
      level1: 152,
      level2: 17,
      level3: 4,
      total: 175
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
      },
      {
        content: "Is my father saying that my insurance is more than it is?",
        platform: "reddit",
        level: 2,
        date: "2025-12-07",
        url: "https://www.reddit.com/r/personalfinance/comments/1ph3qxd/is_my_father_saying_that_my_insurance_is_more/"
      },
      {
        content: "Landlords have lost their minds",
        platform: "reddit",
        level: 1,
        date: "2025-12-01",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pbgrff/landlords_have_lost_their_minds/"
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
        platform: "YouTube",
        current: 160,
        target: 160,
        percentage: 100
      },
      {
        platform: "Reddit",
        current: 32,
        target: 200,
        percentage: 6
      }
    ],
    dataSources: [
      "Consumer Reports: Average 12 subscriptions per household",
      "Streaming service pricing data: All major platforms tracked",
      "Google Trends: Subscription fatigue search volume",
      "Industry reports: 73% of services raised prices in 2025",
      "YouTube: 160 videos analyzing subscription fatigue",
      "Reddit: 32 posts from r/Frugal, r/personalfinance, r/povertyfinance",
      "TikTok: 15 videos via YouTube compilations"
    ],
    methodology: "Official data on average subscriptions, spending, and price increases (40% weight) combined with engagement-weighted social sentiment analysis (60% weight). Content categorized by severity and weighted by reach.",
    lastUpdated: "February 19, 2026"
  },
  "Wage Stagnation": {
    title: "Wage Stagnation",
    score: 40.31,
    label: "Paycheck-to-Paycheck Normal",
    trend: "worsening",
    officialScore: 38.4,
    crisisRatio: 41.58,
    levelDistribution: {
      level1: 132,
      level2: 30,
      level3: 9,
      total: 171
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
        content: "Working Full-Time and Still Can't Eat",
        platform: "youtube",
        level: 1,
        date: "2025-11-03",
        url: "https://www.youtube.com/watch?v=aBw582ctvOA",
        videoId: "aBw582ctvOA",
        viewCount: 495317,
        commentCount: 2408
      },
      {
        content: "I ignored stomach pain for 8 months because I couldn't afford to be sick. Now I'm $12,000 in debt an",
        platform: "reddit",
        level: 3,
        date: "2025-12-15",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pndd3k/i_ignored_stomach_pain_for_8_months_because_i/"
      },
      {
        content: "Today my supervisor asked me to either donate food or cook food for the office holiday party",
        platform: "reddit",
        level: 2,
        date: "2025-12-05",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pf5yus/today_my_supervisor_asked_me_to_either_donate/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 95,
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
        platform: "TikTok",
        current: 15,
        target: 100,
        percentage: 15
      }
    ],
    dataSources: [
      "BLS Employment Cost Index: Real wage growth data",
      "AFL-CIO CEO Pay Database: 285:1 CEO-to-worker pay ratio",
      "Google Trends: Financial stress search volume",
      "YouTube: 95 videos about wage stagnation and financial stress",
      "Reddit: 76 posts from r/antiwork, r/WorkReform, r/povertyfinance",
      "TikTok: 96 videos via YouTube compilations"
    ],
    methodology: "Official wage/CEO pay data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "February 19, 2026"
  },
  "Housing Despair": {
    title: "Housing Despair",
    score: 43.71,
    label: "Multiple Organs Required",
    trend: "worsening",
    officialScore: 37.6,
    crisisRatio: 47.78,
    levelDistribution: {
      level1: 216,
      level2: 38,
      level3: 52,
      total: 306
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
      },
      {
        content: "Scared to be homeless",
        platform: "reddit",
        level: 3,
        date: "2025-12-18",
        url: "https://www.reddit.com/r/povertyfinance/comments/1prjn9p/scared_to_be_homeless/"
      },
      {
        content: "How would you turn $300 into $2500 in 15 days to avoid eviction? Lost everything this year",
        platform: "reddit",
        level: 3,
        date: "2025-12-17",
        url: "https://www.reddit.com/r/povertyfinance/comments/1pr06i3/how_would_you_turn_300_into_2500_in_15_days_to/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 122,
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
        platform: "TikTok",
        current: 90,
        target: 100,
        percentage: 90
      }
    ],
    dataSources: [
      "Redfin: Median home price $383,725",
      "Zillow Rent Index: $2,000/month median rent",
      "Census Bureau: Gen Z rent burden data (37.6%)",
      "YouTube: 122 videos about housing crisis and homeownership despair",
      "Reddit: 184 posts from r/FirstTimeHomeBuyer, r/RealEstate, r/povertyfinance",
      "TikTok: 90 videos via YouTube compilations"
    ],
    methodology: "Official housing price/rent burden data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "February 19, 2026"
  },
  "Airline Chaos": {
    title: "Airline Chaos",
    score: 36.66,
    label: "Expect Delays",
    trend: "worsening",
    officialScore: 21.0,
    crisisRatio: 47.1,
    levelDistribution: {
      level1: 78,
      level2: 26,
      level3: 11,
      total: 115
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
      },
      {
        content: "Amtrak or Flying from Boston to Chicago",
        platform: "reddit",
        level: 3,
        date: "2025-12-01",
        url: "https://www.reddit.com/r/travel/comments/1pbvfap/amtrak_or_flying_from_boston_to_chicago/"
      },
      {
        content: "Spirit did not let me board flight at gate. The agent at gate told me to contact Customs & Borde",
        platform: "reddit",
        level: 2,
        date: "2025-12-19",
        url: "https://www.reddit.com/r/travel/comments/1pqofs3/spirit_did_not_let_me_board_flight_at_gate_the/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 115,
        target: 160,
        percentage: 61
      },
      {
        platform: "Reddit",
        current: 47,
        target: 200,
        percentage: 66
      },
      {
        platform: "TikTok",
        current: 82,
        target: 120,
        percentage: 68
      }
    ],
    dataSources: [
      "Bureau of Transportation Statistics: 22% flight delay rate",
      "ACSI satisfaction scores: Declining airline service quality",
      "FAA safety incident data: Emergency landings, equipment failures",
      "YouTube: 115 videos about airline chaos and travel nightmares",
      "Reddit: 47 posts from r/travel, r/flights, r/delta, r/americanairlines",
      "TikTok: 82 videos via YouTube compilations"
    ],
    methodology: "Official delay/safety data (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "February 19, 2026"
  },
  "Dating App Despair": {
    title: "Dating App Despair",
    score: 30.9,
    label: "Swipe Fatigue Setting In",
    trend: "worsening",
    officialScore: 8.5,
    crisisRatio: 45.83,
    levelDistribution: {
      level1: 100,
      level2: 12,
      level3: 19,
      total: 131
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
      },
      {
        content: "I dated 15 men in 2025, this is what I learned.",
        platform: "reddit",
        level: 2,
        date: "2025-12-15",
        url: "https://www.reddit.com/r/dating/comments/1pngvgp/i_dated_15_men_in_2025_this_is_what_i_learned/"
      },
      {
        content: "First time using any dating app, people are so strict",
        platform: "reddit",
        level: 1,
        date: "2025-12-01",
        url: "https://www.reddit.com/r/Tinder/comments/1pby2fk/first_time_using_any_dating_app_people_are_so/"
      }
    ],
    collectionProgress: [
      {
        platform: "YouTube",
        current: 131,
        target: 160,
        percentage: 82
      },
      {
        platform: "Reddit",
        current: 139,
        target: 200,
        percentage: 70
      },
      {
        platform: "TikTok",
        current: 75,
        target: 120,
        percentage: 62
      }
    ],
    dataSources: [
      "Pew Research: 45% frustrated, 79% burnout among dating app users",
      "Google Trends: Dating app search volume",
      "App store sentiment: Initial analysis",
      "YouTube: 131 videos about dating app burnout and despair",
      "Reddit: 139 posts from r/dating, r/Tinder, r/Bumble",
      "TikTok: 75 videos via YouTube compilations"
    ],
    methodology: "Pew Research data on dating app frustration (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "February 19, 2026"
  },
  "Layoff Watch": {
    title: "Layoff Watch",
    score: 58.51,
    label: "Resume At The Ready",
    trend: "worsening",
    officialScore: 76.5,
    crisisRatio: 46.52,
    levelDistribution: {
      level1: 184,
      level2: 160,
      level3: 9,
      total: 353
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
      },
      {
        content: "Should I ask for feedback on a ridiculous rejection I received?",
        platform: "reddit",
        level: 3,
        date: "2025-12-19",
        url: "https://www.reddit.com/r/careerguidance/comments/1pr3q8h/should_i_ask_for_feedback_on_a_ridiculous/"
      },
      {
        content: "I was laid off on Monday via zoom, they asked me to write up a transition plan and sign separation d",
        platform: "reddit",
        level: 2,
        date: "2025-11-26",
        url: "https://www.reddit.com/r/careerguidance/comments/1p7mqfr/i_was_laid_off_on_monday_via_zoom_they_asked_me/"
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
        current: 279,
        target: 300,
        percentage: 94
      },
      {
        platform: "TikTok",
        current: 95,
        target: 100,
        percentage: 95
      }
    ],
    dataSources: [
      "Layoffs.fyi: 152,922 tech workers laid off in 2025",
      "551 companies reported layoffs",
      "YouTube: 74 videos about layoffs and job search struggles",
      "Reddit: 279 posts from r/jobs, r/careerguidance, r/cscareerquestions, r/Layoffs",
      "TikTok: 95 videos via YouTube compilations"
    ],
    methodology: "Official layoff numbers (40% weight) combined with engagement-weighted social sentiment (60% weight). Content categorized by severity (L1=0.33, L2=0.67, L3=1.0) and weighted by reach.",
    lastUpdated: "February 19, 2026"
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
