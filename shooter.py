import pygame
import sys

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

