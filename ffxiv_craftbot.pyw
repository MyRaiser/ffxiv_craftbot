"""
GUI of FFXIV Craftbot
"""

import logging
import threading
import json
import ctypes
import sys
import time

import tkinter as tk
from tkinter import Tk, Button, Entry, Label, Text, StringVar, IntVar, LabelFrame
from craftbot.macro import get_marco_time
from craftbot.craftbot import Craftbot


DEFAULT_SETTINGS = {
    "macro": "",
    "key": "",
    "time": "",
    "rst_macro_key": "",
    "is_collection": ""
}

SETTINGS = "ffxiv_craftbot.json"

LOGS = "ffxiv_craftbot.log"


class App:
    def __init__(self):
        self.settings: str = SETTINGS  # 配置文件的路径
        self.__craftbot = None
        self.root = Tk()
        self.root.title("FFXIV Craft Bot")
        try:
            self.root.iconbitmap("ffxiv_craftbot.ico")
        except Exception as e:
            logging.error(f"fail to set icon due to {e}")

        self.frame_exec = LabelFrame(self.root, text="单宏循环执行")
        self.frame_exec.pack(side=tk.LEFT)
        self.frame_calc = LabelFrame(self.root, text="计算宏时长")
        self.frame_calc.pack(side=tk.RIGHT)
        self.label_macro_content = Label(self.frame_calc, text="计算宏时长（或粘贴宏内容）")
        self.label_macro_content.pack()
        self.text_macro_content = Text(self.frame_calc)
        self.text_macro_content.pack()
        self.button_calc_macro_len = Button(self.frame_calc, text="计算宏长度", command=self.get_macro_len)
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
        self.label_iteration = Label(self.frame_exec, text="（剩余）执行次数")
        self.label_iteration.pack()
        self.entry_iteration = Entry(self.frame_exec, textvariable=self.var_iteration)
        self.entry_iteration.pack()
        self.var_iteration.set(1)

        self.button_exec = Button(self.frame_exec, text="执行 (2秒后)", command=self.start)
        self.button_exec.pack(side=tk.LEFT)
        self.button_stop = Button(self.frame_exec, text="中止", command=self.stop)
        self.button_stop.pack(side=tk.RIGHT)
        self.root.bind("<F10>", self.start)
        self.root.bind("<F11>", self.stop)
        # initialize macro last used
        self.load()

    def mainloop(self):
        self.root.mainloop()

    def get_macro_len(self):
        macro = self.text_macro_content.get('0.0', 'end')
        t = get_marco_time(macro)
        logging.info(f"Macro length: {t}")
        self.var_macro_len.set(t)
        self.save()

    def load(self):
        """
        加载所有参数
        """
        try:
            with open(SETTINGS, 'r', encoding='utf-8') as f:
                params = json.load(f)
                logging.info(f"Settings loaded:{params}")
                self.text_macro_content.insert('end', params["macro"])
                self.var_macro_key.set(params["key"])
                self.var_macro_len.set(params["len"])
                self.var_rst_macro_key.set(params["rst_macro_key"])
                self.var_iteration.set(params["iteration"])
        except Exception as e:
            logging.error(f"failed to open {SETTINGS} due to {e}")

    def save(self):
        """
        保存所有参数
        """
        # get all content from text.
        macro_content = self.text_macro_content.get('0.0', 'end')
        macro_key = self.var_macro_key.get()
        macro_len = self.var_macro_len.get()
        rst_macro_key = self.var_rst_macro_key.get()
        iteration = self.var_iteration.get()

        with open(self.settings, 'w', encoding='utf-8') as f:
            params = {
                "macro": macro_content,
                "key":  macro_key,
                "len": macro_len,
                "rst_macro_key": rst_macro_key,
                "iteration": iteration
            }
            json.dump(params, f, indent=4, ensure_ascii=False)
        logging.info(f"Settings saved: {params}")

    def start(self, *args):
        # auto-save macro content
        logging.info(f"start with {args}")
        self.save()
        if self.__craftbot:
            self.__craftbot.stop()
        self.__craftbot = Craftbot("")
        self.__craftbot.start()

        rst_key = self.var_rst_macro_key.get()
        macro_key = self.var_macro_key.get()
        macro_len = self.var_macro_len.get()

        def worker(c: Craftbot, v: IntVar):
            time.sleep(2)
            while ((i := v.get()) > 0) and c:
                # press reset button
                if rst_key:
                    c.press(rst_key)
                    c.delay(100)

                # choose recipe, enter crafting
                c.press('numpad_0')
                c.delay(200)
                c.press('numpad_0')
                c.delay(200)
                c.press('numpad_0')
                c.delay(200)
                c.press('numpad_0')
                c.delay(1000)

                c.press(macro_key)
                c.delay(macro_len * 1000)

                c.delay(3000)

                v.set(i - 1)

                while True:
                    if c.is_idle:
                        break

        t = threading.Thread(target=worker, args=(self.__craftbot, self.var_iteration))
        t.setDaemon(True)
        t.start()

    def stop(self, *args):
        logging.info(f"stop with {args}")
        if self.__craftbot:
            self.__craftbot.stop()
            self.__craftbot = None


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(message)s',
                        filename=LOGS, level=logging.INFO)
    DEBUG = False
    if (not DEBUG) and (not ctypes.windll.shell32.IsUserAnAdmin()):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        app = App()
        app.mainloop()
