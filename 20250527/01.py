# 三角形, 四角形, 五角形, 六角形, 八角形を描画するプログラム
from turtle import *

shape("turtle")

# 三角形の描画
for _ in range(3):
    forward(100)  # 100進む
    left(120)     # 120度左回転

# 四角形の描画
for _ in range(4):
    forward(100)  # 100進む
    left(90)      # 90度左回転

# 五角形の描画
for _ in range(5):
    forward(100)  # 100進む
    left(72)      # 72度左回転

# 六角形の描画
for _ in range(6):
    forward(100)  # 100進む
    left(60)      # 60度左回転

# 八角形の描画
for _ in range(8):
    forward(100)  # 100進む
    left(45)      # 45度左回転

done()
