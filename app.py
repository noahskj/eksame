import pygame as pg
import random

# Initialize Pygame
pg.init()

# Define the window size
win_width = 768
win_height = 504

# Define the camera size
camera_width = 400
camera_height = 300

# Create the Pygame window
win = pg.display.set_mode((win_width, win_height))

# Set the window title
pg.display.set_caption("Lord of the QuarterPoundMac")

#musicussy
pg.mixer.pre_init(44100, 32, 2, 1024)
pg.mixer.init()
pg.mixer.music.load("ring.wav")
pg.mixer.music.play(1)
pg.mixer.music.queue("hammer.mp3")
pg.mixer.music.play(loops = 1)

# Define the player sprite and starting position
player_img = pg.image.load("player.png")
player_x = 50
player_y = 50

# Define the enemy sprite and starting position
enemy_img = pg.image.load("enemy.png")
enemy_x = random.randint(0, win_width - enemy_img.get_width())
enemy_y = random.randint(0, win_height - enemy_img.get_height())

# Define the player's movement speed
move_speed = 0.1
enemy_speed = 1

# Define the camera position
camera_x = player_x - camera_width/2
camera_y = player_y - camera_height/2

# Define the background image and its position
bg = pg.image.load("bg.png")
bg_x = 0
bg_y = 0

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

    # Move the enemy randomly
    enemy_dir = random.choice(["left", "right", "up", "down"])
    if enemy_dir == "left":
        enemy_x -= enemy_speed
    elif enemy_dir == "right":
        enemy_x += enemy_speed
    elif enemy_dir == "up":
        enemy_y -= enemy_speed
    elif enemy_dir == "down":
        enemy_y += enemy_speed

    # Keep the enemy within the screen bounds
    if enemy_x < 0:
        enemy_x = 0
    elif enemy_x > win_width - enemy_img.get_width():
        enemy_x = win_width - enemy_img.get_width()
    if enemy_y < 0:
        enemy_y = 0
    elif enemy_y > win_height - enemy_img.get_height():
        enemy_y = win_height - enemy_img.get_height()

    # Check for collision between player and enemy
    if (player_x + player_img.get_width() > enemy_x and player_x < enemy_x + enemy_img.get_width()
        and player_y + player_img.get_height() > enemy_y and player_y < enemy_y + enemy_img.get_height()):
        # Player touched the enemy, do something
        print("Player touched the enemy!")

    # Update the camera position to follow the player
    camera_x = player_x - camera_width/2
    camera_y = player_y - camera_height/2

    # Limit the camera position to prevent going outside the background image
    if camera_x < 0:
        camera_x = 0
    elif camera_x > bg.get_width() - camera_width:
        camera_x = bg.get_width() - camera_width
    if camera_y < 0:
        camera_y = 0
    elif camera_y > bg.get_height() - camera_height:
        camera_y = bg.get_height() - camera_height

    # Check for collision between player and enemy
    player_rect = player_img.get_rect(topleft=(player_x, player_y))
    enemy_rect = enemy_img.get_rect(topleft=(enemy_x, enemy_y))
    if player_rect.colliderect(enemy_rect):
        print("Game over!")
        

# Update the background position based on the camera position
    bg_x = -camera_x
    bg_y = -camera_y

# Redraw the screen
    win.blit(bg, (bg_x, bg_y))
    win.blit(enemy_img, (enemy_x, enemy_y))
    win.blit(player_img, (player_x - camera_x, player_y - camera_y))
    pg.display.update()
pg.quit()