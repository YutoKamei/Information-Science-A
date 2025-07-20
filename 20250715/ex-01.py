# 課題(1)の解読プログラム：総当たり攻撃

# 解読対象の暗号文
ciphertext = 'slx xr uvkvdf bfnrbl erzpf'

print(f"暗号文: {ciphertext}")
print("-" * 30)
print("総当たりによる解読結果:")

# 鍵を0から25まで変化させて総当たりで試行
for key in range(26):
  # 復号した平文を格納する変数
  decrypted_text = ''
  
  # 暗号文を1文字ずつ処理
  for char in ciphertext:
    # isalpha()でアルファベットかどうかを判定
    if char.isalpha():
      # 復号処理（暗号化とは逆の操作で、鍵を引く）
      decrypted_char_code = (ord(char) - key - ord('a')) % 26 + ord('a')
      # 文字コードを文字に変換して連結
      decrypted_text += chr(decrypted_char_code)
    else:
      # アルファベット以外（記号や空白）はそのまま連結
      decrypted_text += char
      
  # 鍵と復号結果を出力
  # str(key).zfill(2) は、1桁の数字を'01'のように2桁で表示するための処理
  print(f"鍵 {str(key).zfill(2)}: {decrypted_text}")