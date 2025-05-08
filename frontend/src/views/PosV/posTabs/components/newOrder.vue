<template>
    <div class="container card h-75 mt-5" 
    style="display: block; overflow-y: auto;">
        <div class="card-body" >
            <form @submit.prevent="save">
                <div class="mb-3 row">
                    <label for="" 
                    class="col-sm-4 col-form-label">Order Number</label>
                    <div class="col-sm-8" >
                        <input type="text"
                        v-model="data.order_number"
                        class="form-control">

                    </div>
                </div>

                <div class="mb-3 row" >
                    <label for="" 
                    class="col-sm-4 col-form-label">Number of People</label>
                    <div class="col-sm-8">
                        <input type="number" 
                        v-model="data.num_people"
                        class="form-control" >
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="" 
                    class="col-sm-4 col-form-label">Status</label>
                    <select class="form-select"
                    v-model="data.status" 
                    aria-label="">
                        <option selected v-for="status in status_choices">{{ status }}</option>
                    </select>
                </div>

                <div class="mb-3 row">
                    <label for="" 
                    class="col-sm-4 col-form-label">Total</label>
                    <div class="col-sm-8">
                        <input type="number" 
                        v-model="data.total_price"
                        class="form-control" >
                    </div>
                </div>

                <div class="mb-3 row" v-if="data.order_type == 'dine-in'">
                    <label for="" 
                    class="col-sm-4 col-form-label">Service Charge</label>
                    <div class="col-sm-8">
                        <input type="number" 
                        v-model="data.service_charge"
                        class="form-control" >
                    </div>
                </div>

                <div class="mb-3 row">
                    <label for="" 
                    class="col-sm-4 col-form-label">Tips</label>
                    <div class="col-sm-8">
                        <input type="number" 
                        v-model="data.tips"
                        class="form-control" >
                    </div>
                </div>

                <button class="btn btn-success" type="submit">
                    Save
                </button>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

const data = ref<{
    order_number: string,
    num_people: number,
    status: string,
    total_price: number,
    service_charge: number,
    tips: number,
    order_type: string
}>({
    order_number: '',
    num_people: 0,
    status: '',
    total_price: 0,
    service_charge: 0,
    tips: 0,
    order_type: ''
})

const props = defineProps<{
    table_Number: number
}>()

const status_choices = ref()
const userStore = useUserStore()
const emit = defineEmits(['order-added'])

async function getChoices() {
    try {
        const res = await axios.get('pos-api/get-order-enum/')
        status_choices.value = res.data.status_choices

    } catch (err) {

    }
}

async function save() {
    try {
        const res = await axios.post('pos-api/add-order-by-table/', {
            order_type: 'dine-in',
            order_number: data.value.order_number,
            num_people: data.value.num_people,
            table_Number: props.table_Number,
            status: 'pending',
        }, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }
        })

        emit('order-added', res.data.id)
    } catch (err) {}
}

onMounted( async () => {
    await getChoices();
})
</script>