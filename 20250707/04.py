# matplotlibでグラフ描画
import matplotlib.pyplot as plt  # matplotlib.pyplot を plt として扱う

filepath = 'word.txt'  # 読み込むファイル名

# 出現したアルファベット数を格納するリスト（0〜25 を 0 で初期化）
alphalist = [0 for _ in range(26)]

with open(filepath, mode='r') as fr:
    for line in fr:
        for i in range(len(line) - 1):
            t = ord(line[i]) - ord('a')  # アルファベットに対応するインデックス
            alphalist[t] += 1

# alphalist の内容確認（必要ならコメントを外す）
# print(alphalist)

fig = plt.figure()  # グラフを画像として保存

# x 軸は 'a' から 'z' まで
# ord('a') で 'a' の ASCII コードを取得し、0〜25 を加算して
# chr でアルファベットへ変換
x_label = [chr(i + ord('a')) for i in range(26)]
# print(x_label)

# word.txt に出現したアルファベットの個数を棒グラフで描画
plt.bar(x_label, alphalist)

# グラフを表示
plt.show()

# グラフを画像ファイルとして保存
fig.savefig('12-4.png')
plt.close()
