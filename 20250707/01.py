import random  # 乱数発生用

filepath = 'num1000.txt'  # 作成するファイル名

# num1000.txt を書き込みモードで開く
fw = open(filepath, mode='w')

# 1000 行分ファイルに書き込み
for i in range(1000):
    # フォーマット: 行数 1 から 1000 の間の整数値（乱数）
    # ' ' の間には空白
    fw.write(str(i + 1) + ' ' + str(random.randint(1, 1001)) + '\n')

fw.close()
