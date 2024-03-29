<template>
  <main>
    <div class="container-xxl">
      <CCardGroup>
        <CCard class="h-100">
          <CCardHeader>
            <h3 class="mb-0">Grade Book Sample</h3>
          </CCardHeader>
          <CCardBody>
            <CRow class="mb-3">
              <CCol>
                Below is an image of a sample grade book file. Click on any of the row or column labels to see a
                description of how each portion of the file is layed out.
              </CCol>
            </CRow>
            <CRow>
              <!-- Medium row buttons -->
              <CCol class="col-2 order-1 d-none d-md-block mb-3 pe-1">
                <div class="row-button-spacer"></div>
                <CRow class="row-button-row justify-content-between">
                  <template v-for="row in SAMPLE_ROW_DATA">
                    <CCol xs="3" sm="12" class="row-button-col">
                      <CButton
                        class="row-btn-md w-100"
                        :class="{ 'sample-btn-selected': this.selectedImageURL == row.image_url }"
                        color="light"
                        @mouseover="updateHoveredImageURL(row.image_url)"
                        @mouseleave="updateHoveredImageURL(null)"
                        @click="updateSelectedImageURL(row)"
                      >
                        {{ row.label }}
                      </CButton>
                    </CCol>
                  </template>
                </CRow>
              </CCol>

              <!-- Small row buttons -->
              <CCol class="col-12 order-2 col-sm-3 col-md-2 order-sm-1 d-none d-sm-block d-md-none mb-3 pe-1">
                <CButtonGroup vertical role="group" aria-label="Vertical button group" class="w-100 h-100">
                  <template v-for="row in SAMPLE_ROW_DATA">
                    <CButton
                      class="row-btn-sm"
                      :class="{ 'sample-btn-selected': this.selectedImageURL == row.image_url }"
                      color="light"
                      @mouseover="updateHoveredImageURL(row.image_url)"
                      @mouseleave="updateHoveredImageURL(null)"
                      @click="updateSelectedImageURL(row)"
                    >
                      {{ row.label }}
                    </CButton>
                  </template>
                </CButtonGroup>
              </CCol>

              <!-- Extra small row buttons -->
              <CCol class="order-2 d-sm-none mb-3">
                <CButtonGroup role="group" aria-label="Button group" class="w-100">
                  <template v-for="row in SAMPLE_ROW_DATA">
                    <CButton
                      class="row-btn-sm"
                      :class="{ 'sample-btn-selected': this.selectedImageURL == row.image_url }"
                      color="light"
                      @mouseover="updateHoveredImageURL(row.image_url)"
                      @mouseleave="updateHoveredImageURL(null)"
                      @click="updateSelectedImageURL(row)"
                    >
                      {{ row.label }}
                    </CButton>
                  </template>
                </CButtonGroup>
              </CCol>

              <CCol class="col-12 order-1 col-sm-9 col-md-10 order-sm-2">
                <CCardImage :src="samplePictureURL" class="mb-3" />
              </CCol>
            </CRow>

            <CRow>
              <!-- Medium col buttons -->
              <CCol class="col-10 offset-2 d-none d-md-block">
                <table class="col-table">
                  <tr>
                    <td class="col0"></td>
                    <template v-for="col in SAMPLE_COL_DATA">
                      <td class="col-main">
                        <CButton
                          class="col-btn-md w-75 mx-auto d-block"
                          :class="{ 'sample-btn-selected': this.selectedImageURL == col.image_url }"
                          color="light"
                          @mouseover="updateHoveredImageURL(col.image_url)"
                          @mouseleave="updateHoveredImageURL(null)"
                          @click="updateSelectedImageURL(col)"
                        >
                          {{ col.label }}
                        </CButton>
                      </td>
                    </template>
                    <td></td>
                  </tr>
                </table>
              </CCol>

              <!-- Small col buttons -->
              <CCol class="col-sm-9 offset-sm-3 d-block d-md-none">
                <CButtonGroup role="group" aria-label="Button group" class="w-100 bg-primary">
                  <template v-for="col in SAMPLE_COL_DATA">
                    <CButton
                      class="col-btn-sm"
                      :class="{ 'sample-btn-selected': this.selectedImageURL == col.image_url }"
                      color="light"
                      @mouseover="updateHoveredImageURL(col.image_url)"
                      @mouseleave="updateHoveredImageURL(null)"
                      @click="updateSelectedImageURL(col)"
                    >
                      {{ col.label }}
                    </CButton>
                  </template>
                </CButtonGroup>
              </CCol>
            </CRow>

            <CRow>
              <CCol class="sm-9 md-10 offset-sm-3 offset-md-2 px-3">
                <div class="callout sample-callout callout-primary">
                  <h6 class="callout-header">{{ descriptionHeader }}</h6>
                  <span>{{ descriptionText }}</span>
                </div>
              </CCol>
            </CRow>
          </CCardBody>
        </CCard>
      </CCardGroup>
    </div>
  </main>
</template>

<script>
import { CRow, CCol, CCard, CCardHeader, CCardBody, CCardImage, CCardGroup, CButtonGroup, CButton } from '@coreui/vue';

const SAMPLE_ROW_DATA = [
  {
    label: 'Row 1',
    image_url: 'src/assets/images/alt2-row1.jpg',
    header_text: 'Row 1: Curricular Competencies',
    body_text:
      "These typically can be found on the BC curriculum https://curriculum.gov.bc.ca/. Each assessment can have as many curricular competencies as you would like. When adding more than one curricular competencies you must separate them with a comma ','.",
  },
  {
    label: 'Row 2',
    image_url: 'src/assets/images/alt2-row2.jpg',
    header_text: 'Row 2: Content',
    body_text:
      "Just like curricular competencies you can include as many as you want for each assessment. If you are adding more then one content you must separate them with a comma ','.",
  },
  {
    label: 'Row 3',
    image_url: 'src/assets/images/alt2-row3.jpg',
    header_text: 'Row 3: Assessment Type',
    body_text:
      'This has been prefilled with a drop down menu of the common assessment types but this can be changed to what ever you want. Just make sure when generating your report that the assessment types you enter match what is entered in your grade book.',
  },
  {
    label: 'Row 4',
    image_url: 'src/assets/images/alt2-row4.jpg',
    header_text: 'Row 4: Assessment Name',
    body_text:
      'The assessment name helps you keep track of your grade book (the name will not used in the generating of your report.)',
  },
  {
    label: 'Row 5',
    image_url: 'src/assets/images/alt2-row5.jpg',
    header_text: 'Row 5: Total Marks',
    body_text:
      'So if you have a test out of 20 marks you would put 20 here. If you are using proficiency scale you can put a 4 here (4/4 is extending, 3/4 is proficient, etc.) or you can leave it blank.',
  },
  {
    label: 'Row 6+',
    image_url: 'src/assets/images/alt2-row6.jpg',
    header_text: 'Row 6+: Students',
    body_text:
      'These rows are used to put students name and their marks on each assessment. Please see the help page for information on proficiency scales.',
  },
];

const SAMPLE_COL_DATA = [
  {
    label: 'Column 1',
    image_url: 'src/assets/images/alt2-col1.jpg',
    header_text: 'Column 1',
    body_text: 'Used only to give headings to the rows and is not used in the report.',
  },
  {
    label: 'Column 2',
    image_url: 'src/assets/images/alt2-col2.jpg',
    header_text: 'Column 2',
    body_text:
      'Used for listing the students name. You can put first and last name or just first name. The report will only use first names.',
  },
  {
    label: 'Column 3+',
    image_url: 'src/assets/images/alt2-col3.jpg',
    header_text: 'Column 3+',
    body_text:
      'These columns are used for entering assessment information, each assessment should be in its own column.',
  },
];

export default {
  name: 'grade-book-view',
  components: {
    CRow,
    CCol,
    CCard,
    CCardHeader,
    CCardBody,
    CCardImage,
    CCardGroup,
    CButtonGroup,
    CButton,
  },
  data() {
    return {
      SAMPLE_ROW_DATA,
      SAMPLE_COL_DATA,
      hoveredImageURL: null,
      selectedImageURL: null,
      descriptionHeader: 'Sample Grade Book',
      descriptionText: 'Click on any of the above row or column labels to view a description of the data it contains.',
    };
  },
  computed: {
    samplePictureURL() {
      if (this.hoveredImageURL != null) {
        return this.hoveredImageURL;
      } else if (this.selectedImageURL != null) {
        return this.selectedImageURL;
      } else {
        return 'src/assets/images/alt2-baseline.jpg';
      }
    },
  },
  methods: {
    updateHoveredImageURL(imgURL) {
      this.hoveredImageURL = imgURL;
    },

    updateSelectedImageURL(section) {
      if (this.selectedImageURL == section.image_url) {
        this.selectedImageURL = null;
        this.descriptionHeader = 'Sample Grade Book';
        this.descriptionText =
          'Click on any of the above row or column labels to view a description of the data it contains.';
      } else {
        this.selectedImageURL = section.image_url;
        this.descriptionHeader = section.header_text;
        this.descriptionText = section.body_text;
      }
    },
  },
};
</script>

<style scoped>
.row-btn-md:hover,
.row-btn-sm:hover,
.col-btn-md:hover,
.col-btn-sm:hover {
  background-color: var(--primary-color-dark);
}

.row-btn-md {
  height: 100%;
  padding-top: 0px;
  padding-bottom: 0px;
}

.row-btn-md,
.row-btn-sm,
.col-btn-md,
.col-btn-sm,
.row-btn-md:focus,
.row-btn-sm:focus,
.col-btn-md:focus,
.col-btn-sm:focus {
  background-color: var(--primary-color);
  border: 1px solid var(--secondary-color) !important;
  font-size: 14px;
}

.row-button-spacer {
  height: 26.7%;
}

.row-button-row {
  height: 49.5%;
}

.row-button-col {
  height: 15%;
}

.col-table {
  width: 100%;
}

.col-table .col0 {
  width: 4%;
}

.col-table .col-main {
  width: 18.16%;
}

.col-btn-md {
  min-width: 100px;
}

.sample-btn-selected,
.sample-btn-selected.row-btn-md:hover,
.sample-btn-selected.row-btn-sm:hover,
.sample-btn-selected.col-btn-md:hover,
.sample-btn-selected.col-btn-sm:hover {
  color: var(--secondary-color) !important;
  background-color: #ebedef !important;
}

.sample-callout {
  background-color: var(--primary-color-light);
}

.callout-header {
  color: var(--secondary-color);
}
</style>
