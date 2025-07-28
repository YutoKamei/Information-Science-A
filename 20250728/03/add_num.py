#filepath = 'test-numbers.txt'
filepath = 'numbers.txt'

count = 0
with open(filepath, 'r') as f:
    for line in f:
        sum = 0
        for i in range(len(line)-1):
            sum += int(line[i])

        if sum != 0:
            print(sum)
            count+=1

print(f'出力したのは，{count}行です')
