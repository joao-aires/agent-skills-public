<script setup>
defineProps({ note: { type: Object, required: true } })
</script>

<template>
  <article>{{ note.body }}</article>
</template>
