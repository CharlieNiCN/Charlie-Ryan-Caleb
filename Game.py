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
import math

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200

#Bullet trajectory function
def bullet(inputAngle, inputPower):
    gravConstant = 20
    inputAngle = math.radians(inputAngle) #input angle (x) 0<x<90 #these are the variables to control the power, angle of fireing, and the strength of gravity 
    x = 0.0
    y = 0.0
    while y>=0: #displays the equation (use this later on for mapping the trajectory of the bullet)
        y= (x*math.tan(inputAngle))-(gravConstant*x*x)/(2*inputPower*inputPower*math.cos(inputAngle)*math.cos(inputAngle)) #the physics projective equation (pull this up for the video)
        x+=1 
        print("(",x,",", y,")")

def main():
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





main()


