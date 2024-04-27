import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/main.css'

import 'bootstrap'

import '@coreui/coreui/dist/css/coreui.min.css'
import '@coreui/coreui/dist/css/coreui.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { CIcon } from '@coreui/icons-vue';
import { cilHamburgerMenu, cilChevronRight, cilDataTransferDown, cilPlus, cilMinus, cilThumbDown, cilMagnifyingGlass } from '@coreui/icons'

const icons = { cilHamburgerMenu, cilChevronRight, cilDataTransferDown, cilPlus, cilMinus, cilThumbDown, cilMagnifyingGlass }

const app = createApp(App)

app.provide('icons', icons)
app.component('CIcon', CIcon)

app.use(router)

app.mount('#app')

