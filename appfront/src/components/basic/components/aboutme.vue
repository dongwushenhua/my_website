<template>
  <div>
    <a class="ui label">
      运营天数
      <div class="detail">{{ webData.websiteOperationTime }}</div>
    </a>
    <a class="ui label">
      用户数量
      <div class="detail">{{ webData.nowUserNumber }}</div>
    </a>
    <a class="ui label">
      今日新增用户
      <div class="detail">{{ webData.newUsers }}</div>
    </a>
    <a class="ui label">
      文章总数
      <div class="detail">{{ webData.nowArticleNumber }}</div>
    </a>
    <a class="ui label">
      今日新增文章
      <div class="detail">{{ webData.newArticles }}</div>
    </a>
    <a class="ui label">
      在线用户
      <div class="detail">{{ webData.code }}</div>
    </a>
    <a class="ui label">
      最近登录
      <div class="detail">{{ webData.recentLogTime.split("T")[0] }}</div>
    </a>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "aboutme",
  data() {
    return { webData: "" };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/website/websiteData/")
      .then(function (response) {
        console.log(response);
        that.webData = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>

<style scoped>
.label {
  margin-top: 5px;
}
</style>
