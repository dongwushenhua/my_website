<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div class="ui large feed">
          <div class="event">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                <router-link :to="{ path: '/home/webdata/douban' }">
                  <a class="user"> 豆瓣热门 </a>
                </router-link>
              </div>
            </div>
          </div>
          <div class="event">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                <router-link :to="{ path: '/home/webdata/weibo' }">
                  <a class="user"> 微博热门 </a>
                </router-link>
              </div>
            </div>
          </div>
          <div class="event">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                <router-link :to="{ path: '/home/webdata/zhihu' }">
                  <a class="user"> 知乎热门 </a>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="f">
      <div class="ui third basic segment">
        <h4 class="ui right floated header">热门文章</h4>
        <div class="ui clearing divider"></div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">网站信息</h4>
        <div class="ui clearing divider"></div>
        <div></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "webdata",
};
</script>

<style scoped>
.framework {
  width: 850px;
}

.main {
  width: 600px;
  float: left;
}

.f {
  width: 250px;
  float: left;
}
</style>
