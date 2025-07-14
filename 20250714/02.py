# モンテカルロ法での円周率の近似結果を描画
import numpy as np               # NumPyライブラリ
import matplotlib.pyplot as plt  # Matplotlibライブラリ

# 点の数を増やせば実際の pi との差は小さくなるが
# プログラムの実行時間は増加する
plotnumber = 2000           # プロットする点の数
incount = 0                 # 円の内部に入った数を計数

# matplotlib の描画領域を確保
fig = plt.figure()
# fig 内に座標軸を 1 つ追加
ax = fig.add_subplot()
# アスペクト比(縦横比)の設定
ax.set_aspect('equal', adjustable='box')

plt.xlim(0, 1)              # X 軸の範囲を設定
plt.ylim(0, 1)              # Y 軸の範囲を設定
plt.fill_between(
    np.linspace(0, 1, 100),
    0,
    np.sqrt(1 - np.linspace(0, 1, 100) ** 2),
    color='lightcoral',
    alpha=0.3
)

for i in range(plotnumber):
    # (x, y) 座標 (0 <= x, y < 1)
    x = np.random.random()
    y = np.random.random()
    if x ** 2 + y ** 2 < 1.0:
        incount += 1            # 円の内側
        plt.plot(x, y, 'ro')    # 赤い ● をプロット
    else:
        plt.plot(x, y, 'bx')    # 青い × をプロット

print(f'円周率: {incount * 4.0 / plotnumber}')
plt.show()                      # グラフ描画

# グラフの画像ファイルを保存
fig.savefig('pi_sim.png')
plt.close()
