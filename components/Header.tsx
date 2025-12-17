import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-black border-b-4 border-white">
      <div className="container mx-auto px-4 md:px-6 py-6 md:py-8">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-black text-white tracking-tight leading-none mb-2 md:mb-3">
              THE ABSURDITY INDEX
            </h1>
            <p className="text-white text-sm md:text-base lg:text-lg font-bold mono">
              QUANTIFYING THE ABSURDITY OF MODERN EXISTENCE
            </p>
          </div>
          <Link
            href="/methodology"
            className="px-4 md:px-6 py-2 md:py-3 bg-white text-black font-black hover:bg-red-600 hover:text-white transition-colors border-4 border-black hover:border-white text-xs md:text-sm uppercase tracking-wide whitespace-nowrap"
          >
            DATA
          </Link>
        </div>
      </div>

    </header>
  );
}
