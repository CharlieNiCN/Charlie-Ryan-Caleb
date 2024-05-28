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

# Initialize Pygame
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


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
        if self.rect.left < 0 or self.rect.right > WIDTH or self.rect.bottom > HEIGHT:
            self.kill()  # Remove the sprite from all groups

# Sprite group
all_sprites = pygame.sprite.Group()
sprite = Bullet(WIDTH // 2, HEIGHT // 2, 5, -10)  # Initial position and velocity
all_sprites.add(sprite)


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

   if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                game_loop()
            if settings_button.collidepoint(event.pos):
                settings_menu()
            if shop_button.collidepoint(event.pos):
                shop_menu()
            if inventory_button.collidepoint(event.pos):
                inventory_menu()
            keys = pygame.key.get_pressed() 

        font = pygame.font.SysFont(None, 55)
        button_font = pygame.font.SysFont(None, 40)

        screen.fill((255, 255, 255))  # always the first drawing command
        draw_Button('Main Menu', font, dark, screen, Width // 2 - 100, Height // 4)
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

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
    
    pygame.quit()

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
        main()
        


main()


