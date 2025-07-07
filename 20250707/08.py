import matplotlib.pyplot as plt
import random

# random.uniform では、0 から 1000 の範囲の実数を生成
x1 = [random.uniform(0, 1000) for _ in range(2000)]
y1 = [random.uniform(0, 1000) for _ in range(2000)]
# random.random では 0 から 1 の範囲の実数を生成し 1000 倍
x2 = [random.random() * 1000 for _ in range(2000)]
y2 = [random.random() * 1000 for _ in range(2000)]

fig = plt.figure()

# (x1, y1) を赤、(x2, y2) を青で散布図を描画
plt.scatter(x1, y1, s=10, alpha=0.5, linewidths=2, c='r')
plt.scatter(x2, y2, s=10, alpha=0.5, linewidths=2, c='b')

plt.show()

fig.savefig('12-8-scatter.png')
plt.close()
