<script setup>
import NoteList from './components/NoteList.vue'
const notes = [{ id: 1, body: 'First note' }]
</script>

<template>
  <main>
    <h1>Notes</h1>
    <NoteList :notes="notes" />
  </main>
</template>
