<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <table class="ui celled padded table">
          <thead>
            <tr>
              <th class="single line">海报</th>
              <th>名称</th>
              <th>评分</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in contentList" key="item.id">
              <td>
                <img class="ui tiny rounded image" :src="item.cover" />
              </td>
              <td>
                <h3 class="ui center aligned header">{{ item.title }}</h3>
              </td>
              <td>
                <h3 class="ui center aligned header">{{ item.rate }}</h3>
              </td>
              <td class="single line">
                <div class="ui vertical animated button" tabindex="0">
                  <div class="hidden content">详情</div>
                  <div class="visible content">
                    <i class="shop icon"></i>
                  </div>
                </div>
                <div class="ui vertical animated button" tabindex="0">
                  <div class="hidden content">评论</div>
                  <div class="visible content">
                    <i class="shop icon"></i>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
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
  name: "douban",
  data() {
    return { contentList: "" };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/data/douBanHotMovie/")
      .then(function (response) {
        console.log(response);
        that.contentList = response.data.content.subjects;
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
