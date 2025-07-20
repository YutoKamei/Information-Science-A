import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))

# 月の画像を読み込み（右向き）
imgR = pg.image.load('moonR.png')
# 画像を左右反転して左向きの画像を用意
imgL = pg.transform.flip(imgR, True, False)

# 画像を画面中央に配置するように設定
rect1 = pg.Rect(
    400 - imgR.get_width() / 2,
    300 - imgR.get_height() / 2,
    imgR.get_width(),
    imgR.get_height()
)

# 進行方向が右の場合 rightFlag を True にする（左の場合 False）
rightFlag = True

while True:
    screen.fill(pg.Color('WHITE'))

    # X軸方向の移動量
    vx = 0
    # Y軸方向の移動量
    vy = 0
    # キー入力状態を取得
    key1 = pg.key.get_pressed()

    # 右カーソルキー
    if key1[pg.K_RIGHT]:
        vx = 5
        rightFlag = True  # 右向き
    # 左カーソルキー
    if key1[pg.K_LEFT]:
        vx = -5
        rightFlag = False  # 左向き
    # 上カーソルキー
    if key1[pg.K_UP]:
        vy = -5
    # 下カーソルキー
    if key1[pg.K_DOWN]:
        vy = 5

    # 画像位置を更新
    rect1.x += vx
    rect1.y += vy

    # 向きに応じて画像を描画
    screen.blit(imgR if rightFlag else imgL, rect1)

    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
