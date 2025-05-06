<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">FinEasy</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
                <button class="nav-link" aria-current="page" @click="router.push('/')">Home</button>
                <a class="nav-link" @click="router.push('/menu')">Menu</a>
                <a class="nav-link" @click="router.push('/rating')">Rating</a>
                <a class="nav-link" v-if="userStore.isAuthenticated == true"
                @click="router.push('/pos')">Pos</a>
            </div>
            <div class="navbar-nav ms-auto pr-4">
                <a class="nav-link border " @click="router.push('/login')">
                    <v-icon icon="mdi-login"></v-icon> Login
                </a>
                <a class="nav-link border " @click="logout" v-if="userStore.isAuthenticated == true">
                    <v-icon icon="mdi-logout"></v-icon> Logout
                </a>
            </div>
            </div>
        </div>
    </nav>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { useRouter } from 'vue-router';
const router = useRouter();
const userStore = useUserStore()

async function logout(){
    try {
        const res = await axios.post('api/logout/', {}, {
            withCredentials: true,
        })
        userStore.logout()
        router.push('/')
    } catch (err){

    }
}

</script>
