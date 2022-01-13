<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <img :src="imgSrc" class="ui fluid rounded image" />
        <div class="ui fluid labeled input">
          <div class="ui label">标签名</div>
          <input type="text" placeholder="" v-model="newTagName" />
        </div>
        <button
          class="ui circular green right floated vertical animated icon button"
          @click="sure()"
        >
          <div class="hidden content">确定</div>
          <div class="visible content">
            <i class="check icon"></i>
          </div>
        </button>
      </div>
    </div>
    <div class="f">
      <div class="ui basic segment">
        <h4 class="ui right floated header">已创建</h4>
        <div class="ui clearing divider"></div>
        <div>
          <a class="ui label" v-for="item in tagList" v-bind:key="item.id">
            {{ item.tagName }}
            <i class="delete icon" @click="deleteTag(item.id)"></i>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "addtags",
  data() {
    return {
      imgSrc: require("../../../assets/EBG.jpg"),
      tagList: [],
      newTagName: "",
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
    sure() {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/tags/addTag/", {
          params: {
            tagName: that.newTagName,
          },
        })
        .then(function (response) {
          console.log(response);
          that.tagList = response.data.tagsSerializer;
          that.$message({
            message: "添加成功",
            type: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteTag(tagId) {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/tags/deleteTag/", {
          params: {
            tagId: tagId,
          },
        })
        .then(function (response) {
          console.log(response);
          that.tagList = response.data.tagsSerializer;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
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
  margin-top: 14px;
}
</style>
