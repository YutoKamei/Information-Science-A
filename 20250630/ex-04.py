import TkEasyGUI as eg

layout = [[eg.Text('0', key='results_display', size =(12 ,1) , text_align ='right')],
          [eg.Button('1'),eg.Button('2'),eg.Button('3')],

          [eg.Button('4'),eg.Button('5'),eg.Button('6')],
          [eg.Button('7'),eg.Button('8'),eg.Button('9')],
          [eg.Button('0'), eg.Button('+', key='exec_plusop'), eg.Button('=', key='exec_op')],
          [eg.Button('clear', key='clear')]]

win = eg.Window('足し算', layout, font=(None, 14), size=(200 ,250) , resizable=True)

num1 = 0
disp1 = '0'
while True:
    e, v = win.read()
    if e == 'exec_plusop':
        num1 = int(win['results_display'].get())
        disp1 = '0'
        win['results_display']. update(disp1)
    elif e == 'exec_op':
        num2 = int(win['results_display'].get())
        disp1 = f'{num1+num2 :,}'
        win['results_display'].update(disp1)
    elif e == '1':
        if disp1 == '0':
            disp1 = '1'
        else:
            disp1 += '1'
        win['results_display'].update(disp1)
    elif e == '2':
        if disp1 == '0':
            disp1 = '2'
        else:
            disp1 += '2'
        win['results_display'].update(disp1)
    elif e == '3':
        if disp1 == '0':
            disp1 = '3'
        else:
            disp1 += '3'
        win['results_display'].update(disp1)
    elif e == '4':
        if disp1 == '0':
            disp1 = '4'
        else:
            disp1 += '4'
        win['results_display'].update(disp1)
    elif e == '5':
        if disp1 == '0':
            disp1 = '5'
        else:
            disp1 += '5'
        win['results_display'].update(disp1)
    elif e == '6':
        if disp1 == '0':
            disp1 = '6'
        else:
            disp1 += '6'
        win['results_display'].update(disp1)
    elif e == '7':
        if disp1 == '0':
            disp1 = '7'
        else:
            disp1 += '7'
        win['results_display'].update(disp1)
    elif e == '8':
        if disp1 == '0':
            disp1 = '8'
        else:
            disp1 += '8'
        win['results_display'].update(disp1)
    elif e == '9':
        if disp1 == '0':
            disp1 = '9'
        else:
            disp1 += '9'
        win['results_display'].update(disp1)
    elif e == '0':
        if disp1 == '0':
            disp1 = '0'
        else:
            disp1 += '0'
        win['results_display'].update(disp1)
    elif e == 'clear':
        disp1 = '0'
        win['results_display'].update(disp1)
        num1 = 0
        num2 = 0

    if e == eg.WINDOW_CLOSED:
        break

win.close()
