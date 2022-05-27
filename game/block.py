import pygame
from Constans.Valuable import RED, GREEN, YELLOW

class Block:
    def __init__(self, x, y, width, height, health, feature):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.score = health
        self.feature = feature
        if self.health == 3:
            self.score = 100
        elif self.health == 2:
            self.score = 80
        elif self.health == 1:
            self.score = 50

    def draw(self, window):
        if self.health == 3:
            self.color = RED
        elif self.health == 2:
            self.color = YELLOW
        elif self.health == 1:
            self.color = GREEN
        self.block = pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def damage(self, damage):
        self.health -= damage