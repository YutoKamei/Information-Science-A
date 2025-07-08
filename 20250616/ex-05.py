## サイコロの各目がでる確率

import random

# サイコロを振る
hist = [0 for _ in range(6)]

for i in range(100000):
    dice = random.randint(1, 6)
    hist[dice - 1] += 1

# 確率を求める
p = [0.0 for _ in range(6)]

psum = 0.0
for i in range(len(hist)):
    p[i] = hist[i] / 100000
    print(i + 1, p[i], abs((1 / 6) - p[i]))
    psum += p[i]

print(psum)
