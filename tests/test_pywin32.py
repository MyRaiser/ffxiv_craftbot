import win32con
import win32gui
import win32api

from craftbot.utils import delay, VK_CODE


def press(hwnd, key, duration=5):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, VK_CODE[key], None)
    delay(duration)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, VK_CODE[key], None)


if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, "一致性测试平台设计文档.docx - Word")
    print(hwnd)
    for i in range(100):
        press(hwnd, "1")
