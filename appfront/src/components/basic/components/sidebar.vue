<template>
  <div class="sidebar">
    <div class="ui basic segment">
      <div :style="{ height: getHeight + 'px' }">
        <img
          :src="$store.state.icon "
          class="ui circular centered image"
          style="width: 120px"
        />
        <!-- <h3>{{ $store.state.username }}</h3>
        <p style="color: grey">
          {{ $store.state.signature }}
        </p> -->
        <h4 class="ui horizontal divider header">
          <i class="bookmark icon"></i>
          导航
        </h4>
        <div class="ui fluid vertical buttons">
          <router-link
            :to="{
              path: '/home/main',
              query: { type: blog },
            }"
          >
            <button class="ui button">一些博客</button></router-link
          >
          <router-link
            :to="{
              path: '/home/main',
              query: { type: diary },
            }"
          >
            <button class="ui button">一些日记</button>
          </router-link>
          <router-link
            :to="{
              path: '/home/main',
              query: { type: idea },
            }"
          >
            <button class="ui button">一些快记</button>
          </router-link>
          <router-link
            :to="{
              path: '/home/main',
              query: { type: summary },
            }"
          >
            <button class="ui button">一些总结</button>
          </router-link>
          <!--          <button class="ui button" @click="turnToAddDatas()">数据中心</button>-->
          <router-link
            :to="{
              path: '/home/addtags',
            }"
          >
            <button class="ui button">添加标签</button>
          </router-link>
          <router-link
            :to="{
              path: '/home/editor',
            }"
          >
            <button class="ui button">发布文章</button>
          </router-link>
          <router-link
            :to="{
              path: '/home/personal/archieve',
            }"
          >
            <button class="ui button">个人主页</button>
          </router-link>
        </div>
        <h4 class="ui horizontal divider header">
          <i class="tags icon"></i>
          分类
        </h4>
        <div class="ui icon buttons">
          <button class="ui button" @click="turnToPersonalMessage">
            <i class="envelope icon"></i>
          </button>
          <button class="ui button" @click="turnToPersonalFollowing">
            <i class="user plus icon"></i>
          </button>
          <button class="ui button" @click="turnToPersonalFollowed">
            <i class="users icon"></i>
          </button>
          <button class="ui button" @click="turnToWatchOut">
            <i class="american sign language interpreting icon"></i>
          </button>
          <button class="ui button" @click="turnToObserve">
            <i class="eye icon"></i>
          </button>
        </div>
        <div class="ui icon buttons">
          <button class="ui button" @click="turnToPersonalCollections">
            <i class="bookmark icon"></i>
          </button>
          <button class="ui button" @click="turnToPersonalEditeMine">
            <i class="edit icon"></i>
          </button>
          <button class="ui button" @click="turnToPersonalData">
            <i class="user icon"></i>
          </button>
          <button class="ui button">
            <i class="user secret icon"></i>
          </button>
          <button class="ui button">
            <i class="folder icon"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import headers from "./headers";
import axios from "axios";

export default {
  name: "sidebar",
  data() {
    return {
      getHeight: window.innerHeight - 30,
    };
  },

  components: { headers },
  methods: {
    /*turnToPersonalArchive() {
      this.$router.push("/home/personal/archive");
    },*/
    turnToPersonalMessage() {
      this.$router.push("/home/personal/message");
    },
    turnToPersonalEditeMine() {
      this.$router.push("/home/personal/editemine");
    },
    turnToPersonalFollowing() {
      this.$router.push("/home/personal/following");
    },
    turnToPersonalData() {
      this.$router.push("/home/personal/personaldata");
    },
    turnToPersonalFollowed() {
      this.$router.push("/home/personal/followed");
    },
    turnToPersonalCollections() {
      this.$router.push("/home/personal/collections");
    },
    turnToWatchOut() {
      this.$router.push("/home/personal/watchout");
    },
    turnToObserve() {
      this.$router.push("/home/personal/observe");
    },
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/user/getUserData/")
      .then(function (response) {
        console.log(response);
        that.$store.commit("getNewIcon", response.data.userSerializer.icon);
        that.$store.commit(
          "getNewUsername",
          response.data.userSerializer.user.username
        );
        if (response.data.userSerializer.signature) {
          that.$store.commit(
            "getNewSignature",
            response.data.userSerializer.signature
          );
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  },
};
</script>
<style scoped>
.sidebar {
  width: 230px;
  min-height: 100%;
  height: auto;
  text-align: center;
  position: fixed;
}

.navigate {
  width: 870px;
  height: 50px;
  float: left;
  margin-left: 230px;
}

.main {
  width: 870px;
  float: left;
  margin-left: 230px;
}

.button {
  background-color: white;
}
</style>
