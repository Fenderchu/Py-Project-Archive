import DominoSprites.constants, pygame
from DominoSprites.constants import *
class Domino():
    def __init__(self, pips, pos = (0, 0)):
        self.pips = pips
        self.pip_sprites = pip_sprites
        self.bone_sprites = bone_sprites
        self.angle = 0
        self.pos = pos
        self.surface = pygame.surface.Surface((32, 64))
        self.rect = self.surface.get_rect()
        self.center = self.rect.center
        self.is_selected = False
        open_bool = True
        self.build()
    
    def update(self):
        
        if self.is_selected:
            mouse_pos = pygame.mouse.get_pos()
            self.pos = (mouse_pos[0] - self.rect.width/2, mouse_pos[1] - self.rect.height/2)
        pygame.draw.rect(win_surface, (0, 0, 0), self.rect)
        self.pos = (round(self.pos[0]/16)*16, round(self.pos[1]/16)*16)
        rotated_surface = pygame.transform.rotate(self.surface, self.angle)
        self.center = (self.pos[0] + (self.rect.width/2), self.pos[1] + (self.rect.height/2))
        self.rect = rotated_surface.get_rect(center = self.center)
        
        win_surface.blit(rotated_surface, self.pos)
    
    def build(self):
        self.surface.fill((1, 1, 1))
        self.surface.set_colorkey((1, 1, 1, 0))
        self.surface.blit(self.bone_sprites[1], (0, 0))
        self.surface.blit(self.bone_sprites[0], (0, 32))

        if self.pips[0] > 0 :
            self.surface.blit(self.pip_sprites[self.pips[0]-1], (0, 0))
        if self.pips[1] > 0:
            self.surface.blit(self.pip_sprites[self.pips[1]-1], (0, 32))
    def rotate(self, direction):
        if direction:
            self.angle += 90
        else:
            self.angle = abs(self.angle - 90)


