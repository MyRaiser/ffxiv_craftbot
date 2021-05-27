import datetime

import win32api
import win32con
import win32gui

from craftbot.utils import is_admin, delay, VK_CODE


class Craftbot:
    """
    generate a Craftbot object.
    - `window_title`: title of FFXIV window. Typically, do it as:
        ```py
        ffxiv = Craftbot('最终幻想XIV')
        ```
    """

    @staticmethod
    def get_hwnd(name):
        hwnd = win32gui.FindWindow(None, name)
        report("hwnd is:", hwnd)
        return hwnd

    def __init__(self, window_title):
        # get admin
        if is_admin():
            self.hwnd = Craftbot.get_hwnd(window_title)
            if self.hwnd == 0:
                raise ValueError("hwnd is zero!")
                # self.VK_CODE = VK_CODE

        else:
            raise ValueError("No admin permission!")

    def press(self, key, duration=5):
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYDOWN, VK_CODE[key], 0)
        delay(duration)
        win32gui.SendMessage(self.hwnd, win32con.WM_KEYUP, VK_CODE[key], 0)
        report(key, "is pressed!")

    def delay(self, ms, jitter=0.05):
        delay(ms, jitter)  # call delay() outside class

    def forge(self, *macros, rst_macro_key=None, is_collection=False):
        """
        do crafting(once).
        - `macros`: macros to execute.
        - `rst_macro_key`: Key of rst_macro. Make a macro in FFXIV to interrupt all macros. This can improve stability. Default None.
        - `is_collection`: whether to do the additional collection confirmation step. Default False.
        """
        # press rst_macro
        if rst_macro_key is not None:
            self.press(rst_macro_key)
            self.delay(100)

        # choose recipe, enter crafting
        self.press('numpad_0')
        self.delay(200)
        self.press('numpad_0')
        self.delay(200)
        self.press('numpad_0')
        self.delay(200)
        self.press('numpad_0')
        self.delay(1000)

        # execute macros
        for macro in macros:
            self.press(macro.key)
            self.delay(macro.time * 1000)

        # collection confirmation
        if is_collection:
            self.press('numpad_0')
            self.delay(200)
            self.press('numpad_0')
            self.delay(200)

        # delay after crafting is completed
        self.delay(3000)


def present_time():
    return datetime.datetime.now().strftime('%H:%M:%S.%f')


def report(*x):
    print("[", present_time(), "]", *x)


def execute_macro(obj, macroButton, macroLength, delay_sec):
    obj.press(macroButton)
    delay((macroLength + delay_sec) * 1000)


def left_click(x, y, duration=50):
    x = round(x)
    y = round(y)

    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    delay(duration)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    report("mouse left clicked at", x, y)