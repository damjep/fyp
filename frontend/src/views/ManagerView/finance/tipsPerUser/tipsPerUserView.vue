<template>
  <div class="card shadow-sm mt-5">
    <div class="card-body">
      <h3 class="card-title text-center mb-4">My Shift Earnings</h3>

      <div v-if="loading" class="text-center mb-3">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>

      <div v-if="errorMessage" class="alert alert-danger">
        {{ errorMessage }}
      </div>

      <table v-if="shifts.length" class="table table-striped">
        <thead>
          <tr>
            <th>Date</th>
            <th>Shift</th>
            <th>Clock In</th>
            <th>Clock Out</th>
            <th>Total Tips</th>
            <th>Service Charge</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="shift in shifts" :key="shift.id">
            <td>{{ shift.date }}</td>
            <td>{{ shift.shift_name }}</td>
            <td>{{ formatTime(shift.clock_in_time) }}</td>
            <td>{{ formatTime(shift.clock_out_time) }}</td>
            <td> {{ shift.total_tips }}</td>
            <td>{{ shift.total_service_charge }}</td>
          </tr>
        </tbody>
      </table>

      <div v-if="!shifts.length && !loading" class="text-center">
        No shift records found.
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

interface ClockedShift {
  id: number;
  date: string;
  shift_name: string;
  clock_in_time: string | null;
  clock_out_time: string | null;
  total_tips: string;
  total_service_charge: string;
}

const shifts = ref<ClockedShift[]>([]);
const loading = ref(true);
const errorMessage = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await axios.get('/api/clocked-shift-summary/');
    shifts.value = response.data;
  } catch (error) {
    console.error('Failed to fetch clocked shifts:', error);
    errorMessage.value = 'Failed to load shift earnings.';
  } finally {
    loading.value = false;
  }
});

// Helper to format datetime nicely
const formatTime = (datetimeStr: string | null) => {
  if (!datetimeStr) return '-';
  const date = new Date(datetimeStr);
  return date.toLocaleString();
};
</script>

<style scoped>
.table th, .table td {
  vertical-align: middle;
}
</style>
