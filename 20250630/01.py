import TkEasyGUI as eg

layout = [[eg.Text('', key='out1')],
          [eg.Button('あいさつ'), eg.Button('クリア'), eg.Button('終了')]]

msg1 = ['おはよう', 'こんにちは', 'こんばんは', 'おやすみ']

# ウィンドウを作成
window = eg.Window('問題1', layout)

bpush_count = 0
# 無限ループ内でウィンドウを表示し対話
while True:
    event, values = window.read()

    # ウィンドウ上にメッセージを表示
    if event == 'あいさつ':
        window['out1'].update(msg1[bpush_count % 4])
        bpush_count += 1
    if event == 'クリア':
        window['out1'].update('')
        bpush_count = 0

    # ユーザがウィンドウを閉じるか「終了」ボタンを押したらループを抜ける
    if event == eg.WINDOW_CLOSED or event == '終了':
        break

# 画面を閉じて終了
window.close()
