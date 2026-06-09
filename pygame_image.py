import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_x = 0
    bg_width = bg_img.get_width()
    scroll_speed = 5
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        bg_x -= scroll_speed
        if bg_x <= 0:
            bg_x = bg_width

        screen.blit(bg_img, (bg_x, 0))
        screen.blit(bg_img, (bg_x - bg_width, 0))
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
