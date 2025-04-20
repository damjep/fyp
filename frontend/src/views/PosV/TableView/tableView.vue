<template>
    <div class="container">
      <div class="container d-flex flex-row m-2 gap-1">
        <div>
          <button class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#addTable">
            + table
          </button>
        </div>
        <div>
          <button class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#editTable">
            edit table
          </button>
        </div>
      </div>

      <div v-if="tableList" class="row justify-content-center">
          <div v-for="item in tableList" :key="item.tableNo" 
          class="col-md-4 col-sm-6 col-12 mb-3" >
          <button 
          class="btn border p-3 text-center"
          :class="{ 'btn-warning': seatedTable.includes(item.tableNo) }"
          data-bs-toggle="modal" :data-bs-target="'#tableViewModal'+item.id"
          @click="handleTableClick(item)">
              <span class="fw-bold">Table No: {{ item.tableNo }}</span><br>
              <span>Max: {{ item.max_seating }} pax</span>
          </button>
          </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref, watch } from 'vue';


interface Table {
  id: number;
  tableNo: number;
  max_seating: number;
}

const tableList = ref<Table[]>([]);
const seatedTable = ref<number[]>([]);
const seatedTableData = ref<any[]>([]);

const props = defineProps<{
  tableid: number
}>()

watch(() => props.tableid, async (newTableID) => {
  if(newTableID){
    await getTableList()
  }
})
const emit = defineEmits(['tableSelected', 'orderID']);

function selectTable(id: number, order_id: number|null) {
  emit('tableSelected', id);
  emit('orderID', order_id);
}

async function getTableList() {
  try {
    const res = await axios.get('pos-api/get-table-list');
    tableList.value = res.data;
  } catch (error) {
    console.error('Error:', error);
  }
}


function handleTableClick(item: Table) {
  const foundOrderID = seatedTableData.value.find(order => order.table_number === item.tableNo);
  if (foundOrderID) {
    selectTable(item.id, foundOrderID.order_id)
    console.log("foundOrderID" + foundOrderID.order_id);
    
    
  } else {
    selectTable(item.id, null);
  }
}

async function getActiveTables() {
  try {
    const res = await axios.get<{ active_orders: any[] }>('pos-api/get-active-tables');
    seatedTableData.value = res.data.active_orders;
    seatedTable.value = res.data.active_orders.map(order => order.table_number);
  } catch (err) {
    console.error('Error loading active tables:', err);
  }
}

onMounted(async () => {
  await getTableList();
  await getActiveTables();
});
</script>


