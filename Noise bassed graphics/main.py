import opensimplex, pygame, time

seed = 100
size = (500, 500)
pixel_size = (5, 5)
y, x, z = 0, 0, 0
noise = opensimplex.OpenSimplex(seed)
win_surface = pygame.surface.Surface(size)

pix_surface = pygame.surface.Surface(pixel_size)

def main_loop():
    global z
    

    

    win = pygame.display.set_mode(size)

    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_noise()
        win.blit(win_surface, (0, 0))
        z += 1
        pygame.display.update()
        

def draw_noise():
    global x, y, z
    for y in range(size[1]//pixel_size[1]):
        for x in range(size[0]//pixel_size[0]):
            win_surface.blit(get_colour(x, y, z),(x*pixel_size[0], y*pixel_size[1]))
            

def get_colour(x, y, z):
    bassline = (50, 150, 150)
    scale = 0.05
    value = noise.noise3(x*scale, y*scale, z*scale) * 100

    colour =[]

    for i in range(0, 3):
        val = bassline[i] + value
        if val > 255:
            val = 255
        elif val < 0:
            val = 0
        colour.append(val)
    pix_surface.fill(colour)
    
    return pix_surface




main_loop()