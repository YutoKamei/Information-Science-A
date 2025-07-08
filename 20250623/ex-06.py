import random

print('国盗りゲームはじめるよ')
print('60マス到達したらゴールだよ')

game_over_flag = 0
current = 0
dice_list = [1, 2, 5, 5, 10, 10, 15, 15, 17, 20]

while game_over_flag != 1:
    print('1でサイコロを振るよ(0を打つとゲーム終了だよ)')
    dice_flag = int(input())
    if dice_flag == 0:
        game_over_flag = 1
        break

    dice = random.choice(dice_list)
    print('サイコロの目>' + str(dice))
    print('エンターでそのまま進むか, 2倍の数進むか, 後ろに進むか, ゲームオーバーかを決めるよ')
    forward_flag = input()

    forward = random.randint(-1, 2)
    if forward == 1:
        print('前に進むよ')
    elif forward == 2:
        print('2倍進むよ')
    elif forward == -1:
        print('後ろに戻るよ')
    else:
        print('Game Over')
        game_over_flag = 1
        break

    current += dice * forward
    if current < 0:
        print('Game Over')
        game_over_flag = 1
        break

    print('+' * current)

    if current >= 60:
        print('Goal!!')
        game_over_flag = 1
