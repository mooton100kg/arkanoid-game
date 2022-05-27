import pygame
import threading
from random import choices,choice

from Constans.Images import *
from Constans.Valuable import *
from Constans.Level import level
from CollideFunc import *
from game import Player, Ball, Feature, Block, Score_bar



pygame.font.init()

heightest_level = 0

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
    protection = False
    plus_lenght = False
    game_over = False
    FPS = 60

    score_bar = Score_bar(3)

    vel = 5

    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT - 35, 50, 8, vel)
    balls = []
    blocks = []
    for b in choice(level):
        blocks.append(Block(b[0],b[1],b[2],b[3],choices([1,2,3],[GREEN_W,YELLOW_W,RED_W])[0],choices(['none','PLUS_LENGHT','HEAL_POTION','POISON_POTION','SPECIAL_BALL_BOMB','PROTECTION'],[NONE_W,PLUS_LENGHT_W,HEAL_POTION_W,POSISON_POTION_W,SPECIAL_BALL_BOMB_W,PROTECTION_W])[0]))
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
        if protection:
            pygame.draw.rect(WIN, BLUE, (0,HEIGHT - PROTECTION_HEIGHT,WIDTH,5))

        WIN.blit(health_label, (10, 10))
        WIN.blit(level_label, (10, HEIGHT - 7 - level_label.get_height()))
        WIN.blit(heightest_level_label, (WIDTH - heightest_level_label.get_width() - 10, 10))

        if player.health <= 0:
            game_over_label = large_status_font.render("GAME OVER", True, RED)
            restart_lebel = status_font.render("press any key to restart", True, WHITE)
            player_level_label = status_font.render(f"level: {score_bar.level}", True, YELLOW)

            WIN.blit(game_over_label, (WIDTH//2 - game_over_label.get_width()//2, HEIGHT//2 - game_over_label.get_height()//2))
            WIN.blit(restart_lebel, (WIDTH//2 - restart_lebel.get_width()//2, HEIGHT//2 - restart_lebel.get_height()//2 + 30))
            WIN.blit(player_level_label, (WIDTH//2 - player_level_label.get_width()//2, HEIGHT//2 - player_level_label.get_height()//2 + 60))
            if heightest_level < score_bar.level:
                heighest_label = large_status_font.render("!new heighest level!", True, RED)
                WIN.blit(heighest_label, (WIDTH//2 - heighest_label.get_width()//2, HEIGHT//2 - heighest_label.get_height()//2 - 60))

        if pause and not game_over:
            pause_label = large_status_font.render("PAUSE", True, WHITE)

            WIN.blit(pause_label, (WIDTH//2 - pause_label.get_width()//2, HEIGHT//2 - pause_label.get_height()//2))


        pygame.display.update()


    while run:
        clock.tick(FPS)

        redraw_window()

        key_pressed = pygame.key.get_pressed()
        if not pause and not game_over:
            #movement
            player.movement(key_pressed)

            if player.health <= 0:
                game_over = True

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
                if protection:
                    direction.add(protection_collide(ball))
                ball.movement(direction, player)
                if ball.y >= HEIGHT:
                    if ball.color != RED:
                        player.damage()
                    balls.remove(ball)
                if player.protection_time == 0:
                    protection = False
            

            for feature in features:
                feature.movement()                

                if type(feature.feature) is pygame.Rect and player.block.colliderect(feature.feature):

                    features.remove(feature)
                    if feature.effect == 'PLUS_LENGHT':
                        if not plus_lenght:
                            PLUS_LENGHT_count_down = threading.Thread(target=player.collect_feature, args=(feature.effect,))
                            PLUS_LENGHT_count_down.start()
                        elif plus_lenght:
                            player.plus_lenght_time += 5
                    elif feature.effect == 'PROTECTION':
                        if not protection:
                            protection = True
                            PROTECTION_count_down = threading.Thread(target=player.collect_feature, args=(feature.effect,))
                            PROTECTION_count_down.start()
                        elif protection:
                            player.protection_time += 5
                    elif feature.effect == 'SPECIAL_BALL_BOMB':
                        balls.append(Ball(player, 8, score_bar.ball_vel, RED, 3))
                    else:
                        effect_count_down = threading.Thread(target=player.collect_feature, args=(feature.effect,))
                        effect_count_down.start()

            if len(blocks) <= 0:
                for b in choice(level):
                    blocks.append(Block(b[0],b[1],b[2],b[3],choices([1,2,3],[GREEN_W,YELLOW_W,RED_W])[0],choices(['none','PLUS_LENGHT','HEAL_POTION','POISON_POTION','SPECIAL_BALL_BOMB','PROTECTION'],[NONE_W,PLUS_LENGHT_W,HEAL_POTION_W,POSISON_POTION_W,SPECIAL_BALL_BOMB_W,PROTECTION_W])[0]))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.plus_lenght_time = 1
                player.protection_time = 1
                run = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and not pause and not game_over:
                    ball = Ball(player, 8, score_bar.ball_vel, WHITE, 1)
                    balls.append(ball)
                elif event.key == pygame.K_ESCAPE and not game_over:
                    pause = not pause
                elif event.key != pygame.K_ESCAPE and game_over:
                    run = False 
                    main()
                elif event.key == pygame.K_ESCAPE and game_over:
                    run = False
                    main_menu()




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