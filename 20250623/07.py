import random

def state_of_board(p_pos, c_pos):
    # プレイヤーの位置表示
    print('・' * (p_pos - 1) + 'P' + '・' * (30 - p_pos))
    # コンピューターの位置表示
    print('・' * (c_pos - 1) + 'C' + '・' * (30 - c_pos))


def goal(p_pos, c_pos, winner):
    if winner == 'P':
        print('・' * 30 + 'P (Goal)')
        print('・' * (c_pos - 1) + 'C' + '・' * (30 - c_pos))
        print('Player won.')
    elif winner == 'C':
        print('・' * (p_pos - 1) + 'P' + '・' * (30 - p_pos))
        print('・' * 30 + 'C (Goal)')
        print('Computer won.')
    elif winner == 'D':
        print('・' * 30 + 'P (Goal)')
        print('・' * 30 + 'C (Goal)')
        print('End in a draw.')

player_position = 1
computer_position = 1

while True:
    state_of_board(player_position, computer_position)
    input('Enterを押すとサイコロを振ってコマを進めます: ')
    player_position += random.randint(1, 6)
    computer_position += random.randint(1, 6)
    # player_position += 3
    # computer_position += 3

    if player_position >= 30 and computer_position >= 30:
        goal(player_position, computer_position, 'D')
        break
    elif player_position >= 30:
        goal(player_position, computer_position, 'P')
        break
    elif computer_position >= 30:
        goal(player_position, computer_position, 'C')
        break
