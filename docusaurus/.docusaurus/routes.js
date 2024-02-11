import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/XPMSL/markdown-page',
    component: ComponentCreator('/XPMSL/markdown-page', 'f8e'),
    exact: true
  },
  {
    path: '/XPMSL/docs',
    component: ComponentCreator('/XPMSL/docs', '600'),
    routes: [
      {
        path: '/XPMSL/docs',
        component: ComponentCreator('/XPMSL/docs', '115'),
        routes: [
          {
            path: '/XPMSL/docs',
            component: ComponentCreator('/XPMSL/docs', '868'),
            routes: [
              {
                path: '/XPMSL/docs/',
                component: ComponentCreator('/XPMSL/docs/', 'aa2'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/XPMSL/docs/historicalversion',
                component: ComponentCreator('/XPMSL/docs/historicalversion', 'b00'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/XPMSL/',
    component: ComponentCreator('/XPMSL/', 'bb0'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
