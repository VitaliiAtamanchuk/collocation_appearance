import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import VueResource from 'vue-resource'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = true
Vue.use(VueResource)

Vue.filter('formatTime', function(value) {
  return value.split('.')[0]
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
