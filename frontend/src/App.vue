<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import axios from 'axios';
import ManagerNavDrawer from './components/ManagerNavDrawer.vue';
import router from './router';
import { useUserStore } from './stores/userStore';
import { ref } from 'vue';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;  // Ensures cookies are sent with each request

const userStore = useUserStore()

const show = ref('visually-hidden')

function handleShow(){
  show.value = 'visually hidden'
  return show.value
}
</script>

<template>
  <v-app>

    <!--Employee Nav (authenticated)-->
    <v-navigation-drawer :width="180" 
    v-if="userStore.isAuthenticated == true">
      <br>
      <v-list-item :title="'Welcome '+userStore.user?.name+'!'" 
      :subtitle="userStore.user?.role"></v-list-item>
      <br>

      <!--Profile View-->
      <v-list-item link @click="router.push('/profile')">
        <template #default>
          <v-icon class="me-2" icon="mdi-account" />
          <span>Profile</span>
        </template>
      </v-list-item> 

      <v-divider></v-divider>

      <!--Profile View-->
      <v-list-item link @click="router.push('/dashboard')">
        <template #default>
          <v-icon class="me-2" icon="mdi-monitor-dashboard" />
          <span>Dashboard</span>
        </template>
      </v-list-item> 

      <v-divider></v-divider>

      <!--List Users Link-->
      <v-list-item v-if="userStore.role == 'Manager'"
      link @click="router.push('/list-users')">
      <template #default>
        <v-icon class="me-2" icon="mdi-view-list-outline" />
        <span>Employees</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/shifts')">
      <template #default>
        <v-icon class="me-2" icon="mdi-clipboard" />
        <span>Shifts</span>
        <br>
        <span>Availability</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/rota-scheduler')"
      v-if="userStore.role == 'Manager'">
      <template #default>
        <v-icon class="me-2" icon="mdi-clipboard" />
        <span>Rota</span>
        <br>
        <span>Scheduler</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/clock')">
      <template #default>
        <v-icon class="me-2" icon="mdi-clock" />
        <span>Clock in/out</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item
      link @click="router.push('/rotalist')">
      <template #default>
        <v-icon class="me-2" icon="mdi-view-list-outline" />
        <span>Rota</span>
      </template>
      </v-list-item>

      <v-divider></v-divider>

      <!--POS Link-->
      <v-list-item link @click="router.push('/pos')">
      <template #default>
        <v-icon class="me-2" icon="mdi-cash-register" />
        <span>POS</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/finance')"
      v-if="userStore.role == 'Manager'">
      <template #default>
        <v-icon class="me-2" icon="mdi-finance" />
        <span>Finance</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/tips')">
      <template #default>
        <v-icon class="me-2" icon="mdi-finance" />
        <span>Personal Tips</span>
      </template>
      </v-list-item>

      <v-divider></v-divider>

      <!--Menu Editor Link-->
      <v-list-item v-if="userStore.role == 'Manager'"
      link @click="router.push('/menu-edit')">
      <template #default>
        <v-icon class="me-2" icon="mdi-book-edit-outline" />
        <span>Menu Editor</span>
      </template>
      </v-list-item>

      <!--Shifts Editor Link-->
      <v-list-item v-if="userStore.role == 'Manager'"
      link @click="router.push('/manager-shifts-edit')">
      <template #default>
        <v-icon class="me-2" icon="mdi-clipboard-edit-outline" />
        <span>Shifts Editor</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/inventory')">
      <template #default>
        <v-icon class="me-2" icon="mdi-archive" />
        <span>Inventory

          <span class="position-absolute top-0 start-75 translate-middle badge rounded-pill bg-danger" :class="show">
           9
          <span class="visually-hidden">unread messages</span>
          </span>
        </span>
          
      </template>
      </v-list-item>

    </v-navigation-drawer>

    <!--Main View-->
    <v-main>
      <Navbar />
    <div class="container mt-3">
      <router-view />
    </div>
    </v-main>
    
  </v-app>
</template>

<style scoped>
.container {
  height: 90vh;
  width: 100vw;
}
</style>