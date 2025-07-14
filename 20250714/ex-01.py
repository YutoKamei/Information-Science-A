import math
import random

plotnum = 2000
incount = 0

for _ in range(plotnum):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y > x**2 and y < x:
        incount += 1

print(incount / plotnum)
