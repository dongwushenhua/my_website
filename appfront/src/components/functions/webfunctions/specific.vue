<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div id="canvasContent">
          <div class="ui large feed">
            <div class="event">
              <div class="label">
                <img :src="article.postMan.icon" />
              </div>
              <div class="content">
                <div class="summary">
                  <a>
                    <router-link
                      :to="{
                        path: '/home/visitor',
                        query: { userName: article.postMan.user.username },
                      }"
                      >{{ article.postMan.user.username }}
                    </router-link>
                  </a>
                  <div class="date">
                    {{ article.createTime.split("T")[0] }}
                    {{ article.createTime.split("T")[1].split(".")[0] }}
                  </div>
                </div>
              </div>
            </div>
          </div>
          <h3 style="text-align: center">{{ article.title }}</h3>
          <div v-html="articleContent" style="overflow: auto">
            {{ articleContent }}
          </div>
          <div class="ui divider"></div>
          <div style="margin-left: 30%">
            <button
              :class="likeFlag == '1' ? articleLikeIsActive : articleLike"
              @click="likeArticle()"
            >
              <div class="hidden content">{{ nowArticleLikeNumber }}</div>
              <div class="visible content">
                <i class="heart icon"></i>
              </div>
            </button>
            <button
              :class="
                collectFlag == '1' ? articleCollectIsActive : articleCollect
              "
              @click="collectArticle()"
            >
              <div class="hidden content">{{ nowArticleCollectNumber }}</div>
              <div class="visible content">
                <i class="star icon"></i>
              </div>
            </button>
            <button class="ui circular vertical animated blue icon button">
              <div class="hidden content">{{ article.views }}</div>
              <div class="visible content">
                <i class="eye icon"></i>
              </div>
            </button>
            <button
              class="ui circular vertical animated green icon button"
              @click="share()"
            >
              <div class="hidden content">分享</div>
              <div class="visible content">
                <i class="share icon"></i>
              </div>
            </button>
            <button
              v-show="showFlag"
              class="ui blue circular vertical animated icon button"
              @click="deleteArticle()"
            >
              <div class="hidden content">删除</div>
              <div class="visible content">
                <i class="trash icon"></i>
              </div>
            </button>
          </div>
          <h3 class="ui header">评论</h3>
          <div class="ui large feed">
            <div
              :class="item.parent ? child : parent"
              v-for="(item, index) in commentList"
              key="item.id"
            >
              <div class="label">
                <img :src="item.user.icon" />
              </div>
              <div class="content">
                <div class="summary">
                  <a>
                    <router-link
                      :to="{
                        path: '/home/visitor',
                        query: { userName: item.user.user.username },
                      }"
                      >{{ item.user.user.username }}
                    </router-link>
                  </a>
                  <div class="date">
                    {{ item.commentTime.split("T")[0] }}
                    {{ item.commentTime.split("T")[1].split(".")[0] }}
                  </div>
                </div>
                <div class="extra text" v-html="item.commentContent">
                  {{ item.commentContent }}
                </div>
                <div class="meta">
                  <a class="like" @click="likeComment(item.id)">
                    <i class="heart icon"></i>赞（{{ item.commentLikes }}）
                  </a>
                  <a class="like" @click="commentComment(item.id)">
                    <i class="comment icon"></i> 评论
                  </a>
                  <a class="like" @click="deleteComment(item.id)">
                    <i class="trash icon"></i>删除
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <tinyMce @input="getContent" class="tinyMce"></tinyMce>
        <div
          class="ui circular right floated vertical green animated icon button"
          tabindex="0"
          @click="addComment()"
        >
          <div class="hidden content">确定</div>
          <div class="visible content">
            <i class="check icon"></i>
          </div>
        </div>
      </div>
    </div>
    <div class="f">
      <div class="ui basic segment">
        <h4 class="ui right floated header">作者</h4>
        <br />
        <div class="ui basic segment">
          <img
            class="ui centered tiny circular image"
            :src="article.postMan.icon"
          />
          <h4>
            <a href="">
              <router-link
                :to="{
                  path: '/home/visitor',
                  query: { userName: article.postMan.user.username },
                }"
                >{{ article.postMan.user.username }}
              </router-link>
            </a>
          </h4>
          <p></p>
          <div style="width: 120px; margin: auto; margin-top: 10px">
            <button
              :class="followFlag == '1' ? followIsActive : notFollow"
              @click="follow(article.postMan.user.username)"
            >
              <div class="hidden content">关注</div>
              <div class="visible content">
                <i class="heart icon"></i>
              </div>
            </button>
            <button
              class="ui circular vertical animated blue icon button"
              @click="addDirectMessage(article.postMan.user.username)"
            >
              <div class="hidden content">私信</div>
              <div class="visible content">
                <i class="envelope icon"></i>
              </div>
            </button>
          </div>
        </div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">标签</h4>
        <br />
        <div class="ui divider"></div>
        <div>
          <a class="ui label" v-for="item in tagList" key="item.id">
            {{ item.tagName }}
          </a>
        </div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">相关文章</h4>
        <br />
        <div class="ui divider"></div>
        <div>
          <a class="ui link label" v-for="item in articleList" key="item.id">
            <router-link
              :to="{
                path: '/article/specific',
                query: { articleId: item.id },
              }"
            >
              {{ item.title }}
            </router-link>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import html2canvas from "html2canvas";
import { saveAs } from "file-saver";
import tinyMce from "../../basic/components/tinyMce";

export default {
  name: "specific",
  components: { tinyMce },

  data() {
    return {
      content: "",
      editorOption: {},
      /*----------------------------------*/
      article: "",
      articlePostMan: "",
      articleContent: "",
      commentText: "",
      commentList: [],
      articleList: [],
      likeFlag: "",
      nowCommentLike: "",
      articleLikeIsActive: "ui circular vertical animated red icon button",
      articleLike: "ui circular vertical animated icon button",
      nowArticleLikeNumber: "",
      collectFlag: "",
      articleCollectIsActive:
        "ui circular vertical animated yellow icon button",
      articleCollect: "ui circular vertical animated icon button",
      nowArticleCollectNumber: "",
      commentLikeIsActive: "red heart icon",
      commentLike: "heart icon",
      showFlag: "",
      parentId: null,
      parent: "parent event",
      child: "child event",
      commentLikeList: [],
      tagList: [],
      followFlag: "0",
      notFollow: "ui circular vertical animated icon button",
      followIsActive: "ui circular red vertical animated icon button",
      commentContent: "",
    };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/showSpecificArticle/", {
        params: { articleId: this.$route.query.articleId },
      })
      .then(function (response) {
        console.log(response);
        that.article = response.data.nowArticleSerializer;
        if (that.article.postMan.user.username == response.data.nowUser) {
          that.showFlag = true;
        } else {
          that.showFlag = false;
        }
        that.commentList = response.data.nowCommentsSerializer;
        that.articlePostMan =
          response.data.nowArticleSerializer.postMan.user.username;
        that.articleContent = response.data.nowArticleSerializer.content;
        that.likeFlag = response.data.likeFlag;
        that.nowArticleLikeNumber = response.data.nowArticleSerializer.likes;
        that.collectFlag = response.data.collectFlag;
        that.nowArticleCollectNumber =
          response.data.nowArticleSerializer.collects;
        that.tagList = response.data.nowArticleSerializer.articleTags;
        that.followFlag = response.data.followFlag;
        axios
          .get("http://127.0.0.1:8000/article/showVisitorArticle/", {
            params: { userName: that.articlePostMan },
          })
          .then(function (response) {
            console.log(response);
            that.articleList = response.data.visitorArticlesSerializer;
          })
          .catch(function (error) {
            console.log(error);
          });
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    getContent(value) {
      this.commentContent = value;
      console.log("____________________");
      console.log(this.commentContent);
    },
    likeArticle() {
      var that = this;
      console.log(this.$route.query.articleId);
      axios
        .get("http://127.0.0.1:8000/article/likeArticle/", {
          params: {
            articleId: this.$route.query.articleId,
          },
        })
        .then(function (response) {
          console.log(response);
          that.likeFlag = response.data.nowArticleLikeFlag;
          that.nowArticleLikeNumber = response.data.nowArticleLikeNumber;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    collectArticle() {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/article/collectArticle/", {
          params: { articleId: this.$route.query.articleId },
        })
        .then(function (response) {
          console.log(response);
          that.collectFlag = response.data.nowArticleCollectFlag;
          that.nowArticleCollectNumber = response.data.nowArticleCollectNumber;
          that.$message({
            message: response.data.msg,
            type: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deleteArticle() {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/article/deleteArticle/", {
          params: { articleId: this.$route.query.articleId },
        })
        .then(function (response) {
          console.log(response);
          that.$message({
            message: "删除成功",
            type: "success",
          });
          that.$router.push("/home/main");
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    likeComment(commentId) {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/comment/likeComment/", {
          params: {
            likeCommentId: commentId,
          },
        })
        .then(function (response) {
          console.log(response);
          that.commentList = response.data.nowCommentsSerializer;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    commentComment(commentId) {
      var that = this;
      that.parentId = commentId;
    },
    deleteComment(commentId) {
      var that = this;
      axios
        .get("http://127.0.0.1:8000/comment/deleteComment/", {
          params: {
            commentId: commentId,
          },
        })
        .then(function (response) {
          console.log(response);
          that.commentList = response.data.nowCommentsSerializer;
          that.$message({
            message: "删除成功",
            type: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    addComment() {
      var that = this;
      if (this.commentContent) {
        axios
          .get("http://127.0.0.1:8000/comment/addComment/", {
            params: {
              commentContent: this.commentContent,
              /*text: this.phoneEditor.txt.text(),*/
              articleId: that.$route.query.articleId,
              parentId: that.parentId,
              /*parentId: that.parentId,*/
              /*tagIdList: that.tagIdList,*/
            },
          })
          .then(function (response) {
            console.log(response.data);
            that.commentList = response.data.nowCommentsSerializer;
            that.$message({
              message: "回复成功",
              type: "success",
            });
            that.parentId = null;
          })
          .catch(function (error) {
            console.log(error);
          });
      } else {
        this.$message({
          message: "请填写评论内容",
          type: "warning",
        });
      }
    },
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
          that.followFlag = response.data.followFlag;
          that.$message({
            message: response.data.msg,
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
                this.$message({
                  type: "success",
                  message: "私信成功",
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
    share() {
      html2canvas(document.querySelector("#canvasContent"), {
        allowTaint: true,
        useCORS: true,
      }).then((canvas) => {
        canvas.toBlob(function (blob) {
          saveAs(blob, "hangge.png");
          /*document.querySelector("#canvasContent").appendChild(canvas)*/
          /*document.getElementById("test").src = canvas.toDataURL();*/
        });
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
  float: left;
}

.f {
  width: 250px;
  float: left;
}

.tinyMce {
  margin-top: 30px;
}

.label {
  margin-top: 10px;
}

h2 {
  text-align: center;
}

h4 {
  text-align: center;
}

p {
  text-align: center;
}

.ui.right.floated.vertical.green.animated.button {
  margin-top: 20px;
}

.child.event {
  margin-left: 50px;
}


</style>
