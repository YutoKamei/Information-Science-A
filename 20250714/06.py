import secrets

# ビット長を格納したリスト
bitlength = [32, 64, 128, 256, 512, 1024]

# bitlength から要素を取り出し、当該ビット数の整数値を出力
for i in bitlength:
    num = secrets.randbits(i)
    # 桁数もあわせて出力
    print(f'{i}bits: {num:,}, 桁数: {len(str(num))}')
