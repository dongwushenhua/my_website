<template>
  <div>
    <div class="ui fluid card" v-for="(item, index) in personalArticleList"
         key="item.id"
         style="margin-top: 14px">
      <div class="content">
        <img
          class="ui left floated mini circular image"
          :src="item.postMan.icon"
        />
        <a class="header">
          <router-link
            :to="{
                  path: '/article/specific',
                  query: { articleId: item.id },
                }"
          >{{ item.title }}
          </router-link>
        </a>
        <div class="meta">
          {{ item.createTime.split("T")[0] }}
          {{ item.createTime.split("T")[1].split(".")[0] }}
        </div>
        <div class="description">
          Elliot requested permission to view your contact details
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "archieve",
  data() {
    return {personalArticleList: []};
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/showPersonalArticle/")
      .then(function (response) {
        console.log(response);
        that.personalArticleList = response.data.personalArticlesSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
}
</script>

<style scoped>

</style>
