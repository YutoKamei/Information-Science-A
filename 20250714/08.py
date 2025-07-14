import math
import matplotlib.pyplot as plt
import random

plotnum = 2000
incount = 0

fig = plt.figure()

plt.xticks([0, 45, 90, 135, 180])
plt.grid(True)
xlist = []
siny = []          # 上限
ylist = []         # 下限
for i in range(0, 181):
    xlist.append(i)
    siny.append(math.sin(math.radians(i)))
    ylist.append(0)

plt.plot(xlist, siny, color='r')
plt.plot(xlist, ylist, color='r')

for _ in range(plotnum):
    x = random.randint(0, 181)
    y = random.random()

    # sin(x) の内側に (x, y) があるかどうかを判定
    if y < math.sin(math.radians(x)):
        plt.plot(x, y, 'ro')
        incount += 1
    else:
        plt.plot(x, y, 'bx')

print((incount / plotnum) * math.pi)
plt.show()

plt.close()
