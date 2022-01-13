<template>
  <div class="ui segment">
    <div class="ui feed" v-for="item in messageList">
      <div class="event">
        <div class="label">
          <img :src="item.actor.icon" />
        </div>
        <div class="content">
          <div class="summary">
            <a>
              <router-link
                :to="{
                  path: '/home/visitor',
                  query: { userName: item.actor.user.username },
                }"
              >
                {{ item.actor.user.username }}
              </router-link> </a
            >{{ item.verb
            }}<a v-if="item.target">
              <router-link
                :to="{
                  path: '/article/specific',
                  query: { articleId: item.target.id },
                }"
              >
                {{ item.target.title }}
              </router-link>
            </a>
            <a v-if="item.action_object">{{ item.action_object.message }}</a>
            <div class="date">
              {{ item.timestamp.split("T")[0] }}
              {{ item.timestamp.split("T")[1].split(".")[0] }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <button
      style="margin-left: 80%"
      class="ui circular vertical animated blue icon button"
      @click="deleteAllUserMessage()"
      v-if="messageList.length > 0"
    >
      <div class="hidden content">删除</div>
      <div class="visible content">
        <i class="trash icon"></i>
      </div>
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "message",
  data() {
    return { messageList: [] };
  },
  created() {
    var that = this;
    //alert(this.$route.query.articleId)
    axios
      .get("http://127.0.0.1:8000/user/showUserMessage/")
      .then(function (response) {
        console.log(response);
        that.messageList = response.data.userMessagesSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    deleteAllUserMessage() {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/user/deleteAllUserMessage/")
        .then(function (response) {
          console.log(response);
          that.messageList = [];
          that.$message({
            message: "删除成功",
            type: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.button {
  margin-top: 15px;
}
</style>
