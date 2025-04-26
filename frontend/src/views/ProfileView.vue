<template>
    <div>
        <h2>Profile Setup</h2>
        <div v-if="loading">Loading...</div>
        <div v-if="errorMessage" class="alert alert-danger">
            {{ errorMessage }}
        </div>
        <div v-if="profile">
            <div class="card">
                <div class="card-body">
                    <form @submit.prevent="saveUserDetails">
                        <div class="mb-3 row">
                            <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" id="staticEmail" v-model="profile.email">
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <label for="name" class="col-sm-2 col-form-label">Name</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" id="name" v-model="profile.name">
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <label for="name" class="col-sm-2 col-form-label">Role</label>
                            <div class="col-sm-10">
                                <input type="text" class="form-control" 
                                id="name" v-model="profile.role" readonly>
                            </div>
                        </div>
                        <div>
                            <button type="submit" class="btn btn-success">
                                Save
                            </button>
                        </div>
                    </form>
                </div>
                <div class="card-footer p-3" v-if="alert.success || alert.error">
                    <span class="alert alert-success" v-if="alert.success">
                        {{ alert.success }}
                    </span>
                    <span class="alert alert-danger" v-if="alert.error">
                        {{ alert.error }}
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const userStore = useUserStore();
const token = ref('');
const profile = ref();
const errorMessage = ref<String>('');
const loading = ref(true);
const alert = ref<{
    success: string | null,
    error: string | any,
}>({
    success: null,
    error: null,
})

onMounted(async () => {
    try {
        await fetchCSRFToken(); 
        profile.value = userStore.getUserData()
        console.log(profile.value);
        
    } catch (err) {
        console.error('Error during onMounted:', err);
    } finally {
        loading.value = false;  // Hide loading once everything is done
    }
});

async function fetchCSRFToken() {
    try {
        const response = await axios.get('/api/get-token/', { withCredentials: true });
        token.value = response.data.token;
        console.log('CSRF Token:', token.value);
    } catch (error) {
        console.error('Error fetching CSRF token:', error);
        errorMessage.value = 'Failed to fetch CSRF token. Please try again.';
    }
}

async function saveUserDetails(){
    try {
        const res = await axios.patch('api/profile-view/', {
            name: profile.value.name,
            email: profile.value.email
        }, {
            headers: {
                'X-CSRFToken': userStore.getUserToken()
            },
            withCredentials: true
        })

        userStore.updateUser()
        alert.value.success = 'Success Saving'
        setTimeout(() => {
            alert.value.success = null
        }, 2500)
    } catch (err) {
        alert.value.error = 'Error Saving Details'
        setTimeout(() => {
            alert.value.error = null
        }, 2500)
    }
}

</script>
