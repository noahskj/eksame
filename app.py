import pygame as pg

# Initialize Pygame
pg.init()

# Define the window size
win_width = 800
win_height = 600

# Create the Pygame window
win = pg.display.set_mode((win_width, win_height))

# Set the window title
pg.display.set_caption("Legend of Jeff")

# Define the player sprite
player_img = pg.image.load("player.png")
player_x = 50
player_y = 50

# Define the player's movement speed
move_speed = 0.1

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

    # Redraw the screen
    win.fill((255, 255, 255))
    win.blit(player_img, (player_x, player_y))
    pg.display.update()

# Quit Pygame
pg.quit()
