<template>
      <footer class="mt-5">
          <div class="container" :class="containerClass">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
</template>

<script setup>
import { ref, defineProps } from "vue";

const year = (new Date).getFullYear();
</script>

<style scoped>

.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container-light-theme {
  color: black;
}

.container-dark-theme {
  color: #d4d4d4;
}

p {
  font-family: "Georgia", "Times New Roman", serif;
  bottom: 0px;
  position: absolute;
}
</style>




