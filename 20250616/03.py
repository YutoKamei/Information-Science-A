# -*- coding: utf-8 -*-
import random

numlist = [random.randint(1, 1000) for _ in range(100)]

total = 0
for i in range(100):
    total += numlist[i]
    # print(numlist[i], total)

print('total:' + str(total))
average = total / len(numlist)  # 分母は100でも可
print('average:' + str(average))

inc_rate_list = []
for i in range(100):
    inc_rate = (numlist[i] - average) / average * 100
    inc_rate_list.append(inc_rate)
    print('data(' + str(i + 1) + '): ' + str(numlist[i]) + ' ' + format(inc_rate_list[i], '.2f') + '%')
