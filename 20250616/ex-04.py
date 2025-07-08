##
def display_alphabet_count(strlist):
    for x in range(len(strlist)):
        print(chr(x + ord('a')), ':', '*' * strlist[x])

## 文字の出現回数
strlist = [0 for _ in range(26)]

str1 = input()
for x in range(len(str1)):
    t = ord(str1[x]) - ord('a')
    strlist[t] += 1

display_alphabet_count(strlist)
