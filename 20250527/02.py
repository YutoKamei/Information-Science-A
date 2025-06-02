# 三角形, 四角形, 五角形, 六角形, 八角形を描画するプログラム
from turtle import *

shape("turtle")

polygon = [3, 4, 5, 6, 8]       # 描画する n 角形の数値のリスト

# 多角形の描画
for n in polygon:               # polygon からひとつずつ値を取り出す
    print(n, "角形を描画します")
    for _ in range(n):          # 下の処理を n 回繰り返す
        forward(100)            # 100進む
        left(360 / n)           # n を使って回転する角度を表現

done()
