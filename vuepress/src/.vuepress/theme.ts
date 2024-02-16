import { hopeTheme } from "vuepress-theme-hope";

import navbar from "./navbar.js";
import sidebar from "./sidebar.js";

export default hopeTheme({

  favicon: "https://xiaofeishu-picture.pages.dev/picture/5.png",

  hostname: "https://xpmsl.pages.dev/",

  author: {
    name: "ymh0000123",
    url: "https://ymh0000123.github.io/ymh0000123/",
  },

  iconAssets: "fontawesome-with-brands",

  logo: "https://xiaofeishu-picture.pages.dev/picture/5.png",

  repo: "ymh0000123/XPMSL",

  docsDir: "src",

  // navbar
  navbar,

  // sidebar
  sidebar,

  footer: "<p>GPL-3.0 license | XPMSL免费开源 | Docs Powered by VuePress</p><p>文档由没用的小废鼠编写</p><p id='ys'></p>",

  displayFooter: true,

  // page meta
  metaLocales: {
    editLink: "在 GitHub 上编辑此页",
  },

  plugins: {
    components: {
      // 你想使用的组件
      components: [
        "Badge",
        "BiliBili",
        "CodePen",
        "PDF",
        "Replit",
        "Share",
        "SiteInfo",
        "StackBlitz",
        "VPBanner",
        "VPCard",
        "XiGua",
      ],
      rootComponents: {
        notice: [
          {
            path: "/",
            title: "欢迎来到XPSML官方文档",
            content: '<p>Hi</p><p>我们有新的镜像站</p><a href="https://xpmsl.pages.dev/">访问</a>'
          },
        ],
      },
    },

    // You should generate and use your own comment service
    comment: {
      provider: "Giscus",
      repo: "ymh0000123/XPMSL",
      repoId: "R_kgDOKNxvWg",
      category: "官网评论",
      categoryId: "DIC_kwDOKNxvWs4CZBTA",
      inputPosition: "top",

    },

    // All features are enabled for demo, only preserve features you need here
    mdEnhance: {
      align: true,
      attrs: true,

      // install chart.js before enabling it
      // chart: true,

      codetabs: true,

      // insert component easily
      // component: true,

      demo: true,

      // install echarts before enabling it
      // echarts: true,

      figure: true,
      footnote: true,

      // install flowchart.ts before enabling it
      // flowchart: true,

      // gfm requires mathjax-full to provide tex support
      // gfm: true,

      imgLazyload: true,
      imgSize: true,
      include: true,

      // install katex before enabling it
      // katex: true,

      // install mathjax-full before enabling it
      // mathjax: true,

      mark: true,

      // install mermaid before enabling it
      mermaid: true,

      playground: {
        presets: ["ts", "vue"],
      },

      // install reveal.js before enabling it
      // revealJs: {
      //   plugins: ["highlight", "math", "search", "notes", "zoom"],
      // },

      stylize: [
        {
          matcher: "Recommended",
          replacer: ({ tag }) => {
            if (tag === "em")
              return {
                tag: "Badge",
                attrs: { type: "tip" },
                content: "Recommended",
              };
          },
        },
      ],
      sub: true,
      sup: true,
      tabs: true,
      vPre: true,

      // install @vue/repl before enabling it
      // vuePlayground: true,
    },


    // uncomment these if you want a pwa
    // pwa: {
    //   favicon: "/favicon.ico",
    //   cacheHTML: true,
    //   cachePic: true,
    //   appendBase: true,
    //   apple: {
    //     icon: "/assets/icon/apple-icon-152.png",
    //     statusBarColor: "black",
    //   },
    //   msTile: {
    //     image: "/assets/icon/ms-icon-144.png",
    //     color: "#ffffff",
    //   },
    //   manifest: {
    //     icons: [
    //       {
    //         src: "/assets/icon/chrome-mask-512.png",
    //         sizes: "512x512",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-mask-192.png",
    //         sizes: "192x192",
    //         purpose: "maskable",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-512.png",
    //         sizes: "512x512",
    //         type: "image/png",
    //       },
    //       {
    //         src: "/assets/icon/chrome-192.png",
    //         sizes: "192x192",
    //         type: "image/png",
    //       },
    //     ],
    //     shortcuts: [
    //       {
    //         name: "Demo",
    //         short_name: "Demo",
    //         url: "/demo/",
    //         icons: [
    //           {
    //             src: "/assets/icon/guide-maskable.png",
    //             sizes: "192x192",
    //             purpose: "maskable",
    //             type: "image/png",
    //           },
    //         ],
    //       },
    //     ],
    //   },
    // },
    feed: {
      rss: true,
      json: true,
      icon: "https://xiaomeishu-picture.pages.dev/picture/ico.png",
      rssOutputFilename: "rss.xml",
      rssXslFilename: "rss.xsl",
    },
  },
  encrypt: {
    config: {
      // 加密
      "/course/Needs-to-be-unlocked": ["ymh0000123"],
    },
  },
});
