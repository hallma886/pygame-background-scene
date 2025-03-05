# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    def draw_tree():
        pygame.draw.rect(screen, config.BARK_BROWN, [60, 400, 30, 45])
        pygame.draw.polygon(screen, config.FOREST_GREEN, [[150, 400], [75, 250], [0, 400]])
        pygame.draw.polygon(screen, config.FOREST_GREEN, [[140, 350], [75, 230], [10, 350]])
 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.BLACK) 

        #y_offset = 10
        #x_offset = 10
        #while y_offset < 100:
        #    draw_tree()
        #    y_offset = y_offset + 10 # Increase value of y_offset by 10 each time the loop runs

        draw_tree()

        font = pygame.font.SysFont("Ariel", 50)
        text = font.render('Matthew hall', True, config.WHITE)
        screen.blit(text, [0, 50])
        text = font.render('Grand Traverse Academy', True, config.WHITE)
        screen.blit(text, [0, 90])





        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































