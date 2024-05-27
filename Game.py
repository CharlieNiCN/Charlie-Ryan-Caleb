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

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
{
   "style_name": "green_tank",
   "images": [
      "green_tank.png"
   ],
   "orientation": "vertical",
   "padding": 5,
   "custom_styles": {
      "display": "inline-block"
   },
   "stylesheet": "css",
   "path_prefix": "",
   "output": "png",
   "enable_cache_busting": true
}

# ---------------------------
#speed 
vel = 10 


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

    pygame.draw.rectangle(screen, (0, 0, 255), (1, 0), 30)

keys = pygame.key.get_pressed() 
      
    # if left arrow key is pressed 
if keys[pygame.K_LEFT] and circle_x>0: 
          
        # decrement in x co-ordinate 
        circle_x -= vel 
          
    # if left arrow key is pressed 
if keys[pygame.K_RIGHT] and circle_x<500-WIDTH: 
          
        # increment in x co-ordinate 
        circle_x += vel 
         
    # if left arrow key is pressed    
if keys[pygame.K_UP] and circle_y>0: 
          
        # decrement in y co-ordinate 
        circle_y -= vel 
              # if left arrow key is pressed    
if keys[pygame.K_DOWN] and circle_y<500-HEIGHT: 
        # increment in y co-ordinate 
        circle_y += vel 
    # Must be the last two lines
    # of the game loop
pygame.display.update()
pygame.display.flip()
clock.tick(30)
    #---------------------------


pygame.quit()
