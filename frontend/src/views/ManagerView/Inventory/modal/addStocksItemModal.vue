<template>

<!-- Modal -->
<div class="modal fade" id="addStocksItemModal" data-bs-backdrop="static" 
data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Stocks Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="addStocksItem">
                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">Name</span>
                                <input type="text" class="form-control" placeholder="name" v-model="stocksData.name"
                                aria-label="name" aria-describedby="basic-addon1" >
                            </div>

                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">Quantity</span>
                                <input type="number" class="form-control" placeholder="quantity" v-model="stocksData.quantity"
                                aria-label="quantity" aria-describedby="basic-addon1">
                            </div>

                            <div>
                                <button class="btn btn-success" type="submit">
                                    Save
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { ref } from 'vue';

const stocksData = ref<{
    name: string,
    quantity: number
}>({
    name: '',
    quantity: 0,
})

const emit =defineEmits(['item-added'])

const userStore = useUserStore()

async function addStocksItem() {
    try {
        const res = await axios.post(`stocks-api/get-stock-list/`, {
            name: stocksData.value.name,
            quantity: stocksData.value.quantity
        }, {
            withCredentials:true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }
        })

        emit('item-added', res.data.id)
    } catch (err) {}
}
</script>