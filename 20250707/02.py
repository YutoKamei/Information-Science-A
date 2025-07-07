filepath = 'num1000.txt'  # 読み込むファイル名

nlist = []  # 空のリストを準備
# ファイル操作のために with 文でファイルを開く（読み込みモード）
with open(filepath, mode='r') as fr:
    # ファイルの内容を 1 行ずつ操作
    for line in fr:
        # 2 つの整数値を空白で区切り、i と j にそれぞれ代入
        i, j = map(int, line.split())
        nlist.append(j)  # リストに j の値を追記

total = 0  # 合計値
average = 0.0  # 平均値

# nlist の要素を取り出し、total に加算し合計値を求める
for i in nlist:
    total += i

# total を nlist の要素数で割り、平均値を求める
average = total / len(nlist)
# 合計値と平均値を f 文字列で出力（平均値は小数点以下 3 桁まで）
print(f'合計: {total:,}, 平均: {average:.3f}')
