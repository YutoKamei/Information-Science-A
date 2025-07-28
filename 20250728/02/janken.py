import TkEasyGUI as eg
import random

def judge(mh, ch):
    if mh == ch:
        return -1
    elif (mh == 0 and ch == 1) or (mh == 1 and ch == 2) or (mh == 2 and ch == 0):
        return 1
    else:
        return 0

layout = [[eg.Text('じゃんけんゲームはじめるよ。グーチョキパーのボタンを押してね')],
          [eg.Image('janken_boys.png', key='cmp_img', enable_events=True)],
          [eg.Button('グー', key='rock'), eg.Button('チョキ', key='scissors'), eg.Button('パー', key='paper')],
          [eg.Text('', key='textbox1')]
          ]

win = eg.Window('じゃんけんゲーム', layout, font=(None, 14), size=(800, 600))

cmphand_img = ['janken_gu.png', 'janken_choki.png', 'janken_pa.png']

while True:
    e, v = win.read()

    judgeflag = 0
    cmphand = -1
    myhand = -1
    if e == 'rock':
        myhand = 0
        cmphand = random.randint(0,2)
        win['cmp_img'].update(cmphand_img[cmphand])
        judgeflag = 1
    elif e == 'scissors':
        myhand = 1
        cmphand = random.randint(0,2)
        win['cmp_img'].update(cmphand_img[cmphand])
        judgeflag = 1
    elif e == 'paper':
        myhand = 2
        cmphand = random.randint(0,2)
        win['cmp_img'].update(cmphand_img[cmphand])
        judgeflag = 1

    if judgeflag == 1:
        res = judge(myhand, cmphand)
        if res == 1:
            win['textbox1'].update('あなたの勝ち')
        elif res == 0:
            win['textbox1'].update('あなたの負け')
        else:
            win['textbox1'].update('あいこだよ。もう一回')

    if e == eg.WINDOW_CLOSED:
        break
win.close()
