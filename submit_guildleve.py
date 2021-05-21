"""
自动交巨匠，需要确保屏幕内没别人，并手动确保初始状态
"""

from ffxiv_craftbot import Craftbot, delay


ffxiv = Craftbot('最终幻想XIV')
delay(2000)
while True:
    # select npc 1
    ffxiv.press('numpad_4')
    delay(300)
    ffxiv.press('numpad_0')
    delay(300)
    ffxiv.press('numpad_0')
    delay(800)
    ffxiv.press('numpad_0')
    delay(300)

    # select leve
    ffxiv.press('numpad_2')
    delay(300)
    ffxiv.press('numpad_0')
    delay(1000)
    ffxiv.press('numpad_0')
    delay(300)
    ffxiv.press('numpad_0')
    delay(300)
    ffxiv.press('esc')
    delay(500)
    ffxiv.press('esc')
    delay(300)

    delay(1000)

    # select npc 2
    ffxiv.press('numpad_6')
    delay(300)
    ffxiv.press('numpad_0')
    delay(300)
    ffxiv.press('numpad_0')
    delay(1000)

    # select target leve
    ffxiv.press('numpad_2')
    delay(200)
    ffxiv.press('numpad_2')
    delay(300)
    ffxiv.press('numpad_0')
    delay(1000)
    ffxiv.press('numpad_0')

    for i in range(3):
        # submit item
        delay(800)
        ffxiv.press('numpad_*')
        delay(200)
        ffxiv.press('numpad_0')
        delay(200)
        ffxiv.press('numpad_0')
        delay(200)
        ffxiv.press('numpad_0')
        delay(300)
        ffxiv.press('numpad_0')
        delay(300)
        ffxiv.press('numpad_0')
        delay(300)
        ffxiv.press('numpad_0')
        delay(300)
        ffxiv.press('numpad_0')
        delay(300)
        if i < 2:
            ffxiv.press('numpad_0')
            delay(500)

    delay(3000)
