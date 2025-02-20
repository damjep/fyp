<template>
    <div>
        <div v-if="menu" v-for="(items) in menu" >
            <h1 class="m-2">{{ items.dish_type}}</h1>

            <div v-for="(item , category) in items.extra_dish_types" class="mt-3">
                <h3>{{ category }}</h3>

                <div v-for="dish in item" :key="items.id">
                    <ul class="list-group list-group-horizontal" :key="dish.id">
                        <li class="list-group-item">{{ dish.name }}</li>
                        <li class="list-group-item">GBP {{ dish.price }}</li>
                        <li class="list-group-item"> {{ dish.description }}</li>
                    
                        <!-- Button trigger modal -->
                        <button type="button" class="btn btn-success" 
                        data-bs-toggle="modal"
                        :data-bs-target="`#exampleModal${dish.id}`">
                            Edit
                        </button>
                    </ul>

                    <ModalMenu :dishProp='dish' :idx="dish.id"/>
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

const menu = ref()

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
