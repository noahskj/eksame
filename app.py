import pygame as pg

# Initialize Pygame
pg.init()

# Define the window size
win_width = 768
win_height = 504

# Define the camera size
camera_width = 384
camera_height = 252

# Create the Pygame window
win = pg.display.set_mode((win_width, win_height))

# Set the window title
pg.display.set_caption("Legend of Jeff")

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
bg = pg.image.load("background.png")
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

    # Update the background position based on the camera position
    bg_x = -camera_x
    bg_y = -camera_y

    # Redraw the screen
    win.blit(bg, (bg_x, bg_y))
    win.blit(player_img, (player_x - camera_x, player_y - camera_y))
    pg.display.update()

# Quit Pygame
pg.quit()