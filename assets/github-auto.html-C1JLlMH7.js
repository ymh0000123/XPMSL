import{o as r,c as a,b as e,d as p,w as m,v as d,F as h,f as c,t as n}from"./app-ByR6HzJY.js";import{_ as u}from"./plugin-vue_export-helper-DlAUqK2U.js";const _={data(){return{releases:[],selectedMirror:""}},created(){this.fetchReleases()},methods:{async fetchReleases(){try{const o=await fetch("https://api.github.com/repos/ymh0000123/XPMSL/releases");if(!o.ok)throw new Error("Network response was not ok");this.releases=await o.json()}catch(o){console.error("There was a problem with the fetch operation: ",o)}}}},g=e("h1",{id:"github同步历史版本",tabindex:"-1"},[e("a",{class:"header-anchor",href:"#github同步历史版本"},[e("span",null,"Github同步历史版本")])],-1),y=e("option",{value:""},"默认Github",-1),b=e("option",{value:"https://slink.ltd/"},"slink.ltd 镜像",-1),f=e("option",{value:"https://mirror.ghproxy.com/"},"[⭐国内推荐] [ghproxy]ghproxy.com 镜像",-1),v=[y,b,f],w=e("p",null,"更新日志：",-1),k=e("p",null,"下载：",-1),x=["href"];function M(o,l,T,G,s,z){return r(),a("div",null,[g,e("div",null,[p(" 下载源（可使用镜像源）: "),m(e("select",{"onUpdate:modelValue":l[0]||(l[0]=t=>s.selectedMirror=t),class:"DataEchoUI-select"},v,512),[[d,s.selectedMirror]])]),e("ul",null,[(r(!0),a(h,null,c(s.releases,t=>(r(),a("div",{key:t.id,class:"DataEchoUI-div"},[e("h2",null,n(t.name)+" - "+n(t.tag_name),1),w,e("p",null,n(t.body),1),k,e("ul",null,[(r(!0),a(h,null,c(t.assets,i=>(r(),a("div",{key:i.id},[e("a",{href:s.selectedMirror+i.browser_download_url,target:"_blank"},n(i.name),9,x)]))),128))])]))),128))])])}const S=u(_,[["render",M],["__file","github-auto.html.vue"]]),P=JSON.parse('{"path":"/zh-cn/github-auto.html","title":"Github同步历史版本","lang":"zh-CN","frontmatter":{"description":"Github同步历史版本 下载源（可使用镜像源）: {{ release.name }} - {{ release.tag_name }} 更新日志： {{ release.body }} 下载： {{ asset.name }} ","head":[["meta",{"property":"og:url","content":"https://xpmsl.pages.dev/XPMSL/zh-cn/github-auto.html"}],["meta",{"property":"og:site_name","content":"XPMSL"}],["meta",{"property":"og:title","content":"Github同步历史版本"}],["meta",{"property":"og:description","content":"Github同步历史版本 下载源（可使用镜像源）: {{ release.name }} - {{ release.tag_name }} 更新日志： {{ release.body }} 下载： {{ asset.name }} "}],["meta",{"property":"og:type","content":"article"}],["meta",{"property":"og:locale","content":"zh-CN"}],["meta",{"property":"og:updated_time","content":"2024-03-14T13:28:41.000Z"}],["meta",{"property":"article:author","content":"ymh0000123"}],["meta",{"property":"article:modified_time","content":"2024-03-14T13:28:41.000Z"}],["script",{"type":"application/ld+json"},"{\\"@context\\":\\"https://schema.org\\",\\"@type\\":\\"Article\\",\\"headline\\":\\"Github同步历史版本\\",\\"image\\":[\\"\\"],\\"dateModified\\":\\"2024-03-14T13:28:41.000Z\\",\\"author\\":[{\\"@type\\":\\"Person\\",\\"name\\":\\"ymh0000123\\",\\"url\\":\\"https://ymh0000123.github.io/ymh0000123/\\"}]}"]]},"headers":[],"git":{"createdTime":1710422921000,"updatedTime":1710422921000,"contributors":[{"name":"没用的小废鼠","email":"107793048+ymh0000123@users.noreply.github.com","commits":1}]},"readingTime":{"minutes":0.75,"words":224},"filePathRelative":"zh-cn/github-auto.md","localizedDate":"2024年3月14日","autoDesc":true}');export{S as comp,P as data};