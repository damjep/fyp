<template>
<button class="btn btn-secondary mb-4"
data-bs-toggle="modal" data-bs-target="#addStocksItemModal">
    Add Stocks
</button>

<AddStocksItemModal @item-added="handleNewItem" />

<div class="card">
    <div class="card-body">
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Last Edited</th>
                    <th>Edit?</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="listData" v-for="items in listData">
                    <td>{{ items.id }}</td>
                    <td>{{ items.name }}</td>
                    <td>{{ items.quantity }}</td>
                    <td>{{ formatTime(items.timestamp) }}</td>
                    <td>
                        <button type="button" class="btn btn-secondary"
                        data-bs-toggle="modal" :data-bs-target="'#editModal'+items.id">
                            edit
                        </button>
                    </td>

                    <EditByIDModal :table-id="items.id" @item-update="handleUpdate" />
                </tr>
            </tbody>
        </table>
    </div>
</div>

</template>

<script setup lang="ts">
import axios from 'axios';
import dayjs from 'dayjs';
import { onMounted, ref, watch } from 'vue';
import EditByIDModal from './modal/editByIDModal.vue';
import AddStocksItemModal from './modal/addStocksItemModal.vue';

const listData = ref()
const update = ref(false)
const newId = ref<number | null>()

function handleUpdate() {
    update.value = !update.value
}

function handleNewItem(id: number){
    newId.value = id
}

watch(() => (update.value, newId.value) , async () => {
    if (update.value == true) {
        await getStocks()
        update.value = false
    }

    if (newId.value) {
        await getStocks()
        newId.value = null
    }
})

async function getStocks(){
    try {
        const res = await axios.get('stocks-api/get-stock-list/', {
            withCredentials: true
        })

        listData.value = res.data
        console.log(listData.value)
    } catch(err){}
}

function formatTime(time: any){
    return dayjs(time).format('DD MMM, YYYY h:mm A')
}

onMounted( async () => {
    await getStocks();
})
</script>