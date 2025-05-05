import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Auth/Login.vue'
import HomeView from '@/views/HomeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MenuView from '@/views/MenuView.vue'
import MenuEditorView from '@/views/ManagerView/menu/MenuEditorView.vue'
import ManagerShiftMaker from '@/views/ManagerView/shifts/ManagerShiftMaker.vue'
import Pos from '@/views/PosV/Pos.vue'
import PosTabs from '@/views/PosV/posTabs/posTabs.vue'
import { useUserStore } from '@/stores/userStore'
import ListUsersView from '@/views/ManagerView/employees/listUsersView.vue'
import DashboardManager from '@/views/ManagerView/Dashboard/dashboardManager.vue'
import FinanceView from '@/views/ManagerView/finance/financeView.vue'
import Inventory from '@/views/ManagerView/Inventory/inventory.vue'
import ShiftsAvailability from '@/views/ManagerView/shifts/shiftsAvailability/shiftsAvailability.vue'
import RotaScheduler from '@/views/ManagerView/shifts/Rota/RotaScheduler.vue'
import RotaList from '@/views/ManagerView/shifts/Rota/RotaView/RotaList.vue'


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
      component: PosTabs,
      meta: { requiresAuth: true },
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: { requiresAuth: true },
    },
    {
      path: '/list-users',
      name: 'listUsers',
      component: ListUsersView,
      meta: { requiresAuth: true },
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardManager,
      meta: { requiresAuth: true },
    },
    {
      path: '/finance',
      name: 'finance',
      component: FinanceView,
      meta: { requiresAuth: true },
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory,
      meta: { requiresAuth: true },
    },
    {
      path: '/shifts',
      name: 'shifts',
      component: ShiftsAvailability,
      meta: { requiresAuth: true },
    },
    {
      path: '/rota-scheduler',
      name: 'rota-scheduler',
      component: RotaScheduler,
      meta: { requiresAuth: true },
    },
    {
      path: '/rotalist',
      name: 'rotalist',
      component: RotaList,
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

  const userStore = useUserStore()

  if (to.meta.requiresAuth && !userStore.isAuthenticated) {
    next({ name: 'login' })
  } else {
    next()
  }
})



export default router
