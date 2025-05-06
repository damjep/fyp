<template>
    <div class="card shadow-sm mt-4">
      <div class="card-body">
        <h3 class="card-title text-center mb-4">Clock In/Out for Your Shift</h3>
  
        <!-- Shift Dropdown -->
        <div class="mb-3">
          <label for="shift" class="form-label">Select Shift:</label>
          <select
            id="shift"
            v-model="selectedShiftItemId"
            class="form-select"
          >
            <option disabled value="">-- Select a shift --</option>
            <option
              v-for="shift in shifts"
              :key="shift.id"
              :value="shift.shift_item"
            >
              {{ shift.shift_item_str }}
            </option>
          </select>
        </div>
  
        <div v-if="statusMessage" class="alert alert-info mt-3">
          {{ statusMessage }}
        </div>
  
        <div class="d-flex justify-content-between mt-4">
          <button
            @click="clockIn"
            class="btn btn-success w-45"
            :disabled="!selectedShiftItemId || isClockedIn"
          >
            Clock In
          </button>
          <button
            @click="clockOut"
            class="btn btn-danger w-45"
            :disabled="!selectedShiftItemId || !isClockedIn || isClockedOut"
          >
            Clock Out
          </button>
        </div>
  
        <hr class="my-4" />
  
        <div class="mt-3">
          <p class="mb-1">
            <strong>Clock In Time:</strong>
            {{ clockInTime || 'Not yet clocked in' }}
          </p>
          <p class="mb-1">
            <strong>Clock Out Time:</strong>
            {{ clockOutTime || 'Not yet clocked out' }}
          </p>
        </div>
      </div>
    </div>
</template>
  
<script lang="ts" setup>
  import { ref, onMounted, watch } from 'vue';
  import axios from 'axios';
  import { useUserStore } from '@/stores/userStore';
  
  const userStore = useUserStore();
  
  interface ShiftAvailability {
    id: number;
    shift_item: number;
    shift_item_str: string;
    user_role: string;
    user_name: string;
  }
  
  // State
  const shifts = ref<ShiftAvailability[]>([]);
  const selectedShiftItemId = ref<number | null>(null);
  const clockInTime = ref<string | null>(null);
  const clockOutTime = ref<string | null>(null);
  const statusMessage = ref<string | null>(null);
  
  // State flags
  const isClockedIn = ref(false);
  const isClockedOut = ref(false);
  
  // Fetch available shifts on mount
  onMounted(async () => {
    try {
      const response = await axios.get('/shifts-api/test/');
      const userId = userStore.getUserData()?.id;
  
      // Filter shifts for the logged-in user
      shifts.value = response.data.filter((item: any) => item.user === userId);
  
      // Auto-select first shift if only one available
      if (shifts.value.length === 1) {
        selectedShiftItemId.value = shifts.value[0].shift_item;
      }
    } catch (error) {
      console.error('Failed to fetch shifts:', error);
      statusMessage.value = 'Could not load shifts.';
    }
  });
  
  // Watch for shift change to check backend clock status
  watch(selectedShiftItemId, async (newShiftId) => {
    clockInTime.value = null;
    clockOutTime.value = null;
    statusMessage.value = null;
    isClockedIn.value = false;
    isClockedOut.value = false;
  
    if (newShiftId) {
      try {
        const response = await axios.get('/api/clock-status/', {
          params: {
            shift_id: newShiftId
          }
        });
  
        const data = response.data;
        clockInTime.value = data.clock_in_time;
        clockOutTime.value = data.clock_out_time;
  
        if (data.clock_in_time && !data.clock_out_time) {
          isClockedIn.value = true;
          isClockedOut.value = false;
        } else if (data.clock_in_time && data.clock_out_time) {
          isClockedIn.value = true;
          isClockedOut.value = true;
        }
      } catch (error) {
        console.error('Failed to fetch clock status:', error);
      }
    }
  });
  
  // Clock In Method
  const clockIn = async () => {
    if (!selectedShiftItemId.value) return;
  
    try {
      const response = await axios.post('/api/clock-in/', {
        shift_id: selectedShiftItemId.value
      });
      clockInTime.value = response.data.clock_in_time;
      statusMessage.value = response.data.message || 'Clocked in successfully.';
      isClockedIn.value = true;
      isClockedOut.value = false;
    } catch (error: any) {
      console.error('Clock in error:', error);
      statusMessage.value = error.response?.data?.error || 'Failed to clock in.';
    }
  };
  
  // Clock Out Method
  const clockOut = async () => {
    if (!selectedShiftItemId.value) return;
  
    try {
      const response = await axios.post('/api/clock-out/', {
        shift_id: selectedShiftItemId.value
      });
      clockOutTime.value = response.data.clock_out_time;
      statusMessage.value = response.data.message || 'Clocked out successfully.';
      isClockedOut.value = true;
    } catch (error: any) {
      console.error('Clock out error:', error);
      statusMessage.value = error.response?.data?.error || 'Failed to clock out.';
    }
  };
</script>
  
<style scoped>
  .w-45 {
    width: 45%;
  }
</style>
  