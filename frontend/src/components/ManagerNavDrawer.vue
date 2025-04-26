<template>
  <div class="d-flex " style="height: 1000px;">
    <!-- Vertical tab navigation -->
    <div class="nav flex-column nav-pills me-3" style="width: 200px;" role="tablist">
      <button
        class="nav-link"
        :class="{ active: currentTab === 'home' }"
        @click="currentTab = 'home'"
        role="tab"
      >
        Home
      </button>
      <button
        class="nav-link"
        :class="{ active: currentTab === 'pos' }"
        @click="currentTab = 'pos'"
        role="tab"
      >
        POS
      </button>
    </div>

    <!-- Tab content -->
    <div class="tab-content flex-grow-1">
      <div v-if="currentTab === 'home'" class="tab-pane fade show active">
        <p>Welcome to the Home tab.</p>
      </div>

      <div v-if="currentTab === 'pos'" class="tab-pane fade show active">
        <PosTabs />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import PosTabs from '@/views/PosV/posTabs/posTabs.vue'

const currentTab = ref<'home' | 'pos'>('home')
</script>

<style scoped>
/* Optional: custom styles for the vertical layout */
.d-flex {
  display: flex;
  flex-direction: row;
}

.nav-pills {
  background-color: #f8f9fa;
  border-radius: 4px;
}

.nav-link.active {
  background-color: #007bff;
  color: white;
}
</style>
