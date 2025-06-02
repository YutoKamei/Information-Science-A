# 20個の円を描画するプログラム
from turtle import *

shape("turtle")

for _ in range(20):            # 7-8行目を20回繰り返す
   print(position())           # カメの現在の座標(X,Y)形式でターミナル上に出力
   circle(200)                 # 回転半径200で,円を描く
   penup()                     # 改良 : ペンを上げる
   goto(xcor()+10, ycor()+10)  # 円の描画開始位置をX軸, Y軸ともに10ピクセル移動
   pendown()                   # 改良 : ペンを下ろす

done()