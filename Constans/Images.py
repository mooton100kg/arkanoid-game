import pygame
import os
from Constans.Valuable import IMAGE_HEIGHT, IMAGE_WIDTH

#load images
HEAL_POTION = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'heal.png')), (IMAGE_WIDTH,IMAGE_HEIGHT))
POISON_POTION = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'damage.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))
SPECIAL_BALL_BOMB = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'bom_ball.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))
PLUS_LENGHT = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'plus_lenght.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))