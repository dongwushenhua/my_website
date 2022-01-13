<template>
  <div>
    <div
      v-for="(item, index) in collectArticleList"
      key="item.id"
      style="margin-top: 14px"
    >
      <div
        class="ui fluid card"
        v-if="item.collectArticle.articleTags.length > 0"
      >
        <div class="content">
          <a class="header">
            <router-link
              :to="{
                path: '/article/specific',
                query: { articleId: item.collectArticle.id },
              }"
              >{{ item.collectArticle.title }}
            </router-link>
          </a>
          <div class="meta">
            <span class="right floated time"
              >{{ item.collectArticle.createTime.split("T")[0] }}
              {{
                item.collectArticle.createTime.split("T")[1].split(".")[0]
              }}</span
            >
            <!--                  <span class="category">sss</span>-->
          </div>
          <div class="description">
            <p></p>
          </div>
        </div>
        <div class="extra content">
          <a class="ui label">
            <img
              class="ui right spaced avatar image"
              :src="item.collectArticle.postMan.icon"
            />
            <router-link
              :to="{
                path: '/home/visitor',
                query: { userName: item.collectArticle.postMan.user.username },
              }"
              >{{ item.collectArticle.postMan.user.username }}
            </router-link>
          </a>
          <a
            class="ui label"
            v-for="tags in item.collectArticle.articleTags"
            style="margin-top: 3px"
          >
            <img
              class="ui right spaced avatar image"
              :src="tags.tagCreater.icon"
            />
            {{ tags.tagName }}
          </a>
        </div>
      </div>
      <!--          //有标签-->
      <div class="ui fluid card" v-else>
        <div class="content">
          <img
            class="ui left floated mini circular image"
            :src="item.collectArticle.postMan.icon"
          />
          <a class="header">
            <router-link
              :to="{
                path: '/article/specific',
                query: { articleId: item.collectArticle.id },
              }"
              >{{ item.collectArticle.title }}
            </router-link>
          </a>
          <div class="meta">
            {{ item.collectArticle.createTime.split("T")[0] }}
            {{ item.collectArticle.createTime.split("T")[1].split(".")[0] }}
          </div>
          <div class="description">
            Elliot requested permission to view your contact details
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "collections",
  data() {
    return { collectArticleList: [] };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/showCollectArticle/")
      .then(function (response) {
        console.log(response);
        that.collectArticleList = response.data.personalCollectionsSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>

<style scoped>
</style>
