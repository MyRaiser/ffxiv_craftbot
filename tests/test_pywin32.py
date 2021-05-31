import win32gui

from craftbot.utils import press_hwnd


if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, "")
    print(hwnd)
    for i in range(100):
        press_hwnd(hwnd, "1")
