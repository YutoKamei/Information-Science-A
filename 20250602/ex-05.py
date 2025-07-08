## 情報科学A 第7回 問題5
## author: Yuto Kamei
## プログラムの概要

F = int(input('華氏で表現した温度>'))

# 華氏から摂氏に変換
C = (F - 32) * 5/9
print(int(C), "(C)")

# 華氏から摂氏に変換（簡易版）
CC = (F -30)//2
print(CC , "(C) ## 簡易版")
