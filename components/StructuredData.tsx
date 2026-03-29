export default function StructuredData() {
  const structuredData = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'WebApplication',
        name: 'The Absurdity Index',
        url: 'https://absurdity-index.vercel.app',
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
        name: 'The Absurdity Index',
        url: 'https://absurdity-index.vercel.app',
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
