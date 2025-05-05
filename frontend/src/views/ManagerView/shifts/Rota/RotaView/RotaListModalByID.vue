<template>
    <!-- Modal -->
    <div class="modal fade" :id="'rota'+rotaId" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Rota ID {{ rotaId }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
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
                                    <div v-for="(item,key) in shiftsData" :key="item.id">
                                        <div v-for="shift in item.shifts_detail">
                                            <span v-if="shift.shift_item_days === day && shift.shift_item_type === shiftType">
                                                {{ shift.user_name }} - {{ shift.user_role }}
                                            </span>
                                        </div>
                                            
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    rotaId: number
    shiftsData: any
}>()

const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
const type = ['AM', 'PM']
</script>

