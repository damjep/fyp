<template>
    <!-- Modal -->
    <div class="modal fade" id="addTable" aria-labelledby="exampleModalLabel" tabindex="-1" 
     aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" >Add Table Modal</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="card container" >
                    <div class="card-body ">
                        <form @submit.prevent="addTable()">
                            <div class="mb-3 row">
                                <label for="tn" 
                                class="col-sm-4 col-form-label">Table Number</label>
                                <div class="col-sm-6">
                                    <input v-model="newTableData.table_no"
                                    type="number" class="form-control" id="tn">
                                </div>
                            </div>

                            <div class="mb-3 row">
                                <label for="ms" 
                                class="col-sm-4 col-form-label">Max Seating</label>
                                <div class="col-sm-6">
                                    <input v-model="newTableData.max_seating"
                                    type="number" class="form-control" id="ms">
                                </div>
                            </div>

                            <div>
                                <button class="btn btn-success" type="submit">
                                    Save
                                </button>
                            </div>
                        </form>
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
import { ref } from 'vue';

const emit = defineEmits(['table-added'])
const newTabID = ref()

const newTableData = ref<{
    table_no : number,
    max_seating: number,
}>(
    {
        table_no: 0,
        max_seating: 0
    }
)

async function addTable() {
    try {
        const res = await axios.post('pos-api/get-table-list/', {
            tableNo: newTableData.value.table_no,
            max_seating: newTableData.value.max_seating
        }, {withCredentials: true})

        newTabID.value = res.data.id
        newTableData.value.max_seating = 0
        newTableData.value.table_no = 0

        emit('table-added', newTabID.value)
    } catch (err) {

    }
}
</script>