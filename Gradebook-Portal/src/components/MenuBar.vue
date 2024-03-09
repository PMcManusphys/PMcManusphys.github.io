<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand mb-4">
    <div class="container-fluid">
      <RouterLink class="navbar-brand text-white" to="/">Curricular Comment Generator</RouterLink>
      <ul class="navbar-nav me-2 mb-2 mb-lg-0">
        <li class="nav-item" :class="{'active': this.$route.name == 'Generator'}">
          <RouterLink class="nav-link" to="/">Generator</RouterLink>
        </li>
        <li class="nav-item" :class="{'active': this.$route.name == 'Grade Book'}">
          <RouterLink class="nav-link" to="/gradeBook">Grade Book</RouterLink>
        </li>
        <li class="nav-item" :class="{'active': this.$route.name == 'Help'}">
          <RouterLink class="nav-link" to="/help">Help</RouterLink>
        </li>
        <li class="nav-item" :class="{'active': this.$route.name == 'About'}">
          <RouterLink class="nav-link" to="/about">About</RouterLink>
        </li>
        <li class="nav-item" :class="{'active': this.$route.name == 'Contact Us'}">
          <RouterLink class="nav-link" to="/contact">Contact Us</RouterLink>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
</script>

<style scoped>
  .navbar {
    background-color: #2596be;
    height: 60px;
  }

  .active > .nav-link {
    color: white !important;
    font-weight: bold;
    border-bottom: 4px solid white;
  }

  .nav-link:hover {
    color: white;
  }
</style>