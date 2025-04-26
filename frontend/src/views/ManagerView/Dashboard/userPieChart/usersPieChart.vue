<template>
    <div style="max-width: 500px; margin: auto;">
      <Pie v-if="chartData.labels.length" :data="chartData" :options="chartOptions" />
      <div v-else>Loading...</div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { Pie } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    ArcElement,
  } from 'chart.js'
  import axios from 'axios'
  
  // 🛠 Register Chart.js components (MANDATORY)
  ChartJS.register(Title, Tooltip, Legend, ArcElement)
  
  // 🛠 Define chart data and options
  const chartData = ref({
    labels: [] as string[],
    datasets: [
      {
        label: 'Users by Role',
        backgroundColor: ['#42A5F5', '#66BB6A', '#FFA726', '#FF6384', '#36A2EB'],
        data: [] as number[],
      },
    ],
  })
  
  const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,  // 🛠 Makes it easier to fit in container
    plugins: {
      legend: {
        position: 'bottom' as const,
      },
      title: {
        display: true,
        text: 'User Role Distribution',
      },
    },
  })
  
  // 🛠 Fetch user data
  async function getUserCount() {
    try {
      const res = await axios.get('api/count-users/', { withCredentials: true })
      chartData.value.labels = res.data.map((item: any) => item.role)
      chartData.value.datasets[0].data = res.data.map((item: any) => item.count)
    } catch (err) {
      console.error('Failed to load user counts', err)
    }
  }
  
  // 🛠 Fetch data on mount
  onMounted(getUserCount)
  </script>
  