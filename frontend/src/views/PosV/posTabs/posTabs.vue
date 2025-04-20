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
            Pos
        </v-tab>
        <v-tab value="three">Item Three</v-tab>
    </v-tabs>

    <v-card-text>
        <v-tabs-window v-model="tab">
        <v-tabs-window-item value="one">
            <TableView @table-selected="handleTableSelected"
            @order-i-d="handleOrderID" :tableid="newTableID"/>
        </v-tabs-window-item>

        <v-tabs-window-item value="two">
            <Pos />
        </v-tabs-window-item>

        <v-tabs-window-item value="three">
            Three
        </v-tabs-window-item>
        </v-tabs-window>
    </v-card-text>
</v-card>

<TableViewModal v-if="selectedTable" :id="selectedTable" :order-i-d="seatedData" />
<AddTableModal @table-added="handleNewTableID"/>
<EditTableModal />
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Pos from '../Pos.vue';
import TableViewModal from '../TableView/tableViewModal.vue';
import TableView from '../TableView/tableView.vue';
import AddTableModal from '../TableView/table_add_edit/addTableModal.vue';
import EditTableModal from '../TableView/table_add_edit/editTableModal.vue';

const tab = ref()
const selectedTable = ref()
const seatedData = ref()
const newTableID = ref()

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
</script>