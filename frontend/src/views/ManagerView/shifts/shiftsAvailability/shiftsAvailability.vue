<template>
<div class="card">
    <div class="card-body">
        <div class="row">
            <div class="col">
                <ShiftsList @item-added="handleItemAdded" :id-deleted="deletedId"/>
            </div>
            <div class="col">
                <ShiftsSelected :id="newId" @item-deleted="handleItemDeleted"/>
            </div>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ShiftsList from './shiftsList.vue/shiftsList.vue';
import ShiftsSelected from './shiftsSelected/shiftsSelected.vue';

const newId = ref(0)
const deletedId = ref(0)

function handleItemDeleted(state:number){
    deletedId.value = state
}
function handleItemAdded(state: number){
    newId.value = state
}
</script>