import { createWebHistory, createRouter } from 'vue-router'

import HomeVue from './components/HomeVue.vue'
import AboutView from "./components/AboutView.vue"


const routes = [
    {
        name: "HomeVue",
        path: '/',
        component: HomeVue
    },
    {
        name: "AboutView",
        path: '/about',
        component: AboutView
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;