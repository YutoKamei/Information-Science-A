import math
import matplotlib.pyplot as plt

# matplotlib の描画領域を確保
fig = plt.figure()

# X 軸の凡例
plt.xticks([-360, -270, -180, -90, 0, 90, 180, 270, 360])
plt.grid(True)  # グリッド線を描画
xlist = []      # X 軸用のリスト (角度 -360 から 360 度)
siny = []       # sin 関数用のリスト (-360 から 360 度の sin の値)
cosy = []       # cos 関数用のリスト (-360 から 360 度の cos の値)

# -360 度から 360 度まで繰り返し処理
for i in range(-360, 361):
    xlist.append(i)
    # 角度を math.radians でラジアンに変換
    siny.append(math.sin(math.radians(i)))
    cosy.append(math.cos(math.radians(i)))

# グラフ描画
plt.plot(xlist, siny, color='r')
plt.plot(xlist, cosy, color='b')
plt.pause(0.01)  # 0.01 秒ごとに描画

plt.show()
plt.close()
