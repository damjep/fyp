<template>
    <div>
        <h2>Profile Setup</h2>
        <div v-if="loading">Loading...</div>
        <div v-if="errorMessage" class="alert alert-danger">
            {{ errorMessage }}
        </div>
        <div v-if="profile">
            <form>
                <div class="mb-3 row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" id="staticEmail" :value="profile.email">
                    </div>
                </div>
                <div class="mb-3 row">
                    <label for="staticEmail" class="col-sm-2 col-form-label">Name</label>
                    <div class="col-sm-10">
                        <input type="text" class="form-control" id="staticEmail" :value="profile.name">
                    </div>
                </div> 
            </form>
            
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, ref } from 'vue';

const userStore = useUserStore();
const token = ref('');
const profile = ref(null);
const errorMessage = ref<String>('');
const loading = ref(true);

onMounted(async () => {
    try {
        await fetchCSRFToken();  // ✅ Ensure token is fetched before fetching profile
        profile.value = userStore.getUser
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

</script>
