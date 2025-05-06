<template>
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col">
                    <UsersPieChart />
                </div>
                <div class="col">
                    <FinanceGraph />
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <DishGraph />
                </div>
                <div class="col">
                </div>
            </div>
            
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import UsersPieChart from './userPieChart/usersPieChart.vue';
import FinanceGraph from './financeReport/financeGraph.vue';
import DishGraph from './DishesOrdered/DishGraph.vue';

</script>