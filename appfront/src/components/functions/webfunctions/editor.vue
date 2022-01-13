<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <!--        <img :src="imgSrc" class="ui fluid rounded image" />-->
        <div class="ui icon message">
          <i class="inbox icon"></i>
          <div class="content">
            <div class="header">文章说明</div>
            <p>坚持原创，从我做起</p>
          </div>
        </div>
        <div class="ui fluid labeled input">
          <div class="ui label">标题</div>
          <input type="text" placeholder="" v-model="title"/>
        </div>
        <div class="ui fluid labeled input">
          <div class="ui label">概述</div>
          <input type="text" placeholder="" v-model="title"/>
        </div>
        <tinyMce class="tinyMce" @input="getContent"></tinyMce>
        <button class="ui icon circular button">
          博客
        </button>
        <button class="ui icon circular button">
          日记
        </button>
        <button class="ui icon circular button">
          快记
        </button>
        <button class="ui icon circular button">
          总结
        </button>
        <button class="ui icon circular button">
          提醒好友
        </button>
        <div
          class="ui circular right floated icon vertical green animated button"
          tabindex="0"
          @click="submit()"
        >
          <div class="hidden content">确定</div>
          <div class="visible content">
            <i class="check icon"></i>
          </div>
        </div>
        <button class="ui right floated icon circular button">
          私密
        </button>
      </div>
    </div>
    <div class="f">
      <div class="ui basic segment">
        <h4 class="ui right floated header">标签选择</h4>
        <div class="ui clearing divider"></div>
        <div>
          <a
            class="ui label"
            v-for="item in tagList"
            v-bind:key="item.id"
            @click="chooseTag(item.tagName, item.id)"
          >
            {{ item.tagName }}
          </a>
        </div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">已选标签</h4>
        <div class="ui clearing divider"></div>
        <div>
          <a
            class="ui label"
            v-for="item in chooseTagList"
            v-bind:key="item.tagId"
          >
            {{ item.tagName }}
            <i
              class="delete icon"
              @click="deleteTag(item.tagId, item.tagName)"
            ></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import tinyMce from "../../basic/components/tinyMce";

export default {
  inject: ["content"],
  name: "editor",
  components: {tinyMce},
  data() {
    return {
      content: "",
      imgSrc: require("../../../assets/EBG.jpg"),
      tagList: [],
      chooseTagList: [],
      tagIdList: [],
      tagNameList: [],
    };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/tags/showPersonalTags/")
      .then(function (response) {
        console.log(response);
        that.tagList = response.data.tagsSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    getContent(value) {
      this.content = value;
      console.log("____________________");
      console.log(this.content);
    },
    // 设置保存发送后台数据事件
    submit() {
      console.log("++++++++++++++++");
      console.log(this.content);

      var that = this;
      if (this.title && this.content) {
        axios
          .post("http://127.0.0.1:8000/article/addArticle/", {
            title: this.title,
            content: this.content,
            text: "",
            tagIdList: that.tagIdList,
          })
          .then(function (response) {
            console.log(response);
            that.$message({
              message: "发布成功",
              type: "success",
            });
          })
          .catch(function (error) {
            console.log(error);
          });
        this.$router.push("/home/main");
      } else {
        this.$message({
          message: "请填写所有内容",
          type: "warning",
        });
      }
    },
    chooseTag(tagName, tagId) {
      var that = this;
      var tagObject = {tagId: "", tagName: ""};
      tagObject.tagId = tagId;
      tagObject.tagName = tagName;
      that.chooseTagList.push(tagObject);
      console.log(that.chooseTagList);
      that.tagIdList.push(tagId);
      console.log(that.tagIdList);
      that.tagNameList.push(tagName);
      console.log(that.tagNameList);
    },
    deleteTag(tagId, tagName) {
      var that = this;
      var index = that.tagIdList.indexOf(tagId);
      that.tagIdList.splice(index, 1);
      var index = that.tagNameList.indexOf(tagName);
      that.tagNameList.splice(index, 1);
      for (var i = 0; i < that.chooseTagList.length; i++) {
        if (that.chooseTagList[i].tagId === tagId) {
          that.chooseTagList.splice(i, 1);
        }
      }
      console.log(that.chooseTagList);
      console.log(that.tagIdList);
      console.log(that.tagNameList);
    },
  },

  mounted() {
  },
};
</script>
<style scoped>
.tinyMce {
  margin-top: 14px;
}

.framework {
  width: 850px;
}

.main {
  width: 600px;

  /* height: 400px;*/
  float: left;
}

.f {
  width: 250px;

  float: left;
}

.input {
  margin-top: 14px;
}

.label {
  margin-top: 10px;
}

.button {
  margin-top: 20px;
}
</style>
