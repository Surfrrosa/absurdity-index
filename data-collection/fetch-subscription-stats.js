require('dotenv').config({ path: '../.env' });
const axios = require('axios');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

// Subscription Overload video IDs (filtered for relevance)
const videoIds = [
  'pc4MgspmiUs', // Subscription Fatigue Is Bleeding Americans Dry - 8,637 views
  'Xv6q3gcHro0', // why I'm cancelling ALL my subscription services - 9,754 views
  'lxJG6FBo9h8', // Microsoft f*cked up real bad.. - 2,383,779 views
  'GZPr9fJG1wA'  // Streaming is OVERWHELMING! Why Netflix is LOSING Viewers! - 1,926 views
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
  console.log('Fetching stats for Subscription Overload videos...\n');
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
