<template>
<!-- Modal -->
<div class="modal fade" :id="'addTakeawayOrderItems'+orderId" data-bs-backdrop="static" 
data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-scrollable">
    <div class="modal-content w-auto">
      <div class="modal-header">
        <h1 class="modal-title fs-5">Takeaway {{ orderId }}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body container-fluid"
      >
        <div class=" w-100">
            <div class="card w-100">
                <div class="card-body w-100">
                    <div class="row">
                        <div class="col-md-6 mb-3 mb-md-0">
                            <TableOrderItemsListAdd :order_id="orderId" 
                            @item-added="async () => {
                                await getOrderList()
                                await getOrderInfo()
                            }"/>
                        </div>
                        <div class="col-md-6">
                            <TableOrderItemsList :order-data="orderListData" 
                            @item-deleted="async () => {
                                await getOrderList()
                                await getOrderInfo()
                            }"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6 mb-3 mb-md-0" v-if="orderInfoData">
                            <ExistingOrder :o_id="orderId" :data="orderInfoData"/>
                        </div>
                        <div class="col-md-6">
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
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
import axios from 'axios';
import TableOrderItemsList from '../../TableView/tableOrderItemsList/tableOrderItemsList.vue';
import { onMounted, ref, watch } from 'vue';
import TableOrderItemsListAdd from '../../TableView/tableOrderItemsListAdd/tableOrderItemsListAdd.vue';
import ExistingOrder from '../../posTabs/components/existingOrder.vue';


const props = defineProps<{
    orderId:number,
}>()

const orderListData = ref() 
const orderInfoData = ref()

async function getOrderList(){
    try {
        const res = await axios.get(`pos-api/${props.orderId}/items/`, 
        {withCredentials: true})

        orderListData.value = res.data
    } catch (err){}
}

async function getOrderInfo(){
    try{
        const res = await axios.get(`pos-api/get-order-by-id/${props.orderId}`, {
            withCredentials: true
        })

        orderInfoData.value = res.data
    } catch (err){

    }
}

watch(() => props.orderId, async () => {
    await getOrderList()
    await getOrderInfo()
})

onMounted( async () => {
    await getOrderList();
    await getOrderInfo()
})
</script>