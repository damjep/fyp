<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000/';

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