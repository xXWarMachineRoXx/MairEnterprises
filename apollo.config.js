// apollo.config.js
module.exports = {
    client: {
      service: {
        name: 'vendure',
        // URL to the GraphQL API
        url: 'http://localhost:3000/shop-api',
      },
      // Files processed by the extension
      includes: [
        'src/**/*.vue',
        'src/**/*.js',
      ],
    },
  }