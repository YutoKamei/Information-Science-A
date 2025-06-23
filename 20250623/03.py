str1 = input('文字列を入力してください: ')

str1_len = len(str1)
kaibun = ''

for i in range(str1_len - 1, -1, -1):
    kaibun += str1[i]

# 別の書き方
# for i in range(str1_len):
#     kaibun += str1[str1_len - i - 1]

print(str1, 'を逆にすると', kaibun)
if str1 == kaibun:
    print(str1, 'は回文です')
else:
    print(str1, 'は回文ではないです')
