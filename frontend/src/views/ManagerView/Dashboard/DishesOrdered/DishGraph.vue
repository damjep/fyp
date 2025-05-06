<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Bar } from 'vue-chartjs';
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
} from 'chart.js';
import type { ChartData, ChartOptions } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

// Chart state
const chartData = ref<ChartData<'bar'>>({
    labels: [],
    datasets: []
});

const chartOptions = ref<ChartOptions<'bar'>>({
    responsive: true,
    plugins: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Top Ordered Dishes (Paid Orders)'
        }
    }
});

onMounted(async () => {
    try {
        const response = await axios.get('/api/dish-sales-chart/');
        const data = response.data;

        chartData.value = {
            labels: Object.keys(data),
            datasets: [
                {
                    label: 'Quantity Sold',
                    data: Object.values(data),
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }
            ]
        };
    } catch (error) {
        console.error('Error fetching dish sales data:', error);
    }
});
</script>

<template>
    <div>
        <Bar v-if="chartData.labels && chartData.labels.length" :data="chartData" :options="chartOptions" />
    </div>
</template>
