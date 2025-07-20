# pygame ライブラリを pg と省略して表記
import pygame as pg
import sys

# pygame の初期化
pg.init()
# 画面サイズの設定 幅800×高さ600（ピクセル）
screen = pg.display.set_mode((800, 600))

# 画像の読み込み
# 読み込む画像ファイルは Moodle からダウンロードして
# プログラムと同じフォルダに保存すること
cloud_img1 = pg.image.load('cloud.png')
# cloud_img1 の画像サイズを 80×60 に縮小
cloud_img2 = pg.transform.scale(cloud_img1, (80, 60))
# cloud_img1 の画像の向きを上下反転
cloud_img3 = pg.transform.flip(cloud_img1, False, True)
# get_width と get_height で画像の幅と高さを取得
rect1 = pg.Rect(100, 100, cloud_img1.get_width(), cloud_img1.get_height())
rect2 = pg.Rect(300, 100, 80, 60)
rect3 = pg.Rect(400, 100, cloud_img3.get_width(), cloud_img3.get_height())

# フォントの指定（IPA ゴシックフォント）
# Moodle から必ず ipaexg.ttf ファイルをダウンロードし
# プログラムと同じフォルダに保存すること
font1 = pg.font.Font('ipaexg.ttf', 50)
str1 = 'こんにちは'
textimg1 = font1.render(str1, True, pg.Color('BLUE'))

while True:
    screen.fill(pg.Color('WHITE'))
    # 画像を描画
    screen.blit(cloud_img1, rect1)
    screen.blit(cloud_img2, rect2)
    screen.blit(cloud_img3, rect3)

    # 文字列を画像として描画
    screen.blit(textimg1, (100, 300))

    pg.display.update()
    # 1 秒間に 60 回以下のスピードに調整
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
