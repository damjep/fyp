<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { Line } from 'vue-chartjs';
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
} from 'chart.js';
import type { ChartData, ChartOptions } from 'chart.js';

// Register required chart elements
ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

// Define the expected FinanceReport type (based on your backend data)
interface FinanceReport {
    date: string;
    total_sales: number;
    total_tips: number;
    total_service_charge: number;
}

// Chart data state
const chartData = ref<ChartData<'line'>>({
    labels: [],
    datasets: []
});

// Optional: chart options (can customize later)
const chartOptions = ref<ChartOptions<'line'>>({
    responsive: true,
    plugins: {
        legend: {
            display: true
        }
    }
});

onMounted(async () => {
    try {
        const response = await axios.get<FinanceReport[]>('/api/finance-report-chart/');
        const data = response.data;

        chartData.value = {
            labels: data.map(item => item.date),
            datasets: [
                {
                    label: 'Total Sales',
                    data: data.map(item => item.total_sales),
                    borderColor: 'blue',
                    tension: 0.3,
                    fill: false,
                },
                {
                    label: 'Total Tips',
                    data: data.map(item => item.total_tips),
                    borderColor: 'green',
                    tension: 0.3,
                    fill: false,
                },
                {
                    label: 'Total Service Charge',
                    data: data.map(item => item.total_service_charge),
                    borderColor: 'orange',
                    tension: 0.3,
                    fill: false,
                }
            ]
        };
    } catch (error) {
        console.error('Error fetching finance report data:', error);
    }
});
</script>

<template>
    <div>
        <Line v-if="chartData.labels && chartData.labels.length" :data="chartData" :options="chartOptions" />
    </div>
</template>
