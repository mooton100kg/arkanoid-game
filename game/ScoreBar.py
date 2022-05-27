import pygame

from Constans.Valuable import WIDTH,HEIGHT,YELLOW


class Score_bar:
    def __init__(self, ball_vel):
        self.lenght = 0
        self.level = 1
        self.ball_vel = ball_vel

    def draw(self, window):
        pygame.draw.rect(window, YELLOW, (0, HEIGHT - 5, self.lenght, 5))
    
    def score(self, s):
        full_score = WIDTH
        current_score = self.lenght + s/self.level
        if current_score >= full_score:
            self.level += 1
            self.lenght = s/self.level
            self.ball_vel += 0.25
        else:
            self.lenght = current_score

            