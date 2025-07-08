import TkEasyGUI as eg
import datetime

layout = [[eg.Text('', key='time1')],
          [eg.Button('終了')]]

# ウィンドウを作成
window = eg.Window('問題2', layout, size=(250, 100))

# 無限ループ内でウィンドウを表示し対話
now = datetime.datetime.now()
while True:
    event, values = window.read(timeout=1000, timeout_key='timeout1')

    if event == 'timeout1':
        window['time1'].update(f'{datetime.datetime.now():%Y年%m月%d日(%a) %H時%M分%S秒}')

    # ユーザがウィンドウを閉じるか「終了」ボタンを押したらループを抜ける
    if event == eg.WINDOW_CLOSED or event == '終了':
        break

# 画面を閉じて終了
window.close()
