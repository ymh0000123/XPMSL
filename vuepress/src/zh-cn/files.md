---
icon: fa-solid fa-box
---
<script>
export default {
  data() {
    return {
      items: []
    }
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const response = await fetch('https://xpmsl.pages.dev/announcement/list.txt');
      const text = await response.text();
      this.items = text.split('\n').map(line => {
        const match = line.match(/\[(.*?)\]\((.*?)\)/);
        return match ? { name: match[1], url: match[2] } : null;
      }).filter(item => item !== null);
    }
  }
}
</script>

<style>
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
.card {
  background-color: var(--info-border-color);
  background: var(--info-bg-color);
  border: 1px solid #4cb3d4;
  padding: 16px;
  width: 200px;
  border-radius: 8px; /* 添加圆角 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 添加过渡效果 */
}
.right {
    float: right;
}
.box {
    display: inline-block;
    padding: 10px 20px; /* 设置内边距，以控制链接框大小 */
    background-color: var(--info-border-color); /* 设置背景色 */
    border-radius: 10px; /* 设置圆角为 10px */
    color: white; /* 设置文本颜色为白色 */
    text-decoration: none; /* 移除下划线 */
}

</style>

# 模块列表（自动同步）  
::: info 提醒
我们 ==无法保障这些模块安全== ，请自行判断。  
如果想要添加你的模块，请先在[GitHub](https://github.com/ymh0000123/XPMSL-Modules)上提交PR。
:::

<div class="card-container">
    <div v-for="item in items" :key="item.url" class="card">
      <h3>{{ item.name }}</h3>
      <a :href="item.url" target="_blank" class="right box">下载</a>
    </div>
  </div>
