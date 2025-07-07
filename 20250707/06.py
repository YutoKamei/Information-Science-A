## 日本の情報通信産業の部門別名目国内生産額の推移(2000年から2022年)
## 通信業, 情報サービス業, 情報通信情報サービス業の3つの業種の推移

import matplotlib.pyplot as plt

filepath = 'gdp2.csv'  # 読み込むファイル名

xlist = []   # X軸の値用リスト (年)
ylist1 = []  # 通信業の名目 GDP 値
ylist2 = []  # 情報サービス業の名目 GDP 値
ylist3 = []  # 情報通信情報サービス業の名目 GDP 値

# gdp2.csv を with 文でファイルオープン (読み込み用)
with open(filepath, mode='r') as fr:
    # ファイルの内容を 1 行ずつ取り出す
    for line in fr:
        # 1 行の内容を line に読み込み, split(',') でカンマ区切りの値を
        # 4 つの変数に代入 (float で読み込み)
        x, y1, y2, y3 = map(float, line.split(','))
        xlist.append(int(x))  # x は年を表す (整数に変換)
        ylist1.append(y1)     # 通信業の名目 GDP
        ylist2.append(y2)     # 情報サービス業の名目 GDP
        ylist3.append(y3)     # 情報通信情報サービス業の名目 GDP

fig = plt.figure()

plt.grid(True)
plt.xticks([2000, 2005, 2010, 2015, 2020])  # X軸の凡例
# plt.plot で同じ X 軸に対して異なる系列 (線種やマーカー) を描画
plt.plot(xlist, ylist1, linestyle="solid", marker='o')
plt.plot(xlist, ylist2, linestyle="dashed", marker='x')
plt.plot(xlist, ylist3, linestyle="dashdot", marker='d')

plt.show()  # グラフを表示

# グラフを画像ファイルとして保存
fig.savefig('12-6-gdp2.png')
plt.close()
