<template>
  <div class="ui segment">
    <el-row :gutter="24">
      <el-col :span="4"
        ><h4 style="margin-left: 10px; margin-top: 10px">用户昵称</h4></el-col
      >
      <el-col :span="8">
        <div class="ui fluid input">
          <input
            type="text"
            :placeholder="$store.state.icon"
            v-model="nickname"
          />
        </div>
      </el-col>
      <el-col :span="3"
        ><h4 style="margin-left: 15px; margin-top: 10px">性别</h4></el-col
      >
      <el-col :span="8">
        <div class="ui fluid selection dropdown" style="width: 175px">
          <input type="hidden" name="gender" />
          <i class="dropdown icon"></i>
          <div class="default text" v-if="$store.state.sex">
            <div v-if="$store.state.sex == 'true'">男</div>
            <div v-if="$store.state.sex == 'false'">女</div>
          </div>
          <div class="default text" v-else>无</div>
          <div class="menu">
            <div class="item" @click="boy()">男</div>
            <div class="item" @click="girl()">女</div>
          </div>
        </div>
      </el-col>
    </el-row>
    <br /><el-row :gutter="24">
      <el-col :span="4"
        ><h4 style="margin-left: 10px; margin-top: 10px">修改密码</h4></el-col
      >
      <el-col :span="8">
        <div class="ui fluid input">
          <input type="text" placeholder="长度为7至11" v-model="passWord" />
        </div>
      </el-col>
      <el-col :span="4"><h4 style="margin-top: 10px">确认密码</h4></el-col>
      <el-col :span="8">
        <div class="ui fluid input" style="margin-left: -22px; width: 175px">
          <input
            type="text"
            placeholder="再次输入确认"
            v-model="surePassWord"
          />
        </div>
      </el-col> </el-row
    ><br /><el-row :gutter="24">
      <el-col :span="4"
        ><h4 style="margin-left: 10px; margin-top: 10px">个性签名</h4></el-col
      >
      <el-col :span="19">
        <div class="ui fluid input">
          <input
            type="text"
            :placeholder="$store.state.signature"
            v-model="signature"
          />
        </div>
      </el-col> </el-row
    ><br /><el-row :gutter="24">
      <el-col :span="4"
        ><h4 style="margin-left: 10px; margin-top: 10px">联系方式</h4></el-col
      >
      <el-col :span="19">
        <div class="ui fluid input">
          <input
            type="text"
            :placeholder="$store.state.contact"
            v-model="contact"
          />
        </div>
      </el-col>
    </el-row>

    <div
      class="ui circular vertical green animated icon button"
      tabindex="0"
      @click="submitPersonalFile()"
      style="margin-top: 15px; margin-left: 80%"
    >
      <div class="hidden content">确定</div>
      <div class="visible content">
        <i class="check icon"></i>
      </div>
    </div>

    <div class="s2">
      <div class="s3">
        <el-upload
          class="avatar-uploader"
          action=""
          :auto-upload="false"
          :show-file-list="false"
          :on-change="changeUpload"
          name="icon"
        >
          <img v-if="imageUrl" :src="imageUrl" class="avatar" />
          <i
            v-else
            class="el-icon-plus avatar-uploader-icon"
            style="width: 229px"
          ></i>
        </el-upload>
        <div class="ui disabled fluid button">上传</div>
      </div>
    </div>
    <el-dialog
      title="图片剪裁"
      :visible.sync="dialogVisible"
      :close-on-press-escape="false"
      :close-on-click-modal="false"
      append-to-body
      ><input
        type="file"
        id="uploads"
        :value="imgFile"
        style="position: absolute; clip: rect(0 0 0 0)"
        accept="image/png, image/jpeg, image/gif, image/jpg"
        @change="uploadImg($event, 1)"
      />

      <div class="cropper-content">
        <div class="cropper" style="text-align: center">
          <vueCropper
            ref="cropper"
            :img="option.img"
            :outputSize="option.size"
            :outputType="option.outputType"
            :info="true"
            :canScale="option.canScale"
            :autoCrop="option.autoCrop"
            :autoCropWidth="option.autoCropWidth"
            :autoCropHeight="option.autoCropHeight"
            :full="option.full"
            :fixedBox="option.fixedBox"
            :fixed="option.fixed"
            :fixedNumber="option.fixedNumber"
            :canMove="option.canMove"
            :canMoveBox="option.canMoveBox"
            :original="option.original"
            :centerBox="option.centerBox"
            :infoTrue="option.infoTrue"
            :enlarge="option.enlarge"
            :mode="option.mode"
          >
          </vueCropper>
        </div>
        <!--        <div class="show-preview">
                  <div :style="previews.div" class="preview">
                    <img :src="previews.url" :style="previews.img">
                  </div>
                </div>-->

        <!--        <div style="margin-left:20px;">
                  <div class="show-preview"
                       :style="{'width': '150px', 'height':'155px',  'overflow': 'hidden', 'margin': '5px'}">
                    <div :style="previews.div" class="preview">
                      <img :src="previews.url" :style="previews.img">
                    </div>
                  </div>
                </div>-->
        <div style="margin-top: 20px">
          <div
            class="ui vertical animated button"
            tabindex="0"
            @click="changeScale(1)"
          >
            <div class="hidden content">放大</div>
            <div class="visible content">
              <i class="plus icon"></i>
            </div>
          </div>
          <div
            class="ui vertical animated button"
            tabindex="0"
            @click="changeScale(-1)"
          >
            <div class="hidden content">缩小</div>
            <div class="visible content">
              <i class="minus icon"></i>
            </div>
          </div>
          <div
            class="ui vertical animated button"
            tabindex="0"
            @click="rotateLeft"
          >
            <div class="hidden content">左旋转</div>
            <div class="visible content">
              <i class="undo icon"></i>
            </div>
          </div>
          <div
            class="ui vertical animated button"
            tabindex="0"
            @click="rotateRight"
          >
            <div class="hidden content">右旋转</div>
            <div class="visible content">
              <i class="redo icon"></i>
            </div>
          </div>
          <div
            class="ui vertical animated button"
            tabindex="0"
            @click="down('blob')"
          >
            <div class="hidden content">下载</div>
            <div class="visible content">
              <i class="download icon"></i>
            </div>
          </div>
        </div>
      </div>
      <div slot="footer" class="dialog-footer">
        <div
          class="ui vertical animated button"
          tabindex="0"
          @click="dialogVisible = false"
        >
          <div class="hidden content">取消</div>
          <div class="visible content">
            <i class="close icon"></i>
          </div>
        </div>
        <div
          class="ui vertical animated button"
          tabindex="0"
          @click="finish('blob')"
          :loading="loading"
        >
          <div class="hidden content">确认</div>
          <div class="visible content">
            <i class="check icon"></i>
          </div>
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";
import { VueCropper } from "vue-cropper";

export default {
  name: "editemine",
  data() {
    return {
      imgFile: "",
      imageUrl: "",
      userName: "",
      sex: "",
      signature: "",
      contact: "",
      school: "",
      /*------------------------------*/
      /*previews: {},*/
      msg: "Welcome to Your Vue.js App",
      fileImg: "",
      dialogVisible: false,
      // 防止重复提交
      loading: false,
      // 裁剪组件的基础配置option
      option: {
        img: "", // 裁剪图片的地址
        outputSize: 1, // 裁剪生成图片的质量
        outputType: "jpeg", // 裁剪生成图片的格式
        info: true, // 裁剪框的大小信息
        canScale: true, // 图片是否允许滚轮缩放
        autoCrop: true, // 是否默认生成截图框
        autoCropWidth: 320, // 默认生成截图框宽度
        autoCropHeight: 320, // 默认生成截图框高度
        fixedBox: true, // 固定截图框大小 不允许改变
        fixed: true, // 是否开启截图框宽高固定比例
        fixedNumber: [1, 1], // 截图框的宽高比例
        canMove: true, // 上传图片是否可以移动
        canMoveBox: true, // 截图框能否拖动
        original: false, // 上传图片按照原始比例渲染
        centerBox: true, // 截图框是否被限制在图片里面
        infoTrue: true, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
        full: false, // 是否输出原图比例的截图
        enlarge: "1", // 图片根据截图框输出比例倍数
        mode: "contain", // 图片默认渲染方式
      },
    };
  },
  components: {
    VueCropper,
  },
  methods: {
    submitPersonalFile() {
      var that = this;
      axios
        .post("http://127.0.0.1:8000/user/modifyUser/", {
          sex: that.sex,
          signature: that.signature,
          contact: that.contact,
          school: that.school,
        })
        .then(function (response) {
          console.log(response);
          that.$message({
            message: "修改成功",
            type: "success",
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    // 上传按钮 限制图片大小
    changeUpload(file, fileList) {
      const isLt5M = file.size / 1024 / 1024 < 5;
      if (!isLt5M) {
        this.$message.error("上传文件大小不能超过 5MB!");
        return false;
      }
      // 上传成功后将图片地址赋值给裁剪框显示图片
      this.$nextTick(() => {
        this.option.img = URL.createObjectURL(file.raw);
        this.dialogVisible = true;
      });
    },
    //放大/缩小
    changeScale(num) {
      console.log("changeScale");
      num = num || 1;
      this.$refs.cropper.changeScale(num);
    },
    //左旋转
    rotateLeft() {
      console.log("rotateLeft");
      this.$refs.cropper.rotateLeft();
    },
    //右旋转
    rotateRight() {
      console.log("rotateRight");
      this.$refs.cropper.rotateRight();
    }, // 实时预览函数
    /* realTime(data) {
       console.log('realTime')
       this.previews = data
     },*/
    //下载图片
    down(type) {
      console.log("down");
      var aLink = document.createElement("a");
      aLink.download = "author-img";
      if (type === "blob") {
        this.$refs.cropper.getCropBlob((data) => {
          this.downImg = window.URL.createObjectURL(data);
          aLink.href = window.URL.createObjectURL(data);
          aLink.click();
        });
      } else {
        this.$refs.cropper.getCropData((data) => {
          this.downImg = data;
          aLink.href = data;
          aLink.click();
        });
      }
    },
    // 点击裁剪，这一步是可以拿到处理后的地址
    finish() {
      // 获取截图的base64 数据
      this.$refs.cropper.getCropBlob((data) => {
        console.log(data);
        // do something
        this.loading = true;
        let formData = new FormData();
        formData.append("icon", data, "DX.jpg");
        //调用axios上传
        let { data: res } = axios.post(
          "http://127.0.0.1:8000/user/modifyIcon/",
          formData
        );

        /*axios
          .post("http://127.0.0.1:8000/user/modifyIcon/", {
            icon: data
          })
          .then(function (response) {
            console.log(response);
            this.$message({
              message: "上传头像成功",
              type: "success",
            });
          })
          .catch(function (error) {
            console.log(error);
          });*/
        // 把图片上传到服务器
        setTimeout(() => {
          this.loading = false;
          this.dialogVisible = false;
          this.fileImg = data;
          /*this.imageUrl = data*/
        }, 1000);
      });
    },

    /*handleAvatarSuccess(res, file) {
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    }*/
  },
};
</script>

<style scoped>
.s2 {
  width: 50%;
  float: left;
}

.s3 {
  width: 80%;
  margin: auto;
}

.labeled {
  margin-top: 15px;
}

.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}

.cropper {
  width: auto;
  height: 300px;
}

/*.show-preview {

  flex: 1;
  -webkit-flex: 1;
  display: flex;
  display: -webkit-flex;
  justify-content: center;
}

.preview {
  overflow: hidden;
  border: 1px solid #67c23a;
  background: #cccccc;
}*/
</style>
