import Vue from 'vue'
import Vuex from 'vuex'

import { auth } from '@/plugins/store/auth'
import { error } from '@/plugins/store/error'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    auth,
    error
  },
  strict: debug
})
