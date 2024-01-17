import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './style.scss';
import { ApolloClient, createHttpLink, InMemoryCache } from '@apollo/client/core';
import { DefaultApolloClient } from '@vue/apollo-composable'; // Import from vue-apollo


// Create an Apollo Client instance
const httpLink = createHttpLink({
  uri: 'http://localhost:3000/shop-api/', // Your GraphQL API endpoint
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
});

const app = createApp(App);

// Provide Apollo Client to the app using vue-apollo
app.provide(DefaultApolloClient, apolloClient);

app
  .use(router)
  .mount('#app');
