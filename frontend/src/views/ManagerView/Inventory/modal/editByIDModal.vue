<template>
    <!-- Modal -->
    <div class="modal fade" :id="'editModal'+tableId" aria-labelledby="exampleModalLabel" tabindex="-1" 
     aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" >Modal Edit {{ tableId }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="updateStocks">
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
import { onMounted, ref } from 'vue';

const userStore = useUserStore()
const stocksData = ref<{
    name: string,
    quantity: number
}>({
    name: '',
    quantity: 0,
});
const props = defineProps<{
    tableId: number,
}>()
const emit = defineEmits(['item-update'])

async function getStocksById(){
    try {
        const res = await axios.get(`stocks-api/update-stocks/${props.tableId}/`, {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        stocksData.value = res.data
    } catch (err) {

    }
}

async function updateStocks(){
    try {
        const res = await axios.patch(`stocks-api/update-stocks/${props.tableId}/`, {
            name: stocksData.value.name,
            quantity: stocksData.value.quantity
        }, {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        emit('item-update')
    } catch (err) {

    }
}

onMounted( async () => {
    await getStocksById()
})

</script>