<template>
  <!-- Modal -->
  <div class="modal fade" :id="user_id+'modal'" 
    data-bs-backdrop="static" data-bs-keyboard="false" 
    tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ user_id }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        
        <div class="modal-body">
          <p>
            Are you sure you want to fire
            <b>{{ name }}</b> ?
          </p>

          <div v-if="isDeleting" class="text-center mt-3">
            <div class="spinner-border text-danger" role="status">
              <span class="visually-hidden">Deleting...</span>
            </div>
            <p class="mt-2">Deleting in 3 seconds...</p>
          </div>
        </div>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" :disabled="isDeleting">
            Close
          </button>
          <button 
            @click="delayedDelete" 
            type="button" 
            class="btn btn-danger" 
            data-bs-dismiss="modal"
            :disabled="isDeleting"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { ref } from 'vue'

const userStore = useUserStore()

const props = defineProps<{
  user_id: number,
  name: string
}>()

const emit = defineEmits(['user-deleted'])

const isDeleting = ref(false)

async function deleteUser() {
  try {
    await axios.delete(`api/update-user-role/${props.user_id}/`, {
      headers: {
        'X-CSRFToken': userStore.getUserToken()
      },
      withCredentials: true
    })

    emit('user-deleted')
  } catch (err) {
    console.error(err)
  } finally {
    isDeleting.value = false
  }
}

async function delayedDelete() {
  isDeleting.value = true
  await deleteUser()
}
</script>
