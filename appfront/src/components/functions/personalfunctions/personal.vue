<template>
  <div class="framework">
    <div class="main">
      <div class="ui basic segment">
        <div class="ui fluid card">
          <img class="ui fluid image" src="../../../assets/background.jpg" />
        </div>
      </div>
      <div class="mainContent" style="margin-top: -30px">
        <div class="ui basic segment">
          <router-view></router-view>
        </div>
        <!-- <div class="ui basic segment">
          <div>
            <div class="ui fluid card">
              <div class="content">
                <el-empty description="暂无内容"></el-empty>
              </div>
            </div>
          </div>
        </div> -->
      </div>
      <!-- <div class="ui basic segment">
        <div class="paging">
          <el-pagination
            layout="prev, pager, next"
            @current-change="handleCurrentChange"
            :page-count="pageSize"
            :hide-on-single-page="true"
          >
          </el-pagination>
        </div>
      </div> -->
    </div>
    <div class="f">
      <img
        class="ui circular centered image"
        style="width: 120px"
        :src="$store.state.icon"
      />
      <!-- <h3>{{ $store.state.username }}</h3>
      <p style="color: grey">
        {{ $store.state.signature }}
      </p> -->
      <div class="ui basic segment">
        <h4 class="ui right floated header">留言板</h4>
        <div class="ui clearing divider"></div>
        <div class="ui feed">
          <div class="event" v-for="item in visitorMessageList" key="item.id">
            <div class="label">
              <img :src="item.actor.icon" />
            </div>
            <div class="content">
              <div class="summary">
                {{ item.action_object.message }}
              </div>
              <div class="meta">
                <a class="like" @click="deleteVisitorMessage(item.id)">
                  <i class="trash icon"></i> 删除
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="ui fluid input">
          <input type="text" placeholder="" v-model="messageContent" />
        </div>
        <div
          class="ui circular right floated icon blue vertical animated button"
          tabindex="0"
          @click="addVisitorMessage()"
          style="margin-top: 10px"
        >
          <div class="hidden content">留言</div>
          <div class="visible content">
            <i class="comments icon"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--  <div>
      <div class="ui basic segment">
        <div>
          <div class="ui fluid card">
            <div class="content">
              <el-empty description="暂无内容"></el-empty>
            </div>
          </div>
        </div>
      </div>
      <div class="ui basic segment">
        <div
          v-for="(item, index) in personalArticleList"
          key="item.id"
          style="margin-top: 14px"
        >
          <div class="ui fluid card" v-if="item.articleTags.length > 0">
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
              <a class="ui label">
                <img
                  class="ui right spaced avatar image"
                  :src="item.postMan.icon"
                />
                <router-link
                  :to="{
                    path: '/home/visitor',
                    query: { userName: item.postMan.user.username },
                  }"
                >{{ item.postMan.user.username }}
                </router-link>
              </a>
              <a
                class="ui label"
                v-for="tags in item.articleTags"
                style="margin-top: 3px"
              >
                <img
                  class="ui right spaced avatar image"
                  :src="tags.tagCreater.icon"
                />
                {{ tags.tagName }}
              </a>
            </div>
          </div>
          &lt;!&ndash;          //有标签&ndash;&gt;
          <div class="ui fluid card" v-else>
            <div class="content">
              <img
                class="ui left floated mini circular image"
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
          </div>
        </div>
      </div>
    </div>-->
</template>

<script>
import axios from "axios";

export default {
  name: "personal",
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
</style>
