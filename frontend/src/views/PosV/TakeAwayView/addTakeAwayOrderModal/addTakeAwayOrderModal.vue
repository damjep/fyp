<template>
    <!-- Modal -->
    <div class="modal fade" id="addTakeAwayOrder" 
    data-bs-backdrop="static" data-bs-keyboard="false"
    tabindex="-1" aria-labelledby="addTakeAwayOrder" 
    aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" 
                    >Modal title</h1>
                    <button type="button" class="btn-close"
                     data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="card">
                        <div class="card-body">
                            <div class="mb-3 row">
                                <label for="orderName" 
                                class="col-sm-2 col-form-label">Order Name</label>
                                <div class="col-sm-10">
                                    <input type="text" class="form-control"
                                    id="orderName" v-model="orderName">
                                </div>
                            </div>
                            <div>
                                <button @click="addTakeAwayOrder"
                                class="btn btn-success" type="submit">
                                    Add
                                </button>
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
import { ref } from 'vue';


const orderName = ref()
const emit = defineEmits(['order-takeaway-added'])

async function addTakeAwayOrder() {
    try {
        const res = await axios.post('pos-api/add-order-by-table/', {
            order_number: orderName.value,
            num_people: 0,
            order_type: 'takeaway',
            status: 'pending'
        }, {withCredentials:true})

        emit('order-takeaway-added', res.data.id)
        orderName.value = ''

    } catch (err) {
        console.log(err)
    }
}
</script>