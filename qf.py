from craftbot.macro import Macro
from craftbot.craftbot import Craftbot, delay

ffxiv = Craftbot('最终幻想XIV')
while True:
    ffxiv.press('numpad_0')
    delay(800)
    ffxiv.press('numpad_0')
    delay(800)
    ffxiv.press('numpad_0')
    delay(800)
    ffxiv.press('numpad_0')
    delay(800)
    ffxiv.press('numpad_4')
    delay(800)
    ffxiv.press('numpad_0')
    delay(800)
    delay(30000)

