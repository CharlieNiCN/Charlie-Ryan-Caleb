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
from pygame import event
import json




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
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,120,0)
Yellow= (255,255,0)
Purple = (160,30,240)
Orange = (230,160,0)
black = (0, 0, 0)
lightcolor = (170, 170, 170)
dark = (100, 100, 100)
playerTurnNum=0
scores = []

background_image_path = "TanksBackround.jpg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (Width, Height))

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

green_tank_x = 200
green_tank_y = 200
green_tank_width = 4
greenFuel = 0
greenHealth = 3
green_tank_height = 3


red_tank_x = 600
red_tank_y = 200
red_tank_width = 4

redFuel = 0
redHealth = 3

red_tank_height = 3


# make the tank
green_tank =pygame.image.load("green_tank.png")
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

def load_progress():
    global coins, next_power_up, Inventory_power_ups, power_up_prices
    try:
        with open("progress.json", "r") as file:
            progress = json.load(file)
            coins = progress.get("coins", 100)
            next_power_up = progress.get("next_power_up", 1)
            Inventory_power_ups = progress.get("Inventory_power_ups", ["Default Damage"])
            power_up_prices = set(progress.get("power_up_prices", [10, 20, 30, 40, 50]))
    except FileNotFoundError:
        coins = 100  # Default to 100 coins if file not found

# Save progress to JSON file
def save_progress():
    progress = {
        "coins": coins,
        "next_power_up": next_power_up,
        "Inventory_power_ups": Inventory_power_ups,
        "power_up_prices": list(power_up_prices)
    }
    with open("progress.json", "w") as file:
        json.dump(progress, file)
        
# make floor
floor = (circle_x, circle_y)
floor_1 = pygame.Rect(rect_x , rect_y, 200, 500)
floor_2 = (circle1_x, circle1_y)
floor_3 = pygame.Rect(rect1_x, rect1_y, 200, 500)
floor_4 = (circle2_x, circle2_y)
floor_5 = pygame.Rect(rect3_x, rect3_y, 200, 500)
floor_6 = pygame.Rect(rect4_x, rect4_y, 190, 1000)

#Menus
def draw_Button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def inventory_menu():
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    colors_inventory = [['Blue', 'Red', 'Green'], ['Yellow', 'Purple', 'Orange']]
    power_ups_inventory = [['Power Up 1', 'Power Up 2', 'Power Up 3'], ['Power Up 4', 'Power Up 5', 'Power Up 6']]
    current_page = 0
    current_bg_color = white  # Initialize with white background
    page_Buttons = [pygame.Rect(Width - 110, 10, 100, 50), pygame.Rect(Width - 310, 10, 160, 50)]  # Moved to the left by another 60 pixels and increased length by 30

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:  # if clicked
                if back_button.collidepoint(Py_Event.pos):  # if back button is clicked on the button area
                    main()  # Goes back to the main menu and method
                if page_Buttons[0].collidepoint(Py_Event.pos):
                    current_page = 0  # Switch to colors page
                if page_Buttons[1].collidepoint(Py_Event.pos):
                    current_page = 1  # Switch to power-ups page
                if current_page == 0:  # Only changes color on the colors page 
                    for i, row in enumerate(colors_inventory):
                        for ii, item in enumerate(row): # loops each item
                            item_button = pygame.Rect(100 + ii * 120, 100 + i * 120, 120, 120) # definted variable to store where the button is
                            if item_button.collidepoint(Py_Event.pos): # if the location of the button is clicked
                                if item == 'Blue': # if it is x color then change background color to x
                                    current_bg_color = Blue
                                elif item == 'Red':
                                    current_bg_color = Red
                                elif item == 'Green':
                                    current_bg_color = Green
                                elif item == 'Yellow':
                                    current_bg_color = Yellow
                                elif item == 'Purple':
                                    current_bg_color = Purple
                                elif item == 'Orange':
                                    current_bg_color = Orange

        screen.fill(current_bg_color) #puts the updated color into the background
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        # Draw the Power-up and Colors buttons
        pygame.draw.rect(screen, dark, page_Buttons[0])
        draw_Button('Skins', back_font, white, screen, page_Buttons[0].x + 10, page_Buttons[0].y + 5)
        pygame.draw.rect(screen, dark, page_Buttons[1])
        draw_Button('Power-Ups', back_font, white, screen, page_Buttons[1].x + 10, page_Buttons[1].y + 5)

        # shows inventory items as buttons this is is chat gpt
        inventory_items = colors_inventory if current_page == 0 else power_ups_inventory
        for i, row in enumerate(inventory_items):
            for ii, item in enumerate(row):
                item_button = pygame.Rect(100 + ii * 120, 100 + i * 120, 120, 120)
                pygame.draw.rect(screen, Blue if item == 'Blue' else Red if item == 'Red' else Green if item == 'Green' else Yellow if item == 'Yellow' else Purple if item == 'Purple' else Orange if item == 'Orange' else dark, item_button)
                draw_Button(item, back_font, white, screen, item_button.x + 12, item_button.y + 35)

        pygame.display.flip()
        clock.tick(30)



def settings_menu():
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    music_on = True  # boolean music off or on
    music_button = pygame.Rect(Width // 2 - 100, Height // 2 - 25, 200, 50) #button location of the music
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    main()  # Goes back to the main menu and method 
                if music_button.collidepoint(Py_Event.pos): #if user clicked on music button
                    music_on = not music_on  # pdate music boolean

        screen.fill(white)
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        #Draw the Title thing on the top that says Settings
        title_font = pygame.font.SysFont('timesnewroman', 55)
        draw_Button('Settings', title_font, dark, screen, Width // 2 - 100, Height // 4 - 70)

        # Draw the music button
        music_text = 'Music: On' if music_on else 'Music: Off'
        pygame.draw.rect(screen, dark, music_button)
        draw_Button(music_text, back_font, white, screen, music_button.x + 10, music_button.y + 10)

        # Settings content

        pygame.display.flip()
        clock.tick(30) 
    

def shop_menu():
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    main()  # Goes back to the main menu and method   

        screen.fill(white)
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        # Shop content

        pygame.display.flip()
        clock.tick(30) 
def game_loop():
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    main()  # Goes back to the main menu and method   

            elif event.type == pygame.MOUSEBUTTONDOWN and bullet is None:
                if playerTurnNum == 0:#player1
                    vx = 5  # Set initial horizontal velocity (+ means going right, - means left)
                    vy = -10  # Set initial vertical velocity (- means going up, + means going down)
                    green_tank_x, green_tank_y = event.pos
                    bullet = Bullet(green_tank_x, green_tank_y, vx, vy)
                    all_sprites.add(bullet)
                    playerTurnNum=1
                else:
                    vx = 5  # Set initial horizontal velocity (+ means going right, - means left)
                    vy = -10  # Set initial vertical velocity (- means going up, + means going down)
                    green_tank_x, green_tank_y = event.pos
                    bullet = Bullet(green_tank_x, green_tank_y, vx, vy)
                    all_sprites.add(bullet)
                    playerTurnNum=0


            if pygame.sprite.spritecollide(bullet, powerup, dokill=True):
                print("Bullet hit the target!")
                redFuel += 100
                greenFuel += 100
                bullet.kill()
            



            elif powerUpRNG == 1 and powerupNum <= 3:
                powerup = PowerUp(random.randint(0, 640), 0)
                all_sprites.add(powerup)
                powerUpRng += 1

            if event.type == pygame.K_LEFT and red_tank_x > 0 and redFuel > 0:
                red_tank_x -= 10
                redFuel -= 5
            if event.type == pygame.K_RIGHT and red_tank_x < 0 and redFuel > 0:
                red_tank_x += 1
                redFuel -= 5
            if event.type == pygame.K_a and green_tank_x > 0 and greenFuel > 0:
                green_tank_x -= 10
                greenFuel -= 5
            if event.type == pygame.K_d and green_tank_x < 0 and greenFuel > 0:

            if Py_Event.type == pygame.K_LEFT and red_tank_x > 0:
                red_tank_x -= 10
            if Py_Event.type == pygame.K_RIGHT and red_tank_x < 0:
                red_tank_x += 1
            if Py_Event.type == pygame.K_a and green_tank_x > 0:
                green_tank_x -= 10
            if Py_Event.type == pygame.K_d and green_tank_x < 0:

                green_tank_x += 10
                greenFuel -= 15


        screen.fill(white)
        
        # Draws the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        # Game loop

        pygame.display.flip()
        clock.tick(30) 

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
powerUpRNG = 0

def main():
    global bullet, powerup
    load_progress()
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
                save_progress()
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                        game_loop()
                if settings_button.collidepoint(event.pos):
                        settings_menu()
                if shop_button.collidepoint(event.pos):
                        shop_menu()
                if inventory_button.collidepoint(event.pos):
                        inventory_menu()
            
            
        screen.fill((140, 170, 255))  # always the first drawing command
        screen.blit(background_image, (0, 0))

        pygame.draw.circle(screen, (0, 100, 0), (circle_x, circle_y), circle_rad)
        pygame.draw.rect(screen, (0, 100, 0), (rect_x, rect_y, 200, 500), 200)
        pygame.draw.rect(screen, (0, 100, 0), (rect1_x, rect1_y, 200, 500), 200)
        pygame.draw.circle(screen, (0, 100, 0), (circle1_x, circle1_y), circle1_rad)
        pygame.draw.circle(screen, (0, 100, 0), (circle2_x, circle2_y), circle2_rad)
        pygame.draw.rect(screen, (0, 100, 0), (rect3_x, rect3_y, 200, 500), 20)
        pygame.draw.rect(screen, (0, 100, 0), (rect4_x, rect4_y, 190, 1000), 100)


        if pygame.green_tank.colliderect(floor_1):
            green_tank_y = floor_1.top - green_tank_height
        if pygame.green_tank.colliderect(floor_3):
            green_tank_y = floor_3.top - green_tank_height
        if pygame.green_tank.colliderect(floor_5):
            green_tank_y = floor_5.top - green_tank_height
        if pygame.green_tank.colliderect(floor_6):
            green_tank_y = floor_6.top - green_tank_height



        if pygame.red_tank.colliderect(floor_1):
            red_tank_y = floor_1.top - red_tank_height
        if pygame.red_tank.colliderect(floor_3):
            red_tank_y = floor_3.top - red_tank_height
        if pygame.red_tank.colliderect(floor_5):
            red_tank_y = floor_5.top - red_tank_height
        if pygame.red_tank.colliderect(floor_6):
            red_tank_y = floor_6.top - red_tank_height


    

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
        all_sprites.update()  # Update all sprites
        all_sprites.draw(screen)  # Draw all sprites
        pygame.display.flip()  # Flip the display
        clock.tick(30)  # Cap the frame rate
    save_progress()    
    pygame.quit()

main()



  


