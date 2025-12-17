import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-black border-b-4 border-white">
      <div className="container mx-auto px-6 py-8">
        <div className="flex justify-between items-start">
          <div>
            <h1 className="text-6xl font-black text-white tracking-tight leading-none mb-3">
              THE ABSURDITY INDEX
            </h1>
            <p className="text-white text-lg font-bold mono">
              QUANTIFYING THE ABSURDITY OF MODERN EXISTENCE
            </p>
          </div>
          <Link
            href="/methodology"
            className="px-6 py-3 bg-white text-black font-black hover:bg-red-600 hover:text-white transition-colors border-4 border-black hover:border-white text-sm uppercase tracking-wide"
          >
            DATA
          </Link>
        </div>
      </div>

    </header>
  );
}
