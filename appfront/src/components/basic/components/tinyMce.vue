<template>
  <div class="tinymce-editor">
    <editor
      v-model="myValue"
      :init="init"
      :disabled="disabled"
      @onClick="onClick"
    >
    </editor>
  </div>
</template>

<script>
import tinymce from "tinymce/tinymce";
import Editor from "@tinymce/tinymce-vue";
import "tinymce/themes/mobile/theme";
import "tinymce/themes/silver";
import "tinymce/icons/default/icons";
import "tinymce/plugins/image";
import "tinymce/plugins/media";
import "tinymce/plugins/table";
import "tinymce/plugins/lists";
import "tinymce/plugins/contextmenu";
import "tinymce/plugins/wordcount";
import "tinymce/plugins/colorpicker";
import "tinymce/plugins/textcolor";
import "tinymce/plugins/searchreplace";
import "tinymce/plugins/print";
import "tinymce/plugins/preview";
import "tinymce/plugins/autolink";
import "tinymce/plugins/directionality";
import "tinymce/plugins/visualblocks";
import "tinymce/plugins/visualchars";
import "tinymce/plugins/fullscreen";
import "tinymce/plugins/template";
import "tinymce/plugins/code";
import "tinymce/plugins/link";
import "tinymce/plugins/codesample";
import "tinymce/plugins/charmap";
import "tinymce/plugins/hr";
import "tinymce/plugins/pagebreak";
import "tinymce/plugins/anchor";
import "tinymce/plugins/nonbreaking";
import "tinymce/plugins/insertdatetime";
import "tinymce/plugins/advlist";
import "tinymce/plugins/imagetools";
import "tinymce/plugins/textpattern";
import "tinymce/plugins/help";
import "tinymce/plugins/emoticons";
import "tinymce/plugins/autosave";
import "tinymce/plugins/bdmap";
import "tinymce/plugins/indent2em";
import "tinymce/plugins/autoresize";
/*import 'tinymce/plugins/formatpainter'*/
import "tinymce/plugins/axupimgs";
import "tinymce/plugins/importword";
import "tinymce/plugins/kityformula-editor";
import "tinymce/plugins/emoticons";

export default {
  name: "tinyMce",
  components: {
    Editor,
  },
  props: {
    //传入一个value，使组件支持v-model绑定
    value: {
      type: String,
      default: "",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    plugins: {
      type: [String, Array],
      default:
        "print preview searchreplace autolink directionality visualblocks visualchars fullscreen image link media template code codesample table charmap hr pagebreak nonbreaking anchor insertdatetime advlist lists wordcount imagetools textpattern help emoticons autosave bdmap indent2em autoresize formatpainter axupimgs importword kityformula-editor",
    },
    toolbar: {
      type: [String, Array],
      default:
        "code undo redo restoredraft  cut copy paste selectall pastetext  forecolor backcolor bold italic underline strikethrough link anchor  alignleft aligncenter alignright alignjustify outdent indent  bullist numlist  blockquote subscript superscript removeformat  table image media charmap emoticons hr pagebreak insertdatetime print preview  fullscreen  bdmap indent2em lineheight formatpainter axupimgs importword styleselect fontselect fontsizeselect kityformula-editor",
    },
  },
  data() {
    return {
      //初始化配置
      init: {
        language_url: "/static/tinymce/langs/zh_CN.js",
        language: "zh_CN",
        skin_url: "/static/tinymce/skins/ui/oxide",
        height: 600,
        plugins: this.plugins,
        content_style: "img {max-width:100%;}",
        toolbar: this.toolbar,
        branding: false,
        menubar: false,
        fontsize_formats: "12px 14px 16px 18px 24px 36px 48px 56px 72px",
        font_formats:
          "微软雅黑=Microsoft YaHei,Helvetica Neue,PingFang SC,sans-serif;苹果苹方=PingFang SC,Microsoft YaHei,sans-serif;宋体=simsun,serif;仿宋体=FangSong,serif;黑体=SimHei,sans-serif;Arial=arial,helvetica,sans-serif;Arial Black=arial black,avant garde;Book Antiqua=book antiqua,palatino;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Georgia=georgia,palatino;Helvetica=helvetica;Impact=impact,chicago;Symbol=symbol;Tahoma=tahoma,arial,helvetica,sans-serif;Terminal=terminal,monaco;Times New Roman=times new roman,times;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats;知乎配置=BlinkMacSystemFont, Helvetica Neue, PingFang SC, Microsoft YaHei, Source Han Sans SC, Noto Sans CJK SC, WenQuanYi Micro Hei, sans-serif;小米配置=Helvetica Neue,Helvetica,Arial,Microsoft Yahei,Hiragino Sans GB,Heiti SC,WenQuanYi Micro Hei,sans-serif",
        link_list: [
          { title: "预置链接1", value: "http://www.tinymce.com" },
          { title: "预置链接2", value: "http://tinymce.ax-z.cn" },
        ],
        image_list: [
          {
            title: "预置图片1",
            value: "https://www.tiny.cloud/images/glyph-tinymce@2x.png",
          },
          {
            title: "预置图片2",
            value: "https://www.baidu.com/img/bd_logo1.png",
          },
        ],
        image_class_list: [
          { title: "None", value: "" },
          { title: "Some class", value: "class-name" },
        ],
        file_picker_callback: function (callback, value, meta) {
          if (meta.filetype === "file") {
            callback("https://www.baidu.com/img/bd_logo1.png", {
              text: "My text",
            });
          }
          if (meta.filetype === "image") {
            callback("https://www.baidu.com/img/bd_logo1.png", {
              alt: "My alt text",
            });
          }
          if (meta.filetype === "media") {
            callback("movie.mp4", {
              source2: "alt.ogg",
              poster: "https://www.baidu.com/img/bd_logo1.png",
            });
          }
        },
        //为内容模板插件提供预置模板
        templates: [
          { title: "模板1", description: "介绍文字1", content: "模板内容" },
          {
            title: "模板2",
            description: "介绍文字2",
            content:
              '<div class="mceTmpl"><span class="cdate">CDATE</span>，<span class="mdate">MDATE</span>，我的内容</div>',
          },
        ],
        //content_security_policy: "script-src *;",
        extended_valid_elements: "script[src]",
        template_cdate_format: "[CDATE: %m/%d/%Y : %H:%M:%S]",
        template_mdate_format: "[MDATE: %m/%d/%Y : %H:%M:%S]",
        autosave_ask_before_unload: false,
        toolbar_mode: "wrap",
        //此处为图片上传处理函数，这个直接用了base64的图片形式上传图片，
        //如需ajax上传可参考https://www.tiny.cloud/docs/configure/file-image-upload/#images_upload_handler
        images_upload_handler: (blobInfo, success, failure) => {
          const img = "data:image/jpeg;base64," + blobInfo.base64();
          success(img);
        },
      },
      myValue: this.value,
    };
  },
  mounted() {
    tinymce.init({});
  },
  watch: {
    value(newValue) {
      this.myValue = newValue;
    },
    myValue(newValue) {
      this.$emit("input", newValue);
      console.log(this.myValue);
    },
  },
};
</script>
<style scoped>
</style>

