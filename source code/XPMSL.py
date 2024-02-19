import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import yaml
import threading
import requests
import time
import webbrowser
import http.client
import json
from tkinter import simpledialog
import argparse
import sys
import subprocess

version = "V1.1.1"
Build = "20240219"
current_build = Build
api_url = "https://xpmsl.pages.dev/"
api_releases = "releases.json"
api_download_button = "announcement/list.txt"
api_announcement = "announcement/announcement.txt"
Update_module = 'XPMSL-Update-module.exe'
github_url = "https://slink.ltd/https://github.com/"
Update_module_github = "ymh0000123/XPMSL-Update-module"

def update_or_create_releases_json(build_value, directory_path="XPMSL"):
    # 构造releases.json文件的路径
    releases_json_path = os.path.join(directory_path, "releases.json")

    # 确保directory_path目录存在
    os.makedirs(directory_path, exist_ok=True)

    # 检查文件是否存在
    if not os.path.exists(releases_json_path):
        print(f"文件{releases_json_path}不存在，将创建一个新的文件。")
        # 创建带有Build值的初始字典
        data = {"Build": build_value}
    else:
        # 如果文件存在，读取现有的JSON数据
        with open(releases_json_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # 如果文件存在但是为空或格式不正确，创建一个新的字典
                print(f"文件{releases_json_path}格式不正确，将创建一个新的文件。")
                data = {}

        # 修改数据
        data["Build"] = build_value

    # 写回文件
    with open(releases_json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"已成功将Build更新为{build_value}在{releases_json_path}")

def update_tool():
    # 获取当前脚本的目录路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构造XPMSL-Update-module.exe的完整路径
    exe_path = os.path.join(current_dir, "XPMSL-Update-module.exe")

    # 使用subprocess模块启动程序
    subprocess.run([exe_path])

# 示例调用函数
update_or_create_releases_json(Build)

def check_for_updates(current_build):
    try:
        # 请求远程JSON数据
        url = api_url + api_releases
        response = requests.get(url)
        data = response.json()
        
        # 获取远程build值并转换为整数
        remote_build = data['build']
        up_releases = data['up_releases']
        Update_download(up_releases)
        # 比较build值
        if remote_build > current_build:
            if messagebox.askyesno("更新提醒", "有新的程序版本可用，请更新！"):
                try:
                    update_tool()
                except:
                    messagebox.showerror("更新失败", "无法更新程序。")

        else:
            messagebox.showinfo("提示", "注意！你正在使用的可能是测试版。")
    except Exception as e:
        messagebox.showerror("更新检查失败", f"无法检查更新：{e}")

def check_updates_in_thread(current_build):
    update_thread = threading.Thread(target=check_for_updates, args=(current_build,))
    update_thread.start()



def open_announcement():
    # 创建解析器
    parser = argparse.ArgumentParser(description='处理命令行参数的示例。')
    
    # 添加 '-v' 或 '--verbose' 选项
    parser.add_argument('-b', '--Build', action='store_true', help='查看版本号')
    
    # 解析命令行参数
    args = parser.parse_args()

    # 根据 '-v' 或 '--verbose' 选项是否存在来决定程序行为
    if args.Build:
        print('Build')
        # 执行一些操作后，退出程序
        sys.exit()

open_announcement()


def Update_download(up_releases):
    filename = Update_module
    if not os.path.exists(filename):
        download_file_Update(up_releases)

def download_file_Update(up_releases):
    url = github_url + Update_module_github +"/releases/download/V"+ up_releases +"/"+ Update_module
    print (url)
    filename = Update_module
    try:
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        print("文件下载成功！")
    except Exception as e:
        print(f"文件下载失败：{e}")



# 在程序启动时自动检查更新（在单独的线程中）
check_updates_in_thread(current_build)


# 下载模块
# 函数，用于执行下载操作
def download_file(status_label):
    global file_listbox  # 使用全局变量 file_listbox
    selected_file = file_listbox.get(tk.ACTIVE)
    if not selected_file:
        return

    # 获取选定文件的URL
    file_url = file_info_dict[selected_file]

    try:
        response = requests.get(file_url)
        if response.status_code == 200:
            file_name = os.path.basename(file_url)
            # 获取当前工作目录
            current_directory = os.getcwd()
            # 创建目标文件夹（如果不存在）
            target_folder = os.path.join(current_directory, "XPMSL", "module")
            os.makedirs(target_folder, exist_ok=True)
            file_path = os.path.join(target_folder, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)
            status_label.config(text=f"文件 {file_name} 已成功下载到 {file_path}")

            # 下载成功时显示弹窗提示
            messagebox.showinfo("下载成功", f"文件 {file_name} 已成功下载到 {file_path}")
        else:
            status_label.config(text=f"下载失败，HTTP状态码: {response.status_code}")
    except Exception as e:
        status_label.config(text=f"下载发生错误: {str(e)}")


# 函数，用于解析文件列表
def parse_file_list(file_content):
    global file_info_dict  # 使用全局变量 file_info_dict
    file_info_dict = {}
    lines = file_content.split("\n")
    for line in lines:
        if line.strip():  # 忽略空行
            parts = line.split("](")
            if len(parts) == 2:
                file_name = parts[0].strip("[").strip()
                file_url = parts[1].strip(")").strip()
                file_info_dict[file_name] = file_url
    return file_info_dict


def open_download_module_window():
    global file_listbox  # 使用全局变量 file_listbox
    download_window = tk.Toplevel(root)
    download_window.title("下载模块")

    download_window.geometry("439x455")
    # 创建一个Frame用于容纳文件列表框和滚动条
    frame = tk.Frame(download_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # 创建滚动条
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # 创建文件列表框，并设置可见行数
    file_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    file_listbox.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=file_listbox.yview)

    # 创建状态标签
    status_label = tk.Label(download_window, text="")
    status_label.pack()

    # 获取文件列表内容
    url = api_url + api_download_button
    response = requests.get(url)

    if response.status_code == 200:
        file_content = response.text
        file_info_dict = parse_file_list(file_content)
        # 将文件名添加到列表框中
        for file_name in file_info_dict.keys():
            file_listbox.insert(tk.END, file_name)
    else:
        messagebox.showerror("错误", f"无法获取文件列表，HTTP状态码: {response.status_code}")
        # 创建下载按钮，并传递status_label作为参数
    download_button = tk.Button(
        download_window, text="下载文件", command=lambda: download_file(status_label)
    )
    download_button.pack()


# 最新版的函数
def check_for_updates():
    update_url = "https://github.com/ymh0000123/XPMSL/releases"
    webbrowser.open(update_url)


def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("关于")

    about_label = ttk.Label(
        about_window,
        text="Xiaofeishu Python Minecraft Server Launcher(XPMSL) "+ version+ "\n作者: 没用的小废鼠\n\n程序免费开源,但是要遵守 GPL-3.0 license"+"\n内部版本: "+Build+"\n\n因为没有服务器API功能依赖 Cloudflare",
    )
    about_label.pack(padx=20, pady=20)


def set_memory_settings():
    max_memory = simpledialog.askinteger("设置内存", "请输入最大内存 (以MB为单位):", parent=root)
    min_memory = simpledialog.askinteger("设置内存", "请输入最小内存 (以MB为单位):", parent=root)

    if max_memory is not None and min_memory is not None:
        # 更新配置文件中的内存设置
        config["max_memory"] = max_memory
        config["min_memory"] = min_memory

        # 保存配置到config.yaml
        with open("XPMSL\\config.yaml", "w") as config_file:
            yaml.dump(config, config_file)


root = tk.Tk()
root.title("Minecraft 服务器启动器")

# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 创建“帮助”菜单
menu_bar.add_cascade(label="关于", command=open_about_window)

menu_bar.add_cascade(label="设置内存", command=set_memory_settings)
# 在菜单栏中添加一个选项来触发显示单独界面的函数
menu_bar.add_cascade(label="打开下载模块", command=open_download_module_window)
menu_bar.add_command(label="查看Github最新版", command=check_for_updates)


# 创建标签框架
frame = ttk.LabelFrame(root, text="服务器配置")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# 创建标签框架
frame = ttk.LabelFrame(root, text="服务器配置")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# 创建标签
java_label = ttk.Label(frame, text="选择Java版本:")
java_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

jar_file_label = ttk.Label(frame, text="Minecraft服务器JAR文件名:")
jar_file_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# 创建下拉列表框和输入框
java_var = tk.StringVar()
java_dropdown = ttk.Combobox(frame, textvariable=java_var)
java_dropdown.grid(row=0, column=1, padx=10, pady=5)
java_dropdown.state(["readonly"])  # 禁止手动输入

jar_file_entry = ttk.Entry(frame, width=40)
jar_file_entry.grid(row=1, column=1, padx=10, pady=5)

button_frame = ttk.Frame(frame)
button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

command_frame = ttk.Frame(frame)
command_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


# 获取Java版本
def get_java_version(java_executable):
    try:
        output = subprocess.check_output(
            [java_executable, "-version"], stderr=subprocess.STDOUT, text=True
        )
        lines = output.splitlines()
        for line in lines:
            if "version" in line:
                return line.strip()
    except subprocess.CalledProcessError:
        pass
    return "无法获取版本信息"


# 搜索Java可执行文件并获取版本信息
def find_java_executables():
    java_executables = []
    # 包括Oracle JDK和Zulu JDK的路径
    java_paths = [
        os.path.join("C:\\", "Program Files", "Java"),
        os.path.join("C:\\", "Program Files", "Zulu")
    ]

    for program_files_path in java_paths:
        if os.path.exists(program_files_path):
            for root, dirs, files in os.walk(program_files_path):
                for dir in dirs:
                    # 对于Zulu和Oracle JDK的检查无需变更
                    if dir.lower().startswith(("jdk", "zulu")):
                        jdk_path = os.path.join(root, dir, "bin", "java.exe")
                        if os.path.exists(jdk_path):
                            java_executables.append(jdk_path)

    return java_executables


# 搜索Java可执行文件并获取版本信息
java_executables = find_java_executables()
java_versions = [get_java_version(java_exe) for java_exe in java_executables]


# 检查并创建XPMSL目录
def create_xpmsl_directory():
    xpmsl_dir = "XPMSL"
    if not os.path.exists(xpmsl_dir):
        os.mkdir(xpmsl_dir)


# 检查并创建XPMSL/server目录
def create_server_directory():
    server_dir = os.path.join("XPMSL", "server")
    if not os.path.exists(server_dir):
        os.mkdir(server_dir)


create_xpmsl_directory()
create_server_directory()


# 创建启动按钮
def start_minecraft_server():
    def run_server():
        selected_java_version = java_var.get()
        new_jar_file_name = jar_file_entry.get()

        max_memory = config.get("max_memory", "2G")
        min_memory = config.get("min_memory", "1G")

        # 进入Minecraft服务器目录
        os.chdir("XPMSL\\server")

        # 启动Minecraft服务器命令
        cmd_command = f'"{java_executables[java_versions.index(selected_java_version)]}" -Xmx{max_memory}m -Xms{min_memory}m -jar {new_jar_file_name} nogui'

        # 使用subprocess启动服务器进程，使用PIPE连接输入和输出
        global server_process
        server_process = subprocess.Popen(
            cmd_command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # 清空输出框
        output_text.delete("1.0", tk.END)

        # 在输出框中显示输出
        output_text.config(state="normal")  # 设置输出框为可编辑状态
        output_text.insert(tk.END, f"启动Minecraft服务器:\n")
        while True:
            line = server_process.stdout.readline()
            if not line:
                break
            output_text.insert(tk.END, line)
            output_text.see(tk.END)  # 滚动到最新输出
            root.update_idletasks()  # 更新界面以响应用户操作
        output_text.insert(tk.END, f"服务器已关闭:\n")
        while True:
            line = server_process.stderr.readline()
            if not line:
                break
            output_text.insert(tk.END, line)
            output_text.see(tk.END)
            root.update_idletasks()
        output_text.config(state="disabled")  # 设置输出框为只读状态

    # 使用线程运行服务器启动函数
    server_thread = threading.Thread(target=run_server)
    server_thread.start()


start_button = ttk.Button(
    button_frame, text="启动Minecraft服务器", command=start_minecraft_server
)
start_button.grid(row=0, column=0, padx=10, pady=10)


# 创建关闭服务器按钮
def stop_minecraft_server():
    # 向Minecraft服务器发送关闭命令，例如使用"stop"命令
    if server_process:
        server_process.stdin.write("stop\n")
        server_process.stdin.flush()


stop_button = ttk.Button(
    button_frame, text="关闭Minecraft服务器", command=stop_minecraft_server
)
stop_button.grid(row=0, column=1, padx=10, pady=10)

# 创建文本框用于输入命令
command_entry = ttk.Entry(command_frame, width=40)
command_entry.grid(row=0, column=0, padx=10, pady=5)


# 创建发送命令按钮
def send_command():
    command = command_entry.get()
    if server_process:
        server_process.stdin.write(command + "\n")
        server_process.stdin.flush()
    command_entry.delete(0, "end")


send_button = ttk.Button(command_frame, text="发送命令", command=send_command)
send_button.grid(row=0, column=1, padx=5, pady=5)

# 创建文本框
output_text = tk.Text(root, height=15, width=50, state="disabled")
output_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# 创建垂直和水平滚动条
v_scrollbar = tk.Scrollbar(root, orient="vertical", command=output_text.yview)
v_scrollbar.grid(row=1, column=1, sticky="ns")
output_text.config(yscrollcommand=v_scrollbar.set)

h_scrollbar = tk.Scrollbar(root, orient="horizontal", command=output_text.xview)
h_scrollbar.grid(row=2, column=0, columnspan=2, sticky="ew")
output_text.config(xscrollcommand=h_scrollbar.set)


# 读取配置文件
def read_config():
    with open("XPMSL\\config.yaml", "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config


# 检查并创建配置文件
def create_config_if_not_exists():
    if not os.path.exists("XPMSL\\config.yaml"):
        default_config = {"jar_file": "server.jar"}
        with open("XPMSL\\config.yaml", "w") as config_file:
            yaml.dump(default_config, config_file)


# 创建文本框用于显示公告
announcement_textbox = tk.Text(root, height=5, width=50)
announcement_textbox.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
announcement_textbox.config(state="disabled")


# 获取公告文本
def fetch_announcement():
    try:
        url = api_url + api_announcement
        response = requests.get(url)
        if response.status_code == 200:
            announcement_text = response.text
            return announcement_text.splitlines()  # 拆分成行
    except requests.exceptions.RequestException:
        pass
    except Exception as e:
        print("Error fetching announcement:", str(e))
    return ["无法获取公告"]


announcement_lines = fetch_announcement()
current_announcement_line = 0


# 在单独的线程中逐行显示公告
def display_announcement_thread():
    global current_announcement_line
    while current_announcement_line < len(announcement_lines):
        line = announcement_lines[current_announcement_line]
        announcement_textbox.config(state="normal")
        announcement_textbox.insert(tk.END, line + "\n")
        announcement_textbox.config(state="disabled")
        current_announcement_line += 1
        root.update()  # 手动更新界面
        time.sleep(1)  # 每隔1秒显示一行


# 创建并启动单独的线程来逐行显示公告
announcement_thread = threading.Thread(target=display_announcement_thread)
announcement_thread.start()

create_config_if_not_exists()

# 读取配置文件中的JAR文件名
config = read_config()
jar_file_name = config.get("jar_file", "server.jar")


# 将Java版本列表设置为下拉列表框的选项
java_dropdown["values"] = java_versions

# 设置默认选中的Java版本
if java_versions:
    java_var.set(java_versions[0])
else:
    java_var.set("未找到Java")

# 设置默认的JAR文件名
jar_file_entry.insert(0, jar_file_name)

# 启动主事件循环
root.mainloop()
