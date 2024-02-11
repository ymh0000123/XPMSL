import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "简单快速",
    Svg: require("@site/static/img/undraw_docusaurus_mountain.svg").default,
    description: <>使用python编写，并且有gui操作界面</>,
  },
  {
    title: "免费开源",
    Svg: require("@site/static/img/undraw_docusaurus_tree.svg").default,
    description: <>代码需要遵守GPL-3.0 license。</>,
  },
  {
    title: "Powered by Docusaurus",
    Svg: require("@site/static/img/undraw_docusaurus_react.svg").default,
    description: (
      <>
        Docusaurus是一个不错的文档生成工具，并且是开源免费的。
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
