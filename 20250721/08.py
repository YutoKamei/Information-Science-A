import pygame as pg
import sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))

# プレイヤーデータ（右向きの月のキャラクタ画像）
plyimgR = pg.image.load('moonR.png')                           # 画像の読み込み
# 画像の幅・高さのサイズを 1/2 に変更
plyimgR = pg.transform.scale(plyimgR, (plyimgR.get_width() // 2,
                                       plyimgR.get_height() // 2))
# 右向きの月のキャラクタ画像を左右反転して左向きの画像を作成
plyimgL = pg.transform.flip(plyimgR, True, False)
rect1 = pg.Rect(50, 200, plyimgR.get_width()/2, plyimgR.get_height()/2)

# 壁データ（緑色）─ 枠の領域から 20 ピクセル分
# pg.Rect(left, top, width, height)
walls = [
    pg.Rect(0,   0,   800, 20),   # 上壁
    pg.Rect(0,   0,    20, 600),  # 左壁
    pg.Rect(780, 0,    20, 600),  # 右壁
    pg.Rect(0, 580,   800, 20)    # 下壁
]

# トラップ（障害物のボックスを 20 個配置）─ 重なりは気にしない
trap_boxes = []
for i in range(20):
    wx = 150 + i * 30                         # X 座標は 150 を起点に 30 ピクセルずつ
    wy = random.randint(20, 550)              # Y 座標は 20〜550 の範囲でランダム
    trap_boxes.append(pg.Rect(wx, wy, 30, 30))  # 幅 30, 高さ 30

# ゴール領域（黄色の四角）
goalrect = pg.Rect(750, 250, 30, 100)

# リセットボタン
reset_img = pg.image.load('reset_button.png')

# 画像の向きを表すフラグ
rightFlag = True
# ボタンを一度押したことを表すフラグ
pushFlag = False
# ページ番号
page = 1


# btn ボタンを押したら newpage に移動
def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    mx, my = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag is False:
            page = newpage
            pushFlag = True
    else:
        pushFlag = False


# ゲームリセット（トラップを再生成）
def gamereset():
    rect1.x = 50
    rect1.y = 50
    for d in range(20):
        trap_boxes[d].x = 150 + d * 30
        trap_boxes[d].y = random.randint(20, 550)


# ゲームオーバー
def gameover():
    gamereset()
    screen.fill(pg.Color('WHITE'))
    font1 = pg.font.Font(None, 150)
    text1 = font1.render('GAME OVER', True, pg.Color('RED'))
    screen.blit(text1, (100, 200))
    btn1 = screen.blit(reset_img, (320, 480))
    button_to_jump(btn1, 1)


# ゲームクリア
def gameclear():
    gamereset()
    screen.fill(pg.Color('GOLD'))
    font1 = pg.font.Font(None, 150)
    textimg1 = font1.render('GAME CLEAR', True, pg.Color('RED'))
    screen.blit(textimg1, (60, 200))
    btn1 = screen.blit(reset_img, (320, 480))
    button_to_jump(btn1, 1)


# ゲームステージ
def gamestage():
    global page, rightFlag
    screen.fill(pg.Color('WHITE'))
    vx = 0
    vy = 0
    key = pg.key.get_pressed()

    if key[pg.K_RIGHT]:
        vx = 4
        rightFlag = True
    if key[pg.K_LEFT]:
        vx = -4
        rightFlag = False
    
    # ここら辺で，上下の移動を加える（ゲームクリアできない）
    
    if key[pg.K_UP]:
        vy = -4                 # 追加: 上方向
    if key[pg.K_DOWN]:
        vy = 4                  # 追加: 下方向

    rect1.x += vx
    rect1.y += vy

    # 壁との衝突判定
    if rect1.collidelist(walls) != -1:
        rect1.x -= vx
        rect1.y -= vy

    # キャラクタの描画
    if rightFlag:
        screen.blit(plyimgR, rect1)
    else:
        screen.blit(plyimgL, rect1)

    # 壁の描画
    for wall in walls:
        pg.draw.rect(screen, pg.Color('DARKGREEN'), wall)

    # トラップの描画と衝突判定
    for trap in trap_boxes:
        pg.draw.rect(screen, pg.Color('BLUE'), trap)
    if rect1.collidelist(trap_boxes) != -1:
        page = 2  # ゲームオーバーへ

    # ゴールの描画・判定
    pg.draw.rect(screen, pg.Color('GOLD'), goalrect)
    if rect1.colliderect(goalrect):
        page = 3  # ゲームクリアへ


while True:
    if page == 1:
        gamestage()   # ゲームスタート
    elif page == 2:
        gameover()    # ゲームオーバー
    elif page == 3:
        gameclear()   # ゲームクリア

    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
