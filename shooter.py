import pygame
import sys
import random

#initialize Pygame
pygame.init()

# create a clock object
clock = pygame.time.Clock()

#set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Shooter Game")

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill the screen with black color
    screen.fill((0, 0, 0))

    #update the display
    pygame.display.flip()

    #cap the frame rate at 60 frames per second
    clock.tick(60)

    # player settings
    player_width = 50
    player_height = 60
    player_x = screen_width // 2 - player_width // 2
    player_y = screen_height - player_height - 10
    player_speed = 5

    #main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFY] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        #fill the screen with black
        screen.fill((0, 0, 0))

        #draw the player 
        pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

        #update the display
        pygame.display.flip()

        #cap the frame rate at 60 frames per second
        clock.tick(60)

        #bullet settings
        bullet_width = 5
        bullet_height = 10
        bullet_speed = 7
        bullets = []

        #main game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #create a bullet at  the current player position
                        bullet_x = player_x + player_width // 2 - bullet_width // 2
                        bullet_y = player_y
                        bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))


            #handle player movement
            keys = pygame.ley.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
                player_x += player_speed

            #update bullet positions
            for bullet in bullets:
                bullet.y -= bullet_speed

            #remove bullets that off the screen
            bullets = [bullet for bullet in bullets if bullet.y > 0]

            #fill the screen with black
            screen.fill((0, 0, 0))

            #draw the player
            pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

            # Draw the bullets
            for bullet in bullets:
                pygame.draw.rect(screen, (255, 255, 255), bullet)

            #update the display
            pygame.display.flip()

            #cap the fram rate at 60 frames per second
            clock.tick(60)

            #enemy settings
            enemy_width = 50
            enemy_height = 60
            enemy_speed = 2
            enemies = []

            #spawn an enemy every 2 seconds
            enemy_timer = 0
            enemy_spawn_time = 2000

            #main game loop
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            bullet_x = player_x + player_width // 2 - bullet_width // 2
                            bullet_y = player_y
                            bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

                #handle player movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and player_x > 0:
                    player_x -= player_speed
                if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
                    player_x += player_speed

                #update bullet positions
                for bullet in bullets:
                    bullet.y -= bullet_speed
                bullets = [bullet for bubllet in bullets if bullet.y > 0]

                #update enemy positions and spawn new ones
                current_time = pygame.time.get_ticks()
                if current_time - enemy_timer > enemy_spawn_time:
                    enemy_x = random.randint(0, screen_width - enemy_width)
                    enemy_y = -enemy_height
                    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
                    enemy_timer = current_time

                for enemy in enemies:
                    enemy.y += enemy_speed

                #remove enemies that are off the screen
                enemies = [enemy for enemy in enemies if enemy.y < screen_height]

                #fill the screen with black
                screen.fill((0, 0, 0))

                #draw the player
                pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

                #draw the bullets
                for bullet in bullets:
                    pygame.draw.rect(screen, (255, 255, 255), bullet)

                #draw the enemies
                for enemy in enemies:
                    pygame.draw.rect(screen, (255, 0, 0), enemy)

                #update the display
                pygame.display.flip()

                #cap the frame rate at 60 frames per second
                clock.tick(60)

                #function for detecting collisions
                def check_collision(rect1, rect2):
                    return rect1.colliderect(rect2)
                
                #main game loop
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                bullet_x = player_x + player_width // 2 - bullet_width // 2
                                bullet_y = player_y
                                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))


                    #handle player movement
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT] and player_x > 0:
                        player_x -= player_speed
                    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
                        player_x += player_speed

                    #update bullet positions
                    for bullet in bullets:
                        bullet.y -= bullet_speed
                    bullets = [bullet for bullet in bullets if bullet.y > 0]

                    #update enemy positinos and spawn new ones
                    current_time = pygame.time.get_ticks()
                    if current_time - enemy_timer > enemy_spawn_time:
                        enemy_x = random.randint(0, screen_width - enemy_width)
                        enemy_y = -enemy_height
                        enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
                        enemy_timer = current_time

                    for enemy in enemies:
                        enemy.y += enemy_speed

                    #check for collisions
                    for bullet in bullets[:]:
                        for enemy in enemies[:]:
                            if check_collision(bullet, enemy):
                                bullets.remove(bullet)
                                enemies.remove(enemy)
                                break


                    #remove off-screen enemies
                    enemies = [enemy for enemy in enemies if enemy.y < screen_height]

                    #fill the screen with black
                    screen.fill((0, 0, 0))

                    #draw the player
                    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

                    #draw the enemies
                    for enemy in enemies:
                        pygame.draw.rect(screen, (255, 0, 0), enemy)

                    #update the display
                    pygame.display.flip()

                    #cap the frame rate at 60 frames per second
                    clock.tick(60)




