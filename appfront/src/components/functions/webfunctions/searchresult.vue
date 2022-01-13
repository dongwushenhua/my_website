<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <img :src="imgSrc" class="ui fluid rounded image" />
      </div>
      <div class="mainContent">
        <div class="ui basic segment">
          <div class="ui fluid card" v-for="item in searchResultList">
            <div class="content">
              <a class="header"
                ><router-link
                  :to="{
                    path: '/article/specific',
                    query: { articleId: item.id },
                  }"
                  >{{ item.title }}</router-link
                ></a
              >
              <div class="meta">
                <span class="right floated time">{{ item.createTime }}</span>
                <span class="category">{{ item.text }}</span>
              </div>
              <div class="description">
                <p></p>
              </div>
            </div>
            <div class="extra content">
              <div class="right floated author">
                <img class="ui avatar image" :src="item.postMan.icon" />
                {{ item.postMan.userName }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="ui basic segment">
        <div class="paging">
          <el-pagination layout="prev, pager, next" :total="1000">
          </el-pagination>
        </div>
      </div>
    </div>
    <div class="f">
      <div class="ui basic segment">
        <h4 class="ui right floated header">热门文章搜索</h4>
        <div class="ui clearing divider"></div>
        <div><labels></labels></div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">热门标签搜索</h4>
        <div class="ui clearing divider"></div>
        <div><aboutme></aboutme></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "searchresult",
  data() {
    return {
      searchResultList: [],
      imgSrc: require("../../../assets/SRBG.jpg"),
    };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/searchArticle", {
        params: { search: this.$route.query.search },
      })
      .then(function (response) {
        console.log(response);
        that.searchResultList = response.data;
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

.card {
  height: 200px;
  background-image: url("../../../assets/SRBG.jpg");
}
.paging {
  margin-left: 20%;
}
</style>
