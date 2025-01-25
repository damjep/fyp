<template>
    <div>
        Profile Setup
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted } from 'vue';

onMounted(() =>  {
    // Fetch user profile data from API
    fetchUserProfile();
}) 

async function fetchUserProfile() {
    try {
        const response = await axios.get('/api/profile-view/', {
            withCredentials: true
        });
        
        // Store the fetched profile data in a reactive state
    } catch (error) {
        console.error('Error fetching user profile:', error);
    }
}
</script>