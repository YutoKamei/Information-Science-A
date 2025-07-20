import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))

# 画像の読み込み
img1 = pg.image.load('sun.png')
# 画像を画面中央に配置するように設定
rect1 = pg.Rect(
    400 - img1.get_width() / 2,
    300 - img1.get_height() / 2,
    img1.get_width(),
    img1.get_height()
)

while True:
    screen.fill(pg.Color('WHITE'))

    # X 軸方向の移動量
    vx = 0
    # Y 軸方向の移動量
    vy = 0
    # キー入力イベントを取得
    key1 = pg.key.get_pressed()

    # 右カーソルキーの場合
    if key1[pg.K_RIGHT]:
        vx = 5  # X 軸方向に +5 (右方向に 5 進む)
    # 左カーソルキーの場合
    if key1[pg.K_LEFT]:
        vx = -5  # X 軸方向に -5 (左方向に 5 進む)
    # 上カーソルキーの場合
    if key1[pg.K_UP]:
        vy = -5  # Y 軸方向に -5 (上方向に 5 進む)
    # 下カーソルキーの場合
    if key1[pg.K_DOWN]:
        vy = 5  # Y 軸方向に +5 (下方向に 5 進む)

    # 画像の位置の X 軸方向の値を vx 分加算
    rect1.x += vx
    # 画像の位置の Y 軸方向の値を vy 分加算
    rect1.y += vy

    screen.blit(img1, rect1)
    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
