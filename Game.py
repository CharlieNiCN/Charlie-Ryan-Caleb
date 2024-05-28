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


# ---------------------------
# Initialize global variables

# ---------------------------


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

running = True
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

    # GAME STATE UPDATES
    all_sprites.update()

    # DRAW
    screen.fill(BLACK)  # Clear the screen
    all_sprites.draw(screen)  # Draw all sprites

    pygame.display.flip()  # Flip the display
    clock.tick(30)  # Cap the frame rate

pygame.quit()






