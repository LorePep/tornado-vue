import Vue from 'vue'
import VueRouter from 'vue-router'
import Analysis from '@/components/Analysis'
import Report from '@/components/Analysis'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
      {
        path: '/',
        name: 'Analysis',
        component: Analysis
      },
      {
        path: '/v1/report',
        name: 'Report',
        component: Report
      },
  ],
  mode: 'history'
})
