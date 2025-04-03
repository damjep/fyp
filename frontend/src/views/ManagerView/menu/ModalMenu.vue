<template>
    <!-- Modal -->
    <div class="modal fade" :id="'exampleModal' + idx"  
    tabindex="-1" aria-hidden="true" v-if="dishProp">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" 
                    :id="'exampleModal' + idx">Modal title</h1>
                    <button type="button" class="btn-close" 
                    data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit.prevent="editDish(dishProp)">
                    <div class="modal-body">
                        <!--ID-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">ID</span>
                            <input type="text" 
                            class="form-control" 
                            v-model="dishProp.id"
                            aria-describedby="addon-wrapping" readonly>
                        </div>

                        <!--Name-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Name</span>
                            <input type="text" 
                            class="form-control" 
                            v-model="dishProp.name"
                            aria-describedby="addon-wrapping">
                        </div>

                        <!--Price-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Price</span>
                            <input type="number" 
                            class="form-control" 
                            v-model="dishProp.price"
                            aria-describedby="addon-wrapping">
                        </div>

                        <!--Desc-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Description</span>
                            <textarea type="number" 
                            class="form-control" 
                            v-model="dishProp.description"
                            aria-describedby="addon-wrapping"> </textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Save changes</button>
                    
                        <span v-if="success" class="alert alert-success">
                            {{ success }}
                        </span>

                        <span v-if="err" class="alert alert-danger">
                            {{ err }}
                        </span>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const success = ref('');
const err = ref('');

defineProps<{
  dishProp: { id: number; name: string; price: number; description: string; };  // Ensure `dish.id` exists
  idx: number;
}>();

async function editDish(dishProp: { id: number; name: string; price: number; description: string;}){
    try {
        await axios.patch(`api/edit-dish/${dishProp.id}`, {
            name: dishProp.name,
            price: dishProp.price,
            description: dishProp.description
        }, {
            withCredentials: true,
        });

        success.value = 'Dish updated successfully!';
    } catch (error) {
        console.error(error);
        err.value = 'Error updating dish. Please try again later.';
    }
}
</script>