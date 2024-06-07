

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
coins = 100
Inventory_power_ups = ["Default Damage"]
#array to store prices of each power up
power_up_prices = {10, 20, 30, 40, 50}
next_powerup = 0 

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
# Colors
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,120,0)
Yellow= (255,255,0)
Purple = (160,30,240)
Orange = (230,160,0)
black = (0, 0, 0)
lightcolor = (170, 170, 170)
dark = (100, 100, 100)
scores = []

background_image_path = "TanksBackround.jpg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (Width, Height))




# ---------------------------
# Initialize global variables


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

                if current_page == 0:  # Only check for color clicks on the colors page
                    for i, row in enumerate(colors_inventory):
                        for ii, item in enumerate(row):
                            item_button = pygame.Rect(100 + ii * 120, 100 + i * 120, 120, 120)
                            if item_button.collidepoint(Py_Event.pos):
                                if item == 'Blue':
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

        screen.fill(current_bg_color)  # Update background color
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        # Draw the Power-up and Colors buttons
        pygame.draw.rect(screen, dark, page_Buttons[0])
        draw_Button('Skins', back_font, white, screen, page_Buttons[0].x + 10, page_Buttons[0].y + 5)
        pygame.draw.rect(screen, dark, page_Buttons[1])
        draw_Button('Power-Ups', back_font, white, screen, page_Buttons[1].x + 10, page_Buttons[1].y + 5)

        # Display inventory items as buttons
        if current_page == 0:
            inventory_items = colors_inventory
            for i, row in enumerate(inventory_items):
                for ii, item in enumerate(row):
                    item_button = pygame.Rect(100 + ii * 120, 100 + i * 120, 120, 120)
                    pygame.draw.rect(screen, Blue if item == 'Blue' else Red if item == 'Red' else Green if item == 'Green' else Yellow if item == 'Yellow' else Purple if item == 'Purple' else Orange if item == 'Orange' else dark, item_button)
                    draw_Button(item, back_font, white, screen, item_button.x + 12, item_button.y + 35)
        else:
            for i, item in enumerate(Inventory_power_ups):
                item_button = pygame.Rect(100, 100 + i * 120, 120, 120)
                pygame.draw.rect(screen, dark, item_button)
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
    global coins, Inventory_power_ups, power_up_prices
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    purchase_button = pygame.Rect(Width // 2 - 100, Height // 2 - 25, 200, 50)  # Center the purchase button
    continuee = True
    next_power_up = 1  # Start with the first power-up

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    main()  # Goes back to the main menu and method
                if purchase_button.collidepoint(Py_Event.pos):
                    Next_Cost = next_power_up * 10
                    if Next_Cost in power_up_prices and coins >= Next_Cost:
                        coins -= Next_Cost
                        Inventory_power_ups.append(f"Power Up {next_power_up}")
                        power_up_prices.remove(Next_Cost)
                        next_power_up += 1
                        if next_power_up * 10 not in power_up_prices:
                            continuee = False

        screen.fill(white)
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)

        # Draw the purchase button if there are power-ups left to buy
        if continuee and next_power_up * 10 in power_up_prices:
            pygame.draw.rect(screen, dark, purchase_button)
            cost = next_power_up * 10
            draw_Button(f'Buy Power Up {next_power_up}: ({cost} coins)', back_font, white, screen, purchase_button.x + 10, purchase_button.y + 10)
        else:
            draw_Button('No more upgrades available', back_font, dark, screen, Width // 2 - 150, Height // 2 - 25)

        pygame.display.flip()
        clock.tick(30)
#remind: make the backround another color
# make floor
floor = (circle_x, circle_y)
floor_1 = pygame.Rect(rect_x , rect_y, 200, 500)
floor_2 = (circle1_x, circle1_y)
floor_3 = pygame.Rect(rect1_x, rect1_y, 200, 500)
floor_4 = (circle2_x, circle2_y)
floor_5 = pygame.Rect(rect3_x, rect3_y, 200, 500)
floor_6 = pygame.Rect(rect4_x, rect4_y, 190, 1000)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_Button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Sprite class for the bullet 


def main():
    global bullet, powerup
    running = True
    play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 50)
    settings_button = pygame.Rect(Width // 2 - 100, Height // 2 - 30, 200, 50)
    shop_button = pygame.Rect(Width // 2 - 100, Height // 2 + 40, 200, 50)
    inventory_button = pygame.Rect(Width // 2 - 100, Height // 2 + 110, 200, 50)
    screen.fill((255, 255, 255))  # always the first drawing command
    
    while running:
        powerUpRNG = random.randint(1,30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_x, mouse_y = event.pos
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
        

        pygame.display.flip()  # Flip the display
        clock.tick(30)  # Cap the frame rate

    pygame.quit()

main()



  

