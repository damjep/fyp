<template>
    <!-- Modal -->
<div class="modal fade" id="deleteShiftAllModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        Confirm Delete All Staff Shifts Availability?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary"
        @click="deleteShifts">Save changes</button>
      </div>
    </div>
  </div>
</div>

</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';

const userStore = useUserStore()

async function deleteShifts(){
    try {
        const res = await axios.delete('shifts-api/delete-all/', {
            withCredentials: true,
            headers: {
                "X-CSRFToken": userStore.getUserToken()
            }
        })
    } catch (err) {

    }
}
</script>