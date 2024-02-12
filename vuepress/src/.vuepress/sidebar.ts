import { sidebar } from "vuepress-theme-hope";

export default sidebar({
  "/": [

    "",
    {
      text: "快速开始",
      icon: "list",
      link: "zh-cn/",
      collapsible: true,
    },

    {
      text: "历史版本",
      icon: "book",
      link: "zh-cn/historicalversion",
    },
    "Contact",
  ],
});
