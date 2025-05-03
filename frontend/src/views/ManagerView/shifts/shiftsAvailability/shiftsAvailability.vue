<template>
<div class="card">
    <div class="card-body">
        <div class="row">
            <div class="col">
                <ShiftsList @item-added="handleItemAdded"/>
            </div>
            <div class="col">
                <ShiftsSelected :id="newId"/>
            </div>
        </div>
    </div>
</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ShiftsList from './shiftsList.vue/shiftsList.vue';
import ShiftsSelected from './shiftsSelected/shiftsSelected.vue';

const newId = ref(false)

function handleItemAdded(){
    newId.value = !newId.value
}
</script>