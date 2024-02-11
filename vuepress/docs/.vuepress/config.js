import { defaultTheme } from '@vuepress/theme-default'
import { defineUserConfig } from 'vuepress/cli'
import { viteBundler } from '@vuepress/bundler-vite'
import viteBundler from "./vi.js";

export default {
    base: '/',
    title: 'XPMSL',
    description: 'Just playing around',
    head: [
        ['link', { rel: 'icon', href: '/ico.png' }]
    ],
    plugins: [
    ],
    theme: defaultTheme({
        Locale: 'auto',
        colorModeSwitch: "true",
        home: "/",
        logo: '/ico.png',
        repo: 'ymh0000123/XPMSL',
        sidebar: [
            // SidebarItem
            {
                text: 'XPMSL',
                link: '/',
                children: [
                    {
                        text: 'Github',
                        link: 'https://github.com/ymh0000123/XPMSL',
                        children: [],
                    },
                    '/zh-cn/',
                    '/zh-cn/historicalversion',
                ],
            },
        ],
        navbar: [
            {
                text: 'Home',
                link: '/'
            },
            {
                text: "其他",
                children: [
                    {
                        text: '历史版本',
                        link: "/zh-cn/historicalversion"
                    }
                ],
            },
        ]
    }),
}
