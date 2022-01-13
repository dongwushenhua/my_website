<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div class="ui shuffling fluid card">
          <shuffling></shuffling>
        </div>
      </div>
      <div class="mainContent"style="margin-top: -30px">
        <div class="ui basic segment">
          <!--博客内容          -->
          <div
            v-for="(item, index) in articleList"
            key="item.id"
            style="margin-top: 14px"
          >
            <div class="ui fluid card" v-if="item.title == '欢迎新人'">
              <div class="ui basic segment">
                <div class="ui large feed">
                  <div class="event">
                    <div class="label">
                      <img :src="item.postMan.icon"/>
                    </div>
                    <div class="content">
                      <div class="summary">
                        <a class="user">
                          <router-link
                            :to="{
                              path: '/home/visitor',
                              query: { userName: item.postMan.user.username },
                            }"
                          >
                            {{ item.postMan.user.username }}
                          </router-link>
                        </a
                        >加入了本组织
                        <div class="date">
                          {{ item.createTime.split("T")[0] }}
                          {{ item.createTime.split("T")[1].split(".")[0] }}
                        </div>
                        <button
                          class="ui right floated circular blue icon button"
                          @click="addDirectMessage(item.postMan.user.username)"
                        >
                          <i class="envelope icon"></i>
                        </button>
                        <button
                          class="ui right floated circular icon button"
                          @click="follow(item.postMan.user.username)"
                        >
                          <i class="heart icon"></i>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--新人加入提醒          -->
            <!--            <div class="ui fluid card" v-else-if="item.views > 10">
                          <div class="content">
                            <i class="right floated like icon"></i>
                            <i class="right floated star icon"></i>
                            <a class="header">
                              <router-link
                                :to="{
                                  path: '/article/specific',
                                  query: { articleId: item.id },
                                }"
                                >{{ item.title }}
                              </router-link>
                            </a>
                            <div class="description">
                              <p></p>
                            </div>
                          </div>
                          <div class="extra content">
                            <span class="left floated like">
                              <i class="like icon"></i>
                              Like
                            </span>
                            <span class="right floated star">
                              <i class="star icon"></i>
                              Favorite
                            </span>
                          </div>
                        </div>-->
            <!--          //热门文章-->
            <div class="ui segment" v-else>
              <div class="ui items">
                <div class="item">
                  <div class="image">
                    <img src="../../../assets/PBG.jpg">
                  </div>
                  <div class="content">
                    <a class="header">
                      <router-link
                        :to="{
                                  path: '/article/specific',
                                  query: { articleId: item.id },
                                }"
                      >{{ item.title }}
                      </router-link>
                    </a>
                    <div class="meta">
                      <a>
                        <router-link
                          :to="{
                                  path: '/home/visitor',
                                  query: { userName: item.postMan.user.userame },
                                }"
                        >{{ item.postMan.user.username }}
                        </router-link>
                      </a>
                    </div>
                    <div class="description">
                      <p>纸短情长啊，诉不完当时年少</p>
                    </div>
                    <div class="extra">
                      {{ item.createTime.split("T")[0] }}
                      {{ item.createTime.split("T")[1].split(".")[0] }}
                    </div>
                    <!--                    <div>
                                          <a
                                          class="ui label"
                                          v-for="tags in item.articleTags"
                                          style="margin-top: 3px"
                                        >
                    &lt;!&ndash;                      <img
                                            class="ui right spaced avatar image"
                                            :src="tags.tagCreater.icon"
                                          />&ndash;&gt;
                                          {{ tags.tagName }}
                                        </a>
                                        </div>-->
                  </div>
                </div>
              </div>
            </div>
            <!-- 有概述无标签            -->
            <!--            <div class="ui fluid card" v-else-if="item.articleTags.length > 0">
                          <div class="content">
                            <a class="header">
                              <router-link
                                :to="{
                                  path: '/article/specific',
                                  query: { articleId: item.id },
                                }"
                              >{{ item.title }}
                              </router-link>
                            </a>
                            <div class="meta">
                              <span class="right floated time"
                              >{{ item.createTime.split("T")[0] }}
                                {{ item.createTime.split("T")[1].split(".")[0] }}</span
                              >
                              &lt;!&ndash;                  <span class="category">sss</span>&ndash;&gt;
                            </div>
                            <div class="description">
                              <p></p>
                            </div>
                          </div>
                          <div class="extra content">
            &lt;!&ndash;                <a class="ui label">
                              <img
                                class="ui right spaced avatar image"
                                :src="item.postMan.icon"
                              />
                              <router-link
                                :to="{
                                  path: '/home/visitor',
                                  query: { userName: item.postMan.user.userame },
                                }"
                              >{{ item.postMan.user.username }}
                              </router-link>
                            </a>&ndash;&gt;
                            <a
                              class="ui label"
                              v-for="tags in item.articleTags"
                              style="margin-top: 3px"
                            >
            &lt;!&ndash;                  <img
                                class="ui right spaced avatar image"
                                :src="tags.tagCreater.icon"
                              />&ndash;&gt;
                              {{ tags.tagName }}
                            </a>
                          </div>
                        </div>-->
            <!--          //有标签-->
            <!--            <div class="ui fluid card" v-else>
                          <div class="content">
                            <img
                              class="ui left mini floated circular image"
                              :src="item.postMan.icon"
                            />
                            <a class="header">
                              <router-link
                                :to="{
                                  path: '/article/specific',
                                  query: { articleId: item.id },
                                }"
                              >{{ item.title }}
                              </router-link>
                            </a>
                            <div class="meta">
                              {{ item.createTime.split("T")[0] }}
                              {{ item.createTime.split("T")[1].split(".")[0] }}
                            </div>
                            <div class="description">
                              Elliot requested permission to view your contact details
                            </div>
                          </div>
                          <div class="extra content">
            &lt;!&ndash;                <a class="ui label">
                              <img
                                class="ui right spaced avatar image"
                                :src="item.postMan.icon"
                              />
                              <router-link
                                :to="{
                                  path: '/home/visitor',
                                  query: { userName: item.postMan.user.userame },
                                }"
                              >{{ item.postMan.user.username }}
                              </router-link>
                            </a>&ndash;&gt;
                            <a
                              class="ui label"
                              v-for="tags in item.articleTags"
                              style="margin-top: 3px"
                            >
            &lt;!&ndash;                  <img
                                class="ui right spaced avatar image"
                                :src="tags.tagCreater.icon"
                              />&ndash;&gt;
                              {{ tags.tagName }}
                            </a>
                          </div>
                        </div>-->
          </div>
          <!--          //无标签-->
          <!--          <div class="ui fluid card">
                      <div class="content">
                        <img
                          class="ui right floated mini circular image"
                          src="../../../assets/avatar.jpg"
                        />
                        <div class="header">Jenny Hess</div>
                        <div class="meta">New Member</div>
                        <div class="description">
                          Jenny wants to add you to the group <b>best friends</b>
                        </div>
                      </div>
                      <div class="extra content">
                        <div class="ui two buttons">
                          <div class="ui basic green button">Approve</div>
                          <div class="ui basic red button">Decline</div>
                        </div>
                      </div>
                    </div>
                    &lt;!&ndash;     投票     &ndash;&gt;
                    <div class="ui fluid card">
                      <div class="content">
                        <div class="header">Elliot Fu</div>
                        <div class="description">
                          Elliot Fu is a film-maker from New York.
                        </div>
                      </div>
                      <div class="ui bottom attached button">
                        <i class="add icon"></i>
                        Add Friend
                      </div>
                    </div>
                    &lt;!&ndash;还没想好要干哈&ndash;&gt;
                    <div class="ui fluid card">
                      <div class="content">
                        <div class="header">Cute Dog</div>
                        <div class="meta">2 days ago</div>
                        <div class="description">
                          <p>
                            Cute dogs come in a variety of shapes and sizes. Some cute
                            dogs are cute for their adorable faces, others for their tiny
                            stature, and even others for their massive size.
                          </p>
                          <p>
                            Many people also have their own barometers for what makes a
                            cute dog.
                          </p>
                        </div>
                      </div>
                      <div class="extra content">
                        <i class="check icon"></i>
                        121 Votes
                      </div>
                    </div>
                    &lt;!&ndash;       热门投票结果   &ndash;&gt;
                    <div class="ui fluid card">
                      <div class="content">
                        <div class="header">Project Timeline</div>
                      </div>
                      <div class="content">
                        <h4 class="ui sub header">Activity</h4>
                        <div class="ui small feed">
                          <div class="event">
                            <div class="content">
                              <div class="summary">
                                <a>Elliot Fu</a> added <a>Jenny Hess</a> to the project
                              </div>
                            </div>
                          </div>
                          <div class="event">
                            <div class="content">
                              <div class="summary">
                                <a>Stevie Feliciano</a> was added as an
                                <a>Administrator</a>
                              </div>
                            </div>
                          </div>
                          <div class="event">
                            <div class="content">
                              <div class="summary">
                                <a>Helen Troy</a> added two pictures
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="extra content">
                        <button class="ui button">Join Project</button>
                      </div>
                    </div>-->
          <!-- 热门数据展示-->
        </div>
      </div>
      <div class="ui basic segment">
        <div class="paging">
          <el-pagination
            layout="prev, pager, next"
            @current-change="handleCurrentChange"
            :page-count="pageSize"
            :hide-on-single-page="true"
          >
          </el-pagination>
        </div>
      </div>
    </div>
    <div class="f">
      <div class="ui third basic segment">
        <h4 class="ui right floated header">热门文章</h4>
        <div class="ui clearing divider"></div>
        <div>
          <a class="ui label" v-for="item in hotArticleList" key="item.id">
            <router-link
              :to="{
                path: '/article/specific',
                query: { articleId: item.id },
              }"
            >
              <img
                class="ui right spaced avatar image"
                :src="item.postMan.icon"
              />
              {{ item.title }}
            </router-link>
          </a>
        </div>
      </div>
      <div class="ui basic segment">
        <h4 class="ui right floated header">网站信息</h4>
        <div class="ui clearing divider"></div>
        <div>
          <aboutme></aboutme>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import shuffling from "../../basic/components/shuffling";
import aboutme from "../../basic/components/aboutme";
import axios from "axios";

export default {
  name: "home",
  data() {
    return {articleList: [], hotArticleList: [], cover: [], pageSize: 0};
  },
  components: {aboutme, shuffling},
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/article/showAllArticle/", {
        params: {page: 1},
      })
      .then(function (response) {
        console.log(response);
        that.articleList = response.data.articlesSerializer;
        that.pageSize = response.data.pageNum;
      })
      .catch(function (error) {
        console.log(error);
      });
    axios
      .get("http://127.0.0.1:8000/article/showHotArticle/")
      .then(function (response) {
        console.log(response);
        that.hotArticleList = response.data.nowArticlesSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    handleCurrentChange(val) {
      var that = this;
      var nowPage = val;
      axios
        .get("http://127.0.0.1:8000/article/showAllArticle/", {
          params: {page: nowPage},
        })
        .then(function (response) {
          console.log(response);
          that.articleList = response.data.articlesSerializer;
          that.pageSize = response.data.pageNum;
        })
        .catch(function (error) {
          console.log(error);
        });
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
          that.userFollowingList = response.data.followedSerializer;
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
        .then(({value}) => {
          if (value) {
            axios
              .post("http://127.0.0.1:8000/user/addDirectMessage/", {
                to: name,
                message: value,
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
          } else {
            this.$message({
              type: "warning",
              message: "请输入私信内容",
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

.shuffling {
  height: 200px;
}

.label {
  margin-top: 5px;
}

.paging {
  margin-left: 20%;
}
</style>
