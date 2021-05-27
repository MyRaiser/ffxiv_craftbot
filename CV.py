
from PIL import ImageGrab
from matplotlib import pyplot as plt
import win32api, win32con
import numpy as np
import cv2
import BackgroundForge as bf
from pymouse import PyMouse

import craftbot.craftbot
import craftbot.utils


def getScreen():
    return np.array(ImageGrab.grab((0, 0, win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))))

hwd=bf.gethWnd("最终幻想XIV")
img = getScreen()
template_board_main = cv2.imread("cv-templates/board-main.png")
template_search_bar = cv2.cvtColor(cv2.imread("cv-templates/search-bar.png"),cv2.COLOR_BGR2RGB)
match = cv2.matchTemplate(img, template_search_bar, cv2.TM_CCOEFF)
plt.subplot(3,1,1)
plt.imshow(match)
plt.subplot(3, 1, 3)
plt.imshow(template_search_bar)
min_val, max_val, min_index, max_index = cv2.minMaxLoc(match)
cv2.rectangle(img, max_index, (max_index[0] + template_search_bar.shape[1], max_index[1] + template_search_bar.shape[0]), 255, 2)

click_x = round(max_index[0] + template_search_bar.shape[1] * 0.5)
click_y = round(max_index[1] + template_search_bar.shape[0] * 0.8)

m = PyMouse()
# bf.leftClick(max_index[0] + template_search_bar.shape[1] * 0.5, max_index[1] + template_search_bar.shape[0] * 0.8)
while(1):
    m.click(click_x,click_y)
plt.subplot(3,1,2)
plt.imshow(img)
craftbot.utils.delay(1000)
plt.show()
