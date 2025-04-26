<template>
    <div class="">
        <span v-if="alert.success" class="alert alert-success">
            {{ alert.success }}
        </span>
        <span v-if="alert.error" class="alert alert-danger">
            {{ alert.error }}
        </span>
    </div>
    <div class="card">
        <div class="card-body">
            <div v-for="(payments, date) in pastOrdersData" :key="date" class="mb-4 card">
                <div class="card-header">
                    <h5 class="fw-bold m-2 p-2">{{ dayjs(date).format('dddd, MMMM D, YYYY') }}</h5>
                </div>
                <div class="card-body">
                    <table class="table table-striped border">
                        <thead>
                        <tr>
                            <th>ID</th>
                            <th>Order Number</th>
                            <th>Order Name</th>
                            <th>Payment Type</th>
                            <th>Total Paid</th>
                            <th>Order Created At</th>
                            <th>Order Type</th>
                            <th>Order Paid At</th>
                            <th>Revert Payment</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="items in payments" :key="items.id">
                            <td>{{ items.id }}</td>
                            <td>{{ items.order }}</td>
                            <td>
                            <span v-if="items.order_dine_type === 'takeaway'">
                                {{ items.order_number }}
                            </span>
                            <span v-else>-</span>
                            </td>
                            <td>{{ items.payment_method }}</td>
                            <td>{{ items.amount_paid }}</td>
                            <td>{{ formatTime(items.order_created_at) }}</td>
                            <td>{{ items.order_dine_type }}</td>
                            <td>{{ formatTime(items.timestamp) }}</td>
                            <td>
                            <button class="btn btn-danger" @click="revertPayment(items.id)">
                                Revert
                            </button>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import dayjs from 'dayjs';
import { onMounted, ref, watch } from 'vue';

const pastOrdersData = ref()
const alert = ref<{
    success: string | null,
    error: string | null,
}>({
    success: null,
    error: null,
})
const emit = defineEmits(['payment-reverted'])

const props = defineProps<{
    paid: number
}>()

function formatTime(time: any){
    return dayjs(time).format('DD MMM, YYYY h:mm A')
}

watch(() => (props.paid), async() => {
    if(props.paid){
        await getPastOrders();
    }
})

async function getPastOrders() {
  try {
    const res = await axios.get('pos-api/get-create-payment/', {
      withCredentials: true
    });

    const grouped = res.data
      .sort((a: any, b: any) => dayjs(b.order_created_at).unix() - dayjs(a.order_created_at).unix()) // sort newest first
      .reduce((acc: Record<string, any[]>, item: any) => {
        const dateKey = dayjs(item.order_created_at).format('YYYY-MM-DD');
        if (!acc[dateKey]) {
          acc[dateKey] = [];
        }
        acc[dateKey].push(item);
        return acc;
      }, {});

    pastOrdersData.value = grouped;
  } catch (err) {
    console.error(err);
  }
}

async function revertPayment(paymentID: number){
    try{
        const res = await axios.delete(`pos-api/revert-payment/${paymentID}/`, {
            withCredentials: true
        })
        alert.value.success = 'Revert Successfull'
        await getPastOrders()
        emit('payment-reverted')
    } catch (err){
        alert.value.error = 'Revert Error. Sorry it is not you but US!'
    }

    setTimeout(() => {
        alert.value.success = null
        alert.value.error = null
    }, 3000)
}

onMounted( async () => {
    await getPastOrders()
})
</script>