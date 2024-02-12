import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "XPMSL",
  description: "XPMSL官方文档",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
