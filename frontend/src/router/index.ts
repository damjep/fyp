import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Login.vue'
import HomeView from '@/views/HomeView.vue'
import ProfileView from '@/views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    { path: '/:pathMatch(.*)*', redirect: '/' },
  ],
})

export default router
