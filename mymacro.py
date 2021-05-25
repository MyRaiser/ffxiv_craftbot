from craftbot.macro import Macro
from craftbot.craftbot import Craftbot

macro1_content =\
"""
/ac "闲静" <wait.3>
/ac 精密制作 <wait.3>
/ac 改革 <wait.2>
/ac 精密制作 <wait.3>
/ac 坯料加工 <wait.3>
/ac 阔步 <wait.2>
/ac 比尔格的祝福 <wait.3>
/ac 崇敬 <wait.2>
/ac 坯料制作 <wait.3>
"""
macro1 = Macro(macro1_content, '4')

ffxiv = Craftbot('最终幻想XIV')
ffxiv.forge(macro1, rst_macro_key='`', is_collection=True)


