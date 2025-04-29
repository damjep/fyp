<template>
    <button type="button" class="btn btn-primary mb-4" 
    data-bs-toggle="modal" data-bs-target="#addUserModal">
    Add Staff
    </button>

    <AddUserModal @user-added="handleNewUser"/>

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
                            <th>Save</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody v-for="user in key" :key="user.id">
                        <tr>
                            <td>{{ user.name }}</td>
                            <td>{{ user.email }}</td>
                            <td>
                                <select v-model="user.role"
                                class="form-select" aria-label="Default select example">
                                    <option :key="item.value" :value="item.value"
                                    v-for="item in rolesEnum"> {{ item.label }}</option>
                                </select>
                            </td>
                            <td>
                                <button type="button" class="btn btn-success"
                                @click="updateUser(user.id, user.role)">
                                    Save
                                </button>
                            </td>
                            <td>
                                <!-- Button trigger modal -->
                                <button type="button" class="btn btn-danger" 
                                data-bs-toggle="modal" :data-bs-target="'#'+user.id+'modal'">
                                fire
                                </button>
                            </td>
                        </tr>
                        <DeleteUserModal :user_id="user.id" :name="user.name" @user-deleted="handleUserDeleted"/>
                    </tbody>
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import DeleteUserModal from './modal/deleteUserModal.vue';
import AddUserModal from './modal/addUserModal.vue';

const userStore = useUserStore()
const UsersList = ref()
const rolesEnum = ref()
const userDeleted = ref(false)
const newUserId = ref()

function handleUserDeleted(){
    userDeleted.value = !userDeleted.value
}

function handleNewUser(id:number){
    newUserId.value = id
}

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

async function getRolesEnum(){
    try {
        const res = await axios.get('api/get-roles-enum/', {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        rolesEnum.value = res.data
    } catch (err){}
}

async function updateUser(user_id: number, role:any){
    try {
        const res = await axios.patch(`api/update-user-role/${user_id}/`,{
            role: role
        } ,{
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        await getEmployeesList()
    } catch (err){}
}

onMounted(async () => {
    await getEmployeesList();
    await getRolesEnum();
})

watch(() => (userDeleted.value, newUserId.value) , async () => {
    if (userDeleted.value == true) {
        await getEmployeesList();
    }
    if (newUserId) {
        await getEmployeesList();
    }
})
</script>