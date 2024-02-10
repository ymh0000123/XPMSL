module.exports = {
    base:'/XPMSL/',
    title: 'XPMSL',
    description: 'Just playing around',
    description: "description",
    head: [
        ['link', { rel: 'icon', href: '/ico.png' }]
    ],
    plugins: ['@vuepress/active-header-links', {
        sidebarLinkSelector: '.sidebar-link',
        headerAnchorSelector: '.header-anchor'
    }],

    themeConfig: {
        sidebar: [
            {
                title: 'XPMSL',
                path: '/zh-cn/',
                collapsable: false,
                sidebarDepth: 5,
                children: [
                    '/',
                    '/zh-cn/',
                    '/zh-cn/historicalversion'
                ]
            },
        ],
        nav: [
            { text: 'Home', link: '/' },
            {
                text: '其他',
                ariaLabel: 'Language Menu',
                items: [
                    { text: '历史版本', link: '/zh-cn/historicalversion' }
                ]
            }
        ]
    }

    /*评论*/
    /*plugins: [
        [
        "vuepress-plugin-giscus", {
            repo: "[repo]",
            repoId: "[repo id]",
            category: "[category name]"
            categoryId: "[category id]",
            mapping: "[page <-> discussion mapping]",
            reactionsEnabled: "[enable reactions or not?]",
            theme: "[theme]",
            lang: "[language]", 
            crossorigin: "[crossorigin]"
        }
        ]
    ]*/

}