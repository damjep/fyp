<template>
<div class="card">
    <div class="card-header" v-if="avgRating">
        <h1>Our Average Rating !</h1>
        {{ avgRating.average_rating }}
        <p>
            <v-icon
                v-for="n in 5"
                :key="n"
                :icon="n <= Math.round(avgRating.average_rating) ? 'mdi-star-circle' : 'mdi-star-outline'">
            </v-icon>
        </p>
    </div>
    <div class="card-body">
        <div class="row">
            <div class="col">
                <RatingForm @item-added="async (id: number) => {
                    handleNewItem(id)
                    await getAvgRating()
                }" />
            </div>
            <div class="col">
                <RatingList :item-added-id="itemAdded" />
            </div>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import RatingForm from './ratingForm.vue';
import RatingList from './ratingList.vue';

const itemAdded = ref()
const avgRating = ref()
const userStore = useUserStore()

function handleNewItem(id: number) {
    itemAdded.value = id
}

async function getAvgRating() {
    try {
        const res = await axios.get('ratings-api/get-avg-rating/', {
            withCredentials: true
        })

        avgRating.value = res.data
    } catch (err) {}
}

onMounted(async () => {
    await getAvgRating()
}) 
</script>