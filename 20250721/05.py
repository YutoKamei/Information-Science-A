import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))

# 星のキャラクタの画像を読み込み
img_star = pg.image.load('star.png')
# 星のキャラクタの画像の幅と高さを取得
star_width = img_star.get_width()
star_height = img_star.get_height()

while True:
    screen.fill(pg.Color('WHITE'))

    # マウスのクリック状態を取得
    mdown = pg.mouse.get_pressed()
    # マウスでクリックしている位置 ((X, Y) 座標) を取得
    mx, my = pg.mouse.get_pos()

    # 左ボタンが押されている状態
    if mdown[0]:
        # 画像のサイズを考慮して画像をマウスの座標位置を中心に描画
        screen.blit(img_star, (mx - star_width / 2, my - star_height / 2, star_width, star_height))

    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
