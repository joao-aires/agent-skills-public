<script setup>
defineProps({ notes: { type: Array, required: true } })
</script>

<template>
  <ul>
    <li v-for="note in notes" :key="note.id">{{ note.body }}</li>
  </ul>
</template>
