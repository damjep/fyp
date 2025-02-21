<template>
    <div class="modal fade" :id="'modalDelete' + idDelete"  tabindex="-1"
     aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5 row" :id="'modalDelete' + idDelete">
                        <div class="col">
                            {{ idDelete }}
                            {{ dishName }}
                        </div>
                    </h1>
                    <button type="button" class="btn-close" 
                    data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p>
                        Are you sure you want to delete {{ dishName }} ?
                    </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" 
                    data-bs-dismiss="modal" @click="deletDish(idDelete)">
                        Delete
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';


defineProps<{
    dishName:string,
    idDelete: number
}>()

const emit = defineEmits(['deleted'])

async function deletDish(id:any) {
    try {
        await axios.delete(`api/edit-dish/${id}`, {
            withCredentials:true
        })

        emit('deleted', id);
    } catch (err) {
        console.error(err);
    }
}
</script>