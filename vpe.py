# 定义文件路径
file_path = 'vuepress/src/.vuepress/config.ts'

# 读取原始文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 替换内容
new_content = content.replace('base: "/"', 'base: "/XPMSL/"')

# 将新内容写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("文件内容已更新。")
