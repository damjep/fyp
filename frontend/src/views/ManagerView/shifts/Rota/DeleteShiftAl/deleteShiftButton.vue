<template>
<!-- Button trigger modal -->
    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteShiftAllModal">
    Delete All Staff Shift Availability
    </button>

    <DeleteShifttModal />
</template>

<script setup lang="ts">
import DeleteShifttModal from './deleteShifttModal.vue';

</script>