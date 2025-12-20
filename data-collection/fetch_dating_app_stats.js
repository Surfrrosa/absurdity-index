require('dotenv').config({ path: '../.env' });
const axios = require('axios');
const fs = require('fs');
const csv = require('csv-parser');

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

async function fetchStats(videoIds) {
  const results = {};
  for (let i = 0; i < videoIds.length; i += 50) {
    const batch = videoIds.slice(i, i + 50);
    const videoIdString = batch.join(',');
    const url = 'https://www.googleapis.com/youtube/v3/videos?part=statistics&id=' + videoIdString + '&key=' + YOUTUBE_API_KEY;
    try {
      const response = await axios.get(url);
      response.data.items.forEach(item => {
        results[item.id] = {
          viewCount: parseInt(item.statistics.viewCount || 0),
          commentCount: parseInt(item.statistics.commentCount || 0)
        };
      });
    } catch (error) {
      console.error('Error:', error.message);
    }
  }
  return results;
}

async function main() {
  console.log('Fetching view counts...');
  const videoIds = [];
  const rows = [];
  
  fs.createReadStream('collected-data/dating_app_despair_youtube_20251217_235336.csv')
    .pipe(csv())
    .on('data', (row) => {
      videoIds.push(row.video_id);
      rows.push(row);
    })
    .on('end', async () => {
      const stats = await fetchStats(videoIds);
      const csvContent = ['search_term,video_id,url,title,category,view_count,comment_count'];
      
      rows.forEach(row => {
        const vs = stats[row.video_id] || { viewCount: 0, commentCount: 0 };
        csvContent.push('"' + row.search_term + '","' + row.video_id + '","' + row.url + '","' + row.title + '","' + row.category + '",' + vs.viewCount + ',' + vs.commentCount);
      });
      
      fs.writeFileSync('collected-data/dating_app_despair_with_stats.csv', csvContent.join('\n'));
      console.log('Done! Written to dating_app_despair_with_stats.csv');
    });
}

main().catch(console.error);
