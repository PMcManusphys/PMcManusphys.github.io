<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav class="navbar navbar-expand mb-4">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/">Curricular Comment Generator</RouterLink>
      <ul class="navbar-nav me-2 mb-2 mb-lg-0">
        <li class="nav-item">
          <RouterLink class="nav-link active" to="/">Generator</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/gradeBook">Grade Book</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/help">Help</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink class="nav-link" to="/about">About</RouterLink>
        </li>
        <li class="nav-item">
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
</style>