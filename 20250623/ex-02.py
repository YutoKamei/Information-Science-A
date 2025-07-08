for i in range(1, 101):
    if i % 3 == 0 and '3' in str(i):
        print('ごろごろにゃーん')
    elif i % 3 == 0 or '3' in str(i):
        print('にゃーん')
    else:
        print(i)
