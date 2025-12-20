require('dotenv').config({ path: '../.env' });
const axios = require('axios');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

// Video IDs we need view counts for
const videoIds = {
  datingApp: [
    'OdjIW8IdbIM', // Why Gen Z is Quitting Dating Apps
    'ygRO028UQUU', // Dating App Fatigue & Mental Health
    'fLYKy51jIVc', // Dating Apps Are Exhausting
    'dxxbcEGKs-c'  // The Gen Z Dating Apocalypse
  ],
  airline: [
    'rxXzYPDl5jc', // Stranded For 10+ hours
    '-NJwQ_I1Y_4', // Stranded with newborn baby
    'gzBWU8ICkOA', // Black Soldier Ignored At Airport
    'X-ElLs6Xo-c'  // Flight Delays, Fees & Fights
  ]
};

async function fetchViewCounts(videoIds) {
  const videoIdString = videoIds.join(',');
  const url = `https://www.googleapis.com/youtube/v3/videos?part=statistics&id=${videoIdString}&key=${YOUTUBE_API_KEY}`;

  try {
    const response = await axios.get(url);
    const results = {};

    response.data.items.forEach(item => {
      results[item.id] = {
        videoId: item.id,
        viewCount: parseInt(item.statistics.viewCount),
        likeCount: parseInt(item.statistics.likeCount || 0),
        commentCount: parseInt(item.statistics.commentCount || 0)
      };
    });

    return results;
  } catch (error) {
    console.error('Error fetching view counts:', error.response?.data || error.message);
    throw error;
  }
}

async function main() {
  console.log('Fetching view counts for Dating App Despair videos...\n');
  const datingAppCounts = await fetchViewCounts(videoIds.datingApp);

  console.log('Dating App Despair:');
  Object.values(datingAppCounts).forEach(video => {
    console.log(`  ${video.videoId}: ${video.viewCount.toLocaleString()} views`);
  });

  console.log('\nFetching view counts for Airline Chaos videos...\n');
  const airlineCounts = await fetchViewCounts(videoIds.airline);

  console.log('Airline Chaos:');
  Object.values(airlineCounts).forEach(video => {
    console.log(`  ${video.videoId}: ${video.viewCount.toLocaleString()} views`);
  });

  console.log('\n=== FULL RESULTS ===\n');
  console.log('Dating App Despair:');
  console.log(JSON.stringify(datingAppCounts, null, 2));
  console.log('\nAirline Chaos:');
  console.log(JSON.stringify(airlineCounts, null, 2));
}

main().catch(console.error);
