from BackgroundForge import *

macro="""/ac 内静 <wait.2>
/ac 阔步 <wait.2>
/ac 新颖II <wait.2>
/ac 稳手II <wait.2>
/ac 坯料加工 <wait.3>
/ac 坯料加工 <wait.3>
/ac 阔步 <wait.2>
/ac 比尔格的祝福 <wait.3>
/ac 再利用 <wait.2>
/ac 模范制作III <wait.3> 
/ ac 模范制作III < wait .3 > """

time = calculateMacroLength(macro)
x = BackgroundForge("最终幻想XIV")
while(1):
    x.press('numpad_0')
    delay(200)
    x.press('numpad_0')
    delay(200)
    x.press('numpad_0')
    delay(200)
    x.press('numpad_0')
    delay(1000)
    x.press('`')
    delay(100)
    x.press('q')
    delay(time*1000)
    delay(3000)

