import pygame

one = pygame.image.load("DominoSprites\One_pip_sprite.png")
two = pygame.image.load("DominoSprites\Two_pip_sprite.png")
three = pygame.image.load("DominoSprites\Three_pip_sprite.png")
four = pygame.image.load("DominoSprites\Four_pip_sprite.png")
five = pygame.image.load("DominoSprites\Five_pip_sprite.png")
six = pygame.image.load("DominoSprites\Six_pip_sprite.png")

pip_sprites = [one, two, three, four, five, six]

bone_sprites = [pygame.image.load("DominoSprites\Bass_sprite_B.png"), pygame.image.load("DominoSprites\Bass_sprite_T.png")]

screen_w, screen_h = 1000, 600

win = pygame.display.set_mode((screen_w, screen_h))

win_surface = pygame.surface.Surface((screen_w, screen_h))
hand_surface = pygame.surface.Surface((screen_w/3, 74))
Turn = 0
