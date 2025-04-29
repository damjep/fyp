<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import axios from 'axios';
import ManagerNavDrawer from './components/ManagerNavDrawer.vue';
import router from './router';
import { useUserStore } from './stores/userStore';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;  // Ensures cookies are sent with each request

const userStore = useUserStore()

</script>

<template>
  <v-app>

    <!--Employee Nav (authenticated)-->
    <v-navigation-drawer :width="164" 
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
          <v-icon class="me-2" icon="mdi-account" />
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
      <v-list-item link @click="router.push('/')">
      <template #default>
        <v-icon class="me-2" icon="" />
        <span>Shifts</span>
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
      <v-list-item link @click="router.push('/finance')">
      <template #default>
        <v-icon class="me-2" icon="" />
        <span>Finance</span>
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
      <v-list-item link @click="router.push('/list-users')">
      <template #default>
        <v-icon class="me-2" icon="" />
        <span>List Users</span>
      </template>
      </v-list-item>

      <!-- Link-->
      <v-list-item link @click="router.push('/')">
      <template #default>
        <v-icon class="me-2" icon="" />
        <span></span>
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