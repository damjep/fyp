<template>
    <div class="m-3" >
        <form @submit.prevent="login" class="container">
            <!--username-->
            <div class="mb-3 row">
                <label for="staticEmail" class="col-form-label">Email</label>
                <div class="col-auto">
                    <input v-model="email" type="text" class="form-control" >
                </div>
            </div>

            
             <!--Password-->
            <div class=" mb-3 row ">
                <div class="col-auto">
                    <label for="inputPassword6" class="col-form-label">Password</label>
                    <input v-model="password" type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
                </div>
            </div>

            <div>
                <button
                type="submit" class="btn btn-primary">Login</button>
                <span >
                    {{ error }}
                </span>
            </div>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore();
const error = ref('')
const router = useRouter();
const email = ref('');
const password = ref('');
const tokenA = ref('');

// Fetch CSRF token from server-side
async function fetchCSRFToken() {
    try {
        const res = await axios.get('/get-token', {withCredentials: true});
        tokenA.value = res.data.token;
        console.log(tokenA.value);
    } catch (error) {
        console.error('Error fetching CSRF token', error);
    }
}

async function login() {
    try {
        await fetchCSRFToken();
        if (email.value && password.value) {
            
            // Simulate login API call
            const res = await axios.post('/api/login/', {
                email: email.value,
                password: password.value,
            }, {
                headers: {
                    'X-CSRFToken': tokenA.value,
                }, 
                withCredentials: true,
            })

            localStorage.setItem('token', res.data.token);

            if (res.status === 200) {
                await userStore.fetchUserProfile();
                console.log('Logged in successfully');
                router.push('/'); // Redirect to home page
            } else {
                error.value = 'Invalid email or password';
                console.error('Login failed');
            }

        } else {
            error.value = 'Invalid email or password';
            console.error('Invalid email or password');
        }
    } catch (error) {
        console.error('Error logging in', error);
    }
}


</script>