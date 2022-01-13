<template>
  <div>
    <div class="background"></div>
    <div class="a">
      <div class="b">
        <button class="ui fluid teal button" @click="turnToLogIn()">
          登录
        </button>
        <button class="ui fluid teal button" @click="turnToSignIn()">
          注册
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return { getHeight: window.innerHeight / 2 - 137.5 };
  },
  methods: {
    turnToSignIn() {
      this.$router.push("/signin");
    },
    turnToLogIn() {
      this.$router.push("/login");
    },
  },
};
</script>


<style scoped>
.background {
  width: 100%;
  height: 100%;
  z-index: -1;
  position: absolute;
  background-image: linear-gradient(to left, #9c88ff, #3cadeb);
  display: flex;
  justify-content: center;
}
.a {
  margin: auto;
  position: relative;
  top: 300px;
  width: 275px;
  height: 275px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.8);
  display: flex;
}
.b {
  width: 80%;
  height: 130px;
  margin: auto;
}
.segment {
  width: 20%;
  height: 150px;
  margin: auto;
}
.button {
  margin-top: 15px;
}
</style>