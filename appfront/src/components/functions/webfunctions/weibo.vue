<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div class="ui large feed">
          <div class="event" v-for="item in contentList" key="item.title">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                <a class="user">
                  {{ item.title }}
                </a>
                <div class="date">
                  {{ item.mark }}
                </div>
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
  name: "weibo",
  data() {
    return { contentList: "" };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/data/weibo/")
      .then(function (response) {
        console.log(response);
        that.contentList = response.data.content;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
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
