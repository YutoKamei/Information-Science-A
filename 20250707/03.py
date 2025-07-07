filepath = 'word.txt'  # 読み込むファイル名

# 出現したアルファベットの個数を保存するためのリストを作成
# 26個の要素(0〜25)を 0 で初期化
alphalist = [0 for _ in range(26)]

# word.txt を読み込みモードで開く
with open(filepath, mode='r') as fr:
    # 1 行ずつ処理
    for line in fr:
        # 先頭文字から改行直前まで調べる
        for i in range(len(line) - 1):
            # アルファベットに対応する要素番号を計算
            t = ord(line[i]) - ord('a')
            # アルファベットをカウント
            alphalist[t] += 1

print(alphalist)
