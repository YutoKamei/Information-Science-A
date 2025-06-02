# turtle の進むピクセル, 角度, 線の色をランダムに決定するプログラム
from turtle import *
from random import *

shape('turtle')

# 5色のうち, いずれかの色を用いて線を描く
col = ["orange", "limegreen", "gold", "plum", "tomato"]

for i in range(20):              # 9行目から17行目のプログラムを20回繰り返す
    steps = int(random() * 150)  # 進むピクセル数を決定
    angle = int(random() * 360)  # 角度の決定
    color(choice(col))           # 5色の中から1つ選び線の色を設定
    pensize(10)                  # ペンの太さを設定
    right(angle)                 # angle分右に回転
    forward(steps)               # steps分直進
    print(position())            # カメの現在の座標(X, Y)形式でターミナル上に出力

done()
