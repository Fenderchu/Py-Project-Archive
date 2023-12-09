import pygame
screen_size = (500, 500)
win = pygame.display.set_mode(screen_size)

win_surf = pygame.surface.Surface(screen_size)

title_bg = pygame.image.load("sprites\Space_ph1.jpg")
title_bg = pygame.transform.scale(title_bg,screen_size)

