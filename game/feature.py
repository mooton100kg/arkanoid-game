import pygame
from Constans.Valuable import IMAGE_HEIGHT, IMAGE_WIDTH
from Constans.Images import PLUS_LENGHT, HEAL_POTION, POISON_POTION, SPECIAL_BALL_BOMB

class Feature:
    def __init__(self, block, vel, effect):
        self.x = block.x
        self.y = block.y
        self.vel = vel
        self.effect = effect
        self.feature = None
        if effect == 'PLUS_LENGHT':
            self.image = PLUS_LENGHT
        elif effect == 'HEAL_POTION':
            self.image = HEAL_POTION
        elif effect == 'POISON_POTION':
            self.image = POISON_POTION
        elif effect == 'SPECIAL_BALL_BOMB':
            self.image = SPECIAL_BALL_BOMB

    def draw(self, window):
        if self.effect != 'None':
            window.blit(self.image, (self.x, self.y))
            self.feature = pygame.Rect(self.x, self.y, IMAGE_WIDTH, IMAGE_HEIGHT)
    
    def movement(self):
        self.y += self.vel