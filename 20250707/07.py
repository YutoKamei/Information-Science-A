import matplotlib.pyplot as plt

import numpy as np  # NumPyライブラリのインポート (資料15.10節参照)
import math  # mathライブラリのインポート (sin, cos で使用)

# xlist は 0 から 360 までの 1 度刻みの角度を要素とするリスト (X 軸用)
xlist = [i for i in range(0, 361)]

# sinlist, coslist は各角度の sin 値・cos 値を保持するリスト
sinlist = [math.sin(math.radians(i)) for i in range(0, 361)]
coslist = [math.cos(math.radians(i)) for i in range(0, 361)]

fig = plt.figure()

plt.grid(True)
# X 軸に表示する目盛り
plt.xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360])

# sin 関数のグラフ
plt.plot(xlist, sinlist, linestyle="solid", color='b')
# cos 関数のグラフ
plt.plot(xlist, coslist, linestyle="solid", color='r')

plt.show()  # グラフを表示

# グラフを画像ファイルとして保存
fig.savefig('12-7-sincos.png')
plt.close()
