import random
import math

def neipia():
    s = 0  # 一様乱数の和
    i = 0  # sが1を超えたときの乱数の個数
    while s < 1:
        # 0から1の乱数（実数）を発生させ s に加算
        s += random.random()
        i += 1
    # s が 1 を超えると while を抜ける
    return i  # i: s が 1 を超えたときの乱数の個数

n = 1000000  # 試行回数
t = 0        # 試行回数分の乱数の個数の総和

for _ in range(n):
    t += neipia()

# t/n: 一様乱数の和が 1 を超えるまでにかかる乱数の個数の平均値
print(f'シミュレーションで求めた e: {t/n}')
print(f'ネイピア数 e = {math.e}')
