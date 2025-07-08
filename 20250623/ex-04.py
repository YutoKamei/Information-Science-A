row_num = 5

# rangeを5から始めて、カウントダウンするパターン
for i in range(row_num, 0, -1):
    print(str(row_num - i + 1) * i)

# rangeを0から始めて、カウントアップするパターン
for i in range(row_num):
    print(str(i + 1) * (row_num - i))
