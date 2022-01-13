<template>
  <div>
    <div class="ui info icon message">
      <i class="notched circle loading icon"></i>
      <div class="content">
        <div class="header">观察系统</div>
        <p>
          你可以在下面的输入框内输入需要观察的消息的关键字，系统会自动获取大家今日关注的热点信息。来，试试看！
        </p>
      </div>
    </div>
    <el-row :gutter="24">
      <el-col :span="20"
        ><div class="ui fluid labeled input">
          <div class="ui label">关键词1</div>
          <input type="text" placeholder="请输入关键词" /></div
      ></el-col>
      <el-col :span="4"
        ><div class="ui right floated button">确定</div></el-col
      > </el-row
    ><br /><el-row :gutter="24">
      <el-col :span="20"
        ><div class="ui fluid labeled input">
          <div class="ui label">关键词2</div>
          <input type="text" placeholder="请输入关键词" /></div
      ></el-col>
      <el-col :span="4"
        ><div class="ui right floated button">确定</div></el-col
      > </el-row
    ><br /><el-row :gutter="24">
      <el-col :span="20"
        ><div class="ui fluid labeled input">
          <div class="ui label">关键词3</div>
          <input type="text" placeholder="请输入关键词" /></div
      ></el-col>
      <el-col :span="4"
        ><div class="ui right floated button">确定</div></el-col
      > </el-row
    ><br />
    <div class="ui fluid segment">
      <div>
        <h3 class="ui left floated header">相关标签</h3>
      </div>
      <div>
        <h3 class="ui left floated header">相关文章</h3>
      </div>
      <div>
        <h3 class="ui left floated header">外链资源</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "observe",
};
</script>

<style scoped>
</style>
