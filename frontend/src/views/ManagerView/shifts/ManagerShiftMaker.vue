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
        <table  class="table">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Days</th>
                    <th scope="col">Shift Type</th>
                    <th scope="col">Shift Start & End</th>
                    <th scope="col">Edit</th>
                </tr>
            </thead>
            <tbody v-for="x in shifts">
                <tr  :key="x.id">
                    <th scope="row">{{ x.id }}</th>
                    <td >{{ x.days }}</td>
                    <td >{{ x.shift_type }}</td>
                    <td>Time: {{ x.shift_start }} - {{ x.shift_end }}</td>
                    <!-- Button trigger modal -->
                    <td>
                        <button type="button" class="btn btn-primary m-2" 
                        data-bs-toggle="modal" :data-bs-target="`#edit${x.id}`">
                            Edit Shifts
                        </button>
                    </td>
                </tr>

                <div v-if="x">
                    <ShiftEditModal :idx="x.id" :data="x" :edit-data-modal="dataModal" />
                </div>
            </tbody>
        </table>
    </div>

</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';
import ShiftAddModal from './ShiftAddModal.vue';
import ShiftEditModal from './ShiftEditModal.vue';

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

onMounted(async() => {
    try {
        await fetchShifts();
    } catch (err) {
        console.error('Error mounting component:', err);
    }
})
</script>