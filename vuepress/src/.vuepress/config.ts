import { defineUserConfig } from "vuepress";
import theme from "./theme.js";
import { registerComponentsPlugin } from '@vuepress/plugin-register-components'


export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "XPMSL",
  description: "XPMSL官方文档",

  theme,
  head: [
    ["script", { src: "https://ymh0000123.github.io/js/xn.js" }],
    ["script", { src: "https://unpkg.com/genshin-good-words/script_npm.js" }]
  ],
  plugins: [
    registerComponentsPlugin({
      // 配置项
    }),
  ],

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
