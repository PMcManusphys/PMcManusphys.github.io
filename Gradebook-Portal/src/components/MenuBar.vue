<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <nav class="navbar navbar-expand position-fixed top-0 start-0 end-0 z-3">
    <div class="container-fluid">
      <RouterLink class="navbar-brand text-white" to="/">Curricular Comment Generator</RouterLink>
      <ul class="navbar-nav mb-lg-0 default-nav-list">
        <li class="nav-item" :class="[this.$route.name == 'Generator' ? 'active' : 'pointer']">
          <RouterLink class="nav-link" to="/">Generator</RouterLink>
        </li>
        <li class="nav-item" :class="[this.$route.name == 'Grade Book' ? 'active' : 'pointer']">
          <RouterLink class="nav-link" to="/gradeBook">Grade Book</RouterLink>
        </li>
        <li class="nav-item" :class="[this.$route.name == 'Help' ? 'active' : 'pointer']">
          <RouterLink class="nav-link" to="/help">Help</RouterLink>
        </li>
        <li class="nav-item" :class="[this.$route.name == 'About' ? 'active' : 'pointer']">
          <RouterLink class="nav-link" to="/about">About</RouterLink>
        </li>
        <li class="nav-item" :class="[this.$route.name == 'Contact Us' ? 'active' : 'pointer']">
          <RouterLink class="nav-link" to="/contact">Contact Us</RouterLink>
        </li>
      </ul>
      <CButton
        color="light"
        variant="outline"
        class="menu-toggle"
        @click="
          () => {
            visible = !visible;
          }
        "
      >
        <CIcon icon="cilHamburgerMenu" size="xl" class="hamburger-icon" />
      </CButton>
    </div>
  </nav>

  <COffcanvas
    placement="start"
    :visible="visible"
    @hide="
      () => {
        visible = !visible;
      }
    "
    class="mobile-nav"
  >
    <COffcanvasHeader>
      <COffcanvasTitle>Navigation Menu</COffcanvasTitle>
      <CCloseButton
        class="text-reset"
        @click="
          () => {
            visible = false;
          }
        "
      />
    </COffcanvasHeader>
    <COffcanvasBody>
      <CListGroup>
        <CListGroupItem @click="redirect('/')" :class="[this.$route.name == 'Generator' ? 'active' : 'pointer']">
          <CIcon icon="cilChevronRight" size="lg" class="pt-1 nav-chevron" />
          Generator
        </CListGroupItem>
        <CListGroupItem
          @click="redirect('/gradeBook')"
          :class="[this.$route.name == 'Grade Book' ? 'active' : 'pointer']"
        >
          <CIcon icon="cilChevronRight" size="lg" class="pt-1 nav-chevron" />
          Grade Book
        </CListGroupItem>
        <CListGroupItem @click="redirect('/help')" :class="[this.$route.name == 'Help' ? 'active' : 'pointer']">
          <CIcon icon="cilChevronRight" size="lg" class="pt-1 nav-chevron" />
          Help
        </CListGroupItem>
        <CListGroupItem @click="redirect('/about')" :class="[this.$route.name == 'About' ? 'active' : 'pointer']">
          <CIcon icon="cilChevronRight" size="lg" class="pt-1 nav-chevron" />
          About
        </CListGroupItem>
        <CListGroupItem
          @click="redirect('/contact')"
          :class="[this.$route.name == 'Contact Us' ? 'active' : 'pointer']"
        >
          <CIcon icon="cilChevronRight" size="lg" class="pt-1 nav-chevron" />
          Contact Us
        </CListGroupItem>
      </CListGroup>
    </COffcanvasBody>
  </COffcanvas>
</template>

<script>
import {
  CButton,
  CNavbar,
  CContainer,
  CNavbarBrand,
  CNavbarToggler,
  CCollapse,
  CNavbarNav,
  CNavLink,
  COffcanvas,
  COffcanvasHeader,
  COffcanvasTitle,
  CCloseButton,
  COffcanvasBody,
  CListGroup,
  CListGroupItem,
} from '@coreui/vue';

export default {
  name: 'menu-bar',
  components: {
    CButton,
    CNavbar,
    CContainer,
    CNavbarBrand,
    CNavbarToggler,
    CCollapse,
    CNavbarNav,
    CNavLink,
    COffcanvas,
    COffcanvasHeader,
    COffcanvasTitle,
    CCloseButton,
    COffcanvasBody,
    CListGroup,
    CListGroupItem,
  },
  data() {
    return {
      visible: false,
    };
  },
  methods: {
    redirect(link) {
      console.log(this.$route);

      if (this.$route.path != link) {
        this.visible = false;
        this.$router.push(link);
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  background-color: var(--primary-color);
  height: 60px;
}

.active > .nav-link {
  color: var(--secondary-color) !important;
  font-weight: 500;
  border-bottom: 3px solid var(--secondary-color);
  padding-bottom: 4px;
  margin-bottom: 3px;
  cursor: default;
}

.nav-link:hover {
  color: var(--secondary-color) !important;
}

.nav-item {
  padding-top: 8px;
  padding-bottom: 7px;
  color: white;
  margin-left: 8px;
  margin-right: 8px;
}

.hamburger-icon {
  margin-top: 2px;
  color: var(--secondary-color) !important;
}
.menu-toggle:hover > .hamburger-icon {
  color: white !important;
}

.navbar-brand {
  color: var(--secondary-color) !important;
  font-weight: 500;
}

.menu-toggle {
  border: 2px solid var(--secondary-color) !important;
  padding-top: 3px;
  padding-bottom: 1px;
}
.menu-toggle:hover {
  /* background-color: var(--primary-color-dark); */
  background-color: var(--secondary-color);
  color: white;
}

.offcanvas-header {
  background-color: var(--primary-color-dark);
  height: 60px;
  color: var(--secondary-color);
}

.offcanvas-body {
  background-color: white;
}

.list-group-item.active,
.list-group-item.active:hover {
  color: var(--secondary-color) !important;
  font-weight: 500;
  background-color: var(--primary-color-light);
  border: 1px solid var(--secondary-color);
  border-radius: 5px !important;
  padding-left: 20px;
  cursor: context-menu;
}

.list-group-item {
  background-color: white;
  border-left: none;
  border-right: none;
  border-radius: 0 !important;
}

.list-group-item:hover {
  background-color: var(--background-soft);
  color: var(--secondary-color) !important;
  padding-left: 5px;
}

.list-group-item:hover > .nav-chevron {
  display: inline;
}

.nav-chevron,
.list-group-item.active:hover > .nav-chevron {
  display: none;
}
</style>
