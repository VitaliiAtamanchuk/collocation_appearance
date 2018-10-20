import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import DisplayWordApp from './views/DisplayWordApp.vue'
import WordList from './views/WordList.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/display_word_app',
      name: 'display_word_app',
      component: DisplayWordApp
    },
    {
      path: '/word_list',
      name: 'word_list',
      component: WordList
    },
  ]
})
