<template>
    <div v-if="menu">
        <ul class="list-group" >

        </ul>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const menu = ref()

async function fetchMenu(){
    try {
        const res = await axios.get('api/get-menu/', {
            withCredentials: true, 
        })
        menu.value = res.data
    } catch (err) {
        console.error(err)
    }
}
</script>
