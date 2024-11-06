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
player_health = 3

#bullet settings
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

#colors
white = (255, 255, 255)
blue = (0, 128, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (169, 169, 169)

#load sound effects
shoot_sound = pygame.mixer.Sound('assets/shoot.mp3')
explosion_sound = pygame.mixer.Sound('assets/explosion.mp3')
background_music = pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.play(-1) #play background music on loop

#fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

#enemy settings
enemy_width = 50
enemy_height = 60
enemy_speed = 2
enemies = []
enemy_spawn_time = 2000 #2s
enemy_timer = pygame.time.get_ticks()

#score
score = 0

#function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


#function to detect collisions
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

#game over function
def game_over():
    while True:
        screen.fill(black)
        draw_text("GAME OVER", game_over_font, red, screen, screen_width // 2, screen_height // 2 - 50)
        draw_text(f"Final Score: {score}", font, white, screen, screen_width // 2, screen_height // 2 + 20)
        draw_text("Play Again", font, gray, screen, screen_width // 2, screen_height // 2 + 100)
    
        #check for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                #check if the "Play Again" button is clicked
                if (screen_width // 2 - 50 <= mouse_x <= screen_width // 2 + 50) and (screen_height // 2 + 80 <= mouse_y <= screen_height // 2 + 120):
                    main() #restart the game
        pygame.display.flip()
        clock.tick(60)

#main game function
def main():
    #declare global variables
    global score, player_health, bullets, enemy_timer, enemies
    #declare player position and speed as global
    global player_x, player_y, player_speed  
    #reset the game variables
    score = 0
    player_health = 3 
    bullets = [] #reset bullets list
    enemies = [] #reset enemies list
    enemy_timer = pygame.time.get_ticks() #reset enemy timer to current time

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

    
        #handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        
        #update bullet positions and remove off-screen bullets
        for bullet in bullets:
            bullet.y -= bullet_speed
        bullets = [bullet for bullet in bullets if bullet.y > 0]

        
        #spawn new enemies at intervals
        current_time = pygame.time.get_ticks()
        if current_time - enemy_timer > enemy_spawn_time:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = -enemy_height
            enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
            enemy_timer = current_time

        
        #update enemy positions and remove off-screen enemies
        for enemy in enemies:
            enemy.y += enemy_speed
        enemies = [enemy for enemy in enemies if enemy.y < screen_height]

        
        #check for collisions between bullets and enemies
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if check_collision(bullet, enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    explosion_sound.play()
                    score += 10
                    break
        
        #check for collisions betwen player and enemies
        for enemy in enemies[:]:
            if check_collision(enemy, pygame.Rect(player_x, player_y, player_width, player_height)):
                enemies.remove(enemy)
                explosion_sound.play()
                player_health -= 1
                if player_health <= 0:
                    game_over()
        
        #fill the screen with black
        screen.fill((0, 0, 0))

        
        #draw the player
        pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))

        
        #draw the bullets
        for bullet in bullets:
            pygame.draw.rect(screen, white, bullet)

        
        #draw the enemies
        for enemy in enemies:
            pygame.draw.rect(screen, red, enemy)

        
        #draw score and health
        draw_text(f"Score: {score}", font, white, screen, 70, 30)
        draw_text(f"Health: {player_health}", font, white, screen, screen_width - 100, 30)
        
        #update the display
        pygame.display.flip()

        
        #cap the frame rate at 60 frames per second
        clock.tick(60)

    pygame.quit()
    sys.exit()

#run the game
main()