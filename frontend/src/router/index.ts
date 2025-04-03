import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Login.vue'
import HomeView from '@/views/HomeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MenuView from '@/views/MenuView.vue'
import MenuEditorView from '@/views/ManagerView/menu/MenuEditorView.vue'
import ManagerShiftMaker from '@/views/ManagerView/shifts/ManagerShiftMaker.vue'
import Pos from '@/views/PosV/Pos.vue'


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
      path: '/menu',
      name: 'menu',
      component: MenuView,
    },
    {
      path: '/menu-edit',
      name: 'menu-edit',
      component: MenuEditorView,
    },
    {
      path: '/manager-shifts-edit',
      name: 'manager-shifts-edit',
      component: ManagerShiftMaker,
    },
    {
      path: '/pos',
      name: 'pos',
      component: Pos,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true },
    },
    { path: '/:pathMatch(.*)*', redirect: '/' },
    {
        path: '/:catchAll(.*)', // Handle all undefined routes
        redirect: '/',
    },
  ],
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('token')) {
    next({ name: 'login' })
  } else {
    next()
  }
})



export default router
