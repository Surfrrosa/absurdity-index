export default function AbsurdityScore() {
  const absurdityScore = 16.26;
  const label = "MANAGEABLE EXISTENTIAL DREAD";

  return (
    <div className="bg-white border-4 md:border-8 border-black p-6 md:p-10 mb-12">
      <div className="text-center border-2 md:border-4 border-black p-6 md:p-8 bg-black">
        <h2 className="text-xl md:text-2xl font-black text-white mb-4 uppercase tracking-tight">
          Current Absurdity Level
        </h2>
        <div className="text-6xl sm:text-7xl md:text-8xl lg:text-9xl font-black text-red-600 my-4 md:my-6 mono tracking-tighter">
          {absurdityScore.toFixed(2)}
          <span className="text-3xl sm:text-4xl md:text-5xl align-super">*</span>
        </div>
        <div className="text-xl sm:text-2xl md:text-3xl text-white font-black mb-4 md:mb-6 uppercase leading-tight px-2">
          "{label}"
        </div>

        <div className="w-full bg-white h-6 md:h-8 border-2 md:border-4 border-white">
          <div
            className="h-full bg-red-600 transition-all duration-1000 flex items-center justify-end pr-2"
            style={{ width: `${absurdityScore}%` }}
          >
            <span className="text-white font-black text-xs mono">
              {absurdityScore.toFixed(0)}%
            </span>
          </div>
        </div>

        <p className="text-white mt-4 md:mt-6 text-xs md:text-sm font-bold mono uppercase">
          8 METRICS | DEC 2025 | ~40% DATA COMPLETE
        </p>
        <p className="text-gray-400 mt-2 md:mt-3 text-xs font-bold uppercase">
          * Collection in progress
        </p>
      </div>
    </div>
  );
}
