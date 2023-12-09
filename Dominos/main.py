import pygame, random, time, DominoSprites.constants, domino
from DominoSprites.constants import *
from domino import Domino


bone_yard = []

def main_loop():

    run = True
    clock = pygame.time.Clock()
    bones = []
    player_hand = []
    open_bones = []
    selected_bone = 0
    make_bone_pool()
    for i in range(0, 7):
        pick = random.choice(bone_yard)
        if not pick in player_hand:
            player_hand.append(pick)
            bone_yard.remove(pick)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if selected_bone != 0:
                    if event.key == pygame.K_d or  event.type == pygame.K_RIGHT:
                        selected_bone.rotate(True)
                    if event.key == pygame.K_a or  event.type == pygame.K_LEFT:
                        selected_bone.rotate(False)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_inputs = pygame.mouse.get_pressed()
                if mouse_inputs[0]:
                    for bone in player_hand:
                        if selected_bone == 0:
                            if bone.rect.collidepoint(pygame.mouse.get_pos()):
                                selected_bone = bone
                                selected_bone.is_selected = True
                                break
                        else:
                            selected_bone.is_selected = False
                            selected_bone = 0
                            break
                            


        win_surface.fill((100, 100, 120))
        hand_surface.fill((80, 80, 80))
        win_surface.blit(hand_surface,(screen_w/3, screen_h-100))
        for bone in player_hand:
            if bone.rect.collidepoint(pygame.mouse.get_pos()) :
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
            elif pygame.mouse.get_cursor != pygame.SYSTEM_CURSOR_ARROW:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for bone in player_hand:       
            bone.update()
        
        for i in range(0, len(player_hand)):
            if player_hand[i].rect.colliderect(hand_surface.get_rect()):
                win_surface.blit(player_hand[i].surface, player_hand[i].pos)
                player_hand[i].pos = ((32*(i+1))+(screen_w/3), 5 + screen_h-100)
        
        win.blit(win_surface, (0, 0))
        pygame.display.update()
        
            

def make_bone_pool():
    global bone_yard
    valid_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1],
                    [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], 
                    [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], 
                    [4, 6], [5, 5], [5, 6], [6, 6]]
    for i in valid_pieces:
        coin = random.randrange(0, 1)
        if coin == 0:
            bone_yard.append(Domino(i))
        else:
            bone_yard.append(Domino([i[1], i[0]]))

            

        
                
    
main_loop()