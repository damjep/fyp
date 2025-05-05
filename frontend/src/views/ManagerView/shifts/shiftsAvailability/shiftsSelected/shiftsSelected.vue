<template>
<div class="card">
    <div class="card-body">
        <table class="table">
            <thead>
                <tr>
                    <th>Day</th>
                    <th>Delete</th>
                </tr>
            </thead>

            <tbody>
                <tr v-if="shiftsData" v-for="item in shiftsData" >
                    <td>{{ item.shift_item_str }}</td>
                    <td>
                        <button type="button" class="btn btn-danger"
                        @click="deleteShifts(item.id)">
                            delete
                        </button>
                    </td>
                </tr>

                <tr v-else>
                    <td colspan="100%">None Selected</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

const shiftsData = ref()

const props = defineProps<{
    id: number,
}>()

const emit = defineEmits(['item-deleted'])

const userStore = useUserStore()

async function getShifts() {
    try {
        const res = await axios.get('shifts-api/test/', {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        shiftsData.value = res.data.filter((item:any) => item.user == userStore.getUserData()?.id)
        console.log(shiftsData.value)
    } catch (err){}
}

async function deleteShifts(id:number){
    try {
        const res = await axios.delete(`shifts-api/delete/${id}/`, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }
        })

        emit('item-deleted', id)
        await getShifts()
    } catch (err){

    }
}

onMounted(async () => {
    await getShifts()
})

watch( () => (props.id), async () => {
    if (props.id != null) {
        await getShifts()
    }
    console.log(props.id)
}, {immediate:true})
</script>