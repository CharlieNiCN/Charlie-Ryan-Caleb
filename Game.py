import pygame
import math
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random
from pygame import event
import json
import sys

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
Blue = (0, 0, 255)
Red = (255, 0, 0)
Green = (0, 120, 0)
Yellow = (255, 255, 0)
Purple = (160, 30, 240)
Orange = (230, 160, 0)
playerTurnNum = 0
coins = 0
Inventory_power_ups = ["Default Damage"]  # array to store prices of each power up
power_up_prices = {10, 20, 30, 40, 50}
next_power_up = 1
current_bg_color = white  # Initialize with white background
music_on = True

background_image_path = "TanksBackround.jpg"
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (Width, Height))

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------

#gpt
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

# Reset progress
def reset_progress():
    global coins, next_power_up, Inventory_power_ups, power_up_prices
    coins = 10
    next_power_up = 1
    Inventory_power_ups = ["Default Damage"]
    power_up_prices = {10, 20, 30, 40, 50}
    save_progress()
    

#Menus
def draw_Button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#Ryans work with only the coordinated and some dimensions made by gpt but altered by Ryan
def inventory_menu():
    global coins, Inventory_power_ups, current_bg_color
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    colors_inventory = [['Blue', 'Red', 'Green'], ['Yellow', 'Purple', 'Orange']]
    power_ups_inventory = [['Power Up 1', 'Power Up 2', 'Power Up 3'], ['Power Up 4', 'Power Up 5', 'Power Up 6']]
    current_page = 0
    page_Buttons = [pygame.Rect(Width - 110, 10, 100, 50), pygame.Rect(Width - 310, 10, 160, 50)]  # Moved to the left by another 60 pixels and increased length by 30

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                save_progress()  # Save progress when exiting
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:  # if clicked
                if back_button.collidepoint(Py_Event.pos):  # if back button is clicked on the button area
                    save_progress()  # Save progress when exiting the inventory menu
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
                    draw_Button(str(item), back_font, white, screen, item_button.x + 12, item_button.y + 35)
        else:
            for i, row in enumerate(power_ups_inventory):
                for ii, item in enumerate(row):
                    item_button = pygame.Rect(100 + ii * 120, 100 + i * 120, 120, 120)
                    item_color = Green if item in Inventory_power_ups else dark
                    pygame.draw.rect(screen, item_color, item_button)
                    draw_Button(str(item), back_font, white, screen, item_button.x + 12, item_button.y + 35)

        pygame.display.flip()
        clock.tick(30)
#Ryan
def settings_menu():
    global coins, next_power_up, Inventory_power_ups, power_up_prices, music_on
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    music_button = pygame.Rect(Width // 2 - 100, Height // 2 - 25, 200, 50)  # button location of the music
    reset_button = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 50)  # button location of the reset progress

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                save_progress()  # Save progress when exiting
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    save_progress()  # Save progress when exiting the settings menu
                    main()  # Goes back to the main menu and method
                if music_button.collidepoint(Py_Event.pos):  # if user clicked on music button
                    music_on = not music_on  # Update music boolean
                    if music_on:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                if reset_button.collidepoint(Py_Event.pos):  # if user clicked on reset button
                    reset_progress()  # Reset progress

        screen.fill(white)
        
        # Draw the back button
        pygame.draw.rect(screen, dark, back_button)
        back_font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('<', back_font, white, screen, back_button.x + 10, back_button.y + 5)
        
        # Draw the Title thing on the top that says Settings
        title_font = pygame.font.SysFont('timesnewroman', 55)
        draw_Button('Settings', title_font, dark, screen, Width // 2 - 100, Height // 4 - 70)

        # Draw the music button
        music_text = 'Music: On' if music_on else 'Music: Off'
        pygame.draw.rect(screen, dark, music_button)
        draw_Button(music_text, back_font, white, screen, music_button.x + 10, music_button.y + 10)

        # Draw the reset progress button
        pygame.draw.rect(screen, dark, reset_button)
        draw_Button('Reset', back_font, white, screen, reset_button.x + 10, reset_button.y + 10)

        pygame.display.flip()
        clock.tick(30)
def pause_menu():
    running = True
    continue_button = pygame.Rect(Width // 2 - 100, Height // 2 - 25, 200, 50)
    main_menu_button = pygame.Rect(Width // 2 - 100, Height // 2 + 50, 200, 50)

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(Py_Event.pos):
                    return  # Exit the pause menu and continue the game
                if main_menu_button.collidepoint(Py_Event.pos):
                    main()  # Go back to the main menu

        screen.fill(white)

        # Draw the continue button
        pygame.draw.rect(screen, dark, continue_button)
        font = pygame.font.SysFont('timesnewroman', 40)
        draw_Button('Continue', font, white, screen, continue_button.x + 10, continue_button.y + 10)

        # Draw the main menu button
        pygame.draw.rect(screen, dark, main_menu_button)
        draw_Button('Main Menu', font, white, screen, main_menu_button.x + 10, main_menu_button.y + 10)

        pygame.display.flip()
        clock.tick(30)

def shop_menu():
    global coins, Inventory_power_ups, power_up_prices, next_power_up, damage
    running = True
    back_button = pygame.Rect(10, 10, 50, 50)  # Defined the go back button square/rectangle
    purchase_button = pygame.Rect(Width // 2 - 100, Height // 2 - 25, 200, 50)  # Center the purchase button
    continuee = True

    while running:
        for Py_Event in pygame.event.get():
            if Py_Event.type == pygame.QUIT:
                pygame.quit()
                save_progress()  # Save progress when exiting
                return
            if Py_Event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(Py_Event.pos):
                    save_progress()  # Save progress when exiting the shop menu
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

        # Draw coin display
        pygame.draw.ellipse(screen, (255, 215, 0), (Width - 200, 20, 170, 60))  # Larger sideways oval
        coin_font = pygame.font.SysFont('timesnewroman', 30)
        draw_Button(f'Coins: {coins}', coin_font, black, screen, Width - 190, 35)

        pygame.display.flip()
        clock.tick(30)

def draw_button(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#gpt
def pause_menu(screen, font):
    screen_width = 800
    screen_height = 600
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    continue_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 25, 200, 50)
    main_menu_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint(event.pos):
                    return  # Exit the pause menu and continue the game
                if main_menu_button.collidepoint(event.pos):
                    main()

        screen.fill(black)
        pygame.draw.rect(screen, white, continue_button)
        pygame.draw.rect(screen, white, main_menu_button)
        draw_button('Continue', font, black, screen, continue_button.x, continue_button.y)
        draw_button('Main Menu', font, black, screen, main_menu_button.x, main_menu_button.y)
        
        pygame.display.flip()

#game_loop was chat gpt
def game_loop():
    global next_power_up, current_bg_color, coins
    damage = next_power_up
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tank Battle')

    # Pause button
    pause_button = pygame.Rect(screen_width // 2 - 25, 10, 50, 50)
    
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    dark = (50, 50, 50)
    
    # Tank properties
    tank_width = 50
    tank_height = 30
    bullet_height = 5
    tank_speed = 5
    bullet_speed = 7
    player1_lives = 5
    player2_lives = 5

    # Power-up variable
    next_power_up = 6  # Change this value as needed
    bullet_width = next_power_up - 1
    
    # Initialize player positions
    player1_x = 50
    player1_y = screen_height // 2 - tank_height // 2
    player2_x = screen_width - 100
    player2_y = screen_height // 2 - tank_height // 2
    
    # Bullet properties
    bullets = []
    
    # Shooting flags
    player1_shooting = False
    player2_shooting = False
    
    # Fonts
    font = pygame.font.Font(None, 36)
    
    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button.collidepoint(event.pos):
                    pause_menu(screen, font)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    player1_shooting = True
                if event.key == pygame.K_m:
                    player2_shooting = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    player1_shooting = False
                if event.key == pygame.K_m:
                    player2_shooting = False
        
        # Key presses
        keys = pygame.key.get_pressed()
        
        # Player 1 movement
        if keys[pygame.K_w]:
            player1_y -= tank_speed
        if keys[pygame.K_s]:
            player1_y += tank_speed
        if keys[pygame.K_a]:
            player1_x -= tank_speed
        if keys[pygame.K_d]:
            player1_x += tank_speed
        if player1_shooting and not any(b[2] == bullet_speed and b[0] > player1_x for b in bullets):
            bullets.append((player1_x + tank_width, player1_y + tank_height // 2 - bullet_height // 2, bullet_speed))
            player1_shooting = False  # Reset shooting flag
        
        # Player 2 movement
        if keys[pygame.K_UP]:
            player2_y -= tank_speed
        if keys[pygame.K_DOWN]:
            player2_y += tank_speed
        if keys[pygame.K_LEFT]:
            player2_x -= tank_speed
        if keys[pygame.K_RIGHT]:
            player2_x += tank_speed
        if player2_shooting and not any(b[2] == -bullet_speed and b[0] < player2_x for b in bullets):
            bullets.append((player2_x, player2_y + tank_height // 2 - bullet_height // 2, -bullet_speed))
            player2_shooting = False  # Reset shooting flag
        
        # Update bullet positions
        for i in range(len(bullets)-1, -1, -1):
            bullets[i] = (bullets[i][0] + bullets[i][2], bullets[i][1], bullets[i][2])
            if bullets[i][0] < 0 or bullets[i][0] > screen_width:
                bullets.pop(i)
        
        # Check for collisions
        for bullet in bullets:
            if player1_x < bullet[0] < player1_x + tank_width and player1_y < bullet[1] < player1_y + tank_height:
                player1_lives -= damage
                bullets.remove(bullet)
            if player2_x < bullet[0] < player2_x + tank_width and player2_y < bullet[1] < player2_y + tank_height:
                player2_lives -= damage
                bullets.remove(bullet)
        
        # Game Over condition
        if player1_lives <= 0 or player2_lives <= 0:
            coins += 5
            return coins
            main()
        
        # Drawing
        screen.fill(black)
        pygame.draw.rect(screen, current_bg_color, (player1_x, player1_y, tank_width, tank_height))
        pygame.draw.rect(screen, current_bg_color, (player2_x, player2_y, tank_width, tank_height))
        for bullet in bullets:
            pygame.draw.rect(screen, white, (bullet[0], bullet[1], bullet_width, bullet_height))
        
        # Pause button
        pygame.draw.rect(screen, dark, pause_button)
        draw_button('P', font, white, screen, pause_button.x, pause_button.y)
        
        # Draw lives
        lives1_text = font.render(f'Lives: {player1_lives}', True, white)
        lives2_text = font.render(f'Lives: {player2_lives}', True, white)
        screen.blit(lives1_text, (10, 10))
        screen.blit(lives2_text, (screen_width - 110, 10))
        
        pygame.display.flip()
        clock.tick(60)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




def main():
    global bullet, powerup
    load_progress()
    running = True
    play_button = pygame.Rect(Width // 2 - 100, Height // 2 - 100, 200, 50)
    settings_button = pygame.Rect(Width // 2 - 100, Height // 2 - 30, 200, 50)
    shop_button = pygame.Rect(Width // 2 - 100, Height // 2 + 40, 200, 50)
    inventory_button = pygame.Rect(Width // 2 - 100, Height // 2 + 110, 200, 50)
    screen.fill((255, 255, 255))  # always the first drawing command
    if music_on:
        pygame.mixer.music.play(-1)
    
    while running:
        powerUpRNG = random.randint(1, 30)
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

        font = pygame.font.SysFont(None, 55)
        button_font = pygame.font.SysFont(None, 40)

        draw_Button('Main Menu', font, black, screen, Width // 2 - 100, Height // 4 - 40)  # Changed to black
        draw_Button('Tanks', font, black, screen, Width // 2 - 50, Height // 4 - 70)  # Changed to black
        # drawing the buttons
        pygame.draw.rect(screen, lightcolor, play_button)
        draw_Button('Play', font, black, screen, play_button.x + 50, play_button.y + 10)  # Changed to black
        pygame.draw.rect(screen, lightcolor, settings_button)
        draw_Button('Settings', font, black, screen, settings_button.x + 25, settings_button.y + 10)  # Changed to black
        pygame.draw.rect(screen, lightcolor, shop_button)
        draw_Button('Shop', font, black, screen, shop_button.x + 50, shop_button.y + 10)  # Changed to black
        pygame.draw.rect(screen, lightcolor, inventory_button)
        draw_Button('Inventory', font, black, screen, inventory_button.x + 25, inventory_button.y + 10)  # Changed to black  

        #end code (MUST BE PUT AT THE BACK)

        pygame.display.flip()  # Flip the display
        clock.tick(30)  # Cap the frame rate
    save_progress()    
    pygame.quit()


main()
