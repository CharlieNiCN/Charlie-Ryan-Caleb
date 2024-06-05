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
pygame.mixer.init()
pygame.mixer.music.load('Duality.mp3')

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
#green_tank =pygame.image.load("green_tank(1).png")
#green_tank_rect = green_tank.get_rect()
#green_tank.center = screen.get_rect().center
#print(green_tank_rect)
#red_tank =pygame.image.load("red_tank.png")
#red_tank_rect = red_tank.get_rect()
#red_tank.center = screen.get_rect().center
#print(red_tank_rect)


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
powerUpRNG = 0

def main():
    global bullet, powerup
    running = True
    play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 50)
    settings_button = pygame.Rect(Width // 2 - 100, Height // 2 - 30, 200, 50)
    shop_button = pygame.Rect(Width // 2 - 100, Height // 2 + 40, 200, 50)
    inventory_button = pygame.Rect(Width // 2 - 100, Height // 2 + 110, 200, 50)
    screen.fill((255, 255, 255))  # always the first drawing command
    # pygame.draw.rect(screen, (100, 0, 0), green_tank_rect, green_tank_width)  # draw hit-box
    # pygame.draw.rect(screen, (100, 0, 0), red_tank_rect, red_tank_width)  # draw hit-box

    pygame.mixer.music.play(-1)
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
                powerUpNum += 1
            if event.type == pygame.K_LEFT and red_tank_x > 0:
                red_tank_x -= 10
            if event.type == pygame.K_RIGHT and red_tank_x < 0:
                red_tank_x += 1
            if event.type == pygame.K_a and green_tank_x > 0:
                green_tank_x -= 10
            if event.type == pygame.K_d and green_tank_x < 0:
                green_tank_x += 10



    

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



  


