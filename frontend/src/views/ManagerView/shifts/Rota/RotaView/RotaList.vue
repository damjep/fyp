<template>
    <div class="card">
        <div class="card-body">
            <table class="table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Weeks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="weeksData" v-for="item in weeksData" :key="item.id"
                     data-bs-toggle="modal" :data-bs-target="'#rota'+item.id">
                        <td>{{ item.id }}</td>
                        <td>{{ item.start_date }} --- {{ item.end_date }}</td>
                    </tr>

                    <RotaListModalByID 
                    v-for="item in weeksData"
                    :key="'modal-' + item.id"
                    :rota-id="item.id"
                    :shifts-data="weeksData"
                    />
                </tbody>
            </table>
        </div>
    </div>

    
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import RotaListModalByID from './RotaListModalByID.vue';

const weeksData = ref()
const userStore = useUserStore()
const weekID = ref()

function handleModal(id:number){
    weekID.value = id
}

async function getWeeks() {
    try {
        const res = await axios.get('shifts-api/create-get-rota/', {
            withCredentials: true,
            headers: {
                "X-CSRFToken": userStore.getUserToken()
            }
        })

        weeksData.value = res.data
    } catch (err) {}
}

onMounted(async () => {
    await getWeeks()
})
</script>