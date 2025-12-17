import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "The Absurdity Index | Quantifying Modern Existence",
  description: "A data-driven dashboard tracking the absurdity of modern life through 8 metrics: wage stagnation, housing despair, subscription overload, AI psychosis, and more.",
  keywords: ["absurdity index", "modern life metrics", "social research", "wage stagnation", "housing crisis", "dating apps", "AI companions", "healthcare", "data visualization"],
  authors: [{ name: "Shaina Pauley" }],
  creator: "Shaina Pauley",
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://absurdity-index.vercel.app",
    title: "The Absurdity Index | Quantifying Modern Existence",
    description: "Active research project tracking 8 metrics of modern absurdity through systematic data collection and transparent methodology.",
    siteName: "The Absurdity Index",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "The Absurdity Index - Data-Driven Dashboard",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "The Absurdity Index | Quantifying Modern Existence",
    description: "Tracking 8 metrics of modern absurdity: healthcare nightmares, housing despair, AI dependency, and more.",
    images: ["/og-image.png"],
    creator: "@shainapauley",
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
