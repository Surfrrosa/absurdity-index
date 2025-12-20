require('dotenv').config({ path: '../.env' });
const axios = require('axios');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

// AI Psychosis video IDs
const videoIds = [
  '12waK-aDHV0', // How Character.ai slowly destroys mental health - 662K views
  'fsHcHr7OqI0', // People Getting ADDICTED - 173K views
  'ftnbNaAMhYU'  // We Ignored Her's Warning - 942 views
  // User's video TBD - need video ID
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
  console.log('Fetching stats for AI Psychosis videos...\n');
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
