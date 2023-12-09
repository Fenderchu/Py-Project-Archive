import pygame
pygame.font.init()
my_font = pygame.font.SysFont("Arial", 20)
class Button():
    def __init__(self, pos = tuple, size = tuple, colour = list, iconflag = bool, surface = pygame.surface, text = "None", textcolour = (0,0,0),textpt = 20, icon = "None") -> None:
        self.pos = pos
        self.size = size
        self.colour = colour
        self.iconflag = iconflag
        self.surface = surface
        self.image = pygame.surface.Surface(self.size)
        self.text = text
        self.icon = icon
        self.over = False

    def make_image(self):
        self.image.fill(self.colour)

        
        font_surface = my_font.render(self.text, self.size, (255, 255, 255))

        self.image.blit(font_surface, (self.size[0]//3, self.size[1]//3))

        

    def update(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        if x_pos >= self.pos[0]- (self.size[0]//2) and x_pos <= (self.size[0]//2) + self.pos[0]\
        and y_pos >= self.pos[1] - (self.size[1]//2) and y_pos <= (self.size[1]//2) + self.pos[1]:

            for i in range(0, 3):
                self.colour[i] = self.colour[i] * 0.5
            self.make_image()
            for i in range(0, 3):
                self.colour[i] = self.colour[i] * 2
            self.over = True
        else:
            self.make_image()
            self.over = False
        self.surface.blit(self.image, (self.pos[0] - self.size[0]//2, self.pos[1] - self.size[1]//2))
        self.is_pressed()
    
    def is_pressed(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.over:
                return True
            else:
                return False


