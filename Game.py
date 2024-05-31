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
green_tank_width = 4

red_tank_x = 600
red_tank_y = 200
red_tank_width = 4

# make the tank
green_tank =pygame.image.load("green_tank(1).png")
green_tank_rect = green_tank.get_rect()
green_tank.center = screen.get_rect().center
print(green_tank_rect)
red_tank =pygame.image.load("red_tank.png")
red_tank_rect = red_tank.get_rect()
red_tank.center = screen.get_rect().center
print(red_tank_rect)
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
    pygame.draw.rect(screen, (100, 0, 0), green_tank_rect, green_tank_width)  # draw hit-box
    pygame.draw.rect(screen, (100, 0, 0), red_tank_rect, red_tank_width)  # draw hit-box

    for event in pygame.event.get():
        if event.type == pygame.K_LEFT and red_tank_x > 0:
            red_tank_x -= 10
        if event.type == pygame.K_RIGHT and red_tank_x < 0:
            red_tank_x += 1
        if event.type == pygame.K_a and green_tank_x > 0:
            green_tank_x -= 10
        if event.type == pygame.K_d and green_tank_x < 0:
            green_tank_x += 10
        

    

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
