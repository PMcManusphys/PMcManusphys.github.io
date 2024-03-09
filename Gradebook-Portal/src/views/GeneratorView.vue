<template>
  <main>
    <!-- <div class="container">
      <IntroBlurb />
    </div> -->

    <div class="container">
      <CRow>
        <CCol>
          <!-- <CCard>
            <CCardBody>
              <CRow>
                <CCol sm="12" md="4">
                  <img alt="Company logo" class="logoImg w-100" src="@/assets/logo1.png" />
                </CCol>
                <CCol>
                  <h3>Gain detailed insight</h3>
                  <h4>and save time</h4>
                  <p>The goal of this project is to better identify students strengths and weakness. When you generate reports on your students you will get analysis on how each students is doing on every part of the course. You will also generate a written report for each student in the form of a report card comment.</p>
                  <p>By using the set grade book available under the grade book tab you will be able to add in what concept and curricular competency each assessment focuses on.</p>
                  <p>The website deletes all data you enter as soon as you download the report. While the data is saved it is hosted on a Canadian server.</p>
                </CCol>
              </CRow>
            </CCardBody>
          </CCard> -->
          <CCardGroup>
            <CCard>
              <CCardImage orientation="top" src="@/assets/Logo1.png" />
              <CImage fluid src="@/assets/Logo1.jpg" />
              <CCardBody>
                <h3>Gain detailed insight</h3>
                <h4>and save time</h4>
              </CCardBody>
            </CCard>
            <CCard>
              <CCardBody>
                <p>The goal of this project is to better identify students strengths and weakness. When you generate reports on your students you will get analysis on how each students is doing on every part of the course. You will also generate a written report for each student in the form of a report card comment.</p>
                <p>By using the set grade book available under the grade book tab you will be able to add in what concept and curricular competency each assessment focuses on.</p>
                <p>The website deletes all data you enter as soon as you download the report. While the data is saved it is hosted on a Canadian server.</p></CCardBody>
            </CCard>
          </CCardGroup>
        </CCol>
      </CRow>
    </div>
  </main>
</template>

<script setup>
import { 
  CRow, 
  CCol,
  CCard,
  CCardHeader,
  CCardBody,
  CCardImage,
  CCardGroup,
  CImage,
} from '@coreui/vue';
import IntroBlurb from '../components/IntroBlurb.vue';


</script>

<style scoped>
  
</style>