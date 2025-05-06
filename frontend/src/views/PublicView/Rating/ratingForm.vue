<template>
    <form @submit.prevent="createRating">
        <div class="input-group mb-3">
            <span class="input-group-text" id="basic-addon1">Name</span>
            <input type="text" class="form-control" v-model="submitData.name"
            placeholder="Name" aria-label="Username" 
            aria-describedby="basic-addon1">
        </div>
        <div>
            <label for="customRange2" class="form-label">Example range</label>
            <input type="range" class="form-range" v-model="submitData.rating"
            min="1" max="5" id="customRange2">
        </div>
        <div class="input-group">
            <span class="input-group-text">Comment</span>
            <textarea class="form-control" v-model="submitData.comment"
            aria-label="With textarea"></textarea>
        </div>
        <div>
            <button type="submit" class="btn btn-success m-2">
                Rate Us !
            </button>
        </div>
    </form>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const emit = defineEmits(['item-added'])

const submitData = ref<{
    rating: number,
    name: string,
    comment: string,
}>({
    rating: 1, 
    name: '',
    comment: '',
})

async function createRating() {
    try {
        const res = await axios.post('ratings-api/get-create-list/', {
            name: submitData.value.name,
            rating: submitData.value.rating,
            comment: submitData.value.comment,
        })

        emit('item-added', res.data.id)
    } catch (err) {

    }
}

</script>