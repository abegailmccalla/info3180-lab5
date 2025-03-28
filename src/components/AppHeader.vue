<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light navbar-dark bg-primary fixed-top" :class="isDarkmode ? 'navbar-dark bg-primary dark-theme' : 'navbar'">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">VueJS with Flask</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link" :class="{ active: $route.path === '/' }">Home</RouterLink>
            </li>
            <!--
               * This is a navigation link component using Vue Router's `RouterLink`.
               * - The `class` attribute applies the "nav-link" class for styling.
          -->
            <li class="nav-item">
              <RouterLink class="nav-link" :class="{ active: $route.path === '/about' }" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :class="{ active: $route.path === '/movies' }" to="/movies">Movies</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :class="{ active: $route.path === '/movies/create' }" to="/movies/create">Add Movie</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
/**
 * This file defines the `AppHeader` component.
 * 
 * Imports:
 * - `defineProps` from Vue: Used to define props for the component.
 */
import { defineProps } from 'vue';

/**
 * Props for the AppHeader component.
 * 
 * @property {Boolean} isDarkmode - Indicates whether the dark mode is enabled.
 */
const props = defineProps({
  isDarkmode: Boolean
});
</script>

<style>
/* Add any component specific styles here */
.dark-theme {
  background-color: #1f2a3a !important; /* Dark mode */
}

.nav-link{
  color: #fff !important;
}

.nav-link:hover {
  color: #ffcc00b4 !important;
}

.nav-link.active {
  color: #ffcc00 !important;
}

</style>