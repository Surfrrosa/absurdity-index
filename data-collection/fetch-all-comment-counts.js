require('dotenv').config({ path: '../.env' });
const axios = require('axios');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

// All video IDs from our sample data
const allVideoIds = {
  housingDespair: [
    '-w_kQ-4q8cc', // 62,827 views
    'BdN7wVBgd6Y', // 4,061 views
    'GrF1MDQ-T0g', // 42 views
    'bqdPtjxzQaE'  // 397,548 views
  ],
  wageStagnation: [
    '4loulWBN5Nw', // 909,737 views
    'NN3zMclcIVs', // 1,176 views
    '_6v1VMlkfrc', // 33,655 views
    'aBw582ctvOA'  // 495,317 views
  ],
  layoffWatch: [
    '-8rg1nPv-rc', // 698 views
    'Xe-dHYhBwVk', // 780 views
    '4-UsaQaRiyA', // 436 views
    'XerzK0QNhnM'  // 45,923 views
  ],
  datingApp: [
    'OdjIW8IdbIM', // 199,804 views
    'ygRO028UQUU', // 1,683 views
    'fLYKy51jIVc', // 6 views
    'dxxbcEGKs-c'  // 104,738 views
  ],
  airline: [
    'rxXzYPDl5jc', // 144,801 views
    '-NJwQ_I1Y_4', // 441,045 views
    'gzBWU8ICkOA', // 4,385 views
    'X-ElLs6Xo-c'  // 12 views
  ]
};

async function fetchStats(videoIds) {
  const videoIdString = videoIds.join(',');
  const url = `https://www.googleapis.com/youtube/v3/videos?part=statistics&id=${videoIdString}&key=${YOUTUBE_API_KEY}`;

  try {
    const response = await axios.get(url);
    const results = {};

    response.data.items.forEach(item => {
      results[item.id] = {
        videoId: item.id,
        viewCount: parseInt(item.statistics.viewCount),
        commentCount: parseInt(item.statistics.commentCount || 0)
      };
    });

    return results;
  } catch (error) {
    console.error('Error fetching stats:', error.response?.data || error.message);
    throw error;
  }
}

async function main() {
  console.log('=== FETCHING COMMENT COUNTS FOR ALL METRICS ===\n');

  for (const [metric, videoIds] of Object.entries(allVideoIds)) {
    console.log(`\n${metric.toUpperCase()}:`);
    const stats = await fetchStats(videoIds);

    Object.values(stats).forEach(video => {
      console.log(`  ${video.videoId}: ${video.commentCount.toLocaleString()} comments (${video.viewCount.toLocaleString()} views)`);
    });
  }

  console.log('\n\n=== FORMATTED FOR COPY-PASTE ===\n');

  for (const [metric, videoIds] of Object.entries(allVideoIds)) {
    console.log(`\n${metric}:`);
    const stats = await fetchStats(videoIds);

    videoIds.forEach(videoId => {
      const video = stats[videoId];
      if (video) {
        console.log(`  commentCount: ${video.commentCount}`);
      }
    });
  }
}

main().catch(console.error);
