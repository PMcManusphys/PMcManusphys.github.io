<script setup>

</script>

<template>
  <div class="content row p-4">
    <div class="logoDiv col-sm-4">
      <img alt="Company logo" class="logoImg" src="@/assets/logo1.png" />
    </div>

    <div class="textDiv col">
      <h1>Gain detailed insight</h1>
      <h2>and save time</h2>
      <p>The goal of this project is to better identify students strengths and weakness. When you generate reports on your students you will get analysis on how each students is doing on every part of the course. You will also generate a written report for each student in the form of a report card comment.</p>
      <p>By using the set grade book available under the grade book tab you will be able to add in what concept and curricular competency each assessment focuses on.</p>
      <p>The website deletes all data you enter as soon as you download the report. While the data is saved it is hosted on a Canadian server.</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: "IntroBlurb",
    data () {
      return {
        windowWidth: window.innerWidth
      }
    },
    mounted() {
      this.$nextTick(() => {
        window.addEventListener('resize', this.onResize);
      })
    },
    beforeUnmount() {
      window.removeEventListener('resize', this.onResize);
    },
    methods: {
      onResize() {
        this.windowWidth = window.innerWidth;
      }
    }
  }
</script>

<style scoped>
  .content {
    background-color: #E2E2E2;
    border-color: black; 
    border-style: solid;
    border-width: 1px;
    border-radius: 10px;
  }


  .logoImg {
    width: 350px;
  }

  .logoDiv, .textDiv {
    padding: 0px !important;
  }

</style>