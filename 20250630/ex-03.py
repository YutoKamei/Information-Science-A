import TkEasyGUI as eg
import datetime

layout = [
    [eg.Text('開始ボタンを押して、10秒ちょうどで10秒ボタンを押してね', key='txt1')],
    [eg.Text('', key='time1')],
    [eg.Button('開始', key='start'),
     eg.Button('10秒', key='stop', disabled=True),
     eg.Button('終了')]
]

# ウィンドウを作成
window = eg.Window('問題3', layout, size=(380, 100))

# 無限ループ内でウィンドウを表示し対話
while True:
    event, values = window.read()

    # ウィンドウ内にメッセージを表示
    if event == 'start':
        start_clck = datetime.datetime.now()
        window['txt1'].update('開始ボタンを押して、10秒ちょうどで10秒ボタンを押してね')
        window['time1'].update('')
        window['start'].set_disabled(True)
        window['stop'].set_disabled(False)

    if event == 'stop':
        btn_clck = datetime.datetime.now()
        sec10 = btn_clck - start_clck
        msg1 = ''
        diff = abs(10 - sec10.total_seconds())

        if diff <= 0.05:
            msg1 = '10秒ぴったり!!'
        elif diff < 1:
            msg1 = 'おしい!'
        elif diff < 2:
            msg1 = 'もうちょっと'
        elif diff < 5:
            msg1 = 'がんばろう'
        else:
            msg1 = '残念'

        window['txt1'].update(msg1)
        window['time1'].update(f'{sec10.total_seconds():.1f}秒でした')
        window['start'].set_disabled(False)
        window['stop'].set_disabled(True)

    if event in (eg.WINDOW_CLOSED, '終了'):
        break

window.close()
