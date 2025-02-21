<template>
    <div class="modal fade" id="modalEditCategory" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                    <div class="modal-body">
                        <div class="row g-3" v-for="items in dishTypeList">
                            <div class="col">
                                <input type="text" class="form-control" 
                                v-model="items.dish_type.name">
                            </div>
                            <div class="col">
                                <input type="text" class="form-control" 
                                v-model="items.dish_type.extra_dish_type">
                            </div>
                            <div class="col">
                                <button type="submit" 
                                @click="saveChanges(items.dish_type)" class="btn btn-primary">Save</button>
                            </div>
                            
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <div  v-if="messageSuccess">
                            <span class="alert alert-success alert-dismiss">
                                {{ messageSuccess }}
                            </span>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const messageSuccess = ref()

defineProps( {
    dishTypeList: Object
})

async function saveChanges(item:any){
    try {
        await axios.patch(`/api/edit-dish-types/${item.id}`, {
            name: item.name,
            extra_dish_type: item.extra_dish_type,
        }, {
            withCredentials: true
        })

        messageSuccess.value = `Category ${item.name} ${item.extra_dish_type} successfully updated`
    } catch (e) {
        console.error(e);
        
    }
}
</script>