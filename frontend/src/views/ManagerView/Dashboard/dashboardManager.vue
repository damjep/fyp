<template>
    <div class="card">
        <div class="card-body">
            <UsersPieChart />
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import UsersPieChart from './userPieChart/usersPieChart.vue';

</script>