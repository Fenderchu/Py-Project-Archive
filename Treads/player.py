import pygame as pg

class Player():
    def __init__(self, tank_type) -> None:\
        ###fill with sprite data
        self.input_state = [0, 0, 0, 0, 0]
        self.size = (0, 0)
        ###change values apropriate to tank
        self.defense_points = [0, 0, 0, 0]
        ###Fill when rounds.py is done 
        self.rounds = None
        self.acceleration = 0.001
        self.velocity = [0, 0]
        self.n_vector = [0, 0]
        self.max_speed = 3
        ### fill these in with sprites
        self.sprite = None
        self.rect = self.sprite
        self.surface = None

    def update_state(self):
        self.velocity[1] += self.acceleration * (self.input_state[0] - self.input_state[1])

        if self.velocity[1] >= self.max_speed:
            self.velocity[1] = self.max_speed

        if self.velocity[1] <= -self.max_speed:
            self.velocity[1] = -self.max_speed

            
        if self.input_state[0] == 0 and self.input_state[1] == 0:   
            self.velocity[1] = self.velocity[1] * 0.999
        
            if self.velocity[1] > -0.5 and self.velocity[1] < 0.5:
                self.velocity[1] = 0

        print(self.velocity)
    
    def update(self):
        self.update_state()
        



