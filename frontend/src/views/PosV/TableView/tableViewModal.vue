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
      <div class="modal-body" style="height: fit-content;">

        <div v-if="orderID"
        style="display: grid; height: 75vh; 
        grid-template-columns: 1fr 1fr; 
        grid-template-rows: auto 50%; gap: 1rem;">
          <!-- First Column, First Row -->
          <div style="grid-column: 1; grid-row: 1; max-height: 50vh;" >
            <TableOrderItemsListAdd 
             :order_id="orderID" @item-added="() => {
              getOrderByID(orderID)
              getOrderItemsList(orderID)}"/>

          </div>

          <!-- Second Column, First Row -->
          <div style="grid-column: 2; grid-row: 1;">
            <TableOrderItemsList :order-data="orderItemsList" @item-deleted="() => {
              getOrderByID(orderID)
              getOrderItemsList(orderID)
            }"/>
          </div>

          <!-- Full-Width Third Row -->
          <div style="grid-column: 1 / span 2; grid-row: 2; ">
            <div class="card">
              <div class="card-body" style="height: 30vh; overflow-y: scroll;">
                <TableNewOrderAdd :t_id="id" :data="seatedData" :o_id="orderID" style="height: 20vh;" />
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
              @order-item-added="() => {
                getOrderByID(orderID)
                handleRefresh
              }"/>
            </div>

          </div>
        </div>


      <!--<div class="row">
            <div class="col">
              <TableOrderItemsList :order-data="orderItemsList"/>
            </div>
            <div class="col">
              <TableOrderItemsList :order-data="orderItemsList"/>
            </div>
        </div>
        <div class="row">
          <div class="col card">
            <div class="card-body">
              <TableNewOrderAdd :data="seatedData" />
            </div>
          </div>

          <div class="col card">
            <div class="card-body">
              <TableNewOrderAdd :data="seatedData" />
            </div>
          </div>
        </div> -->  
      </div>
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

const orderItemsList = ref()
const newOrder = ref(false)
const hide = ref('')

const handleNewOrder = () => {
  newOrder.value = true
  hide.value = 'none'
}

const handleRefresh = () => {
  newOrder.value = false
}

const seatedData = ref<{
  num_people: number,
  order_number: string,
  order_type: string,
  service_charge: string,
  status: string,
  table_Number: number,
  tips: number,
  price: string,
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
    if (newID !== null) {
        await getOrderByID(newID);
        await getOrderItemsList(newID)
    } else {
      seatedData.value = {
        num_people: 0,
        order_number: '',
        order_type: '',
        service_charge: '',
        status: '',
        table_Number: 0,
        tips: 0,
        price: '',
      }

      orderItemsList.value = null
    }
}, {immediate:true});
</script>


<style>
.custom-modal-width .modal-dialog {
  max-width: 75%;
}
</style>