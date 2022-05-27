import pygame

class Ball:
    def __init__(self, player, radius, vel, color, damage):
        self.radius = radius
        self.x = player.x 
        self.y = player.y - player.height//2 - self.radius
        self.vel = vel
        self.color = color   
        self.old_direct = 'top' 
        self.damage = damage

    def draw(self, window):
        self.ball = pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def movement(self, collide : set, player):
        move = True

        while move:
            if 'topleft' in collide or ('top' in collide and 'left' in collide) or ('top' in collide and self.old_direct == 'bottomleft') or ('left' in collide and self.old_direct == 'topright'):
                self.x += self.vel
                self.y += self.vel
                self.old_direct = 'topleft'
                move = False
            elif 'topright' in collide or ('top' in collide and 'right' in collide) or ('top' in collide and self.old_direct == 'bottomright') or ('right' in collide and self.old_direct == 'topleft'):
                self.x -= self.vel
                self.y += self.vel
                self.old_direct = 'topright'
                move = False
            elif 'bottomleft' in collide or ('bottom' in collide and player.move == 'right' and self.old_direct != 'bottom') or ('bottom' in collide and 'left' in collide) or ('bottom' in collide and self.old_direct == 'topleft') or ('left' in collide and self.old_direct == 'bottomright'):
                self.x += self.vel
                self.y -= self.vel
                self.old_direct = 'bottomleft'
                move = False
            elif 'bottomright' in collide or ('bottom' in collide and player.move == 'left' and self.old_direct != 'bottom') or ('bottom' in collide and 'right' in collide) or ('bottom' in collide and self.old_direct == 'topright') or ('right' in collide and self.old_direct == 'bottomleft'):
                self.x -= self.vel
                self.y -= self.vel
                self.old_direct = 'bottomright'
                move = False
            elif 'top' in collide:
                self.y += self.vel
                self.old_direct = 'top'
                move = False
            elif 'bottom' in collide:
                self.y -= self.vel
                self.old_direct = 'bottom'
                move = False
            elif 'none' in collide:
                collide.clear()
                collide.add(self.old_direct)
        