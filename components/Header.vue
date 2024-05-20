<script setup>
import "@/assets/main.scss";
import {ref, onMounted, onUnmounted} from "vue";

const isScrolled = ref(false);

// Function to handle scroll event
const handleScroll = () => {
  isScrolled.value = window.scrollY > 0;
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<template>
  <div :class="{scrolled: isScrolled}" class="header">
    <ul style="margin-top: 10px">
      <li>
        <NuxtLink to="/">
          <IconsLogo />
        </NuxtLink>
      </li>
      <li style="display: flex; align-items: center">
        <NuxtLink to="/about" style="margin-right: 20px">About</NuxtLink>
        <NuxtLink to="/discography">Discography</NuxtLink>
      </li>
    </ul>
  </div>
</template>
