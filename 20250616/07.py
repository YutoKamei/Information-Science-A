import math

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

e = 1
n = 10
for i in range(1, n + 1):
    e += 1 / factorial(i)
    print(i, e)

print(e)
print(math.e)
print(math.fabs(e - math.e))
