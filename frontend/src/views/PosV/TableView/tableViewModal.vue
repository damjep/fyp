<template>
<!-- Modal -->
<div class="modal fade" :id="`tableViewModal${id}`" 
     tabindex="-1" aria-labelledby="tableViewModal" aria-hidden="true">
  <div class="modal-dialog modal-xl custom-modal-width">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" :id="`tableViewModal${id}`" >View Table</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      
      <div class="modal-body container-fluid"
      >
        <div class=" w-100">
            <div class="card w-100">
                <div class="card-body w-100">
                    <div class="row">
                        <div class="col-md-6 mb-3 mb-md-0">
                            <TableOrderItemsListAdd :order_id="orderID" 
                            @item-added="async () => {
                                await getOrderItemsList(orderID)
                                await getOrderByID(orderID)
                            }"/>
                        </div>
                        <div class="col-md-6">
                            <TableOrderItemsList :order-data="orderItemsList" 
                            @item-deleted="async () => {
                                await getOrderItemsList(orderID)
                                await getOrderByID(orderID)
                            }"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6 mb-3 mb-md-0" v-if="seatedData">
                            <ExistingOrder :o_id="id" :data="seatedData"/>
                        </div>
                        <div class="col-md-6">
                            <OrderPayment v-if="seatedData" :order_id="orderID" :total_price="seatedData.total_price"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
      </div>
        <!--<div v-if="currentOrderID"
        style="display: grid; height: 75vh; 
        grid-template-columns: 1fr 1fr; 
        grid-template-rows: auto 50%; gap: 1rem;">
          <div style="grid-column: 1; grid-row: 1; max-height: 50vh;" >
            <TableOrderItemsListAdd 
             :order_id="orderID" @item-added="() => {
              getOrderByID(orderID)
              getOrderItemsList(orderID)}"/>

          </div>

          <div style="grid-column: 2; grid-row: 1;">
            <TableOrderItemsList :order-data="orderItemsList" @item-deleted="() => {
              getOrderByID(orderID)
              getOrderItemsList(orderID)
            }"/>
          </div>

          <div style="grid-column: 1 / span 2; grid-row: 2; ">
            <div class="card">
              <div class="card-body" style="height: 30vh; overflow-y: scroll;">
                <ExistingOrder v-if="seatedData" :data="seatedData" :o_id="orderID"  />
              </div>
            </div>
            
          </div>
        </div>

        <div v-else class="d-flex justify-content-center align-items-center" style="height: 70vh;">
          <div class="text-center" >

            <div :style="{display: hide}">
              <p class="bg-warning-subtle p-5 border rounded-4">No order</p>
              <button class="btn btn-primary w-100"
              @click="handleNewOrder">
                add new order
              </button>
            </div>

            <div v-if="newOrder">
              <TableNewOrderAdd :data="seatedData" :o_id='orderID' :t_id="id" 
              @order-item-added="handleRefresh"/>
            </div>

          </div>
        </div> 

      </div> -->

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>


</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';
import TableNewOrderAdd from './tableNewOrderAdd.vue';
import TableOrderItemsList from './tableOrderItemsList/tableOrderItemsList.vue';
import TableOrderItemsListAdd from './tableOrderItemsListAdd/tableOrderItemsListAdd.vue';
import ExistingOrder from '../posTabs/components/existingOrder.vue';
import PaymentModal from '../TakeAwayView/paymentModal.vue';
import OrderPayment from '../posTabs/components/orderPayment.vue';

const orderItemsList = ref()
const newOrder = ref()
const hide = ref('')
const currentOrderID = ref()

const handleRefresh = (newId: number) => {
  currentOrderID.value = newId;
  newOrder.value = false; // Hide new order form after creation
  hide.value = 'none';
};


const handleNewOrder = () => {
  newOrder.value = true
  hide.value = 'none'
}

const seatedData = ref<{
  order_number: string,
  num_people: number,
  status: string,
  total_price: number,
  service_charge: number,
  tips: number,
  order_type: string
}>()

async function getOrderByID(orderId: number) {
  try {
    const res = await axios.get(`pos-api/get-order-by-id/${orderId}`);
    seatedData.value = res.data
    console.log('Order details:', res.data);
  } catch (err) {
    console.error('Error fetching order by ID:', err);
  }
}

async function getOrderItemsList(id:number){
    try {
        const res = await axios.get(`pos-api/${id}/items`)
        orderItemsList.value = res.data
    } catch(err) {

    }
}

const props = defineProps<{
  id: number,
  orderID:  any | null,
}>()


onMounted(async () => {

})

watch(() => props.orderID, async (newID) => {

  currentOrderID.value = newID

    if (newID !== null) {
        await getOrderByID(newID);
        await getOrderItemsList(newID)
    } else {
      seatedData.value = {
        num_people: 0,
        order_number: '',
        order_type: '',
        service_charge: 0,
        status: '',
        tips: 0,
        total_price: 0,
      }

      orderItemsList.value = null
    }
}, {immediate:true});

watch(currentOrderID, async (id) => {
  if (id !== null) {
    await getOrderByID(id)
    await getOrderItemsList(id)
  }
})

</script>


<style>
.custom-modal-width .modal-dialog {
  max-width: 75%;
}
</style>