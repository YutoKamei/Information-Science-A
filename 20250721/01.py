import pygame as pg
import sys

# pygame の初期化
pg.init()
# 画面サイズの設定 幅 800 × 高さ 600（ピクセル）
screen = pg.display.set_mode((800, 600))

while True:
    # ウィンドウを白で塗りつぶす
    screen.fill(pg.Color('WHITE'))
    # 四角形を描画
    pg.draw.rect(screen, pg.Color('RED'), (100, 100, 150, 150))
    # pg.draw.ellipse(screen, pg.Color('GREEN'), (100, 100, 150, 150), 10)
    # 線を描画（3 本の線で三角形を描画）
    pg.draw.line(screen, pg.Color('BLUE'), (250, 100), (350, 250), 5)
    pg.draw.line(screen, pg.Color('BLUE'), (350, 100), (350, 250), 5)
    pg.draw.line(screen, pg.Color('BLACK'), (250, 100), (350, 100), 5)
    # 四角形を描画
    pg.draw.rect(screen, pg.Color('RED'), (100, 100, 100, 150))

    # 描いた画像をすべてウィンドウ上に描画
    pg.display.update()
    # 1 秒間に 60 回以下のスピードに調整
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
