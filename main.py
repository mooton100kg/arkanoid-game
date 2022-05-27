import pygame
import threading
from random import choices,choice
from time import sleep

from Constans.Images import *
from Constans.Valuable import *
from Constans.Level import level
from CollideFunc import obj_ball_collide, border_collide
from game import Player, Ball, Feature, Block, Score_bar



pygame.font.init()


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid game")


def mouse_click(obj, t, font, color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if obj.x + obj.width > mouse[0] > obj.x and obj.y + obj.height > mouse[1] > obj.y:
        if click[0] == 1:
            main()
            

        else:
            text = font.render(t, True, color)
            WIN.blit(text, (obj.x, obj.y))
            pygame.display.update()

    else:
        text = font.render(t, True, WHITE)
        WIN.blit(text, (obj.x, obj.y))
        pygame.display.update()


def main():
    run = True
    pause = False
    FPS = 60

    score_bar = Score_bar(3)
    heightest_level = 0

    vel = 5

    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT - 35, 50, 8, vel)
    balls = []
    blocks = []
    for b in choice(level):
        blocks.append(Block(b[0],b[1],b[2],b[3],choices([1,2,3],[GREEN_W,YELLOW_W,RED_W])[0],choices(['none','PLUS_LENGHT','HEAL_POTION','POISON_POTION','SPECIAL_BALL_BOMB'],[NONE_W,PLUS_LENGHT_W,HEAL_POTION_W,POSISON_POTION_W,SPECIAL_BALL_BOMB_W])[0]))
    features = []

    large_status_font = pygame.font.SysFont("comicsans", 30)
    status_font = pygame.font.SysFont("comicsans", 20)
    small_status_font = pygame.font.SysFont("comicsans", 16)

    def redraw_window():
        WIN.fill(BLACK)

        health_label = status_font.render(f"Health: {player.health}", True, WHITE)
        level_label = small_status_font.render(f"Level: {score_bar.level}", True, YELLOW)
        if score_bar.level < heightest_level or heightest_level == 0:
            heightest_level_label = status_font.render(f"Heightest level: {heightest_level}", True, WHITE)
        elif score_bar.level >= heightest_level:
            heightest_level_label = status_font.render(f"Heightest level: {score_bar.level}", True, YELLOW)

        score_bar.draw(WIN)
        player.draw(WIN)
        for ball in balls:
            ball.draw(WIN)
        for block in blocks:
            block.draw(WIN)
        for feature in features:
            feature.draw(WIN)

        WIN.blit(health_label, (10, 10))
        WIN.blit(level_label, (10, HEIGHT - 7 - level_label.get_height()))
        WIN.blit(heightest_level_label, (WIDTH - heightest_level_label.get_width() - 10, 10))

        if pause:
            pause_label = large_status_font.render("PAUSE", True, WHITE)

            WIN.blit(pause_label, (WIDTH//2 - pause_label.get_width()//2, HEIGHT//2 - pause_label.get_height()//2))
            pygame.display.update()


        pygame.display.update()

    while run:
        clock.tick(FPS)

        redraw_window()

        if not pause:
            #movement
            key_pressed = pygame.key.get_pressed()
            player.movement(key_pressed)

            for ball in balls:
                direction = set()
                if len(blocks) != 0:
                    for block in blocks:
                        direction.add(obj_ball_collide('block', block, ball))
                        if block.health <= 0:
                            blocks.remove(block)
                            score_bar.score(block.score)
                            if block.feature != 'none':
                                feature = Feature(block, 3, block.feature)
                                features.append(feature)

                direction.add(obj_ball_collide('player', player, ball))
                direction.add(border_collide(ball))
                ball.movement(direction, player)
                if ball.y >= HEIGHT:
                    if ball.color != RED:
                        player.damage()
                    balls.remove(ball)
            

            for feature in features:
                feature.movement()                

                if type(feature.feature) is pygame.Rect and player.block.colliderect(feature.feature):

                    features.remove(feature)
                    if feature.effect == 'PLUS_LENGHT':
                        if len(threading.enumerate()) == 1:
                            effect_count_down = threading.Thread(target=player.collect_feature, args=(feature.effect,))
                            effect_count_down.start()
                        elif len(threading.enumerate()) > 1:
                            player.plus_lenght_time += 5
                    elif feature.effect == 'SPECIAL_BALL_BOMB':
                        balls.append(Ball(player, 8, score_bar.ball_vel, RED, 3))
                    else:
                        effect_count_down = threading.Thread(target=player.collect_feature, args=(feature.effect,))
                        effect_count_down.start()

            if len(blocks) <= 0:
                for b in choice(level):
                    blocks.append(Block(b[0],b[1],b[2],b[3],choices([1,2,3],[GREEN_W,YELLOW_W,RED_W])[0],choices(['none','PLUS_LENGHT','HEAL_POTION','POISON_POTION','SPECIAL_BALL_BOMB'],[NONE_W,PLUS_LENGHT_W,HEAL_POTION_W,POSISON_POTION_W,SPECIAL_BALL_BOMB_W])[0]))
            
            if player.health <= 0:
                pass


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and not pause:
                    ball = Ball(player, 8, score_bar.ball_vel, WHITE, 1)
                    balls.append(ball)
                elif event.key == pygame.K_ESCAPE:
                    timer = 3
                    if pause == True:
                        sleep(1)
                        timer -= 1
                    pause = not pause
                    


                     


    quit()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    menu_font = pygame.font.SysFont("comicsans", 40)

    title = title_font.render("ARKANOID", True, WHITE)
    start = menu_font.render("Start", True, WHITE)

    start_rect = pygame.Rect(WIDTH//2 - start.get_width()//2, HEIGHT//2 - start.get_height()//2 + 60, start.get_width(), start.get_height())

    WIN.fill(BLACK)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - title.get_height()//2))
    WIN.blit(start, (start_rect.x, start_rect.y))

    pygame.display.update()


    run = True

    while run:
        
        mouse_click(start_rect, "Start", menu_font, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        
    pygame.quit()

        

if __name__ == '__main__':
    main()