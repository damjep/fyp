<template>
  <!-- Modal -->
  <div class="modal fade" :id="`tableViewModal${id}`" 
       tabindex="-1" aria-labelledby="tableViewModal" aria-hidden="true">
    <div class="modal-dialog modal-xl custom-modal-width">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" :id="`tableViewModal${id}`">View Table {{ seatedData?.table_no_str }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        
        <div class="modal-body container-fluid">
          <div class="w-100">
            <div class="card w-100">
              <div class="card-body w-100" v-if="activeOrderID && !newOrder">
                <div class="row">
                  <div class="col-md-6 mb-3 mb-md-0">
                    <TableOrderItemsListAdd :order_id="activeOrderID" 
                      @item-added="refreshOrderData"/>
                  </div>
                  <div class="col-md-6">
                    <TableOrderItemsList :order-data="orderItemsList" 
                      @item-deleted="refreshOrderData"/>
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-6 mb-3 mb-md-0" v-if="seatedData">
                    <ExistingOrder 
                      :o_id="activeOrderID" :data="seatedData" :table_number="id"/>
                  </div>
                  <div class="col-md-6" v-if="activeOrderID">
                    <OrderPayment v-if="seatedData" :order_id="activeOrderID" :total_price="seatedData.total_price"/>
                  </div>
                </div>
              </div>
  
              <div v-else>
                <NewOrder @order-added="handleNewOrder" :table_Number="id" />
              </div>
            </div>
          </div>
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
  import { onMounted, ref, watch, computed } from 'vue';
  import TableNewOrderAdd from './tableNewOrderAdd.vue';
  import TableOrderItemsList from './tableOrderItemsList/tableOrderItemsList.vue';
  import TableOrderItemsListAdd from './tableOrderItemsListAdd/tableOrderItemsListAdd.vue';
  import ExistingOrder from '../posTabs/components/existingOrder.vue';
  import PaymentModal from '../TakeAwayView/paymentModal.vue';
  import OrderPayment from '../posTabs/components/orderPayment.vue';
  import NewOrder from '../posTabs/components/newOrder.vue';
  
  const orderItemsList = ref();
  const newOrder = ref(0);
  const currentOrderID = ref();
  
  const props = defineProps<{
    id: number,
    orderID: any | null,
  }>();
  
  const seatedData = ref({
    order_number: '',
    num_people: 0,
    status: '',
    total_price: 0,
    service_charge: 0,
    tips: 0,
    order_type: '',
    table_Number: 0,
    table_no_str: ''
  });
  
  const activeOrderID = computed(() => {
    return newOrder.value !== 0 ? newOrder.value : props.orderID;
  });
  
  function handleNewOrder(id: number) {
    newOrder.value = id;
  }
  
  async function getOrderByID(orderId: number) {
    try {
      const res = await axios.get(`pos-api/get-order-by-id/${orderId}`);
      seatedData.value = res.data;
      console.log('Order details:', res.data);
    } catch (err) {
      console.error('Error fetching order by ID:', err);
    }
  }
  
  async function getOrderItemsList(id: number) {
    try {
      const res = await axios.get(`pos-api/${id}/items`);
      orderItemsList.value = res.data;
    } catch (err) {
      console.error('Error fetching order items:', err);
    }
  }
  
  async function refreshOrderData() {
    if (activeOrderID.value) {
      await getOrderByID(activeOrderID.value);
      await getOrderItemsList(activeOrderID.value);
    }
  }
  
  onMounted(refreshOrderData);
  
  watch(() => props.orderID, refreshOrderData, { immediate: true });
  watch(newOrder, refreshOrderData);
  </script>
  
  <style>
  .custom-modal-width .modal-dialog {
    max-width: 75%;
  }
  </style>
  