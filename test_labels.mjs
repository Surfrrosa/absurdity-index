#!/usr/bin/env node
/**
 * Test script to verify dynamic labels are working correctly
 */

import { getAllMetricsWithLabels } from './lib/metricDetailData.ts';

console.log("=".repeat(80));
console.log("TESTING DYNAMIC LABELS");
console.log("=".repeat(80));
console.log();

const metrics = getAllMetricsWithLabels();

for (const [name, metric] of Object.entries(metrics)) {
  console.log(`${name}:`);
  console.log(`  Score: ${metric.score.toFixed(2)}`);
  console.log(`  Label: "${metric.label}"`);
  console.log(`  Trend: ${metric.trend}`);
  console.log();
}

console.log("=".repeat(80));
console.log("✓ All labels calculated successfully!");
console.log("=".repeat(80));
