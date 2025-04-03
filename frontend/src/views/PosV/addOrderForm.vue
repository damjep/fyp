<template >
<div class="card">
    <div class="card-body">
        <form>
            <div class="mb-3 row">
                <label for="" 
                class="col-sm-2 col-form-label">Order Number</label>
                <div class="col-sm-10">
                    <input type="text" 
                    class="form-control" >
                </div>
            </div>

            <div class="mb-3 row">
                <select class="form-select" 
                aria-label="">
                    <option selected>Table Number</option>
                </select>
            </div>

            <div class="mb-3 row">
                <select class="form-select" 
                aria-label="">
                    <option >Dine Type</option>
                    <option v-if="orderEnums" v-for="type in orderEnums.order_type">
                        {{ type }}
                    </option>
                </select>
            </div>

            <div class="mb-3 row">
                <label for="" 
                class="col-sm-2 col-form-label">Number of People</label>
                <div class="col-sm-10">
                    <input type="number" 
                    class="form-control" >
                </div>
            </div>

            <div class="mb-3 row">
                <select class="form-select" 
                aria-label="">
                    <option selected>Status</option>
                    <option v-if="orderEnums" v-for="status in orderEnums.status_choices">
                        {{ status }}
                    </option>
                </select>
            </div>

            <div class="mb-3 row">
                <label for="" 
                class="col-sm-2 col-form-label">Total</label>
                <div class="col-sm-10">
                    <input type="number" 
                    class="form-control" >
                </div>
            </div>

            <div class="mb-3 row">
                <label for="" 
                class="col-sm-2 col-form-label">Service Charge</label>
                <div class="col-sm-10">
                    <input type="number" 
                    class="form-control" >
                </div>
            </div>

            <div class="mb-3 row">
                <label for="" 
                class="col-sm-2 col-form-label">Tips</label>
                <div class="col-sm-10">
                    <input type="number" 
                    class="form-control" >
                </div>
            </div>
        </form>
    </div>
</div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

const orderEnums = ref()

async function getOrderEnums() {
    try { 
        const res = await axios.get('pos-api/get-order-enum')
        orderEnums.value = res.data
        console.log(orderEnums.value)
    } catch (e) {
        console.error(e)
    }
}

onMounted( async () => {
    await getOrderEnums() 
})
</script>