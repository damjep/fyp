<template>
    <div class="card">
        <div class="card-body" style="max-height: 250px; overflow-y: scroll;">
            <table class="table" >
                <thead class="sticky-top">
                    <tr>
                        <th>Name</th>
                        <th>Rating</th>
                        <th>Comment</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="ratingsList" v-for="items in ratingsList">
                        <td>{{ items.name }}</td>
                        <td>{{ items.rating }}</td>
                        <td>{{ items.comment }}</td>
                    </tr>
                </tbody> 
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

const ratingsList = ref()
const props = defineProps<{
    itemAddedId: number
}>()

watch(() => props.itemAddedId, async () => {
    await getRatingList()
})

async function getRatingList() {
    try { 
        const res = await axios.get('ratings-api/get-create-list/', {
            withCredentials: true
        })

        ratingsList.value = res.data
    } catch (err) {

    }
}

onMounted(async () => {
    await getRatingList()
})
</script>