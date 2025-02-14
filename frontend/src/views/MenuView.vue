<template>
    <div v-if="menu" v-for="(items, category) in menu" >
        <h1>{{ category}}</h1>
        <div  v-for="item in items" :key="items.id">
            <h4>{{ item.extra_dish_type }}</h4>
            <div v-for="dish in item.dishes">
                <ul class="list-group list-group-horizontal" :key="dish.id">
                    <li class="list-group-item">{{ dish.name }}</li>
                    <li class="list-group-item">GBP {{ dish.price }}</li>
                    <li class="list-group-item"> {{ dish.description }}</li>
                </ul>
            </div>
        </div>
        
        <ul class="list-group" >

        </ul>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

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
