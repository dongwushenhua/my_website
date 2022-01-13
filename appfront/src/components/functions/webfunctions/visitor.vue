<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div class="ui fluid card">
          <img class="ui fluid image" src="../../../assets/background.jpg"/>
        </div>
      </div>
      <div class="mainContent">
        <div class="ui basic segment">
          <div>
            <div class="ui fluid card">
              <div class="content">
                <el-empty description="暂无内容"></el-empty>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="ui basic segment">
        <div class="paging">
          <el-pagination
            layout="prev, pager, next"
            @current-change="handleCurrentChange"
            :page-count="pageSize"
            :hide-on-single-page="true"
          >
          </el-pagination>
        </div>
      </div>
    </div>
    <div class="f">
      <img
        class="ui circular centered image"
        style="width: 120px"
        :src="imgSrc"
      />
      <div class="ui basic segment">
        <h4 class="ui right floated header">留言板</h4>
        <div class="ui clearing divider"></div>
        <div class="ui feed">
          <div class="event" v-for="item in visitorMessageList" key="item.id">
            <div class="label">
              <img :src="item.actor.icon"/>
            </div>
            <div class="content">
              <div class="summary">
                {{ item.action_object.message }}
              </div>
              <div class="meta">
                <a class="like" @click="deleteVisitorMessage(item.id)">
                  <i class="trash icon"></i> 删除
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="ui fluid input">
          <input type="text" placeholder="" v-model="messageContent"/>
        </div>
        <div
          class="ui circular right floated icon blue vertical animated button"
          tabindex="0"
          @click="addVisitorMessage()"
          style="margin-top: 10px"
        >
          <div class="hidden content">留言</div>
          <div class="visible content">
            <i class="comments icon"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "visitor",
  data() {
    return {
      articleList: [],
      imgSrc: "",
      messageContent: "",
      visitorMessageList: [],
    };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/showVisitorArticle/", {
        params: {userName: this.$route.query.userName},
      })
      .then(function (response) {
        console.log(response);
        that.articleList = response.data.visitorArticlesSerializer;
        that.imgSrc = response.data.nowUserSerializer.icon;
      })
      .catch(function (error) {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/user/showVisitorMessage/", {
        params: {userName: this.$route.query.userName},
      })
      .then(function (response) {
        console.log(response);
        that.visitorMessageList = response.data.visitorMessagesSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    addVisitorMessage() {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/user/addVisitorMessage/", {
          params: {
            to: this.$route.query.userName,
            message: that.messageContent,
          }
        })
        .then(function (response) {
          console.log(response);
          that.visitorMessageList = response.data.visitorMessagesSerializer;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteVisitorMessage(id) {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/user/deleteVisitorMessage/", {
          params: {
            id: id,
            to: this.$route.query.userName,
          },
        })
        .then(function (response) {
          console.log(response);
          that.visitorMessageList = response.data.visitorMessagesSerializer;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
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

/*.card {
  height: 200px;
  !*:src="cover[index]"*!
  background-image: url("../../../assets/show/SBG1.jpg");
}*/
</style>
