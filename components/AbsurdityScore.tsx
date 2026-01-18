'use client';

import { useEffect, useState } from 'react';
import { calculateOverallScore, getOverallLabel, getLatestUpdateDate } from '@/lib/metricDetailData';

export default function AbsurdityScore() {
  const absurdityScore = calculateOverallScore();
  const label = getOverallLabel(absurdityScore);
  const updateDate = getLatestUpdateDate();

  // Counter animation state
  const [displayScore, setDisplayScore] = useState(0);
  const [progressWidth, setProgressWidth] = useState(0);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Fade in component
    setIsVisible(true);

    // Animate counter
    const duration = 2000; // 2 seconds
    const steps = 60;
    const increment = absurdityScore / steps;
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= absurdityScore) {
        setDisplayScore(absurdityScore);
        clearInterval(timer);
      } else {
        setDisplayScore(current);
      }
    }, duration / steps);

    // Animate progress bar with delay
    setTimeout(() => {
      setProgressWidth(absurdityScore);
    }, 300);

    return () => clearInterval(timer);
  }, [absurdityScore]);

  return (
    <div
      className={`bg-white border-4 md:border-8 border-black p-6 md:p-10 mb-12 transition-all duration-1000 ${
        isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
      }`}
    >
      <div className="text-center border-2 md:border-4 border-black p-6 md:p-8 bg-black">
        <h2 className="text-xl md:text-2xl font-black text-white mb-4 uppercase tracking-tight">
          Current Absurdity Level
        </h2>
        <div className="text-6xl sm:text-7xl md:text-8xl lg:text-9xl font-black text-red-600 my-4 md:my-6 mono tracking-tighter">
          {displayScore.toFixed(2)}
          <span className="text-3xl sm:text-4xl md:text-5xl align-super">*</span>
        </div>
        <div className="text-xl sm:text-2xl md:text-3xl text-white font-black mb-4 md:mb-6 uppercase leading-tight px-2">
          "{label}"
        </div>

        <div className="w-full bg-white h-6 md:h-8 border-2 md:border-4 border-white">
          <div
            className="h-full bg-red-600 transition-all duration-2000 ease-out flex items-center justify-end pr-2"
            style={{ width: `${progressWidth}%` }}
          >
            <span className="text-white font-black text-xs mono">
              {Math.round(progressWidth)}%
            </span>
          </div>
        </div>

        <p className="text-white mt-4 md:mt-6 text-xs md:text-sm font-bold mono uppercase">
          8 METRICS | {updateDate} | UPDATED WEEKLY
        </p>
        <p className="text-gray-400 mt-2 md:mt-3 text-xs font-bold uppercase">
          * Equal-weight average · See methodology for details
        </p>
      </div>
    </div>
  );
}
