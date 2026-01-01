import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router/auto'
import { routes } from 'vue-router/auto-routes'
import App from './App.vue'
import './index.css'

import { VueQueryPlugin } from '@tanstack/vue-query'

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const app = createApp(App)
app.use(router)
app.use(VueQueryPlugin)
app.mount('#app')
