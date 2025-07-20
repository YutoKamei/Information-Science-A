# 課題(2)の解読プログラム：ファイル読み込みと総当たり攻撃

try:
  # cipher2.txtファイルを開き、中身を全て読み込む
  with open('cipher2.txt', 'r') as fr:
    # read()でファイル全体を一つの文字列として読み込む
    ciphertext_from_file = fr.read()
    
  print("--- 元の暗号文 (cipher2.txt) ---")
  print(ciphertext_from_file)
  print("=" * 40)
  
  # 鍵を0から25まで変化させて総当たりで試行
  for key in range(26):
    decrypted_text = ''
    
    # 読み込んだ暗号文を1文字ずつ処理
    for char in ciphertext_from_file:
      # isalpha()でアルファベットかどうかを判定
      if char.isalpha():
        # 復号処理（鍵を引く）
        decrypted_char_code = (ord(char) - key - ord('a')) % 26 + ord('a')
        decrypted_text += chr(decrypted_char_code)
      else:
        # アルファベット以外はそのまま
        decrypted_text += char
        
    print(f"--- 鍵 {str(key).zfill(2)} での復号結果 ---")
    print(decrypted_text)
    print("-" * 40)

except FileNotFoundError:
  print("エラー: 'cipher2.txt' が見つかりません。")
  print("プログラムと同じフォルダにファイルが存在することを確認してください。")