import pygame as pg
from constants import *

from player import Player


def main_loop():
    run = True

    win = pg.display.set_mode(screen_size)

    player = Player(None)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                key = event.key

                if key == pg.K_w:
                    player.input_state[0] += 1
                if key == pg.K_s:
                    player.input_state[1] += 1
                if key == pg.K_a:
                    player.input_state[2] += 1
                if key == pg.K_d:
                    player.input_state[3] += 1

            if event.type == pg.KEYUP:
                key = event.key

                if key == pg.K_w:
                    player.input_state[0] -= 1
                if key == pg.K_s:
                    player.input_state[1] -= 1
                if key == pg.K_a:
                    player.input_state[2] -= 1
                if key == pg.K_d:
                    player.input_state[3] -= 1

        player.update()
        win.blit(win_surface, (0, 0))

        pg.display.update()


main_loop()