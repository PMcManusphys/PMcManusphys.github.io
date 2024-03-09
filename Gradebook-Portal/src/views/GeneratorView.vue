<template>
  <main>
    <div class="container">
          <CCardGroup>
            <CCard class="h-100">
              <CCardHeader>
                <h3 class="">Gain detailed insight and save time</h3>
                <!-- <h4>and save time</h4> -->
              </CCardHeader>
              <CCardBody>
                <!-- <CRow>
                  <CCol class="align-self-center col-12 col-sm-12 col-md-4 col-lg-3 col-xl-2">
                    <CCardImage orientation="top" src="src/assets/Logo1.png" class=""/>
                  </CCol>
                  <CCol> -->
                    <!-- <h3 class="mb-3">Gain detailed insight and save time</h3>
                    <h3 class="">Gain detailed insight</h3>
                    <h4 class="mb-3">and save time</h4> -->
                    <div>
                      <div class="logo-img-div float-start me-3">
                        <!-- <CCardImage orientation="top" src="src/assets/Logo1.png" class="float-start"/> -->
                      </div>
                      <!-- <p>The goal of this project is to better identify students strengths and weakness. When you generate reports on your students you will get analysis on how each students is doing on every part of the course. You will also generate a written report for each student in the form of a report card comment.</p>
                      <p>By using the set grade book available under the grade book tab you will be able to add in what concept and curricular competency each assessment focuses on.</p>
                      <p>The website deletes all data you enter as soon as you download the report. While the data is saved it is hosted on a Canadian server.</p> -->
                      
                      <span>
                        The goal of this project is to better identify students strengths and weakness. When you generate reports on your students you will get analysis on how each students is doing on every part of the course. You will also generate a written report for each student in the form of a report card comment.
                        <br /><br />
                        By using the set grade book available under the grade book tab you will be able to add in what concept and curricular competency each assessment focuses on.
                        <br /><br />
                        The website deletes all data you enter as soon as you download the report. While the data is saved it is hosted on a Canadian server.
                      </span>
                    </div>
                  <!-- </CCol>
                </CRow> -->
              </CCardBody>
            </CCard>
          </CCardGroup>
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
} from '@coreui/vue';


</script>

<style scoped>
  .logo-img-div {
    /* width: 20%; */
    width: 180px;
    height: 224.58px;
    background-color: red;
  }

  @media only screen and (max-width: 500px) {
    .logo-img-div {
      display: none;
    }
  }
</style>