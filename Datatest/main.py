import pygame, random

cell_size = 10
board = []
def main_loop():
    
    run = True

    win = pygame.display.set_mode((500, 500))

    win_surf = pygame.surface.Surface((500, 500))
    cell_surf = pygame.surface.Surface((cell_size,cell_size))
    make_board()
    fill_board()
    while run:
        for i in range(0, 500):
            for j in range(0, 500):
                cellcheck(i, j)
                if board[i][j] == 1:
                    cell_surf.fill((255, 255, 255))
                else:
                    cell_surf.fill((0, 0, 0))
                win_surf.blit(cell_surf, ((i*cell_size),(j*cell_size)))
        win.fill((0, 0, 0))
        win.blit(win_surf,(0, 0))
        win_surf.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
        
def make_board():
    
    for i in range(0, 500):
        board.append([])      
        for j in range(0, 500):
            board[i].append(0)

def fill_board():
    for i in range(0, 500):    
        for j in range(0, 500):
            board[i][j] = random.randint(0, 1)

def cellcheck(x, y):
    surrounding = get_surronding(x, y)
    live = 0
    for i in surrounding:
        if i == 1:
            live += 1
    if live <= 2:
        board[x][y] = 0
    elif live >=4:
        board[x][y] = 1
            

def get_surronding(x, y):
    output = []
    cells = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
    for cell in cells:
        x2, y2 = x+cell[0], y+cell[1]

        if x2 >=0 and  x2 < 500:
            pass
        else:
            x2 = x

        if y2 >=0 and  y2 < 500:
            pass
        else:
            y2 = y
        output.append(board[x2][y2])
            

    return output

main_loop()