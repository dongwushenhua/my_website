<template>
  <div class="bottom">
    <br />
    <div class="message">
      <img
        style="width: 100px"
        class="ui small right floated circular image"
        src="../../../assets/avatar.jpg"
      />
      <h3 class="ui header">联系我</h3>
      <div class="ui hidden divider">
        扫描右边二维码提出您的宝贵意见，么么哒
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "bottom",
};
</script>

<style scoped>
.bottom {
  width: 850px;
  height: 200px;
}
.message {
  width: 90%;
  margin: auto;
}
</style>
