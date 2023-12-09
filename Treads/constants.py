import pygame as pg


screen_size = (500, 500)

win_surface = pg.Surface(screen_size)
win_surface.set_colorkey((1, 1, 1, 0))

###fill with tank information
### def points, rounds, acc, max speed, turret speed
tank_types = { "test":[0]}