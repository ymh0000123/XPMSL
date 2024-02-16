import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "XPMSL",
  description: "XPMSL官方文档",

  theme,
  head: [
    ["script", { src: "https://ymh0000123.github.io/js/xn.js" }],
    ["script", { src: "https://unpkg.com/genshin-good-words/script_npm.js" }]
  ]

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
