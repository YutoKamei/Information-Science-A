import matplotlib.pyplot as plt
import random
import secrets

hist1 = [0 for _ in range(6)]
for _ in range(10000):
    dice = random.randint(1, 6)
    hist1[dice - 1] += 1

hist2 = [0 for _ in range(6)]
for _ in range(10000):
    dice = secrets.randbelow(6) + 1
    hist2[dice - 1] += 1

x1 = [0.9, 1.9, 2.9, 3.9, 4.9, 5.9]
x2 = [1.1, 2.1, 3.1, 4.1, 5.1, 6.1]

plt.bar(x1, hist1, label='random', color='r', width=0.2, align='center')
plt.bar(x2, hist2, label='secrets', color='b', width=0.2, align='center')

plt.show()
plt.close()
