<template>
    <div>
        <h2>Profile Setup</h2>
        <div v-if="loading">Loading...</div>
        <div v-if="error" class="alert alert-danger">
            {{ error }}
        </div>
        <div v-if="profile">
            <p><strong>Name:</strong> {{ profile.name }}</p>
            <p><strong>Email:</strong> {{ profile.email }}</p>
            <!-- Add more profile fields as necessary -->
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

const token = ref('');
const profile = ref(null);
const error = ref('');
const loading = ref(true);

onMounted(async () => {
    try {
        await fetchCSRFToken();  // ✅ Ensure token is fetched before fetching profile
        await fetchUserProfile(); // ✅ Fetch the profile once the token is available
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
        error.value = 'Failed to fetch CSRF token. Please try again.';
    }
}

async function fetchUserProfile() {
    if (!token.value) {
        console.warn('CSRF Token not set. Skipping profile request.');
        error.value = 'CSRF Token not found. Unable to fetch profile.';
        return;
    }

    try {
        const response = await axios.get('/api/profile-view/', {
            withCredentials: true,  // Ensure cookies are sent
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': token.value,  // Include CSRF token in the request header
            },
        });
        profile.value = response.data;  // Store the user profile in a reactive variable
        console.log('User Profile:', response.data);
    } catch (error) {
        console.error('Error fetching user profile:', error);
        error.value = 'Failed to fetch user profile. Please try again.';
    }
}
</script>
