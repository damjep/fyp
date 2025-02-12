import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios';

export const useUserStore = defineStore('userStore', {
    state: () =>  ({
        user: ref(),
        role: ref('')
    }), 
    getters: {
        getUser(state){
            return state.user;
        },
        getRole(state){
            return state.role;
        }
    }, 
    actions: {
        async fetchUserProfile() {
            try {
                const response = await axios.get('/api/profile-view/', {
                    withCredentials: true,  // Ensure cookies are sent
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
                this.role = response.data.role;  // Store the user role in a reactive variable
                this.user = response.data;  // Store the user profile in a reactive variable
                console.log('User Profile:', response.data);
            } catch (error) {
                console.error('Error fetching user profile:', error);
            }
        }
    }
})