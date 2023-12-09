import pygame, math
from v_sprites import *

class VSprite():
    def __init__(self, sprite = 0, start_pos = [0, 0]):
        self.pos = start_pos
        self.angle = 0
        self.scale = 5
        self.sprite = sprite
        self.friction = 0.75
        self.velocity_caps = 10
        self.accel_cap = 2
        self.turn_val = 0
        self.thruster = False

        if self.sprite in [2]:
            self.special_vals = [0, 0, 0, 0]
        else:
            self.special_vals = None
        
        if self.sprite in [2]:
            self.rb_vals = [(0, 0), (0, 0), 0, 0, 0.05, (0, 0)]
            ### Vel, Accl, AngVel, AngAcc, weight, inertia

        else:
            self.rb_vals = None

        

    def get_attributes(self):
        return (self.sprite, self.pos, self.scale, self.angle)

    def get_vector(self):

        sprite = vector_sprites[self.sprite]
        rotated_points = rotate_points(sprite, self.angle)
        center = get_center(rotated_points)
         
        
        poi = rotated_points[2]
        dist = math.sqrt(((poi[0]-center[0])**2) + ((poi[1]-center[1])**2))
        
        return [(poi[0]/dist)*0.001, (poi[1]/dist)*0.001]
    
    def update(self):
        if not self.special_vals == None:
            pass

        if not self.rb_vals == None:
            ###chek inputs
            
            if self.turn_val == 1:
                self.rb_vals[3] += 0.0005
            elif self.turn_val == -1:
                self.rb_vals[3] -= 0.0005
            if self.thruster:
                self.rb_vals[1] = tuple(map(sum, zip(self.get_vector(), self.rb_vals[1])))
            
            ###apply velocity 
            self.rb_vals[0] = tuple(map(sum, zip( self.rb_vals[0], self.rb_vals[1])))
            self.rb_vals[2] += self.rb_vals[3]
            self.angle += self.rb_vals[2]

            ###apply inertia
            temp = []
            for i in range(0, len( self.rb_vals[5])):
                temp.append(self.rb_vals[5][i] + self.rb_vals[0][i] * self.rb_vals[4])
            self.rb_vals[5] = temp

            self.pos = tuple(map(sum, zip( self.rb_vals[5], self.pos)))

            ###apply friction
            if not self.rb_vals[2] == 0:
                self.rb_vals[2] -= self.rb_vals[2]*(self.friction * self.rb_vals[4])
                self.rb_vals[3] -= self.rb_vals[3]*(self.friction * self.rb_vals[4])
            

            ###cap velocity and accel

            if abs(self.rb_vals[2]) > 0.05:
                self.rb_vals[2] -= self.rb_vals[3]*2
            if abs(self.rb_vals[3]) > 0.02:
                self.rb_vals[3] -= self.rb_vals[3] *0.75
            self.rb_vals[2] = round(self.rb_vals[2], 6)
            self.rb_vals[3] = round(self.rb_vals[3], 6)
            
            if abs(self.rb_vals[2]) < 0.0001:
                self.rb_vals[2] = 0
            if abs(self.rb_vals[3]) < 0.0001:
                self.rb_vals[3] = 0
            
            for i in range(0, 2):
                if abs(self.rb_vals[1][i]) > 0.005:
                    self.rb_vals[1][i] -= i*0.5
                if abs(self.rb_vals[0][i]) > 1:
                    self.rb_vals[0][i] -= i*0.5
                if abs(self.rb_vals[5][i]) > 0.5:
                    self.rb_vals[5][i] -= i*0.5
                

            print(self.rb_vals)
            
    

            
            






