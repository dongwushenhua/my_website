<template>
  <div class="ui segment">
    <div
      class="ui large feed"
      v-for="item in userFollowedList"
      key="item.followTime"
    >
      <div class="event">
        <div class="label">
          <img :src="item.following.icon" />
        </div>
        <div class="content">
          <div class="summary">
            <a>
              <router-link
                :to="{
                  path: '/home/visitor',
                  query: { userName: item.following.user.username },
                }"
                >{{ item.following.user.username }}
              </router-link>
            </a>
          </div>
        </div>
        <div style="margin-top: 4px">
          <button
            class="ui circular icon button"
            @click="follow(item.following.userName)"
          >
            <i class="heart icon"></i>
          </button>
          <button
            class="ui circular blue icon button"
            @click="addDirectMessage(item.following.userName)"
          >
            <i class="envelope icon"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "followed",
  data() {
    return { userFollowedList: [] };
  },
  methods: {
    follow(userName) {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/user/follow/", {
          params: {
            userName: userName,
          },
        })
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    addDirectMessage(name) {
      var that = this;
      this.$prompt("请输入内容", "", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          if (value) {
            axios
              .post("http://127.0.0.1:8000/user/addDirectMessage/", {
                to: name,
                message: value,
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
          } else {
            this.$message({
              type: "warning",
              message: "请输入留言内容",
            });
          }
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/user/getUserFollowed/")
      .then(function (response) {
        console.log(response);
        that.userFollowedList = response.data.followedSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>

<style scoped>
</style>
