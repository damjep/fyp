<template>
    <!-- Modal -->
    <div class="modal fade" id="editTable" tabindex="-1" 
     aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" >Edit Table</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="card container">
                    <div class="card-body">
                        <table class="table">
                            <thead>
                                <th>Table No</th>
                                <th>Max Seating</th>
                                <th>Save</th>
                                <th>Delete</th>
                            </thead>

                            <tbody v-if="tableListData">
                                <tr v-for="items in tableListData" :key="items.id">
                                    <td>
                                        <div class="col-sm-6">
                                            <input v-model="items.tableNo" min="0"
                                            type="number" class="form-control">
                                        </div>
                                    </td>
                                    <td>
                                        <div class="col-sm-6">
                                            <input v-model="items.max_seating" min="0"
                                            type="number" class="form-control">
                                        </div>
                                    </td>
                                    <td>
                                        <button @click="editTableByID(items.id, items.tableNo, items.max_seating)"
                                        class="btn btn-success" type="submit">
                                            save
                                        </button>
                                    </td>
                                    <td>
                                        <button @click="deleteTableByID(items.id)"
                                        class="btn btn-danger" type="submit">
                                            delete
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
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
import { onMounted, ref } from 'vue';

const tableListData = ref<{
    id: number;
    tableNo: number;
    max_seating: number;
}[]>()

const emit = defineEmits(['table-edited'])

async function getTableList() {
  try {
    const res = await axios.get('pos-api/get-table-list');
    const sorted = res.data.sort((a: any, b: any) => a.tableNo - b.tableNo)
    tableListData.value = sorted;
  } catch (error) {
    console.error('Error:', error);
  }
}

async function editTableByID(tableId: number, tn: number, ms: number) {
    try {
        const res = await axios.patch(`pos-api/edit-table/${tableId}`, {
            tableNo: tn,
            max_seating: ms
        }, {withCredentials:true})

        emit('table-edited')
        console.log(res.data)
    } catch (err) {}
}

async function deleteTableByID(tableId: number){
    try {
        const res = await axios.delete(`pos-api/edit-table/${tableId}`, {
            withCredentials: true
        })

        emit('table-edited')
        await getTableList()
    } catch (err){}
}

onMounted( async () => {
    await getTableList();
})
</script>