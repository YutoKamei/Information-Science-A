## 日本の情報通信産業の部門別名目国内生産額の推移(2000年から2022年)

import matplotlib.pyplot as plt

filepath = 'gdp.csv'  # 読み込むファイル名

xlist = []  # X軸の値用リスト
ylist = []  # Y軸の値用リスト

# gdp.csv を読み込みモードで開く
with open(filepath, mode='r') as fr:
    # ファイルの内容を1行ずつ処理
    for line in fr:
        # カンマ区切りで 2 つの値を取得（float で読み込み）
        x, y = map(float, line.split(','))
        xlist.append(int(x))  # x は年（整数に変換）
        ylist.append(y)       # y は GDP の値（単位: 兆円）

# print(xlist, ylist)  # 確認用（必要ならコメントを外す）
fig = plt.figure()  # グラフを画像として保存するための Figure

plt.grid(True)  # グリッド線を描画
plt.xticks([2000, 2005, 2010, 2015, 2020])  # X軸に表示する目盛り
# 折れ線グラフ: X軸 = xlist, Y軸 = ylist, 実線, マーカーは ●
plt.plot(xlist, ylist, linestyle='solid', marker='o')

plt.show()  # グラフを表示

# グラフを画像ファイルとして保存
fig.savefig('12-5-gdp1.png')
plt.close()
