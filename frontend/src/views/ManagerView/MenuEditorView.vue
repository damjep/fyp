<template>
    <div>
        <button type="button" class="btn btn-primary" 
        data-bs-toggle="modal"
        data-bs-target="#modalAdd" @click="fetchListRaw">
            Add Dishes 
        </button>

        <button type="button" class="btn btn-primary" 
        data-bs-toggle="modal"
        data-bs-target="#modalAddDishType" @click="fetchDishTypeList">
            Add Dish Type
        </button>

        <button type="button" class="btn btn-primary" 
        data-bs-toggle="modal"
        data-bs-target="#modalEditCategory" @click="fetchListRaw">
            Edit Dish Type Category List
        </button>

        <div v-if="menu" v-for="(items) in menu" >

            <h1 class="m-2">{{ items.dish_type}}</h1>

            <div v-for="(item , category) in items.extra_dish_types" class="mt-3">
                <h3>{{ category }}</h3>

                <div v-for="dish in item" :key="items.id">
                    <ul class="list-group list-group-horizontal row" :key="dish.id">
                        <li class="list-group-item col">{{ dish.name }}</li>
                        <li class="list-group-item col">GBP {{ dish.price }}</li>
                        <li class="list-group-item col"> {{ dish.description }}</li>
                    
                        <!-- Button trigger modal -->
                        <button type="button" class="btn btn-success col" 
                        data-bs-toggle="modal"
                        :data-bs-target="`#exampleModal${dish.id}`">
                            Edit
                        </button>

                         <!-- Button trigger modal -->
                         <button type="button" class="btn btn-danger col" 
                        data-bs-toggle="modal"
                        :data-bs-target="`#modalDelete${dish.id}`">
                            Delete
                        </button>
                        
                    </ul>

                    <ModalMenu :dishProp='dish' :idx="dish.id"/>
                    <ModalMenuAdd :dishType='listRaw' @added="fetchMenu"/>
                    <ModalMenuAddDishType />
                    <ModalMenuEditCategory :dishTypeList="listRaw"/>
                    <ModalDeleteDish :dishName='dish.name' :idDelete="dish.id" @deleted="fetchMenu"/>
                </div>
            </div>

            
            <ul class="list-group" >

            </ul>
        </div> 
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import ModalMenu from './ModalMenu.vue';
import ModalMenuAdd from './ModalMenuAdd.vue';
import ModalMenuAddDishType from './ModalMenuAddDishType.vue';
import ModalMenuEditCategory from './ModalMenuEditCategory.vue';
import ModalDeleteDish from './ModalDeleteDish.vue';

const menu = ref()
const listRaw = ref()
const listDishTypes = ref();

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

async function fetchListRaw() {
    try {
        const res = await axios.get('api/get-list-raw', {
            withCredentials: true
        })
        listRaw.value = res.data
        console.log(listRaw.value);
        
    } catch (err) {
        console.error(err);
    }
        
}

async function fetchDishTypeList() {
    try {
        const res = await axios.get('api/get-list-raw', {
            withCredentials: true
        })

        listDishTypes.value = res.data; 
    } catch (err) {
        console.error(err);
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
