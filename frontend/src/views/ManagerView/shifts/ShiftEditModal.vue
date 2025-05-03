<template>
   <!-- Modal -->
    <div class="modal fade" :id="'edit'+ idx" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form @submit.prevent="editShift(data)" class="card-body row">
                <div class="modal-body">
                    <div v-if="data">
                        <div class="row">
                            <div class="input-group mb-3 col">
                                <span class="input-group-text" id="basic-addon1">ID</span>
                                <input type="text" class="form-control"
                                v-model="data.id" aria-describedby="basic-addon1" readonly>
                            </div>
                        </div>
                        
                        
                        <div class="row">
                            <div class="input-group mb-3 col">
                                <span class="input-group-text" id="basic-addon1">Days</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="data.days">
                                    <option selected>Open this select menu</option>
                                    <option v-for="day in editDataModal.days">{{ day.key }}</option>
                                </select>
                            </div>

                            <div class="input-group mb-3 col">
                                <span class="input-group-text" id="basic-addon1">Shift Type</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="data.shift_type">
                                    <option selected></option>
                                    <option v-for="shiftType in editDataModal.shift_types">{{ shiftType.key }}</option>
                                </select>
                            </div>
                        </div>

                        <div class="row">
                            <div class="input-group mb-3 col">
                                <span class="input-group-text" id="basic-addon1">Shift Start</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="data.shift_start">
                                    <option selected></option>
                                    <option v-for="shiftStart in editDataModal.hours">{{ shiftStart.key }}</option>
                                </select>
                            </div>

                            <div class="input-group mb-3 col">
                                <span class="input-group-text" id="basic-addon1">Shift End</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="data.shift_end">
                                    <option selected></option>
                                    <option v-for="shiftEnd in editDataModal.hours">{{ shiftEnd.key }}</option>
                                </select>
                            </div>
                        </div>   
                    </div>
                </div>
                <div class="modal-footer">
                    <div>
                        <span v-if="success" class="alert alert-success">
                            {{ success }}
                        </span>

                        <span v-if="er" class="alert alert-danger" >
                            {{ er }}
                        </span>
                    </div>
                    <button type="button" data-bs-dismiss="modal" class="btn btn-secondary">Close</button>
                    <button type="submit" class="btn btn-success" >Save</button>
                </div>
            </form>
            </div>
        </div>
    </div> 
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const success = ref('')
const er = ref('')

defineProps<{
    idx: string,
    data: any,
    editDataModal: any,
}>()

async function editShift(item:any) {
    try {
        await axios.patch(`shifts-api/update-shift/${item.id}`, {
            days: item.days,
            shift_type: item.shift_type,
            shift_start: item.shift_start,
            shift_end: item.shift_end,
        }, {
            withCredentials: true,
        })

        alertSuccess()
        setTimeout(() => {
            success.value = ''
        }, 2500)

        console.log('Shift edited:', item);
    } catch (err){
        console.error('Error editing shift:', err);
        er.value = "We're having trouble on our side !"

        setTimeout(() => {
            er.value = ''
        }, 2500)
    }
}

function alertSuccess() {
    success.value = "Successfully Saved"
}
</script>