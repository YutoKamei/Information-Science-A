import sys

print('A以上B以下の自然数のうち、Cの倍数である自然数を昇順に出力')
a = int(input('Aを入力: '))
b = int(input('Bを入力: '))
c = int(input('Cを入力: '))

# A < B でなければプログラム終了
if a >= b:
    sys.exit()

# A から B まで繰り返す
for i in range(a, b + 1):
    # C の倍数であれば出力
    if i % c == 0:
        print(i)
