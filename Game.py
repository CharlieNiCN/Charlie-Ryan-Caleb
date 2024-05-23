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

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
white = (255,255,255) 
lightcolor = (170,170,170)  
dark = (100,100,100) 

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
width = screen.get_width() 
height = screen.get_height() 

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.rect(screen,dark,[width - 500,height - 350,240,80]) 
    mouse = pygame.mouse.get_pos()
#    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        
    pygame.display.flip()

    clock.tick(30)
    #---------------------------


pygame.quit()
