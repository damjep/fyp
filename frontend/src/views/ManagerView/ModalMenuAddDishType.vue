<template>
    <!-- Modal -->
    <div class="modal fade" id="modalAddDishType" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit.prevent="addDishCategory">
                    <div class="modal-body">
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" id="addon-wrapping">Category Name</span>
                            <input type="text" class="form-control"
                            v-model="dishtype.name" aria-describedby="addon-wrapping">
                        </div>
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" id="addon-wrapping">Extra Dish Type Name</span>
                            <input type="text" class="form-control"
                            v-model="dishtype.extra_dish_type" aria-describedby="addon-wrapping">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Save changes</button>
                    </div>

                    <span class="alert alert-success" v-if="messageSuccess">
                        {{ messageSuccess }}
                    </span>
                </form>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const messageSuccess = ref('')
const dishtype = ref<{name:string, extra_dish_type: string,}>({
    name: '',
    extra_dish_type: '',

})

async function addDishCategory(){
    try {
        await axios.post('api/menu-list-editor/', {
            dishes: [],
            dish_type: {
                name: dishtype.value.name,
                extra_dish_type: dishtype.value.extra_dish_type
            }
            
        }, {
            withCredentials:true,
        })

        messageSuccess.value = 'Dish category added successfully.'
    } catch (err) {
        console.error(err);
    }
}
</script>