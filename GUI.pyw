import logging
import threading
import json
import ctypes
import sys

import tkinter as tk
from tkinter import Tk, Button, Entry, Label, Text, StringVar, IntVar, LabelFrame
from craftbot.macro import Macro
from craftbot.craftbot import Craftbot


def thread_it(func, *args):
    """将函数打包进线程"""
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


DEFAULT_SETTINGS = {
    "macro": "",
    "key": "",
    "time": "",
    "rst_macro_key": "",
    "is_collection": ""
}

SETTINGS_FILENAME = "app.json"


class App:
    def __init__(self):
        self._craftbot = None
        self.root = Tk()
        self.root.title("FFXIV Craft Bot")
        try:
            self.root.iconbitmap("ffxiv_craftbot.ico")
        except Exception as e:
            logging.error(f"fail to set icon due to {e}")

        self.frame_exec = LabelFrame(self.root, text="执行")
        self.frame_exec.pack(side=tk.LEFT)
        self.frame_calc = LabelFrame(self.root, text="计算宏长度")
        self.frame_calc.pack(side=tk.RIGHT)
        self.label_macro_content = Label(self.frame_calc, text="宏时长（或粘贴宏内容自动计算）")
        self.label_macro_content.pack()
        self.text_macro_content = Text(self.frame_calc)
        self.text_macro_content.pack()
        self.button_calc_macro_len = Button(self.frame_calc, text="计算宏长度", command=self.calc_macro_len)
        self.button_calc_macro_len.pack()

        self.var_macro_len = IntVar()
        self.label_macro_len = Label(self.frame_exec, text="宏时长")
        self.label_macro_len.pack()
        self.entry_macro_len = Entry(self.frame_exec, textvariable=self.var_macro_len)
        self.entry_macro_len.pack()

        self.var_macro_key = StringVar()
        self.label_macro_key = Label(self.frame_exec, text="宏快捷键")
        self.label_macro_key.pack()
        self.entry_macro_key = Entry(self.frame_exec, textvariable=self.var_macro_key)
        self.entry_macro_key.pack()

        self.var_rst_macro_key = StringVar()
        self.label_rst_macro_key = Label(self.frame_exec, text="重置宏快捷键（默认空）")
        self.label_rst_macro_key.pack()
        self.entry_rst_macro_key = Entry(self.frame_exec, textvariable=self.var_rst_macro_key)
        self.entry_rst_macro_key.pack()

        self.var_iteration = IntVar()
        self.label_iteration = Label(self.frame_exec, text="执行次数")
        self.label_iteration.pack()
        self.entry_iteration = Entry(self.frame_exec, textvariable=self.var_iteration)
        self.entry_iteration.pack()
        self.var_iteration.set(1)

        self.button_exec = Button(self.frame_exec, text="执行 (F10)", ).pack(side=tk.LEFT)
        self.root.bind("<F10>", lambda x: print("hello"))
        self.button_stop = Button(self.frame_exec, text="中止 (F11)", ).pack(side=tk.RIGHT)

        # initialize macro last used
        try:
            with open(SETTINGS_FILENAME, 'r', encoding='utf-8') as f:
                macro_autosaved = json.load(f)
                logging.info(macro_autosaved)
                self.text_macro_content.insert('end', macro_autosaved["macro"])
                self.var_macro_key.set(macro_autosaved["key"])
                self.var_rst_macro_key.set(macro_autosaved["rst_macro_key"])
        except Exception as e:
            logging.error(f"failed to open {SETTINGS_FILENAME} due to {e}")

    def mainloop(self):
        self.root.mainloop()

    def calc_macro_len(self):
        macro = self.text_macro_content.get('0.0', 'end')

    def exec_macro(self):
        # get all content from text.
        macro1_content = self.text_macro_content.get('0.0', 'end')
        macro1_key = self.var_macro_key.get()
        macro1 = Macro(macro1_content, macro1_key)
        rst_macro_key = self.var_rst_macro_key.get()
        iteration = self.var_iteration.get()
        # auto-save macro content
        with open("macro_autosaved.craftbot", 'w', encoding='utf-8') as f:
            macro_autosaved = {
                "macro": macro1.macro,
                "key": macro1.key,
                "time": macro1.time,
                "rst_macro_key": rst_macro_key
            }
            json.dump(macro_autosaved, f, indent=4, ensure_ascii=False)
            logging.info("macro Auto-saved.")

        if rst_macro_key == '':
            rst_macro_key = None

        self._craftbot = Craftbot('最终幻想XIV')
        for i in range(iteration):
            self._craftbot.forge(macro1, rst_macro_key=rst_macro_key)


if __name__ == "__main__":
    DEBUG = True
    if not DEBUG:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        app = App()
        app.mainloop()
