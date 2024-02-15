import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import './style.scss';


// // Create an Apollo Client instance
// const httpLink = createHttpLink({
//   uri: 'http://localhost:3000/shop-api/', // Your GraphQL API endpoint
// });

// const apolloClient = new ApolloClient({
//   link: httpLink,
//   cache: new InMemoryCache(),
// });


const app = createApp(App);
const pinia = createPinia();

// State management using pinia
app.use(pinia);




app
  .use(router)
  .mount('#app');
