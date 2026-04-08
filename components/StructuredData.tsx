import { SITE_URL, SITE_NAME } from '@/lib/siteConfig'

export default function StructuredData() {
  const structuredData = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebApplication',
        name: SITE_NAME,
        url: SITE_URL,
        description:
          'A data-driven dashboard quantifying the absurdity of modern existence through 8 metrics combining official statistics with social media sentiment analysis.',
        applicationCategory: 'ReferenceApplication',
        operatingSystem: 'Any',
        author: {
          '@type': 'Person',
          name: 'Shaina Pauley',
          url: 'https://shainapauley.com',
        },
        offers: {
          '@type': 'Offer',
          price: '0',
          priceCurrency: 'USD',
        },
      },
      {
        '@type': 'WebSite',
        name: SITE_NAME,
        url: SITE_URL,
        description:
          'Tracking 8 metrics of modern absurdity through systematic data collection and transparent methodology.',
      },
    ],
  }

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
    />
  )
}
