<template>
  <div style="width: 850px; margin-top: 20px">
    <div class="ui icon input">
      <input type="text" placeholder="搜索..." v-model="searchContent" />
      <router-link
        :to="{
          path: '/home/searchresult',
          query: { search: this.searchContent },
        }"
      >
        <div class="ui mini icon button">
          <i class="circular search icon"> </i>
        </div>
      </router-link>
    </div>
    <div class="ui top icon buttons">
      <button class="ui button" @click="contectMe()">
        <i class="envelope icon"></i>
      </button>
      <button class="ui button" @click="logOut()">
        <i class="sign-out icon"></i>
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "headers",
  data() {
    return { searchContent: "" };
  },
  methods: {
    contectMe() {
      var that = this;
      this.$prompt("请输入内容", "", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          if (value) {
            axios
              .post("http://127.0.0.1:8000/user/addDirectMessage/", {
                to: "东无神话",
                message: value,
              })
              .then(function (response) {
                console.log(response);
                this.$message({
                  type: "success",
                  message: "感谢您的留言",
                });
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
    logOut() {
      this.$router.push("/");
      axios
        .get("http://127.0.0.1:8000/user/logOut/")
        .then(function (response) {
          console.log(response);
          this.$message({
            type: "success",
            message: "登出成功",
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
.ui.input {
  width: 60%;
  margin-left: 5%;
}

.buttons {
  margin-top: 1.5px;
  float: right;
}

.button {
  background-color: white;
}
</style>
