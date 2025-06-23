import random  # 乱数を使うためのモジュール

def judge(x, y):
    if (y == 0 and x == 1) or (y == 1 and x == 2) or (y == 2 and x == 0):
        print("あなたの負けです")
    else:
        print("あなたの勝ちです")

def hands(z):
    # 手を出力
    if z == 0:
        return "グー"
    elif z == 1:
        return "チョキ"
    else:
        return "パー"

print("じゃんけんゲームはじめるよ")
print("あなたの手を入力してね")
print("グーは0, チョキは1, パーは2を入力してね。それ以外の数字は無効だよ")

x = int(input("あなたの手> "))
y = random.randint(0, 2)  # コンピュータの手は 0, 1, 2 のいずれかを乱数で決める

print("あなた>", hands(x))
print("コンピュータ>", hands(y))

# 自分とコンピュータの手が同じ場合は繰り返す
while x == y:
    print("引き分けです。もう一度手を入力してください")
    x = int(input("あなたの手> "))
    y = random.randint(0, 2)
    print("あなた>", hands(x))
    print("コンピュータ>", hands(y))
else:
    judge(x, y)
