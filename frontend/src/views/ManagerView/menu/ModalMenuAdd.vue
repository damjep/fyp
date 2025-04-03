<template>
    <!-- Modal -->
    <div class="modal fade" 
    tabindex="-1" aria-hidden="true" id="modalAdd">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" 
                    >Add New Dishes</h1>
                    <button type="button" class="btn-close" 
                    data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <form @submit.prevent="addDish()">
                    <div class="modal-body">
                        <label  for="dishtypename" class="form-label">Dish Type</label>
                        <select class="form-select" id="datalistOptions" @change="updateDishType">
                            <option value="">Select Dish Type</option>
                            <option  v-for="item in dishType" :value="item.id" >
                                <div v-if="item.dish_type.extra_dish_type" >
                                    {{ item.dish_type.name }} + {{ item.dish_type.extra_dish_type }}
                                </div>    
                               
                                <div v-else>
                                    {{ item.dish_type.name }}
                                </div>
                            </option>
                        </select>
                    </div>
                    <div class="modal-body">
                        <!--Name-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Name</span>
                            <input type="text" 
                            class="form-control" 
                            v-model="addItem.name"
                            aria-describedby="addon-wrapping">
                        </div>

                        <!--Price-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Price</span>
                            <input type="number" 
                            class="form-control" 
                            v-model="addItem.price"
                            aria-describedby="addon-wrapping">
                        </div>

                        <!--Desc-->
                        <div class="input-group flex-nowrap">
                            <span class="input-group-text" 
                            id="addon-wrapping">Description</span>
                            <textarea type="number" 
                            class="form-control" 
                            v-model="addItem.description"
                            aria-describedby="addon-wrapping"> </textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" 
                        class="btn btn-primary">Save changes</button>
                    
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
import { onMounted, ref } from 'vue';

const selectedDishTypeID = ref();
const success = ref()
const err = ref()
const addItem = ref<{name: string | ''; price: number | 0; description: string | '';}>({
    name: '',
    price: 0,
    description: ''
})
const dishesDataByID = ref()
const emit = defineEmits(['added'])

function updateDishType(event: any) {
    const selectedId = event.target.value;
    selectedDishTypeID.value = selectedId;
    console.log(selectedDishTypeID.value);
    getDishesData();
}

async function getDishesData(){
    try {
        if (selectedDishTypeID.value == '') {
            return;
        }
        const res = await axios.get(`api/edit-menu/${selectedDishTypeID.value}`, {
            withCredentials:true,
        })

        dishesDataByID.value = res.data.dishes;
    } catch (error) {
        console.error(error);
        err.value = "An error occurred while trying to add the dish."
    }
}

async function addDish(){
    try {
        await axios.patch(`api/edit-menu/${selectedDishTypeID.value}`, {
            dishes: [ ...dishesDataByID.value, {
                name: addItem.value.name,
                price: addItem.value.price,
                description: addItem.value.description
            }]
        }, {
            withCredentials:true,
        })

        addItem.value = {
            name: '',
            price: 0,
            description: ''
        }
        emit('added', selectedDishTypeID.value)

        success.value = "Dish added successfully!";

        setTimeout(() => {
            success.value = "";
        }, 2000);
        
    } catch (error) {
        console.error(error);
        err.value = "An error occurred while trying to add the dish."
    }
}

defineProps<{
    dishType:any,
}>()


</script>