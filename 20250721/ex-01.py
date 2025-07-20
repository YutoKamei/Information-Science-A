import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((800, 600))

while True:
    screen.fill(pg.Color("WHITE"))
    # 四角形を描画
    pg.draw.rect(screen, pg.Color("RED"), (100, 100, 200, 200))
    # 円を描画
    pg.draw.ellipse(screen, pg.Color("BLUE"), (100, 100, 200, 200), 5)
    # 線を描画
    pg.draw.line(screen, pg.Color("BLACK"), (100, 100), (300, 300), 5)
    pg.draw.line(screen, pg.Color("BLACK"), (300, 100), (100, 300), 5)
    pg.draw.line(screen, pg.Color("BLACK"), (200, 100), (200, 300), 5)
    pg.draw.line(screen, pg.Color("BLACK"), (100, 200), (300, 200), 5)
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
