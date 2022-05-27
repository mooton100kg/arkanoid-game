import pygame
from time import sleep

from Constans.Valuable import WIDTH, WHITE


class Player:
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.health = 5
        self.color = WHITE
        self.plus_lenght_time = 0
        
    def draw(self, window):
        self.block = pygame.draw.rect(window,self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))

    def movement(self, key_pressed):
        if key_pressed[pygame.K_a] and self.x - self.vel - self.width//2 > 0:
            self.x -= self.vel
            self.move = 'left'
        elif key_pressed[pygame.K_d] and self.x + self.vel + self.width//2 < WIDTH:
            self.x += self.vel
            self.move = 'right'
        else:
            self.move = ''

    def damage(self):
        self.health -= 1

    def collect_feature(self, effect):
        if effect == 'PLUS_LENGHT':
            plus = 0
            self.plus_lenght_time += 5
            loop = True
            for i in range(0,55):
                sleep(0.01)
                if self.width < 100:
                    self.width += 1
                    plus += 1

            while loop:
                sleep(1)
                self.plus_lenght_time -= 1
                print(self.plus_lenght_time)
                if self.plus_lenght_time == 0:
                    loop = False

            for i in range(0,plus):
                sleep(0.01)
                self.width -= 1
        elif effect == 'HEAL_POTION':
            self.health += 1
        elif effect == 'POISON_POTION':
            self.health -= 1

        