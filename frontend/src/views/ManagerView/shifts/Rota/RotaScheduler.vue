<template>
    <div class="card">
        <div class="card-body">
            <DeleteShiftButton />
            <div class="row">
                <div class="col">
                    <label>Start Date</label>
                    <input type="date" class="form-control" 
                    aria-label="Start Date" v-model="startDate">
                </div>
                <div class="col">
                    <label>End Date</label>
                    <input type="date" class="form-control" 
                    aria-label="End Date" v-model="endDate">
                </div>
            </div>
            <form @submit.prevent="createRota">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Days</th>
                            <th v-for="t in type" :key="t">{{ t }}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(day, dayIndex) in days" :key="day">
                            <td>{{ day }}</td>
                            <td v-for="(shiftType, shiftIndex) in type" :key="shiftType">
                                <!-- Display shift data for the current day and shift type -->
                                <div v-for="shift in shiftsUserData" :key="shift.id">
                                    <span v-if="shift.shift_item_days === day && shift.shift_item_type === shiftType">
                                        <div class="form-check form-check-inline">
                                            <input 
                                                class="form-check-input" 
                                                type="checkbox" 
                                                :id="'checkbox-' + shift.id" 
                                                :value="shift.id" 
                                                v-model="selectedShifts[shift.id]" 
                                            />
                                            <label 
                                                class="form-check-label" 
                                                :for="'checkbox-' + shift.id"
                                            >
                                                {{ shift.user_name }} - {{ shift.user_role }}
                                            </label>
                                        </div>
                                    </span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>

                <div>
                    <button class="btn btn-success" type="submit">
                        Save
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore';
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue';
import DeleteShiftButton from './DeleteShiftAl/deleteShiftButton.vue';

const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
const type = ['AM', 'PM']
const startDate = ref()
const endDate = ref()
const selectedShifts = reactive<{ [key: string]: boolean }>({})

const userStore = useUserStore()
const shiftsUserData = ref()

async function getUsersAvail() {
    try{
        const res = await axios.get('shifts-api/test/', {
            withCredentials: true,
            headers: {
                "X-CSRFToken": userStore.getUserToken()
            }
        })

        shiftsUserData.value = res.data
    } catch (err) {}
}

async function createRota() {
    try {
        const selectedIds = Object.keys(selectedShifts).filter(id => selectedShifts[id]).map(Number)
        const res = await axios.post('shifts-api/create-get-rota/', {
            start_date: startDate.value,
            end_date: endDate.value,
            shifts: selectedIds
        }, {
            withCredentials: true,
            headers: {
                "X-CSRFToken": userStore.getUserToken()
            }
        })
    } catch(err){}
}

onMounted(async () => {
    await getUsersAvail()
})
</script>