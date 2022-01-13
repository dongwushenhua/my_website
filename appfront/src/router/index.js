import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)


export default new Router({
  /*mode: "history",*/
  routes: [{
    path: '',
    name: 'HelloWorld',
    component: () =>
      import ("../components/HelloWorld")
  }, {
    path: '/login',
    name: 'logIn',
    component: () =>
      import ("../components/user/logIn")
  }, {
    path: '/signin',
    name: 'signIn',
    component: () =>
      import ("../components/user/signIn")
  }, {
    path: '/model',
    name: 'model',
    component: () =>
      import ("../components/basic/model"),
    children: [{
      path: '/home/main',
      name: 'home',
      component: () =>
        import ("../components/functions/webfunctions/home")
    },
      {
        path: '/article/specific',
        name: 'specific',
        component: () =>
          import ("../components/functions/webfunctions/specific")
      }, {
        path: '/home/addtags',
        name: 'addtags',
        component: () =>
          import ("../components/functions/webfunctions/addtags")
      }, {
        path: '/home/editor',
        name: 'editor',
        component: () =>
          import ("../components/functions/webfunctions/editor")
      }, {
        path: '/home/webdata',
        name: 'webdata',
        component: () =>
          import ("../components/functions/webfunctions/webdata")
      }, {
        path: '/home/webdata/douban',
        name: 'douban',
        component: () =>
          import ("../components/functions/webfunctions/douban")
      }, {
        path: '/home/webdata/weibo',
        name: 'weibo',
        component: () =>
          import ("../components/functions/webfunctions/weibo")
      }, {
        path: '/home/webdata/zhihu',
        name: 'weibo',
        component: () =>
          import ("../components/functions/webfunctions/zhihu")
      }, {
        path: '/home/searchresult',
        name: 'searchresult',
        component: () =>
          import ("../components/functions/webfunctions/searchresult")
      }, {
        path: '/home/visitor',
        name: 'visitor',
        component: () =>
          import ("../components/functions/webfunctions/visitor")
      },
      {
        path: '/home/personal',
        name: 'personal',
        component: () =>
          import ("../components/functions/personalfunctions/personal"),
        children: [{
          path: '/home/personal/archieve',
          name: 'archieve',
          component: () =>
            import ("../components/functions/personalfunctions/archieve")
        }, {
          path: '/home/personal/editemine',
          name: 'editemine',
          component: () =>
            import ("../components/functions/personalfunctions/editemine")
        }, {
          path: '/home/personal/followed',
          name: 'followed',
          component: () =>
            import ("../components/functions/personalfunctions/followed")
        }, {
          path: '/home/personal/following',
          name: 'following',
          component: () =>
            import ("../components/functions/personalfunctions/following")
        }, {
          path: '/home/personal/message',
          name: 'message',
          component: () =>
            import ("../components/functions/personalfunctions/message")
        }, {
          path: '/home/personal/personaldata',
          name: 'personaldata',
          component: () =>
            import ("../components/functions/personalfunctions/personaldata")
        }, {
          path: '/home/personal/collections',
          name: 'collections',
          component: () =>
            import ("../components/functions/personalfunctions/collections")
        }, {
          path: '/home/personal/watchout',
          name: 'watchout',
          component: () =>
            import ("../components/functions/personalfunctions/watchout")
        }, {
          path: '/home/personal/observe',
          name: 'observe',
          component: () =>
            import ("../components/functions/personalfunctions/observe")
        },]
      }
    ]
  }]
})
//解决 Vue 重复点击相同路由出现的问题
/*
const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
*/
