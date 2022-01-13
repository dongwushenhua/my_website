<template>
  <div class="ui segment">
    <h3>发帖量</h3>
    <div id="main1" style="width: 100%; height: 400px"></div>
    <el-row>
      <el-col :span="12">
        <h3>关注</h3>
      </el-col>
      <el-col :span="12">
        <h3>粉丝</h3>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="12">
        <div id="main2" style="width: 100%; height: 200px"></div>
      </el-col>
      <el-col :span="12">
        <div id="main3" style="width: 100%; height: 200px"></div>
      </el-col>
    </el-row>
    <div class="ui five small statistics">
      <div class="statistic">
        <div class="value">
          <i class="ui small pencil alternate icon"></i> {{ dataList.articles }}
        </div>
        <div class="label">文章</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small comment icon"></i> {{ dataList.comments }}
        </div>
        <div class="label">评论</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small heart icon"></i> {{ dataList.likes }}
        </div>
        <div class="label">点赞</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small folder icon"></i> {{ dataList.collects }}
        </div>
        <div class="label">收藏</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small user plus icon"></i> {{ dataList.followings }}
        </div>
        <div class="label">关注</div>
      </div>
    </div>
    <div class="ui five small statistics">
      <div class="statistic">
        <div class="value">
          <i class="ui small users icon"></i> {{ dataList.followeds }}
        </div>
        <div class="label">粉丝</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small envelope icon"></i> {{ dataList.directMessages }}
        </div>
        <div class="label">私信</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small bell icon"></i> {{ dataList.messages }}
        </div>
        <div class="label">消息</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small calendar icon"></i> {{ dataList.networkTime }}
        </div>
        <div class="label">在网</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small hand spock icon"></i> {{ dataList.active }}
        </div>
        <div class="label">活跃</div>
      </div>
    </div>
    <div class="ui five small statistics">
      <div class="statistic">
        <div class="value">
          <i class="ui small eye icon"></i> {{ dataList.views }}
        </div>
        <div class="label">浏览</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small envelope icon"></i> {{ dataList.views }}
        </div>
        <div class="label">私信</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small bell icon"></i> {{ dataList.views }}
        </div>
        <div class="label">消息</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small calendar icon"></i> {{ dataList.views }}
        </div>
        <div class="label">在网</div>
      </div>
      <div class="statistic">
        <div class="value">
          <i class="ui small hand spock icon"></i> {{ dataList.views }}
        </div>
        <div class="label">活跃</div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import axios from "axios";

export default {
  name: "personaldata",
  data() {
    return { dataList: "" };
  },
  created() {
    var that = this;
    axios
      .get("http://127.0.0.1:8000/data/userData/")
      .then(function (response) {
        console.log(response.data);
        that.dataList = response.data.nowUserDataSerializer;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    zhexiantu() {
      var chartDom = document.getElementById("main1");
      var myChart = echarts.init(chartDom);
      var option;
      option = {
        xAxis: {
          type: "category",
          data: [
            "星期一",
            "星期二",
            "星期三",
            "星期四",
            "星期五",
            "星期六",
            "星期天",
          ],
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: "line",
          },
        ],
      };
      option && myChart.setOption(option);
    },
    bingzhuangtu1() {
      var chartDom = document.getElementById("main2");
      var myChart = echarts.init(chartDom);
      var option;
      option = {
        grid: {
          top: 20,
          bottom: 0,
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "80%",
            label: {
              show: false,
            },
            emphasis: {
              label: {
                show: false,
              },
            },
            data: [
              { value: 0, name: "搜索引擎" },
              { value: 0, name: "直接访问" },
            ],
          },
        ],
      };
      option && myChart.setOption(option);
    },
    bingzhuangtu2() {
      var chartDom = document.getElementById("main3");
      var myChart = echarts.init(chartDom);
      var option;
      option = {
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        series: [
          {
            name: "面积模式",
            type: "pie",
            radius: [10, 100],
            center: ["50%", "50%"],
            roseType: "radius",
            itemStyle: {
              borderRadius: 5,
            },
            label: {
              show: false,
            },
            emphasis: {
              label: {
                show: false,
              },
            },
            data: [
              { value: 40, name: "rose 1" },
              { value: 38, name: "rose 2" },
              { value: 32, name: "rose 3" },
              { value: 30, name: "rose 4" },
              { value: 28, name: "rose 5" },
            ],
          },
        ],
      };
      option && myChart.setOption(option);
    },
  },

  mounted() {
    this.zhexiantu();
    this.bingzhuangtu1();
    this.bingzhuangtu2();
  },
};
</script>

<style scoped>
.ui.small.five.statistics {
  margin-top: 30px;
}
</style>
