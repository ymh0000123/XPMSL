<script>
export default {
  data() {
    return {
      releases: [],
      selectedMirror: '', // 用户选择的镜像，默认为空
    };
  },
  created() {
    this.fetchReleases();
  },
  methods: {
    async fetchReleases() {
      try {
        const response = await fetch('https://api.github.com/repos/ymh0000123/XPMSL/releases');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        this.releases = await response.json();
      } catch (error) {
        console.error("There was a problem with the fetch operation: ", error);
      }
    },
  },
};
</script>
<style>
.DataEchoUI-select {
    padding: 8px 0px;
    width: 100%;
    border: 2px solid var(--info-border-color);
    background-color: var(--info-bg-color); 
    outline: none;
    border-radius: 7px;
}
.DataEchoUI-div {
    padding: 8px 0px;
    border: 2px solid var(--important-border-color);
    background-color: var(--important-bg-color); 
    outline: none;
    border-radius: 7px;
    margin-top: 5px;
    margin-bottom: 7px;
}

.DataEchoUI-div a {
  color: var(--important-border-color);
}

</style>

# Github同步历史版本

<div>
      下载源（可使用镜像源）:
      <select v-model="selectedMirror" class="DataEchoUI-select">
        <option value="">默认Github</option>
        <option value="https://slink.ltd/">slink.ltd 镜像</option>
        <option value="https://mirror.ghproxy.com/">[⭐国内推荐] [ghproxy]ghproxy.com 镜像</option>
      </select>
    </div>
<ul>
<div v-for="release in releases" :key="release.id" class='DataEchoUI-div'>
    <h2>{{ release.name }} - {{ release.tag_name }}</h2>
    <p>更新日志：</p>
    <p>{{ release.body }}</p>
    <p>下载：</p>
    <ul>
      <div v-for="asset in release.assets" :key="asset.id">
        <a :href="selectedMirror + asset.browser_download_url" target="_blank">{{ asset.name }}</a>
      </div>
    </ul>
</div>
</ul>