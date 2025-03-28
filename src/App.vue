<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import { ref, computed } from 'vue'

/* - `isDarkmode`: A boolean prop that determines whether the application is in dark mode. */
const isDarkmode = ref(true);

/**
 * Toggles the theme between dark mode and light mode.
 * 
 * This function updates the `isDarkmode` reactive variable to switch
 * between dark mode and light mode. It also updates the `document.body`
 * class list to reflect the current theme:
 * - Adds the 'dark-mode' class and removes the 'light-mode' class when switching to dark mode.
 * - Adds the 'light-mode' class and removes the 'dark-mode' class when switching to light mode.
 */
const toggleTheme = () => {
    isDarkmode.value = !isDarkmode.value;
    if (isDarkmode.value){
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-mode');
    } else {
        document.body.classList.remove('dark-mode');
        document.body.classList.add('light-mode');
    }
}

/**
 * A computed property that determines the CSS class for a button
 * based on the current dark mode state.
 *
 * @returns {string} - Returns 'btn-dark' if dark mode is disabled,
 *                     otherwise returns 'btn-light'.
 */
const state = computed (() => {
  return !isDarkmode.value ? 'btn-dark' : 'btn-light';
});
</script>

<template>
  <!--
    This line renders the `AppHeader` component and passes a prop named `isDarkmode` to it.
  -->
  <AppHeader :isDarkmode="isDarkmode" />

  <main>
    <button class="btn toggle" :class="state" @click="toggleTheme">Switch Mode</button>
    <RouterView :isDarkmode="isDarkmode" />
  </main>

  <AppFooter :isDarkmode="isDarkmode" />
</template>


<style>

body {
  padding-top: 75px;
  position: relative;
}

body.dark-mode {
  background-color: #121d33;
  color: #d4d4d4;
}

body.light-mode {
    background-color: #fff;
    color: black;
}

.toggle {
  top: 70px;
  right: 10px;
  position: absolute;
}

</style>