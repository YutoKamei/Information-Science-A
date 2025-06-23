import random

numlist = [random.randint(1, 1000) for _ in range(100)]

total = 0
for i in range(100):
    total += numlist[i]
    print(numlist[i], total)

print('total:', total)
