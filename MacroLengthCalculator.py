import re

macro="""/ac 稳手II <wait.2>
/ac 坯料加工 <wait.3>
/ac 坯料加工 <wait.3>
/ac 坯料加工 <wait.3>
/ac 回收 <wait.2>
/ac 再利用
/ac 坯料加工
/wait 3
/ac 模范制作III <wait.3> """

pattern = "[1-9]"
result = re.findall(pattern, macro, flags=0)
time = sum([int(x) for x in result])
print(time)