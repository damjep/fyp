<template>
    <button type="submit" class="btn btn-success mb-4"
    @click="getFinanceReport">
        Update Report
    </button>

    <div class="card">
        <div class="card-body">
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Date</th>
                        <th>Total Sales</th>
                        <th>Total Tips</th>
                        <th>Total Service Charge</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="listData" v-for="items in listData">
                        <td>
                            {{ items.id }}
                        </td>
                        <td>
                            {{ items.date }}
                        </td>
                        <td>
                            {{ items.total_sales }}
                        </td>
                        <td>
                            {{ items.total_tips }}
                        </td>
                        <td>
                            {{ items.total_service_charge }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const userStore = useUserStore();
const listData = ref()

async function getFinanceReport() {
    try{
        const res = await axios.post('finance-api/update-finance-report/', {} , {
            withCredentials: true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }
        })

        await getReportList()
    } catch (err){

    }
}

async function getReportList(){
    try {
        const res = await axios.get('finance-api/get-report/', {
            headers:{
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        listData.value = res.data
        
    } catch(err) {

    }
}

onMounted(async () => {
    await getReportList()
})
</script>