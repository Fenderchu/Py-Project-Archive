import pygame, random, time
from constants import *
from ui_objects import *
from ship import Ship

pygame.font.init()
arial= pygame.font.SysFont("arial", 40)

ships = []

def main_loop():
    run = True
    title_bool = True

    

    while run:
        win_surf.fill((0, 0, 0))
        if title_bool:

            if title():
                title_bool = False
        else:
            create_menu()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        win.blit(win_surf, (0, 0))
        pygame.display.update()


play_button = Button((screen_size[0]//2, screen_size[1]//1.5), (100,50), [100, 50, 100], False, win_surf, "Play", textpt=10)

def title():
    
    win_surf.blit(title_bg,(0, 0))
    image = arial.render("DOTSpace", False, (255, 255, 255))
    win_surf.blit(image, (175, 150))
    

    play_button.update()
    if play_button.is_pressed():
        return True
    else:
        return False


create_new_but = Button((60, 60), (50, 50), [100, 50, 100], False, win_surf, "New ship", [255, 255, 255], 10)
new_ship = ""
pix_buttons = []
selection_buttons = []
selection_colours = [[50, 50, 50], [50, 200, 50], [50, 50, 200], [100, 100, 40], [100, 50, 100]]
for i in range(5):
    selection_buttons.append(Button((100+(50*i), 100), (50, 50), selection_colours[i], False, win_surf, " " ))


def create_menu():
    global pix_buttons

    win_surf.fill((100, 100, 100))
    create_new_but.update()
    if create_new_but.is_pressed():
        new_ship = Ship()
        pix_buttons = []
        x, y = 0, 0
        for pix_row in new_ship.pix_array:
            for pix in pix_row:
                pix_buttons.append(Button((150+(50*x), 150+(50*y)), (50, 50), [100, 100, 100], False, win_surf, "t" ))

                x += 1
                if x >= 5:
                    x -= 5
                    y += 1
    for button in pix_buttons:
        button.update()

        if button.is_pressed():
            print("here")
            button.colour = [200, 200, 200]
    for button in selection_buttons:
        button.update()
       
        

        
    
    

    


main_loop()
