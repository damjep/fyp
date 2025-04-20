<template>
<div class="row">
    <div class="col card">
        <div v-if="menu" v-for="items in menu">
            <div>
                <h1 class="">{{ items.dish_type }}</h1>
            </div>

            <div v-for="(item, key) in items.extra_dish_types" :key="key" class="card">
                <div v-if="key" class="card-header">
                    <p>{{ key }}</p>
                </div>

                <div class="card-body row">
                    <ul class="list-group w-100">
                        <li v-for="(dish, index) in item" :key="index" 
                        class="list-group-item d-flex justify-content-between">
                            <span>{{ dish.name }}</span>
                            <button class="btn btn-primary" >Add</button>
                        </li>
                    </ul>
                </div>
            </div>
            
        </div>
    </div>

    <div class="col">
        <div >
            
        </div>
        <AddOrderForm />
    </div>
</div>

</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import MenuView from '../MenuView.vue';
import AddOrderForm from './addOrderForm.vue';
import TableViewModal from './TableView/tableViewModal.vue';

const orderItems = ref()
const orderArray = ref()
const menu = ref()
const tab = ref()

function addOrderItem() {
    orderItems.value.push()
}


async function fetchMenu(){
    try {
        const res = await axios.get('api/get-menu', {
            withCredentials: true, 
        })
        menu.value = res.data
        console.log(menu.value);
        
    } catch (err) {
        console.error(err)
    }
}

onMounted(async () => {
    try {
        await fetchMenu();
    } catch (err) {
        console.error(err)
    };
})
</script>