#This is where all the game code will be

#Tanks:

#Physics engine: Gravity and power

#Be able to move tanks left and right

#Menu system -> Adjust power, angle, type of gun etc

#Settings/preferences: Music On/Off

#Get points for killing

#Random terrain generation (For later)

#Shop -> Buy powerups, new weapons, skins (colors, do later)

# pygame template

import pygame


pygame.init()

WIDTH = 600
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
white = (255,255,255) 
lightcolor = (170,170,170)  
dark = (100,100,100) 

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
width = screen.get_width() 
height = screen.get_height() 
import math

# ---------------------------
# Initialize global variables

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

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
    
    pygame.quit()


main()


