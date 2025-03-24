<template>
<!-- Modal -->
    <div class="modal fade" :id="'delete'+ idDelete" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="staticBackdropLabel">Delete {{ idDelete }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form @submit.prevent="deleteShift(idDelete)" class="card-body row">
                <div class="modal-body">

                </div>
                <div class="modal-footer">
                    <div>
                        <span v-if="success" class="alert alert-success">
                            {{ success }}
                        </span>

                        <span v-if="er" class="alert alert-danger" >
                            {{ er }}
                        </span>
                    </div>
                    <button type="button" data-bs-dismiss="modal" class="btn btn-secondary">Close</button>
                    <button type="submit" data-bs-dismiss="modal" class="btn btn-danger" >Delete</button>
                </div>
            </form>
            </div>
        </div>
    </div> 
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const success = ref('')
const er = ref('')

defineProps<{
    idDelete: any,
}>()

async function deleteShift(idDelete:any) {
    try {
        await axios.delete(`/shifts/update-shift/${idDelete}`, 
            {withCredentials: true,}
        )

        alertSuccess()
        setTimeout(() => {
            success.value = ''
        }, 2500)

        console.log('Shift edited:', idDelete);
    } catch (err){
        console.error('Error editing shift:', err);
        er.value = "We're having trouble on our side !"

        setTimeout(() => {
            er.value = ''
        }, 2500)
    }
}

function alertSuccess() {
    success.value = "Successfully Saved"
}
</script>