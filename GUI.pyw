import tkinter as tk
from ffxiv_craftbot import Macro, Craftbot
import threading
import json


def exec_macro():
    # get all content from text.
    macro1_content = text_macro_content.get('0.0', 'end')
    macro1_key = var_macro_key.get()
    macro1 = Macro(macro1_content, macro1_key)

    # auto-save macro content
    with open("macro1.craftbot", 'w', encoding='utf-8') as f:
        macro1_to_save = {
            "macro": macro1.macro,
            "key": macro1.key,
            "time": macro1.time
        }
        json.dump(macro1_to_save, f, indent=4)
        print("macro1 Auto-saved.")

    rst_macro_key = var_rst_macro_key.get()
    if rst_macro_key == '':
        rst_macro_key = None

    iteration = var_iteration.get()

    ffxiv = Craftbot('最终幻想XIV')
    for i in range(iteration):
        ffxiv.forge(macro1, rst_macro_key=rst_macro_key,
                    is_collection=var_is_collection.get())


def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


root = tk.Tk()
root.title("FFXIV Craft Bot")

label_macro_content = tk.Label(root, text="宏内容").pack()
text_macro_content = tk.Text(root)
text_macro_content.pack()

var_macro_key = tk.StringVar()
label_macro_key = tk.Label(root, text="宏快捷键").pack()
entry_macro_key = tk.Entry(root, textvariable=var_macro_key).pack()

var_rst_macro_key = tk.StringVar()
label_rst_macro_key = tk.Label(root, text="重置宏快捷键（默认空）").pack()
entry_rst_macro_key = tk.Entry(root, textvariable=var_rst_macro_key).pack()

var_iteration = tk.IntVar()
label_iteration = tk.Label(root, text="执行次数").pack()
entry_iteration = tk.Entry(root, textvariable=var_iteration).pack()
var_iteration.set(1)

var_is_collection = tk.BooleanVar()
checkbutton_is_collection = tk.Checkbutton(
    root, text="收藏品", variable=var_is_collection, onvalue=True, offvalue=False).pack()

button_exec = tk.Button(
    root, text="执行", command=lambda: thread_it(exec_macro)).pack()


root.mainloop()
