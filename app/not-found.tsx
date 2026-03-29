import Link from 'next/link'

export default function NotFound() {
  return (
    <main className="min-h-screen bg-black flex items-center justify-center">
      <div className="text-center px-6">
        <h1 className="text-8xl font-black text-white tracking-tight mb-4">404</h1>
        <p className="text-white text-xl font-bold mb-8">
          This page doesn't exist. The absurdity continues elsewhere.
        </p>
        <Link
          href="/"
          className="px-6 py-3 bg-white text-black font-black hover:bg-red-600 hover:text-white transition-colors border-4 border-black hover:border-white text-sm uppercase tracking-wide inline-block"
        >
          Back to the Index
        </Link>
      </div>
    </main>
  )
}
