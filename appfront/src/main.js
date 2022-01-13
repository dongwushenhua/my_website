// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store'
import './plugins/VueQuillEditor.js'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 引入js文件，这里直接使用的是这个文件里的路径，不需要再resolver中修改路径之类的操作
import semantic from '../node_modules/semantic-ui-css/semantic.min.js'
// 引入css文件
import '../node_modules/semantic-ui-css/semantic.min.css'
import cookies from 'vue-cookies'
import router from './router'
/*import * as echarts from 'echarts';
import 'echarts-liquidfill';*/
import VueCropper from 'vue-cropper'

Vue.use(VueCropper)

Vue.use(semantic);
Vue.use(ElementUI);
Vue.config.productionTip = false
Vue.use(cookies)
Vue.prototype.$cookies = cookies
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App) // ElementUI
})
