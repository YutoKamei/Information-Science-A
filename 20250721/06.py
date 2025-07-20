import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))
button_img = pg.image.load('button.png')
button_width = button_img.get_width()
button_height = button_img.get_height()

# ボタンを1回押したことを表すフラグ変数
pushFlag = False
screen.fill(pg.Color('WHITE'))

while True:
    # ボタン画像をスクリーンの中央に配置
    btn = screen.blit(button_img, (400 - button_width / 2, 300 - button_height / 2))

    # マウスのクリックイベントを取得
    mdown = pg.mouse.get_pressed()
    # マウスでクリックしている座標を取得
    mx, my = pg.mouse.get_pos()

    if mdown[0]:
        # クリックした箇所がボタンの範囲内かつ、ボタンがまだ押されていない状態
        if btn.collidepoint(mx, my) and pushFlag == False:
            screen.fill(pg.Color('BLACK'))
            pushFlag = True
        # クリックした箇所がボタンの範囲内かつ、ボタンが押されている状態
        elif btn.collidepoint(mx, my) and pushFlag == True:
            screen.fill(pg.Color('WHITE'))
            pushFlag = False

    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
