plaintext1 = ''

# cipher2.txtファイルの中身をfrで操作できるようにする
# frはファイルの文章全体
with open('cipher2.txt') as fr:
    # frから，1行ずつ取り出しflとして操作する。
    cipher_lines = fr.readlines()

# まずは、この行以降に課題(1)と同じように総当たりでやってみると？

import re
from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# ── ひとめで分かる辞書（上位3000語ほどで十分）を用意 ──
# ここでは最小限の英単語セットをハードコードしているが、
# /usr/share/dict/words などを read してもOK
ENGLISH_WORDS = {
    "the","be","to","of","and","a","in","that","have","i","it","for","not",
    "on","with","he","as","you","do","at","this","but","his","by","from",
    "they","we","say","her","she","or","an","will","my","one","all","would",
    "there","their","what","so","up","out","if","about","who","get","which",
    "go","me","can","just","like","time","no","know","take","people","into",
    "year","your","good","some","could","them","see","other","than","then",
    "now","look","only","come","its","over","think","also","back","after"
}

def decrypt(text: str, key: int) -> str:
    """シーザー暗号（小文字のみ対象）を key だけ左にずらして復号"""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('a')
            result.append(chr((ord(ch) - base - key) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def english_score(text: str) -> int:
    """復号文に含まれる英単語の数を返す（大文字小文字は無視）"""
    words = re.findall(r"[a-z]+", text.lower())
    return sum((w in ENGLISH_WORDS) for w in words)

# すべての鍵でスコア計算
scores = {}
for key in range(26):
    plain = decrypt(''.join(cipher_lines), key)
    scores[key] = english_score(plain)

# 単語ヒット数が最大の鍵を採用
best_key = max(scores, key=scores.get)
best_plaintext = decrypt(''.join(cipher_lines), best_key)

print(f"=== 推定された鍵: {best_key} ===\n")
print(best_plaintext)
