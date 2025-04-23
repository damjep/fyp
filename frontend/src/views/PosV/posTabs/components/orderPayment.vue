<template>
    <div class="card">
        <div class="card-body">
            <form @submit.prevent="createPayment()">
                <div>
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="basic-addon1">
                            Order Number {{ order_id }}
                        </span>
                    </div>
                </div>

                <div>
                    
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="basic-addon1">
                            Amount to Pay
                        </span>
                        <span class="input-group-text">
                            {{ total_price }}
                        </span>
                        <input type="number" class="form-control" 
                         v-model="data.amount_paid"
                        aria-describedby="basic-addon1">
                    </div>
                </div>

                <div>
                    <span class="input-group-text" id="basic-addon1">
                        Payment Method
                    </span>
                    <input type="radio" class="btn-check" v-model="data.payment_method" value="CASH"
                    name="options-base" id="option1" autocomplete="off" >
                    <label class="btn" for="option1">Cash</label>
                    <input type="radio" class="btn-check" v-model="data.payment_method" value="CARD"
                    name="options-base" id="option2" autocomplete="off" >
                    <label class="btn" for="option2">Card</label>
                    <input type="radio" class="btn-check" v-model="data.payment_method" value="ONLINE"
                    name="options-base" id="option3" autocomplete="off" >
                    <label class="btn" for="option3">Online</label>
                </div>

                <div>
                    <button type="submit" class="btn btn-success">
                        Pay
                    </button>
                </div>
            </form>

            <div class="mt-5">
                <span class="alert alert-danger" v-if="alert.error">
                    {{ alert.error }}
                </span>
                <span class="alert alert-success" v-if="alert.success">
                    {{ alert.success }}
                </span>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

const data = ref<{
    payment_method: string,
    amount_paid: number
}>({
    payment_method: 'CASH',
    amount_paid: 0,
})
const alert = ref<{
    success: string | null,
    error: string | null
}>({
    success: null,
    error: null,
})

const props = defineProps<{
    order_id: number,
    total_price: number,
}>()

const emit = defineEmits(['order-paid'])

async function createPayment() {
    if (data.value.amount_paid < props.total_price){
        alert.value.error = 'Amount paid is less ! '
    }
    else {
        try {
            const res = await axios.post('pos-api/get-create-payment/', {
                order: props.order_id,
                payment_method: data.value.payment_method,
                amount_paid: data.value.amount_paid
            }, {
                withCredentials: true
            })

            alert.value.success = 'PAID SUCESS'
            emit('order-paid', res.data.id)
        } catch (err) {
            alert.value.error = String(err)
        }
    }

    if (alert.value.success || alert.value.error){
        setTimeout(() => {
            alert.value.success = null
            alert.value.error = null
        }, 5000)
    }
}

onMounted( async () => {
})
</script>