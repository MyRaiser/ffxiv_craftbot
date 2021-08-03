"""
自动交巨匠，需要确保屏幕内没别人，并手动确保初始状态
"""

from craftbot import Craftbot
from craftbot.utils import delay

delay(2000)  # wait to switch window

ffxiv = Craftbot('最终幻想XIV')
ffxiv.start()
while True:
    # select npc 1
    ffxiv.press('numpad_4')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(800)
    ffxiv.press('numpad_0')
    ffxiv.delay(300)

    # select leve
    ffxiv.press('numpad_2')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(1000)
    ffxiv.press('numpad_0')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(300)
    ffxiv.press('esc')
    ffxiv.delay(500)
    ffxiv.press('esc')
    ffxiv.delay(300)

    ffxiv.delay(1000)

    # select npc 2
    ffxiv.press('numpad_6')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(1000)

    # select target leve
    ffxiv.press('numpad_2')
    ffxiv.delay(200)
    ffxiv.press('numpad_2')
    ffxiv.delay(300)
    ffxiv.press('numpad_0')
    ffxiv.delay(1000)
    ffxiv.press('numpad_0')

    for i in range(3):
        # submit item
        ffxiv.delay(800)
        ffxiv.press('numpad_*')
        ffxiv.delay(200)
        ffxiv.press('numpad_0')
        ffxiv.delay(200)
        ffxiv.press('numpad_0')
        ffxiv.delay(200)
        ffxiv.press('numpad_0')
        ffxiv.delay(300)
        ffxiv.press('numpad_0')
        ffxiv.delay(300)
        ffxiv.press('numpad_0')
        ffxiv.delay(300)
        ffxiv.press('numpad_0')
        ffxiv.delay(300)
        ffxiv.press('numpad_0')
        ffxiv.delay(300)
        if i < 2:
            ffxiv.press('numpad_0')
            ffxiv.delay(500)

    ffxiv.delay(3000)
