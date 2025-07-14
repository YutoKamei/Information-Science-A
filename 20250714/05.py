import secrets                   # secrets ライブラリ
import random
import numpy as np               # NumPy ライブラリ
import matplotlib.pyplot as plt  # Matplotlib ライブラリ

trial = 10000  # 試行回数

# それぞれ 100 個の要素を 0 で初期化したリストを生成
secrets_list = [0 for _ in range(100)]
random_list = [0 for _ in range(100)]

# [0, 100) のランダムな整数を生成して計数
# randbelow 関数を使用
for _ in range(trial):
    secrets_list[secrets.randbelow(100)] += 1

# randint 関数を使用
for _ in range(trial):
    random_list[random.randint(0, 99)] += 1

# 2 つのリストを出力
print(secrets_list)
print(random_list)

# 2 つのリストの要素の平均値・最大値・最小値
print(
    f'secrets_list: 平均値 {sum(secrets_list)/len(secrets_list)}, '
    f'最大値 {max(secrets_list)}, 最小値 {min(secrets_list)}'
)
print(
    f'random_list: 平均値 {sum(random_list)/len(random_list)}, '
    f'最大値 {max(random_list)}, 最小値 {min(random_list)}'
)

# X 軸用の 0.1 ずつずらした 2 つのリスト
xlist1 = [i + 0.9 for i in range(100)]
xlist2 = [i + 1.1 for i in range(100)]

fig = plt.figure()
plt.bar(xlist1, secrets_list, color='r', width=0.2, align='center')
plt.bar(xlist2, random_list, color='b', width=0.2, align='center')

plt.title('random number histgram')

plt.show()

fig.savefig('list8-5.png')
plt.close()
