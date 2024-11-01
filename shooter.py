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

#player settings
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

#bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

#enemy settings
enemy_width = 50
enemy_height = 60
enemy_speed = 2
enemies = []
enemy_spawn_time = 2000 #2s
enemy_timer = pygame.time.get_ticks()

#function to detect collisions
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

#main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                # Create a bullet at the current player position
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

  
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    
    # Update bullet positions and remove off-screen bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet.y > 0]

    
    # Spawn new enemies at intervals
    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height
        enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
        enemy_timer = current_time

    
    # Update enemy positions and remove off-screen enemies
    for enemy in enemies:
        enemy.y += enemy_speed
    enemies = [enemy for enemy in enemies if enemy.y < screen_height]

    
    # Check for collisions between bullets and enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    
    # Fill the screen with black
    screen.fill((0, 0, 0))

    
    # Draw the player
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))

    
    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    
    # Draw the enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

   
    # Update the display
    pygame.display.flip()

    
    # Cap the frame rate at 60 frames per second
    clock.tick(60)



