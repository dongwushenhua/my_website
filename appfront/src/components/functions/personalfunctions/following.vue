<template>
  <div class="ui segment">
    <div class="ui large feed">
      <div
        class="event"
        v-for="item in userFollowingList"
        key="item.followTime"
      >
        <div class="label">
          <img :src="item.followed.icon" />
        </div>
        <div class="content">
          <div class="summary">
            <a>
              <router-link
                :to="{
                  path: '/home/visitor',
                  query: { userName: item.followed.user.username },
                }"
                >{{ item.followed.user.username }}
              </router-link>
            </a>
          </div>
        </div>
        <div style="margin-top: 4px">
          <button
            class="ui circular red icon button"
            @click="follow(item.followed.user.username)"
          >
            <i class="heart icon"></i>
          </button>
          <button
            class="ui circular blue icon button"
            @click="addDirectMessage(item.followed.user.username)"
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
  name: "following",
  data() {
    return { userFollowingList: [] };
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
          that.userFollowingList = response.data.followingSerializer;
          that.$message({
            message: "取关成功",
            type: "success",
          });
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
      .get("http://127.0.0.1:8000/user/getUserFollowing/")
      .then(function (response) {
        console.log(response);
        that.userFollowingList = response.data.followingSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>

<style scoped>
.button {
  background-color: white;
}
</style>
