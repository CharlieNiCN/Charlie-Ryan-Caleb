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
# Initialize Pygame

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

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def draw_Button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def inventory_menu():
    running = True
    while running:
        for Py_Event in pygame.event.get():
            if (Py_Event.type == pygame.QUIT):
                running = False
            screen.fill(white)
            #inventory menu 

            pygame.display.flip()
            clock.tick(30)
            
def settings_menu():
    running = True
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                running = False
                main()

        screen.fill(white)
    #setting

        pygame.display.flip()
        clock.tick(30)
    

def shop_menu():
    running = True
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                running = False
                main()

        screen.fill(white)
      #shop

        pygame.display.flip()
        clock.tick(30) 
def game_loop():
    running = True
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                running = False
                main()
        screen.fill(white)
        # put game code here
        pygame.display.flip()
        clock.tick(30)

# Sprite class for the bullet 
class Bullet(pygame.sprite.Sprite): #MUST CHANGE LATER AND UPDATE
    def __init__(self, x, y, vx, vy): #x,y are starting position, vx,vy is the speed in x and y
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        self.gravity = 0.5 #gravity

    def update(self):
        # Update velocity with gravity
        self.vy += self.gravity

        # Update the position based on velocity
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Boundary checking to keep the sprite within the screen
        if self.rect.left < 0 or self.rect.right > Width or self.rect.bottom > Height:
            self.kill()  # Remove the sprite from all groups

all_sprites = pygame.sprite.Group()

def main():
    running = True
    play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 50)
    settings_button = pygame.Rect(Width // 2 - 100, Height // 2 - 30, 200, 50)
    shop_button = pygame.Rect(Width // 2 - 100, Height // 2 + 40, 200, 50)
    inventory_button = pygame.Rect(Width // 2 - 100, Height // 2 + 110, 200, 50)

    while running:
    # EVENT HANDLING

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Spawn a new sprite at the mouse click position
                mouse_x, mouse_y = event.pos
                vx = 5  # Set initial horizontal velocity (+ means going right, - means left)
                vy = -10  # Set initial vertical velocity (- means going up, + means going down)
                sprite = Bullet(mouse_x, mouse_y, vx, vy)
                all_sprites.add(sprite)
                print('Bullet spawned at:', mouse_x, mouse_y)


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
        

    
=======
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

        screen.fill((255, 255, 255))  # always the first drawing command
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
        pygame.display.flip()


     pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)


  
     all_sprites.update()

     pygame.display.flip()  # Flip the display
     clock.tick(30)  # Cap the frame rate
   
   pygame.quit()
main()