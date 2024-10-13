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