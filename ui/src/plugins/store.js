import Vue from 'vue'
import Vuex from 'vuex'

import { auth } from '@/plugins/store/auth'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    auth
  },
  strict: debug
})
