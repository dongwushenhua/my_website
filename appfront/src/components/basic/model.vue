<template>
  <div class="ui container">
    <el-container>
      <el-aside width="230px">
        <sidebar></sidebar>
      </el-aside>
      <el-container>
        <el-header><headers></headers></el-header>
        <el-main><router-view></router-view></el-main>
        <el-footer><bottom></bottom></el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import sidebar from "./components/sidebar";
import headers from "./components/headers";
import bottom from "./components/bottom";

export default {
  name: "model",
  components: { bottom, headers, sidebar },
};
</script>

<style scoped>
.container {
  width: 1100px;
}

</style>
