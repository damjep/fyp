<template>
<div class="card">
    <div class="card-body">
        <table class="table" v-if="groupedShifts" 
        v-for="(item, category) in groupedShifts">
            <thead>
                <tr>
                    <th>{{ category }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="user in item">
                    <td>{{ user.user_name }}</td>
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

const userStore = useUserStore()
const usersShiftAvailability = ref()

const groupedShifts = ref<{ [key: string]: any[] }>({})

function groupByShiftItemStr(data: any[]) {
  const groups: { [key: string]: any[] } = {}

  data.forEach(item => {
    const key = item.shift_item_str
    if (!groups[key]) {
      groups[key] = []
    }
    groups[key].push(item)
  })

  groupedShifts.value = groups
}

async function getUsersShifts(){
    try{
        const res = await axios.get('shifts-api/test/', {
            withCredentials: true,
            headers: {
                "X-CSRFToken": userStore.getUserToken()
            }
        })

        groupByShiftItemStr(res.data)
        console.log(groupedShifts.value)
    } catch (err) {

    }
}

onMounted( async () => {
    await getUsersShifts()
})
</script>