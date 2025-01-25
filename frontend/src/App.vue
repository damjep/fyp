<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import Login from '@/components/Login.vue'
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