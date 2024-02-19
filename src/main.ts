
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';
import './style.scss';

import { createMetaManager } from 'vue-meta'



const app = createApp(App);
const pinia = createPinia();

// State management using pinia
app.use(pinia);

// Meta tags manager
app.use(createMetaManager());
app
  .use(router)
  .mount('#app');
