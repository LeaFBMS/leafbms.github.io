<script setup>
const nuxt = useNuxtApp()

console.log(nuxt)
</script>

<template>
    <div>
        Track ID: {{ $route.params.id }}
    </div>
</template>