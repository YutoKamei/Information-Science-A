import math
import matplotlib.pyplot as plt

fig = plt.figure()

plt.grid(True)

xlist = []
ylist = []

for i in range(-100, 101):
    xlist.append(i / 10)
    ylist.append((i / 10) ** 2)
    plt.plot(xlist, ylist, color='b')
    plt.pause(0.01)

plt.show()
plt.close()
