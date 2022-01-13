<template>
  <div>
    <div class="ui info icon message">
      <i class="notched circle loading icon"></i>
      <div class="content">
        <div class="header">留意系统</div>
        <p>
          你可以在下面的输入框内输入需要关注的消息的关键字，系统在后台中会自动筛选相关信息给你。来，试试看！
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
        <br /><br />
        <div>
          <a class="ui label">
            <img
              class="ui right spaced avatar image"
              src="../../../assets/avatar.jpg"
            />
            Elliot </a
          ><a class="ui label">
            <img
              class="ui right spaced avatar image"
              src="../../../assets/avatar.jpg"
            />
            Elliot </a
          ><a class="ui label">
            <img
              class="ui right spaced avatar image"
              src="../../../assets/avatar.jpg"
            />
            Elliot </a
          ><a class="ui label">
            <img
              class="ui right spaced avatar image"
              src="../../../assets/avatar.jpg"
            />
            Elliot
          </a>
        </div>
      </div>
      <div>
        <h3 class="ui left floated header">相关文章</h3>
        <div class="ui feed">
          <div class="event">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                您已添加<a>Jenny Hess</a>至您的 <a>同事</a> 分组.
                <div class="date">3 天前</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <h3 class="ui left floated header">外链资源</h3>
        <div class="ui feed">
          <div class="event">
            <div class="label">
              <img src="../../../assets/avatar.jpg" />
            </div>
            <div class="content">
              <div class="summary">
                您已添加<a>Jenny Hess</a>至您的 <a>同事</a> 分组.
                <div class="date">3 天前</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "watchout",
};
</script>

<style scoped>
.label {
  margin-top: 5px;
}
</style>
