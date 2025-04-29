<template>
    <span v-if="success">
        <div class="alert alert-success">
            {{ success }}
        </div>
    </span>
    <span v-if="error">
        <div class="alert alert-danger">
            {{ error }}
        </div>
    </span>
</template>

<script setup lang="ts">
const props = defineProps<{
    success: string,
    error: string
}>()
</script>