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
  border: 1px solid #ddd;
  padding: 16px;
  width: 200px;
  border-radius: 8px; /* 添加圆角 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 添加阴影 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 添加过渡效果 */
}

.card:hover {
  transform: translateY(-5px); /* 鼠标悬停时上移 */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* 鼠标悬停时增加阴影 */
}
.right {
    float: right;
}
.box {
    display: inline-block;
    padding: 10px 20px; /* 设置内边距，以控制链接框大小 */
    background-color: #0295ff; /* 设置背景色为 #0295ff */
    border-radius: 10px; /* 设置圆角为 10px */
    color: white; /* 设置文本颜色为白色 */
    text-decoration: none; /* 移除下划线 */
}

</style>

# 模块列表（自动同步）  
::: info 提醒
我们 ==无法保障这些模块安全== ，请自行判断。  
如果想要添加你的模块，请先在[GitHub](https://github.com/XPMSL/XPMSL-Modules)上提交PR。
:::

<div class="card-container">
    <div v-for="item in items" :key="item.url" class="card">
      <h3>{{ item.name }}</h3>
      <a :href="item.url" target="_blank" class="right box">下载</a>
    </div>
  </div>
