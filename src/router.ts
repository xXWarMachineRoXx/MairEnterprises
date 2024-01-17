// router.ts
import { createRouter, createWebHistory } from 'vue-router'

import Products from './views/Products.vue' // Import your Products component
import Home from './views/Home.vue' // Import your Home component

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/products',
        name: 'Products',
        component: Products,
    },
    {
        path: '/products/:slug',
        name: 'Product',
        component: Products,
    }
    // Add more routes as needed
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
