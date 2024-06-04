

#This is where all the game code will be
#Tanks:
#Physics engine: Gravity and power
#Be able to move tanks left and right
#Menu system -> Adjust power, angle, type of gun etc
#Settings/preferences: Music On/Off
#Get points for killing
#Random terrain generation (For later)
#Shop -> Buy powerups, new weapons, skins (colors, do later)

import pygame
import math
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random
# Initialize Pygame

pygame.init()

Width = 640
Height = 480
SIZE = (Width, Height)
white = (255, 255, 255)
black = (0, 0, 0)
lightcolor = (170, 170, 170)
dark = (100, 100, 100)
scores = []

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


circle_x = 65
circle_y = 220
circle_rad = 70

rect_x = 0
rect_y = 200

circle1_x = 200
circle1_y = 270
circle1_rad = 70

rect1_x = 250
rect1_y = 250

circle2_x = 500
circle2_y = 290
circle2_rad = 100

rect3_x = 500
rect3_y = 190

rect4_x = -120
rect4_y = 149
# ---------------------------

# make floor
floor = (circle_x, circle_y)
floor_1 = pygame.Rect(rect_x , rect_y, 200, 500)
floor_2 = (circle1_x, circle1_y)
floor_3 = pygame.Rect(rect1_x, rect1_y, 200, 500)
floor_4 = (circle2_x, circle2_y)
floor_5 = pygame.Rect(rect3_x, rect3_y, 200, 500)
floor_6 = pygame.Rect(rect4_x, rect4_y, 190, 1000)


# collisions
def green_tank_circle_collision(floor, circle_rad, green_tank):
    green_tank_center = (green_tank_x, green_tank_y)
    distance = math.hypot(green_tank_center[0] - floor[0], green_tank_center[1] - floor[1])
    return distance < 70 + green_tank_width // 2

def green_tank_circle2_collision(floor_2, circle1_rad, green_tank):
    green_tank_center = (green_tank_x, green_tank_y)
    distance = math.hypot(green_tank_center[0] - floor_2[0], green_tank_center[1] - floor_2[1])
    return distance < 70 + green_tank_width // 2

def green_tank_circle3_collision(floor_4, circle2_rad, green_tank):
    green_tank_center = (green_tank_x, green_tank_y)
    distance = math.hypot(green_tank_center[0] - floor_4[0], green_tank_center[1] - floor_4[1])
    return distance < 70 + red_tank_width // 2

def red_tank_circle_collision(floor, circle_rad, red_tank):
    red_tank_center = (red_tank_x, red_tank_y)
    distance = math.hypot(red_tank_center[0] - floor[0], red_tank_center[1] - floor[1])
    return distance < 70 + red_tank_width // 2

def red_tank_circle2_collision(floor_2, circle1_rad, red_tank):
    red_tank_center = (red_tank_x, red_tank_y)
    distance = math.hypot(red_tank_center[0] - floor_2[0], red_tank_center[1] - floor_2[1])
    return distance < 70 + red_tank_width // 2

def red_tank_circle3_collision(floor_4, circle2_rad, red_tank):
    red_tank_center = (red_tank_x, red_tank_y)
    distance = math.hypot(red_tank_center[0] - floor_4[0], red_tank_center[1] - floor_4[1])
    return distance < 70 + red_tank_width // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_Button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Sprite class for the bullet 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):  # x,y are starting position, vx,vy is the speed in x and y
        super().__init__()
        self.radius = 5
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        pygame.draw.circle(self.image, black, (self.radius, self.radius), self.radius)  # Draw a black circle
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        self.gravity = 0.5  # gravity

    def update(self):
        global bullet
        self.vy += self.gravity

        # Update the position based on velocity
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Boundary checking to keep the sprite within the screen
        if self.rect.left < -self.radius or self.rect.right > Width + self.radius or self.rect.bottom > Height + self.radius:
            self.kill()  # Remove the sprite from all groups
            bullet = None

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  # Green color for the power-up
        self.rect = self.image.get_rect(center=(x, y))
        self.vy = 2  # Slow falling speed

    def update(self):
        global powerup
        # Update the position based on velocity
        self.rect.y += self.vy

        # Stop moving when it touches the ground
        if self.rect.bottom >= Height:
            self.rect.bottom = Height
            self.vy = 0  # Stop the vertical velocity
            powerup = None

all_sprites = pygame.sprite.Group()
bullet = None  # Variable to track the bullet
powerupNum = 0  # Variable to track the # of power-ups on the board


def main():
    global bullet, powerup
    running = True
    play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 50)
    settings_button = pygame.Rect(Width // 2 - 100, Height // 2 - 30, 200, 50)
    shop_button = pygame.Rect(Width // 2 - 100, Height // 2 + 40, 200, 50)
    inventory_button = pygame.Rect(Width // 2 - 100, Height // 2 + 110, 200, 50)
    screen.fill((255, 255, 255))  # always the first drawing command
    pygame.draw.rect(screen, (100, 0, 0), green_tank_rect, green_tank_width)  # draw hit-box
    pygame.draw.rect(screen, (100, 0, 0), red_tank_rect, red_tank_width)  # draw hit-box

    while running:
        powerUpRNG = random.randint(1,30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and bullet is None:
                mouse_x, mouse_y = event.pos
                vx = 5  # Set initial horizontal velocity (+ means going right, - means left)
                vy = -10  # Set initial vertical velocity (- means going up, + means going down)
                bullet = Bullet(mouse_x, mouse_y, vx, vy)
                all_sprites.add(bullet)
                print('Bullet spawned at:', mouse_x, mouse_y)
            elif powerUpRNG == 1 and powerupNum <= 3:
                powerup = PowerUp(random.randint(0, 640), 0)
                all_sprites.add(powerup)
                powerUpRng += 1
            if event.type == pygame.K_LEFT and red_tank_x > 0:
                red_tank_x -= 10
            if event.type == pygame.K_RIGHT and red_tank_x < 0:
                red_tank_x += 1
            if event.type == pygame.K_a and green_tank_x > 0:
                green_tank_x -= 10
            if event.type == pygame.K_d and green_tank_x < 0:
                green_tank_x += 10

        screen.fill((140, 170, 255))  # always the first drawing command

        pygame.draw.circle(screen, (0, 100, 0), (circle_x, circle_y), circle_rad)
        pygame.draw.rect(screen, (0, 100, 0), (rect_x, rect_y, 200, 500), 200)
        pygame.draw.rect(screen, (0, 100, 0), (rect1_x, rect1_y, 200, 500), 200)
        pygame.draw.circle(screen, (0, 100, 0), (circle1_x, circle1_y), circle1_rad)
        pygame.draw.circle(screen, (0, 100, 0), (circle2_x, circle2_y), circle2_rad)
        pygame.draw.rect(screen, (0, 100, 0), (rect3_x, rect3_y, 200, 500), 20)
        pygame.draw.rect(screen, (0, 100, 0), (rect4_x, rect4_y, 190, 1000), 100)


        if green_tank.colliderect(floor_1):
            green_tank_y = floor_1.top - green_tank.height
        if green_tank.colliderect(floor_3):
            green_tank_y = floor_3.top - green_tank.height
        if green_tank.colliderect(floor_5):
            green_tank_y = floor_5.top - green_tank.height
        if green_tank.colliderect(floor_6):
            green_tank_y = floor_6.top - green_tank.height



        if red_tank.colliderect(floor_1):
            red_tank_y = floor_1.top - red_tank.height
        if red_tank.colliderect(floor_3):
            red_tank.y = floor_3.top - red_tank.height
        if red_tank.colliderect(floor_5):
            red_tank_y = floor_5.top - red_tank.height
        if red_tank.colliderect(floor_6):
            red_tank_y = floor_6.top - red_tank.height

    

        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    if play_button.collidepoint(event.pos):
    #                game_loop()
        #    if settings_button.collidepoint(event.pos):
      #              settings_menu()
        #    if shop_button.collidepoint(event.pos):
      #              shop_menu()
        #    if inventory_button.collidepoint(event.pos):
      #              inventory_menu()
            keys = pygame.key.get_pressed() 

        font = pygame.font.SysFont(None, 55)
        button_font = pygame.font.SysFont(None, 40)

        draw_Button('Main Menu', font, dark, screen, Width // 2 - 100, Height // 4 - 40)
        draw_Button('Tanks', font, dark, screen, Width // 2 - 50, Height // 4 - 70)
 # drawing the buttons
        pygame.draw.rect(screen, lightcolor, play_button)
        draw_Button('Play', font, dark, screen, play_button.x + 50, play_button.y + 10) 
        pygame.draw.rect(screen, lightcolor, settings_button)
        draw_Button('Settings', font, dark, screen, settings_button.x + 25, settings_button.y + 10)        
        pygame.draw.rect(screen, lightcolor, shop_button)
        draw_Button('Shop', font, dark, screen, shop_button.x + 50, shop_button.y + 10)      
        pygame.draw.rect(screen, lightcolor, inventory_button)
        draw_Button('Inventory', font, dark, screen, inventory_button.x + 25, inventory_button.y + 10)    
        
        
        
        #end code (MUST BE PUT AT THE BACK)
        screen.fill(white)  # Clear the screen
        all_sprites.update()  # Update all sprites
        all_sprites.draw(screen)  # Draw all sprites
        pygame.display.flip()  # Flip the display
        clock.tick(30)  # Cap the frame rate

    pygame.quit()

main()



  


