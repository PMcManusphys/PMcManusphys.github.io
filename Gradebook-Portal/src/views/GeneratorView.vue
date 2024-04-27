<template>
  <main>
    <div class="container">
      <CCardGroup class="mb-5">
        <CCard class="h-100">
          <CCardHeader>
            <h3 class="mb-0">Report Generator</h3>
          </CCardHeader>
          <CCardBody>
            <CForm>
              <CRow>
                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="course-name-input" class="mb-1">Course Name</CFormLabel>
                  <CFormInput
                    type="text"
                    id="course-name-input"
                    placeholder="English-Fall-2024"
                    aria-describedby="course-name-help-text"
                    v-model="formFields.courseName"
                  />
                  <CFormText as="span" id="course-name-help-text">
                    Please write the course name. This name will be used in the report comments.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="output-file-name-input" class="mb-1">Output File Name</CFormLabel>
                  <CFormInput
                    type="text"
                    id="output-file-name-input"
                    placeholder="English-Comment-Report-Fall-2024"
                    aria-describedby="output-file-name-help-text"
                    v-model="formFields.outputFileName"
                  />
                  <CFormText as="span" id="output-file-name-help-text">
                    Please write the file name you would like your report file to be called.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="district-id-input" class="mb-1">District ID</CFormLabel>
                  <CFormInput
                    type="text"
                    id="district-id-input"
                    placeholder="sd36"
                    aria-describedby="district-id-help-text"
                    v-model="formFields.districtId"
                  />
                  <CFormText as="span" id="district-id-help-text">
                    Please enter your district ID, this will be used for comment wording on proficiency scale.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="grade-book-input" class="mb-1">Grade Book File</CFormLabel>
                  <CFormInput
                    type="file"
                    id="grade-book-input"
                    aria-describedby="grade-book-help-text"
                    class="form-label-text"
                    v-model="formFields.gradebookFile"
                  />
                  <CFormText as="span" id="grade-book-help-text">
                    Please upload your grade book file. A template file can be downloaded from the 'Grade Book' page.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="comment-focus-input" class="mb-1">Focus of Comments</CFormLabel>
                  <div class="ms-2">
                    <CFormCheck
                      type="radio"
                      id="comment-focus-input-1"
                      label="Focus on best and worse concepts and compentences"
                      value="bestWorst"
                      class="form-label-text"
                      v-model="formFields.commentFocus"
                    />
                    <CFormCheck
                      type="radio"
                      id="comment-focus-input-2"
                      label="Focus on all concepts and compentences"
                      value="all"
                      class="form-label-text"
                      v-model="formFields.commentFocus"
                    />
                  </div>
                  <CFormText as="span" id="comment-focus-help-text">
                    What would you like the report comments to focus on?
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="zero-grades-input" class="mb-1">Handling of 0% Grades</CFormLabel>
                  <div class="ms-2">
                    <CFormCheck
                      type="radio"
                      name="zero-grades-input"
                      id="zero-grades-input-1"
                      label="Treat 0% as the grade for the assessment"
                      value="assessmentGrade"
                      class="form-label-text"
                      v-model="formFields.zeroGradeHandling"
                    />
                    <CFormCheck
                      type="radio"
                      name="zero-grades-input"
                      id="zero-grades-input-2"
                      label="Treat 0% as an excused assessment"
                      value="excusedAssessment"
                      class="form-label-text"
                      v-model="formFields.zeroGradeHandling"
                    />
                  </div>
                  <CFormText as="span" id="zero-grades-help-text">
                    How would you like grades of 0% to be handled.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="assessment-weights-input" class="mb-1">Assessment Weighting</CFormLabel>

                  <CTable id="assessment-weights-input" class="mb-1" small>
                    <CTableHead>
                      <CTableRow>
                        <CTableHeaderCell scope="col" class="font-14 border-top-0 pt-0">
                          Assessment Type
                        </CTableHeaderCell>
                        <CTableHeaderCell scope="col" class="font-14 border-top-0 pt-0">
                          Assessment Weight
                        </CTableHeaderCell>
                        <CTableHeaderCell scope="col" class="border-top-0 pt-0" />
                      </CTableRow>
                    </CTableHead>
                    <CTableBody>
                      <CTableRow v-for="assessment of formFields.assessmentWeights">
                        <CTableDataCell class="form-label-text align-middle">{{ assessment.type }}</CTableDataCell>
                        <CTableDataCell class="form-label-text align-middle">{{ assessment.weight }}%</CTableDataCell>
                        <CTableDataCell>
                          <CButton
                            class="w-100"
                            color="danger"
                            variant="outline"
                            @click="removeAssessmentWeight(assessment.type)"
                            size="sm"
                          >
                            <CIcon icon="cilMinus" size="" class="me-2" />Remove
                          </CButton>
                        </CTableDataCell>
                      </CTableRow>
                      <CTableRow>
                        <CTableDataCell class="border-bottom-0">
                          <CFormSelect
                            aria-label="Default select example"
                            :options="assessmentOptions"
                            size="sm"
                            v-model="newAssessType"
                            class="form-label-text"
                          />
                        </CTableDataCell>
                        <CTableDataCell class="border-bottom-0">
                          <CFormInput
                            type="number"
                            placeholder="Weight (%)"
                            min="0"
                            max="100"
                            size="sm"
                            v-model="newAssessWeight"
                          />
                        </CTableDataCell>
                        <CTableDataCell class="border-bottom-0">
                          <CButton
                            class="btn-primary-bg w-100"
                            color="primary"
                            @click="addAssessmentWeight()"
                            size="sm"
                            :disabled="disableAssessmentTypeAdd"
                          >
                            <CIcon icon="cilPlus" size="" class="me-2" />Add Type
                          </CButton>
                        </CTableDataCell>
                      </CTableRow>
                    </CTableBody>
                  </CTable>

                  <CFormText as="span" id="assessment-weights-help-text">
                    How you would like to weight the different assessment types.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="grading-type-input" class="mb-1">Grading Type</CFormLabel>
                  <div class="ms-2">
                    <CFormCheck
                      type="radio"
                      name="grading-type-input"
                      id="grading-type-input-1"
                      label="Proficiency Scale (out of 4)"
                      value="profScale"
                      class="form-label-text"
                      v-model="formFields.gradingType"
                    />
                    <CFormCheck
                      type="radio"
                      name="grading-type-input"
                      id="grading-type-input-2"
                      label="Traditional Grading"
                      value="tradGrade"
                      class="form-label-text"
                      v-model="formFields.gradingType"
                    />
                  </div>
                  <CFormText as="span" id="grading-type-help-text">
                    Which grading type is this course using?
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="scale-thresholds-input" class="mb-1">Proficiency Scale Thresholds</CFormLabel>

                  <CTable id="scale-thresholds-input" class="mb-1" small>
                    <CTableHead>
                      <CTableRow>
                        <CTableHeaderCell scope="col" class="font-14 border-top-0 pt-0">Grade Scale</CTableHeaderCell>
                        <CTableHeaderCell scope="col" class="font-14 border-top-0 pt-0">
                          Lowest Eligible Grade (%)
                        </CTableHeaderCell>
                      </CTableRow>
                    </CTableHead>
                    <CTableBody>
                      <CTableRow>
                        <CTableDataCell class="form-label-text align-middle">Extending</CTableDataCell>
                        <CTableDataCell>
                          <CFormInput
                            type="number"
                            placeholder="Lowest Grade"
                            min="0"
                            max="100"
                            size="sm"
                            v-model="formFields.proficiencyTresholds.extending"
                          />
                        </CTableDataCell>
                      </CTableRow>
                      <CTableRow>
                        <CTableDataCell class="form-label-text align-middle">Proficient</CTableDataCell>
                        <CTableDataCell>
                          <CFormInput
                            type="number"
                            placeholder="Lowest Grade"
                            min="0"
                            max="100"
                            size="sm"
                            v-model="formFields.proficiencyTresholds.proficient"
                          />
                        </CTableDataCell>
                      </CTableRow>
                      <CTableRow>
                        <CTableDataCell class="form-label-text align-middle">Developing</CTableDataCell>
                        <CTableDataCell>
                          <CFormInput
                            type="number"
                            placeholder="Lowest Grade"
                            min="0"
                            max="100"
                            size="sm"
                            v-model="formFields.proficiencyTresholds.developing"
                          />
                        </CTableDataCell>
                      </CTableRow>
                      <CTableRow>
                        <CTableDataCell class="form-label-text align-middle">Emerging</CTableDataCell>
                        <CTableDataCell>
                          <CFormInput
                            type="number"
                            placeholder="Lowest Grade"
                            min="0"
                            max="100"
                            size="sm"
                            v-model="formFields.proficiencyTresholds.emerging"
                          />
                        </CTableDataCell>
                      </CTableRow>
                    </CTableBody>
                  </CTable>

                  <CFormText as="span" id="scale-thresholds-help-text">
                    Minimum thresholds for proficiency scale levels.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4">
                  <CFormLabel for="competency-weighting-input" class="mb-1">
                    Concepts & Curricular Competency Weighting
                    <CIcon
                      icon="cilMagnifyingGlass"
                      size="lg"
                      class="tool-tip ms-2"
                      @click="
                        () => {
                          visibleScrolling = !visibleScrolling;
                        }
                      "
                    />
                  </CFormLabel>
                  <div class="ms-2">
                    <CFormCheck
                      type="radio"
                      name="competency-weighting-input"
                      id="competency-weighting-input-1"
                      label="No extra weighting"
                      value="none"
                      class="form-label-text"
                      v-model="formFields.competencyWeightingType"
                    />
                    <CFormCheck
                      type="radio"
                      name="competency-weighting-input"
                      id="competency-weighting-input-2"
                      label="Amount Based"
                      value="amount"
                      class="form-label-text"
                      v-model="formFields.competencyWeightingType"
                    />
                    <CFormCheck
                      type="radio"
                      name="competency-weighting-input"
                      id="competency-weighting-input-3"
                      label="Time Based"
                      value="time"
                      class="form-label-text"
                      v-model="formFields.competencyWeightingType"
                    />
                    <CFormCheck
                      type="radio"
                      name="competency-weighting-input"
                      id="competency-weighting-input-4"
                      label="Time & Amount Based"
                      value="amountTime"
                      class="form-label-text"
                      v-model="formFields.competencyWeightingType"
                    />
                  </div>
                  <CFormText as="span" id="competency-weighting-help-text">
                    This weighting only affects the calculations of compencies.
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4" v-if="isUsingAmountScaling">
                  <CFormLabel for="assessment-scale-input" class="mb-1">
                    Concepts & Curricular Competency Scaling
                  </CFormLabel>
                  <CFormInput
                    type="number"
                    id="assessment-scale-input"
                    placeholder="Scale"
                    aria-describedby="assessment-scale-help-text"
                    min="0"
                    max="1"
                    v-model="formFields.assessmentScaling"
                  />
                  <CFormText as="span" id="assessment-scale-help-text">
                    Please enter the scale you would like (between 0 and 1). 1 is maximum amount of scale (about 50%
                    more weighting on some assignments.) 0 is almost no scaling (about 5% weighting on some
                    assignments).
                  </CFormText>
                </CCol>

                <CCol class="col-12 col-md-6 mb-4" v-if="isUsingTimeScaling">
                  <CFormLabel for="assessment-order-input" class="mb-1">Assessment Ordering</CFormLabel>
                  <div class="ms-2">
                    <CFormCheck
                      type="radio"
                      name="assessment-order-input"
                      id="assessment-order-input-1"
                      label="Leftmost assessment is the earliest assessment"
                      value="leftmostOld"
                      class="form-label-text"
                      v-model="formFields.assessmentOrder"
                    />
                    <CFormCheck
                      type="radio"
                      name="assessment-order-input"
                      id="assessment-order-input-2"
                      label="Leftmost assessment is the newest assessment"
                      value="leftmostNew"
                      class="form-label-text"
                      v-model="formFields.assessmentOrder"
                    />
                  </div>
                  <CFormText as="span" id="assessment-order-help-text">
                    What order have you entered your grade book data?
                  </CFormText>
                </CCol>

                <CCol
                  class="col-12 col-md-6 mt-4 align-self-end"
                  :class="{ 'offset-md-6': isUsingAmountScaling == isUsingTimeScaling }"
                >
                  <CRow>
                    <CCol class="col-4 pe-2">
                      <CButton class="w-100" color="secondary" @click="resetFields()"> Reset </CButton>
                    </CCol>
                    <CCol class="col-8 ps-2">
                      <CButton class="w-100 btn-primary-bg" color="primary" @click="generateReport()">
                        Generate Report
                      </CButton>
                    </CCol>
                  </CRow>
                </CCol>
              </CRow>
            </CForm>
          </CCardBody>
        </CCard>
      </CCardGroup>

      <CToaster class="p-3 error-toaster" placement="top-end">
        <CToast v-for="(toast, index) in toasts" visible :key="index" delay="6500" class="error-toast p-3">
          <CIcon icon="cilThumbDown" size="3xl" class="float-left me-3" />
          <span>{{ toast.content }}</span>
        </CToast>
      </CToaster>

      <COffcanvas
        placement="end"
        scroll
        :visible="visibleScrolling"
        @hide="
          () => {
            visibleScrolling = !visibleScrolling;
          }
        "
        class="help-canvas"
      >
        <COffcanvasHeader class="help-canvas-header">
          <COffcanvasTitle>
            <CRow>
              <CCol class="col-3">
                <CIcon
                  icon="cilMagnifyingGlass"
                  size="3xl"
                  class="position-absolute top-50 start-50 translate-middle"
                  title="Help"
                />
              </CCol>
              <CCol class="col-9 ps-0">Concepts & Curricular Competency Weighting</CCol>
            </CRow>
          </COffcanvasTitle>
          <CCloseButton
            class="text-reset"
            @click="
              () => {
                visibleScrolling = false;
              }
            "
          />
        </COffcanvasHeader>
        <COffcanvasBody class="help-canvas-body">
          <p class="font-15">
            Pick your weighting for Concepts and Curricular Competency, please note that this will not affect the
            overall mark.
          </p>

          <hr class="bg-primary mt-2 mb-3" />

          <h6 class="text-secondary-color mb-1">No Extra Weighting</h6>
          <p class="font-14">
            This weighting option will count assessments as less the more different Concepts or Curricular Competency.
            The idea here is assessments that just cover one Concept or Curricular Competency should have a larger
            impact on the mark of that Concept or Curricular Competency than assessments with multiple.
          </p>

          <h6 class="text-secondary-color mb-1">Amount Based</h6>
          <p class="font-14">
            This weighting option will count assessments as less the more different Concepts or Curricular Competency.
            The idea here is assessments that just cover one Concept or Curricular Competency should have a larger
            impact on the mark of that Concept or Curricular Competency than assessments with multiple.
          </p>

          <h6 class="text-secondary-color mb-1">Time Base</h6>
          <p class="font-14">
            This weighting option adds more weighting for assessments that are newer. The idea here is assessments that
            are more recent are better at showing where the student currently is at. While not weighting assessments
            that cover more Concept or Curricular Competency less than ones that only cover one.
          </p>

          <h6 class="text-secondary-color mb-1">Time & Amount Based</h6>
          <p class="font-14">
            This will add no extra weighting. The Concepts and Curricular Competencies will be marked only based on
            assessment type weighting.
          </p>
        </COffcanvasBody>
      </COffcanvas>
    </div>
  </main>
</template>

<script>
import {
  CRow,
  CCol,
  CCard,
  CCardHeader,
  CCardBody,
  CCardImage,
  CCardGroup,
  CForm,
  CFormLabel,
  CFormInput,
  CFormText,
  CFormCheck,
  CTable,
  CTableHead,
  CTableRow,
  CTableHeaderCell,
  CTableBody,
  CTableDataCell,
  CFormSelect,
  CButton,
  CToaster,
  CToast,
  CToastClose,
  CPopover,
  COffcanvas,
  COffcanvasHeader,
  COffcanvasTitle,
  CCloseButton,
  COffcanvasBody,
} from '@coreui/vue';

export default {
  name: 'generator-view',
  components: {
    CRow,
    CCol,
    CCard,
    CCardHeader,
    CCardBody,
    CCardImage,
    CCardGroup,
    CForm,
    CFormLabel,
    CFormInput,
    CFormText,
    CFormCheck,
    CTable,
    CTableHead,
    CTableRow,
    CTableHeaderCell,
    CTableBody,
    CTableDataCell,
    CFormSelect,
    CButton,
    CToaster,
    CToast,
    CToastClose,
    CPopover,
    COffcanvas,
    COffcanvasHeader,
    COffcanvasTitle,
    CCloseButton,
    COffcanvasBody,
  },
  data() {
    return {
      assessmentOptions: [
        {
          label: '- Assessment Type -',
          value: '',
        },
        {
          label: 'Assignments',
          value: 'Assignments',
        },
        {
          label: 'Essays',
          value: 'Essays',
        },
        {
          label: 'Final Exam',
          value: 'Final Exam',
        },
        {
          label: 'Homework',
          value: 'Homework',
        },
        {
          label: 'Labs',
          value: 'Labs',
        },
        {
          label: 'Midterms',
          value: 'Midterms',
        },
        {
          label: 'Presentations',
          value: 'Presentations',
        },
        {
          label: 'Projects',
          value: 'Projects',
        },
        {
          label: 'Quizzes',
          value: 'Quizzes',
        },
        {
          label: 'Tests',
          value: 'Tests',
        },
      ],
      formFields: {
        courseName: '',
        outputFileName: '',
        districtId: '',
        commentFocus: 'bestWorst',
        zeroGradeHandling: 'assessmentGrade',
        gradingType: 'profScale',
        proficiencyTresholds: {
          extending: null,
          proficient: null,
          developing: null,
          emerging: null,
        },
        assessmentWeights: [],
        competencyWeightingType: 'none',
        assessmentOrder: 'leftmostOld',
        assessmentScaling: null,
        gradebookFile: null,
      },
      newAssessType: '',
      newAssessWeight: null,
      toasts: [],
      visibleScrolling: false,
    };
  },
  computed: {
    disableAssessmentTypeAdd() {
      return this.newAssessType == '' || this.newAssessWeight == null;
    },

    isUsingAmountScaling() {
      return (
        this.formFields.competencyWeightingType == 'amount' || this.formFields.competencyWeightingType == 'amountTime'
      );
    },

    isUsingTimeScaling() {
      return (
        this.formFields.competencyWeightingType == 'time' || this.formFields.competencyWeightingType == 'amountTime'
      );
    },
  },
  methods: {
    generateReport() {
      console.log('Submit');
      console.log('Course Name: ' + this.formFields.courseName);
      console.log('Output File Name: ' + this.formFields.outputFileName);
      console.log('District ID: ' + this.formFields.districtId);
      console.log('Comment Focus: ' + this.formFields.commentFocus);
      console.log('0% Handling: ' + this.formFields.zeroGradeHandling);
      console.log('Grading Type: ' + this.formFields.gradingType);
      console.log('Proficieny Scale Thresholds: ', this.formFields.proficiencyTresholds);
      console.log('Assessment Weighting: ', this.formFields.assessmentWeights);
      console.log('Competency Weighting: ' + this.formFields.competencyWeightingType);
      console.log('Assessment Ordering: ' + this.formFields.assessmentOrder);
      console.log('Assessment Scaling: ' + this.formFields.assessmentScaling);
      console.log('Gradebook File: ' + this.formFields.gradebookFile);
    },

    resetFields() {
      this.formFields = {
        courseName: '',
        outputFileName: '',
        districtId: '',
        commentFocus: 'bestWorst',
        zeroGradeHandling: 'assessmentGrade',
        gradingType: 'profScale',
        proficiencyTresholds: {
          extending: null,
          proficient: null,
          developing: null,
          emerging: null,
        },
        assessmentWeights: [],
        competencyWeightingType: 'none',
        assessmentOrder: 'leftmostOld',
        assessmentScaling: null,
        gradebookFile: null,
      };
    },

    addAssessmentWeight() {
      var existing = this.formFields.assessmentWeights.find((ass) => ass.type == this.newAssessType);

      if (existing) {
        this.createToast('Error', 'There is already an entry for this assessment type.');
      } else {
        this.formFields.assessmentWeights.push({
          type: this.newAssessType,
          weight: this.newAssessWeight,
        });
      }

      this.newAssessType = '';
      this.newAssessWeight = null;
    },

    removeAssessmentWeight(assType) {
      this.formFields.assessmentWeights = this.formFields.assessmentWeights.filter((ass) => ass.type != assType);
    },

    createToast(title, text) {
      this.toasts.push({
        title: title,
        content: text,
      });
    },
  },
};
</script>

<style scoped>
.error-toaster {
  margin-top: 45px;
}

.form-label {
  font-size: 17px !important;
}
</style>
