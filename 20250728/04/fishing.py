def point(u, p):
    return u[0] * p[0] + u[1] * p[1] + (u[0] // 10)*p[2] + (u[1] // 10) * p[3]

taro = list(map(int, input().split()))
jiro = list(map(int, input().split()))

points = list(map(int, input().split()))

taro_point = point(taro, points)
jiro_point = point(jiro, points)

print(f'太郎の得点: {taro_point}')
print(f'次郎の得点: {jiro_point}')

if taro_point > jiro_point:
    print('太郎の勝ち')
elif taro_point < jiro_point:
    print('次郎の勝ち')
else:
    print('引き分け')
