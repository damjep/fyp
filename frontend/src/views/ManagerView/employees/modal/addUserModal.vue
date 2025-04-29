<template>
    <!-- Modal -->
<form @submit.prevent="addNewUser">
    <div class="modal fade" id="addUserModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="addUserModal">Add New Staff</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="card">
                        <div class="card-body">
                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">Email</span>
                                <input type="email" class="form-control" v-model="user.email"
                                placeholder="Email" aria-label="email" 
                                aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">Name</span>
                                <input type="text" class="form-control" v-model="user.name"
                                placeholder="name" aria-label="Username" 
                                aria-describedby="basic-addon1">
                            </div>

                            <div class="input-group mb-3">
                                <select v-model="user.role"
                                class="form-select" aria-label="Default select example">
                                    <option :key="item.value" :value="item.value"
                                    v-for="item in rolesEnum"> {{ item.label }}</option>
                                </select>
                            </div>

                            <div class="input-group mb-3">
                                <span class="input-group-text" id="basic-addon1">Password</span>
                                <input type="password" class="form-control" v-model="user.password"
                                placeholder="password" aria-label="password" 
                                aria-describedby="basic-addon1">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-success">Save</button>

                    
                </div>

                <span v-if="alert.success == true">
                    <Alert :success="'Successfully updated'" :error="''" />
                </span>

                <span v-if="alert.err == true">
                    <Alert :success="''" :error="'Error Updating'" />
                </span>
            </div>
        </div>
    </div>
</form>
</template>

<script setup lang="ts">
import Alert from '@/components/alerts/alert.vue';
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const userStore = useUserStore()
const rolesEnum = ref()
const alert = ref<{
    success: boolean,
    err: boolean
}>({
    success: false,
    err: false
})

const emit = defineEmits(['user-added'])

const user = ref<{
    role: string ,
    name: string,
    email: string,
    password: string,
}>({
    role: '',
    name: '',
    email: '',
    password: '',
})

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

async function addNewUser() {
    try {
        const res = await axios.post('api/list-users/', {
            name: user.value.name,
            email: user.value.email,
            role: user.value.role,
            password: user.value.password,
        }, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            }
        })

        emit('user-added', res.data.id)
        alert.value.success = true

    } catch(err){
        alert.value.err = true
    }
    setTimeout(() => {
        alert.value.err = false;
        alert.value.success = false
        user.value.name = ''
        user.value.email = ''
        user.value.role = ''
        user.value.password = ''
    }, 2500)

    
}

onMounted(async () => {
    await getRolesEnum();
})
</script>