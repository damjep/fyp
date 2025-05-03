<template>
<div class="card">
    <div class="card-body">
        <table class="table">
            <thead>
                <tr>
                    <th>Day</th>
                    <th>Start</th>
                    <th>End</th>
                    <th>Type</th>
                    <th>Add</th>
                </tr>
            </thead>

            <tbody>
                <tr v-if="shiftsData" v-for="item in shiftsData" :key="item.id">
                    <td>{{ item.days }}</td>
                    <td>{{ item.shift_start }}</td>
                    <td>{{ item.shift_end }}</td>
                    <td>{{ item.shift_type }}</td>
                    <td>
                        <button class="btn btn-success" @click="updateShifts(item.id)">
                            add
                        </button>
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
import { tr } from 'vuetify/locale';

const userStore = useUserStore()

const shiftsData = ref()
const selectedShifts = ref()

const emit = defineEmits(['item-added'])

async function getShifts() {
    try {
        const res = await axios.get('shifts-api/test/', {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        selectedShifts.value = res.data.filter((item:any) => item.user == userStore.getUserData()?.id)
        console.log(selectedShifts.value)
    } catch (err){}
}

async function getShiftsList() {
    try {
        await getShifts()
        const res = await axios.get('shifts-api/get-or-create-shifts', {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        selectedShifts.value
        shiftsData.value = res.data.filter((item: any) => item.id != selectedShifts.value.map((x:any) => x.shift_item)  )
    } catch(err){}
}

async function updateShifts(id: number){
    try{
        const res = await axios.post('shifts-api/test/', {
            user: userStore.getUserData()?.id,
            shift_item: id
        }, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }

        })

        emit('item-added')

    } catch (err) {
        console.log(err)
    }
}
onMounted(async () => {
    await getShiftsList()
})
</script>