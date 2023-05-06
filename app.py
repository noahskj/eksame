import pygame as pg
import random
from enemy import Enemy

# Initialize Pygame
pg.init()

# Define the window size
win_width = 768
win_height = 504

# Define the camera size
camera_width = 768
camera_height = 504

# Create the Pygame window
win = pg.display.set_mode((win_width, win_height))

# Set the window title
pg.display.set_caption("Lord of the QuarterPoundMac")

# Define the player sprite and starting position
player_img = pg.image.load("player.png")
player_x = 50
player_y = 50

# Define the player's movement speed
move_speed = 0.1

# Define the camera position
camera_x = player_x - camera_width/2
camera_y = player_y - camera_height/2

# Define the background image and its position
bg = pg.image.load("bg.png")
bg_x = 0
bg_y = 0

# Create a list to hold the enemies and bullets
enemies = []
bullets = []

# Define the time interval between shots (in milliseconds)
SHOT_DELAY = 500

# Define a timer to keep track of the time since the last shot
shot_timer = 0

#musicussy
pg.mixer.pre_init(44100, 32, 2, 1024)
pg.mixer.init()
pg.mixer.music.load("ring.wav")
pg.mixer.music.play()
pg.mixer.music.queue("hammer.mp3")
pg.mixer.music.play(loops = 1)

# Create x enemy objects and add them to the list
for i in range(3):
    enemy_img = pg.image.load("enemy.png")
    enemy = Enemy(random.randint(0, win_width - enemy_img.get_width()), random.randint(0, win_height - enemy_img.get_height()), enemy_img)
    enemies.append(enemy)

# Define the game loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Move the player based on user input
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_x -= move_speed
    if keys[pg.K_RIGHT]:
        player_x += move_speed
    if keys[pg.K_UP]:
        player_y -= move_speed
    if keys[pg.K_DOWN]:
        player_y += move_speed

 # Handle shooting by the player

    if keys[pg.K_z] or keys[pg.K_x]:
        # Check if enough time has elapsed since the last shot
        time_since_last_shot = pg.time.get_ticks() - shot_timer
        if time_since_last_shot >= SHOT_DELAY:
            # Create a new bullet object and add it to the list of bullets
            if keys[pg.K_z]:
                bullet_velocity = (-2, 0) # Shoot left
            else:
                bullet_velocity = (2, 0) # Shoot right
            bullet = {"rect": pg.Rect(player_x + player_img.get_width()/2, player_y + player_img.get_height()/2, 8, 8),
                    "velocity": bullet_velocity}
            bullets.append(bullet)
    
            # Reset the shot timer
            shot_timer = pg.time.get_ticks()
  
    # Move the bullets
    for bullet in bullets:
        bullet["rect"].move_ip(*bullet["velocity"])

        # Remove the bullet if it goes out of screen
        if bullet["rect"].top < 0:
            bullets.remove(bullet)

    # Move the enemies
    for enemy in enemies:
        enemy.move()

        # Keep the enemy within the screen bounds
        if enemy.rect.x < 0:
            enemy.rect.x = 0
        elif enemy.rect.x > win_width - enemy.rect.width:
            enemy.rect.x = win_width - enemy.rect.width
        if enemy.rect.y < 0:
            enemy.rect.y = 0
        elif enemy.rect.y > win_height - enemy.rect.height:
            enemy.rect.y = win_height - enemy.rect.height

        # Handle collision between player and enemy
        if player_img.get_rect().colliderect(enemy.rect):
            print("ow, my nuts")

        # Handle collision between bullet and enemy
        for bullet in bullets:
            if enemy.rect.colliderect(bullet["rect"]):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Update the camera position
    camera_x = player_x - camera_width/2
    camera_y = player_y - camera_height/2
    # Draw the background and sprites to the screen
    win.blit(bg, (bg_x - camera_x, bg_y - camera_y))
    win.blit(player_img, (player_x - camera_x, player_y - camera_y))

    # Draw the enemies to the screen
    for enemy in enemies:
        win.blit(enemy.img, (enemy.rect.x - camera_x, enemy.rect.y - camera_y))

    # Draw the bullets to the screen
    for bullet in bullets:
        bullet_img = pg.image.load("bullet.png")
        win.blit(bullet_img, (bullet["rect"].x - camera_x, bullet["rect"].y - camera_y))


    # Update the display
    pg.display.update()

pg.quit()
