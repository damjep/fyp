<template>
    
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary m-2" 
    data-bs-toggle="modal" data-bs-target="#staticBackdrop">
        Add Shifts
    </button>

    <div>
        <ShiftAddModal @data-modal-add="handleDataModal"/>
    </div>

    <div v-if="shifts">
        <div v-for="item in shifts" class="card m-2">
            <form @submit.prevent="editShift(item)" class="card-body row">

                <div class="row">
                    <div class="input-group mb-3 col">
                        <span class="input-group-text" id="basic-addon1">ID</span>
                        <input type="text" class="form-control"
                        v-model="item.id" aria-describedby="basic-addon1" readonly>
                    </div>

                    <div class="col flex">
                        <button type="submit" class="btn btn-success w-50">Save</button>
                        <button type="button" class="btn btn-danger w-50">Delete</button>
                    </div>
                </div>
                
                
                <div class="row">
                    <div class="input-group mb-3 col">
                        <span class="input-group-text" id="basic-addon1">Days</span>
                        <select class="form-select" 
                        aria-label="Default select example" v-model="item.days">
                            <option selected>Open this select menu</option>
                            <option v-for="day in dataModal.days">{{ day.key }}</option>
                        </select>
                    </div>

                    <div class="input-group mb-3 col">
                        <span class="input-group-text" id="basic-addon1">Shift Type</span>
                        <select class="form-select" 
                        aria-label="Default select example" v-model="item.shift_type">
                            <option selected></option>
                            <option v-for="shiftType in dataModal.shift_types">{{ shiftType.key }}</option>
                        </select>
                    </div>
                </div>

                <div class="row">
                    <div class="input-group mb-3 col">
                        <span class="input-group-text" id="basic-addon1">Shift Start</span>
                        <select class="form-select" 
                        aria-label="Default select example" v-model="item.shift_start">
                            <option selected></option>
                            <option v-for="shiftStart in dataModal.hours">{{ shiftStart.key }}</option>
                        </select>
                    </div>

                    <div class="input-group mb-3 col">
                        <span class="input-group-text" id="basic-addon1">Shift End</span>
                        <select class="form-select" 
                        aria-label="Default select example" v-model="item.shift_end">
                            <option selected></option>
                            <option v-for="shiftEnd in dataModal.hours">{{ shiftEnd.key }}</option>
                        </select>
                    </div>
                </div>
            </form>
        </div>
        
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import ShiftAddModal from './ShiftAddModal.vue';

const shifts = ref();
const dataModal = ref<{
    days: Array<{ key: string, value: string }>,
    shift_types: Array<{ key: string, value: string }>,
    hours: Array<{ key: string, value: string }>,
}>({
    days: [],
    shift_types: [],
    hours: [],
});

const handleDataModal = (x: any) => {
    dataModal.value = x
}

async function fetchShifts() {
    try {
        const response = await axios.get('shifts/get-or-create-shifts', {
            withCredentials: true,
        })

        shifts.value = response.data;
        console.log('Fetched shifts:', response.data);

    } catch (error) {
        console.error('Error fetching shifts:', error);
    }
}

async function editShift(item:any) {
    try {
        await axios.patch(`/shifts/update-shift/${item.id}`, {
            days: item.days,
            shift_type: item.shift_type,
            shift_start: item.shift_start,
            shift_end: item.shift_end,
        }, {
            withCredentials: true,
        })

        console.log('Shift edited:', item);
    } catch (err){
        console.error('Error editing shift:', err);
    }
}

onMounted(async() => {
    try {
        await fetchShifts();
    } catch (err) {
        console.error('Error mounting component:', err);
    }
})
</script>