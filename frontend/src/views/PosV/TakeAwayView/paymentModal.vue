<template>
    <!-- Modal -->
<div class="modal fade" :id="`takeawayPaymentModal${order_id}`"
data-bs-backdrop="static" data-bs-keyboard="false" 
tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" >Payment {{ order_id }}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <OrderPayment @order-paid="handlePaidID"
        :order_id="order_id" :total_price="total_price" />
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Understood</button>
      </div>
    </div>
  </div>
</div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import OrderPayment from '../posTabs/components/orderPayment.vue';

const paid_id = ref()

const props = defineProps<{
    order_id: number,
    total_price: number,
}>()

const emit = defineEmits(['paid'])

function handlePaidID(id: number){
    paid_id.value = id
    emit('paid', paid_id.value)
}
</script>