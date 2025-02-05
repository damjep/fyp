<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;  // Ensures cookies are sent with each request

</script>

<template>
    <Navbar />

  <div class="container ">
    <router-view />
  </div>
  
</template>

<style scoped>
.container {
  height: 90vh;
  width: 100vw;
}
</style>