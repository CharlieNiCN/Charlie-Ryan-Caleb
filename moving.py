# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

green_tank_x = 200
green_tank_y = 200

# make the tank
green_tank =pygame.image.load("green_tank.png")
green_tank_rect = green_tank.get_rect()
green_tank.center = screen.get_rect().center
print(green_tank_rect)
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.rect(screen, (100, 0, 0), green_tank_rect, 2)  # draw hit-box
    keys = pygame.key.get_pressed()
    if keys[119] == True:  # w
        green_tank_y -= 10

    if keys[97] == True:  # a
        green_tank_x -= 10

    if keys[115] == True:  # s
        green_tank_y += 10

    if keys[100] == True:  # d
        green_tank_x += 10

    

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()