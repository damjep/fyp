<template>
    <div>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" 
        data-bs-toggle="modal" data-bs-target="#addTakeAwayOrder">
        Add New Takeaway Order
        </button>
    </div>

    <div class="container card">
        <div class="card-body">
            <table class="table">
                <thead>
                    <tr>
                        <th>Takeaway Order</th>
                        <th>Total Price</th>
                        <th>Edit</th>
                        <th>Payment</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-if="takeawayOrderList" v-for="items in takeawayOrderList" :id="items.id">
                        <td>{{ items.order_number }}</td>
                        <td>{{ items.total_price }}</td>
                        <td>
                            <button type="button" class="btn btn-primary" 
                            data-bs-toggle="modal" :data-bs-target="'#addTakeawayOrderItems'+items.id"
                            @click="() => emit('modal-takeaway-edit-items', items.id)">
                            Edit
                            </button>
                        </td>
                        <td>
                            <button type="button" class="btn btn-secondary" 
                            data-bs-toggle="modal" :data-bs-target="'#takeawayPaymentModal'+items.id"
                            @click="() => {
                                emit('modal-takeaway-edit-items', items.id)
                                emit('total_price', items.total_price)
                                }">
                            Payment
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';

const takeawayOrderList = ref()

const emit = defineEmits(['modal-takeaway-edit-items', 'total_price'])

const props = defineProps<{
    order_id: number, 
    paid_id: number,
    paymentReverted: boolean,
}>()

async function getTakeawayOrderList() {
    try {
        const res = await axios.get('pos-api/add-order-by-table/')
        takeawayOrderList.value = res.data.filter((a:any) => a.order_type == 'takeaway' && a.status == 'pending')
    } catch (err) {
        console.log(err)
    }
}

watch(
  () => [props.order_id, props.paid_id, props.paymentReverted],
  async () => {
    await getTakeawayOrderList()
  },
  { immediate: true }
)


onMounted( async () => {
    await getTakeawayOrderList()
})


</script>