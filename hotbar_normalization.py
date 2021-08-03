content1 = "/hotbar copy"
jobs = ["刻木匠", "锻铁匠", "铸甲匠", "雕金匠", "制革匠", "裁衣匠", "炼金术士", "烹调师"]
base_job = "炼金术士"
filename = "macro.txt"

with open(filename, 'w') as f:
    line = 0
    for job in jobs:
        if job != base_job:
            for i in range(1, 3+1):
                if line >= 15:
                    f.write("\n")
                    line = 0
                f.write(content1 + " " + base_job + " " + str(i) + " " + job + " " + str(i) + "\n")
                line += 1
