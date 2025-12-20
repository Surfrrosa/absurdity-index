require('dotenv').config({ path: '../.env' });
const axios = require('axios');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

// Healthcare video IDs (filtered for relevance)
const videoIds = [
  'BKxGsIbBhnI', // One of the top reasons people go broke? Medical debt - 23,263 views
  '9rJZ17vjSWc', // Medical #Bankruptcy Is an American Problem - 18,233 views
  'spA2CT97xpA', // 11 Investigates local woman denied life-saving cancer treatment - 1,522 views
  'jguj_sabgBY'  // Medical Bills Are Still the #1 Cause of Bankruptcy - 1,065 views
];

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
  console.log('Fetching stats for Healthcare videos...\n');
  const stats = await fetchStats(videoIds);

  Object.values(stats).forEach(video => {
    console.log(`${video.videoId}:`);
    console.log(`  Views: ${video.viewCount.toLocaleString()}`);
    console.log(`  Comments: ${video.commentCount.toLocaleString()}\n`);
  });

  console.log('=== FOR COPY-PASTE ===\n');
  Object.values(stats).forEach(video => {
    console.log(`commentCount: ${video.commentCount}`);
  });
}

main().catch(console.error);
