<template>
    <div class="m-3" >
        <form @submit.prevent="login" class="container">
            <!--username-->
            <div class="mb-3 row">
                <label for="staticEmail" class="col-form-label">Email</label>
                <div class="col">
                    <input v-model="email" type="email" class="form-control" >
                </div>
            </div>

            
             <!--Password-->
            <div class=" mb-3 row ">
                <div class="col">
                    <label for="inputPassword6" class="col-form-label">Password</label>
                    <input v-model="password" type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
                </div>
            </div>

            <div class=" mb-3 row ">
                <button
                type="submit" class="btn btn-primary">Login</button>
            </div>

            <div class=" mb-3 row ">
                <span v-if="alert.error" class="alert alert-danger p-4" >
                    {{ alert.error }}
                </span>
                <span class="alert alert-success text-center m-auto d-flex justify-content-center align-items-center" v-if="alert.success">
                    <span class="me-2">{{ alert.success }}</span>
                    <div class="spinner-border" role="status">
                        <span class="visually-hidden"></span>
                    </div>
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
const router = useRouter();
const email = ref('');
const password = ref('');
const tokenA = ref('');

const alert = ref<{
    success: string,
    error: string
}>({
    success: '',
    error: '',
})

// Fetch CSRF token from server-side
async function fetchCSRFToken() {
    try {
        const res = await axios.get('/get-token', {withCredentials: true});
        tokenA.value = res.data.token;
        console.log(tokenA.value);
        userStore.saveUserToken(res.data.token)
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
                console.log('Logged in successfully');
                alert.value.success = 'Logged in success'
                userStore.getUser()
                setTimeout(() => {
                    router.push('/')
                    alert.value.success = ''
                }, 3000)
                
            } else {
                alert.value.error = 'Invalid email or password';
                console.error('Login failed');
                setTimeout(() => {
                    alert.value.error = '';
                }, 3000)
            }
            
        } else {
            alert.value.error = 'Invalid email or password';
            console.error('Invalid email or password');
            setTimeout(() => {
                alert.value.error = '';
            }, 3000)
        }
    } catch (error) {
        console.error('Error logging in', error);
        alert.value.error = 'Invalid email or password';
        setTimeout(() => {
            alert.value.error = '';
        }, 3000)
    }
}


</script>