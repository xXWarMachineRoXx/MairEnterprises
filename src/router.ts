// router.ts
import { createRouter, createWebHistory } from 'vue-router'

import Products from './views/Products.vue' // Import your Products component
import ProductDetail from './views/ProductDetailPage.vue'
import Home from './views/Home.vue' // Import your Home component
import BlogPost from './views/BlogPost.vue'

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
        path: '/products/:productName',
        name: 'Product',
        component: ProductDetail,
    },
    {
        path: '/blog',
        name: 'Blog',
        component: () => import('./views/Blog.vue'),
    },
    {
        path: '/blog/:blogName',
        name: 'BlogPost',
        component: BlogPost,
      },
    {
        path: '/:pathMatch(.*)*',
        name: '404',
        component: () => import('./views/404.vue'),
    }
    // Add more routes as needed
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
