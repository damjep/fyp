<template>
<v-card>
    <v-tabs
        v-model="tab"
        bg-color="primary"
    >
        <v-tab value="one">
            Table
        </v-tab>
        <v-tab value="two">
            Takeaway
        </v-tab>
        <v-tab value="three">
            Past Orders 
        </v-tab>
    </v-tabs>

    <v-card-text>
        <v-tabs-window v-model="tab">
            <v-tabs-window-item value="one">
                <TableView @table-selected="handleTableSelected"
                @order-i-d="handleOrderID" :tableid="newTableID" 
                :refresh="tableEdited"/>
            </v-tabs-window-item>

            <v-tabs-window-item value="two">
                <TakeAwayView @total_price="handlePrice"
                :order_id="takeawayOrderId" :paid_id="paid_id"
                @modal-takeaway-edit-items="handleNewTakeawayOrderId" :payment-reverted="boolPaymentReverted"/>
            </v-tabs-window-item>

            <v-tabs-window-item value="three">
                <PastOrderView @payment-reverted="handlePaymentReverted" :paid="paid_id"/>
            </v-tabs-window-item>
        </v-tabs-window>
    </v-card-text>
</v-card>

<!--Table Modal-->
<TableViewModal v-if="selectedTable"
 :id="selectedTable" :order-i-d="seatedData" />
<AddTableModal @table-added="handleNewTableID"/>
<EditTableModal @table-edited="handleTableEdited" />

<!--TakeAway Modal-->
<AddTakeAwayOrderModal @order-takeaway-added="handleNewTakeawayOrderId"/>
<AddOrderItemsModal :order-id="takeawayOrderId"/>
<PaymentModal @paid="handlePaidID"
:order_id="takeawayOrderId" :total_price="total_price" />
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Pos from '../Pos.vue';
import TableViewModal from '../TableView/tableViewModal.vue';
import TableView from '../TableView/tableView.vue';
import AddTableModal from '../TableView/table_add_edit/addTableModal.vue';
import EditTableModal from '../TableView/table_add_edit/editTableModal.vue';
import TakeAwayView from '../TakeAwayView/takeAwayView.vue';
import AddTakeAwayOrderModal from '../TakeAwayView/addTakeAwayOrderModal/addTakeAwayOrderModal.vue';
import AddOrderItemsModal from '../TakeAwayView/addOrderItemsModal/addOrderItemsModal.vue';
import PaymentModal from '../TakeAwayView/paymentModal.vue';
import PastOrderView from '../pastOrderView/pastOrderView.vue';

const tab = ref()
const selectedTable = ref()
const seatedData = ref()
const newTableID = ref()
const tableEdited = ref(false)
const takeawayOrderId = ref()
const total_price = ref()
const paid_id = ref()
const boolPaymentReverted = ref(false)

function handleNewTakeawayOrderId(id: number){
    takeawayOrderId.value = id
}
function handleOrderID(id:any) {
    seatedData.value = id
    console.log(seatedData.value)
}
function handleTableSelected(id: any) {
    selectedTable.value = id;
}
function handleNewTableID(id:number){
    newTableID.value = id
}
function handleTableEdited(){
    tableEdited.value = !tableEdited.value
}
function handlePrice(price: number){
    total_price.value = price
}
function handlePaidID(id: number){
    paid_id.value = id;
}
function handlePaymentReverted() {
    boolPaymentReverted.value = !boolPaymentReverted.value
}

</script>