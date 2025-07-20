encryptkey = -1  # 秘密鍵(25 でも同じ)

plaintext1 = 'ibm'              # 平文1
plaintext2 = 'this is a pen.'   # 平文2
ciphertext1 = ''
ciphertext2 = ''

# 平文を 1 文字ずつ操作
for i in range(len(plaintext1)):
    if plaintext1[i].isalpha():
        # アルファベットであれば、暗号化
        base = ord('a') if plaintext1[i].islower() else ord('A')
        ciphertext1 += chr((ord(plaintext1[i]) - base + encryptkey) % 26 + base)
    else:
        # アルファベット以外(数字や記号)であればそのまま
        ciphertext1 += plaintext1[i]
print(ciphertext1)  # 暗号文の出力

# 平文を 1 もじずつ操作
for i in range(len(plaintext2)):
    if plaintext2[i].isalpha():
        # アルファベットであれば、暗号化
        base = ord('a') if plaintext2[i].islower() else ord('A')
        ciphertext2 += chr((ord(plaintext2[i]) - base + encryptkey) % 26 + base)
    else:
        # アルファベット以外(数字や記号)であればそのまま
        ciphertext2 += plaintext2[i]
print(ciphertext2)  # 暗号文の出力
