from craftbot import Craftbot
from craftbot.utils import delay

bot = Craftbot("", debug=True)
bot.start()

for i in range(10):
    bot.press(str(i))
    bot.delay(200)

delay(1000)  # delay 1000 ms to see only "01234"
bot.stop()

