import type { Metadata } from "next";
import { Analytics } from "@vercel/analytics/next";
import { Archivo_Black, Space_Grotesk, Roboto_Mono } from "next/font/google";
import StructuredData from "@/components/StructuredData";
import { SITE_URL } from "@/lib/siteConfig";
import "./globals.css";

const archivoBlack = Archivo_Black({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-archivo",
  display: "swap",
});

const spaceGrotesk = Space_Grotesk({
  weight: "700",
  subsets: ["latin"],
  variable: "--font-space",
  display: "swap",
});

const robotoMono = Roboto_Mono({
  weight: "700",
  subsets: ["latin"],
  variable: "--font-mono",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "The Absurdity Index | Quantifying Modern Existence",
    template: "%s | The Absurdity Index",
  },
  description: "A data-driven dashboard tracking the absurdity of modern life through 8 metrics: wage stagnation, housing despair, subscription overload, AI psychosis, and more.",
  alternates: {
    canonical: "/",
  },
  keywords: ["absurdity index", "modern life metrics", "social research", "wage stagnation", "housing crisis", "dating apps", "AI companions", "healthcare", "data visualization"],
  authors: [{ name: "Shaina Pauley" }],
  creator: "Shaina Pauley",
  openGraph: {
    type: "website",
    locale: "en_US",
    url: SITE_URL,
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
  icons: {
    icon: [
      { url: "/icon.svg", type: "image/svg+xml" },
      { url: "/favicon.ico", sizes: "32x32" },
    ],
    apple: [{ url: "/apple-touch-icon.png", sizes: "180x180" }],
  },
  manifest: "/site.webmanifest",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <StructuredData />
      </head>
      <body className={`antialiased ${archivoBlack.variable} ${spaceGrotesk.variable} ${robotoMono.variable}`}>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
