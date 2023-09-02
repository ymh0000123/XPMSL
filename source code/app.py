import tkinter as tk
from tkinter import ttk
import subprocess
import os
import yaml
import threading
import requests
import time
import webbrowser


# 创建检测更新的函数
def check_for_updates():
    update_url = "https://github.com/ymh0000123/XPMSL/releases"
    webbrowser.open(update_url)


def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("关于")

    about_label = ttk.Label(about_window, text="Minecraft 服务器启动器 v1.0\n作者: 没用的小废鼠")
    about_label.pack(padx=20, pady=20)


root = tk.Tk()
root.title("Minecraft 服务器启动器")

# 创建菜单栏
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 创建“帮助”菜单
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="帮助", menu=help_menu)
# 在“帮助”菜单中添加“检测更新”选项
help_menu.add_command(label="检测更新", command=check_for_updates)
# 在“帮助”菜单中添加“关于”选项
help_menu.add_command(label="关于", command=open_about_window)

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
    program_files_path = os.path.join("C:\\", "Program Files", "Java")

    if os.path.exists(program_files_path):
        for root, dirs, files in os.walk(program_files_path):
            for dir in dirs:
                if dir.lower().startswith("jdk"):
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

        # 进入Minecraft服务器目录
        os.chdir("XPMSL\\server")

        # 启动Minecraft服务器命令
        cmd_command = f'"{java_executables[java_versions.index(selected_java_version)]}" -Xmx2G -Xms1G -jar {new_jar_file_name} nogui'

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
        output_text.insert(tk.END, f"标准错误:\n")
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


start_button = ttk.Button(button_frame, text="启动Minecraft服务器", command=start_minecraft_server)
start_button.grid(row=0, column=0, padx=10, pady=10)


# 创建关闭服务器按钮
def stop_minecraft_server():
    # 向Minecraft服务器发送关闭命令，例如使用"stop"命令
    if server_process:
        server_process.stdin.write("stop\n")
        server_process.stdin.flush()


stop_button = ttk.Button(button_frame, text="关闭Minecraft服务器", command=stop_minecraft_server)
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
        url = "https://github.moeyy.xyz/https://raw.githubusercontent.com/ymh0000123/XPMSL/main/announcement/announcement.txt"
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
