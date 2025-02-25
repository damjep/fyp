<template>
    <!-- Modal -->
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form class="card-body " @submit.prevent="addShift">
                        <div class="">
                            <div class="input-group mb-3 ">
                                <span class="input-group-text" id="basic-addon1">Days</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="dataModalAdd.days">
                                    <option selected>Open this select menu</option>
                                    <option v-for="day in dataModal.days">{{ day.key }}</option>
                                </select>
                            </div>

                            <div class="input-group mb-3 ">
                                <span class="input-group-text" id="basic-addon1">Shift Type</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="dataModalAdd.shift_type">
                                    <option selected>Open this select menu</option>
                                    <option v-for="shiftType in dataModal.shift_types">{{ shiftType.key }}</option>
                                </select>
                            </div>
                        </div>

                        <div class="">
                            <div class="input-group mb-3 ">
                                <span class="input-group-text" id="basic-addon1">Shift Start</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="dataModalAdd.shift_start">
                                    <option selected></option>
                                    <option v-for="hourStart in dataModal.hours">{{ hourStart.key }}</option>
                                </select>
                            </div>

                            <div class="input-group mb-3 ">
                                <span class="input-group-text" id="basic-addon1">Shift End</span>
                                <select class="form-select" 
                                aria-label="Default select example" v-model="dataModalAdd.shift_end">
                                    <option selected> </option>
                                    <option v-for="hourEnd in dataModal.hours">{{ hourEnd.key }}</option>
                                </select>
                            </div>
                        </div>

                        <button type="submit" class="btn btn-success">Add</button>
                    </form>
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

const item = ref<{
    id: string,
    days: string,
    shift_type: string,
    shift_start: string,
    shift_end: string,
}>(
    {
        id: '',
        days: '',
        shift_type: '',
        shift_start: '',
        shift_end: '',
    }
)
const dataModal = ref<{
    days: [{
        key: string,
        value: string,
    }],
    shift_types: [{
        key: string,
        value: string,
    }],
    hours: [{
        key: string,
        value: string,
    }]
}>({
    days: [{
        key: '',
        value: '',
    }],
    shift_types: [{
        key: '',
        value: '',
    }],
    hours: [{
        key: '',
        value: '',
    }]
});

const dataModalAdd = ref<{
    days: string,
    shift_type: string,
    shift_start: string,
    shift_end: string,
}>({
    days: '',
    shift_type: '',
    shift_start: '',
    shift_end: '',
})

const emit = defineEmits(['dataModalAdd'])

async function getModalData() {
    try {
        const resDay = await axios.get('shifts/getShiftsDays', {
            withCredentials: true,
        })
        const resShiftType = await axios.get('shifts/getShiftTypes', {
            withCredentials: true,
        })
        const resHours = await axios.get('shifts/getHours', {
            withCredentials: true,
        })
        dataModal.value.days = resDay.data
        dataModal.value.shift_types = resShiftType.data;
        dataModal.value.hours = resHours.data;
        console.log(dataModal.value);
        emit('dataModalAdd', dataModal.value);

    } catch(err) {
        console.error(err);
    }
}

async function addShift(){
    try {
        await axios.post('shifts/get-or-create-shifts', {
            days: dataModalAdd.value.days,
            shift_type: dataModalAdd.value.shift_type,
            shift_start: dataModalAdd.value.shift_start,
            shift_end: dataModalAdd.value.shift_end,
        }, {
            withCredentials: true,
        })
        console.log('Shift added successfully');
    } catch (err) {
        console.error(err);
    }
}

onMounted(async() => {
    try{
        await getModalData();
    } catch(err){
        console.error(err);
    }
})
</script>