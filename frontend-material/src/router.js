import Vue from 'vue';
import Router from 'vue-router';
import Write from './views/Write.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'write',
            component: Write,
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/history/:dateslug',
            name: 'history',
            component: () => import('./views/History.vue'),
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/history',
            name: 'history',
            component: () => import('./views/History.vue'),
            meta: {
                requiresAuth: true
            }
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        {
            path: '/contact',
            name: 'contact',
            component: () => import('./views/Contact.vue')
        },
        {
            path: '/programs',
            name: 'programs',
            component: () => import('./views/Programs.vue')
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('./views/Profile.vue')
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('./views/Login.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('./views/Register.vue')
        }
    ]
});
