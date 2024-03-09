import { createRouter, createWebHistory } from 'vue-router'
import GeneratorView from '../views/GeneratorView.vue'
import GradeBookView from '../views/GradeBookView.vue'
import HelpView from '../views/HelpView.vue'
import AboutView from '../views/AboutView.vue'
import ContactView from '../views/ContactView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Generator',
      component: GeneratorView,
    },
    {
      path: '/gradeBook',
      name: 'Grade Book',
      component: GradeBookView,
    },
    {
      path: '/help',
      name: 'Help',
      component: HelpView,
    },
    {
      path: '/about',
      name: 'About',
      component: AboutView,
    },
    {
      path: '/contact',
      name: 'Contact Us',
      component: ContactView,
    }
  ]
})

export default router
