import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import { VueShowdownPlugin } from 'vue-showdown';
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
const pinia = createPinia();

// State management using pinia
app.use(pinia);


// Provide Apollo Client to the app using vue-apollo
app.provide(DefaultApolloClient, apolloClient);

app.use(VueShowdownPlugin, {
  // set default flavor of showdown
  flavor: 'github',
  // set default options of showdown (will override the flavor options)
  options: {
    emoji: true,
    headerLevelStart: 1, 
  },
});

app
  .use(router)
  .mount('#app');
