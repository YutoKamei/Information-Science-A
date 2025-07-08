import time

t1 = time.time()  # ループ開始時の時刻を取得
length_list = []

for n in range(2, 1000000):
    numlist = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        numlist.append(n)
    length_list.append(len(numlist))

t2 = time.time()  # ループ終了時の時刻を取得
print(length_list.index(max(length_list)), max(length_list))
print(f"このプログラムの実行には {t2 - t1:.2f} 秒かかりました")
