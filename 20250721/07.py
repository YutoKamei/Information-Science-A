import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))

# プレイヤデータ(太陽のキャラクタ画像)
plyimg = pg.image.load('sun.png')
myrect = pg.Rect(50, 200, plyimg.get_width(), plyimg.get_height())

# 障害物データ
boxrect = pg.Rect(300, 200, 100, 100)

def gamestage():
    screen.fill(pg.Color('WHITE'))
    vx = 0
    vy = 0

    # キーボードのキーの押下イベントを取得
    key = pg.key.get_pressed()

    if key[pg.K_RIGHT]:   # 右カーソルキー
        vx = 4            # 移動距離: X軸方向 +4 設定
    if key[pg.K_LEFT]:    # 左カーソルキー
        vx = -4           # 移動距離: X軸方向 -4 設定
    if key[pg.K_UP]:      # 上カーソルキー
        vy = -4           # 移動距離: Y軸方向 -4 設定
    if key[pg.K_DOWN]:    # 下カーソルキー
        vy = 4            # 移動距離: Y軸方向 +4 設定

    myrect.x += vx        # 現在の位置に移動距離を加算
    myrect.y += vy        # 現在の位置に移動距離を加算

    # 2つの四角形の衝突判定(重なり判定)
    if myrect.colliderect(boxrect):
        # 衝突した場合、vx, vy を引いて前に進めないようにする
        # 元の位置に戻している
        myrect.x -= vx
        myrect.y -= vy

    screen.blit(plyimg, myrect)
    pg.draw.rect(screen, pg.Color('BLUE'), boxrect)

while True:
    gamestage()
    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
