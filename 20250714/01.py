import random
import math

# 点の数を増やせば実際のpiとの差は小さくなるが
# プログラムの実行時間は増加する
plotnumber = 2000  # プロットする点の数
incount = 0        # 円の内部に入った数を計数

for i in range(plotnumber):
    x = random.random()  # 0から1の範囲の実数値を乱数で生成
    y = random.random()  # 0から1の範囲の実数値を乱数で生成
    if x**2 + y**2 < 1.0:
        incount += 1     # 円の内部に入った数を計数

# pi の近似値を計算
avalue = incount * 4.0 / plotnumber
print(f'近似値: {avalue}')
print(f'円周率: {math.pi}')
print(f'円周率との差: {math.pi - avalue}')
