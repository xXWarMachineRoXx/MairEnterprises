// router.ts
import { createRouter, createWebHistory } from 'vue-router'

import Products from './views/Products.vue' // Import your Products component
import ProductDetail from './views/ProductDetailPage.vue'
import Home from './views/Home.vue' // Import your Home component
import BlogPost from './views/BlogPost.vue'
import CategoryVue from './views/Category.vue'

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
        path: '/category/:categoryName',
        name: 'Category',
        component: CategoryVue,
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('./views/About.vue'),
    },
    {
        path: '/contact',
        name: 'Contact',
        component: () => import('./views/Contact.vue'),
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
        path: '/Search',
        name: 'Search',
        component: () => import('./views/Search.vue'),
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
