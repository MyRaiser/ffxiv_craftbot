import re

macro="""/ac 内静 <wait.2>
/ac 俭约II <wait.2>
/ac 稳手II <wait.2>
/ac 新颖II <wait.2>
/ac 坯料加工 <wait.3>
/ac 坯料加工 <wait.3>
/ac 坯料加工 <wait.3>
/ac 模范制作III <wait.3>
/ac 精修 <wait.3>
/ac 稳手II <wait.2>
/ac 阔步 <wait.2>
/ac 比尔格的祝福 <wait.3>
/ac 模范制作III <wait.3>
/ac 模范制作III <wait.3>"""

pattern = "[1-9]"
result = re.findall(pattern, macro, flags=0)
time = sum([int(x) for x in result])
print(time)