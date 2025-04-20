<template>
    <form v-if='o_id' >
        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Order Number</label>
            <div class="col-sm-10" >
                <input type="text"
                v-model="data.order_number"
                class="form-control">

            </div>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Number of People</label>
            <div class="col-sm-10">
                <input type="number" 
                v-model="data.num_people"
                class="form-control" >
            </div>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Status</label>
            <select class="form-select"
            v-model="data.status" 
            aria-label="">
                <option selected v-for="status in status_choices">{{ status }}</option>
            </select>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Total</label>
            <div class="col-sm-10">
                <input type="number" 
                v-model="data.total_price"
                class="form-control" >
            </div>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Service Charge</label>
            <div class="col-sm-10">
                <input type="number" 
                v-model="data.service_charge"
                class="form-control" >
            </div>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Tips</label>
            <div class="col-sm-10">
                <input type="number" 
                v-model="data.tips"
                class="form-control" >
            </div>
        </div>
    </form>

    <form v-else @submit.prevent="addNewOrderItem(data.order_number, data.num_people, t_id)">
        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Order Number</label>
            <div class="col-sm-10" >
                <input type="text"
                v-model="data.order_number"
                class="form-control">

            </div>
        </div>

        <div class="mb-3 row">
            <label for="" 
            class="col-sm-2 col-form-label">Number of People</label>
            <div class="col-sm-10">
                <input type="number" 
                v-model="data.num_people"
                class="form-control" >
            </div>
        </div>

        <div>
            <button class='btn btn-primary' type="submit">
                +
            </button>
        </div>                
    </form>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

const emit = defineEmits(['order-item-added'])

const props = defineProps<{
    data: any | null,
    o_id: number,
    t_id: number
}>()

const status_choices = ref()

async function getChoices() {
    try {
        const res = await axios.get('pos-api/get-order-enum/')
        status_choices.value = res.data.status_choices

    } catch (err) {

    }
}

async function addNewOrderItem(on: number, num_people: number, tn: number){
    try{
        const res = await axios.post('pos-api/add-order-by-table/', {
            order_number: on,
            num_people: num_people,
            table_Number: tn,
            status: 'pending'
        }, {withCredentials:true})

        console.log(res.data)
        emit('order-item-added')


    } catch(err){
        console.log(err)
    }
}
onMounted( async () => {
    await getChoices();
})
</script>