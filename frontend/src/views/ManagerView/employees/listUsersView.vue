<template>
    <div class="card mb-3" 
    v-if="UsersList" v-for="(key, category) in UsersList">
        <div class="card-header">
            <h5 class="fw-bold">{{ category }}</h5>
        </div>
        <div class="card-body" >
            <table class="table">
                    <thead :key="key.id">
                        <tr>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Role</th>
                        </tr>
                    </thead>
                    <tbody v-for="user in key" :key="user.id">
                        <tr>
                            <td>{{ user.name }}</td>
                            <td>{{ user.email }}</td>
                            <td>{{ user.role }}</td>
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
const UsersList = ref()

async function getEmployeesList(){
    try {
        const res = await axios.get('api/list-users/',{
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })
        
        const grouped = res.data.reduce((acc: Record<string, any[]>, user: any) => {
            const role = user.role || 'Unknown';
            if (!acc[role]) {
                acc[role] = [];
            }
            acc[role].push(user);
            return acc;
        }, {});

        UsersList.value = grouped;
    } catch (err){}
}

onMounted(async () => {
    await getEmployeesList();
})
</script>