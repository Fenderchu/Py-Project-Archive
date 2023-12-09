import pygame
from v_sprites import vector_sprites, scribe
from vs_obj import VSprite

win_size = (400, 400)

def main_loop():

    run = True

    win = pygame.display.set_mode(win_size)

    main_surface = pygame.surface.Surface(win_size)
    main_surface.set_colorkey((1, 1, 1, 0))
    player = VSprite(2, [100, 100])
    objects = [player]

    clock = pygame.time.Clock()
    while run:
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key =  event.key 
                if key == pygame.K_RIGHT:
                    player.turn_val = 1
                if key == pygame.K_LEFT:
                    player.turn_val = -1
                if key == pygame.K_UP:
                    player.thruster = True
            if event.type == pygame.KEYUP:
                key = event.key
                if key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    player.turn_val = 0
                if key == pygame.K_UP:
                    player.thruster = False


        main_surface.fill((0, 0, 0))

        for i in objects:
            i.update()
            obj = i.get_attributes()
            scribe(obj[0], obj[1], obj[2], obj[3], main_surface)
           

        
        win.blit(main_surface, (0, 0))
        pygame.display.update()

main_loop()