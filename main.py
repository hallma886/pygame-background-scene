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
    
    def draw_tree(x_offset, y_offset):
        # Draw the trunk
        pygame.draw.rect(screen, config.BARK_BROWN, [60 + x_offset, 400 + y_offset, 30, 45])
        # Draw the leaves
        pygame.draw.polygon(screen, config.FOREST_GREEN, [[150 + x_offset, 400 + y_offset], [75 + x_offset, 230 + y_offset], [0 + x_offset, 400 + y_offset]])
        pygame.draw.polygon(screen, config.FOREST_GREEN, [[140 + x_offset, 350 + y_offset], [75 + x_offset, 230 + y_offset], [10 + x_offset, 350 + y_offset]])
 
    def draw_cresent_right():
        pygame.draw.circle(screen, config.YELLOW, (800, 70), 45, 0)
        pygame.draw.circle(screen, config.BLACK, (780, 70), 45, 0)

    def draw_cresent_left():
        pygame.draw.circle(screen, config.YELLOW, (780, 70), 45, 0)
        pygame.draw.circle(screen, config.BLACK, (800, 70), 45, 0)

    def draw_half_moon_left():
        pygame.draw.circle(screen, config.YELLOW, (780, 70), 45, 0)
        pygame.draw.rect(screen, config.BLACK, [780, 20, 723, 113], 0)

    def draw_full_moon():
        pygame.draw.circle(screen, config.YELLOW, (780, 70), 45, 0)
    
    def draw_new_moon():
        pygame.draw.circle(screen, config.DIM_GREY, (800, 70), 45, 0)

    def draw_rectangle(screen, rect, color, thickness):
        pygame.draw.rect(screen, color, rect, thickness)

    def draw_text(screen, text, font,):
        inserted_text = font.render(text, True)
        screen.blit(inserted_text)

    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.BLACK) 

        
        #draw_new_moon()
        #draw_cresent_left()
        #draw_half_moon_left()
        #draw_cresent_right()
        draw_full_moon()











        # Draw trees at different locations
        draw_tree(0, 0)
        draw_tree(50, 0)
        draw_tree(-50, 0)
        draw_tree(150, 0)
        draw_tree(200, 0)
        draw_tree(250, 0)
        draw_tree(100, 0)
        draw_tree(305, 0)
        draw_tree(350, 0)
        draw_tree(390, 0)
        draw_tree(450, 0)
        draw_tree(500, 0)
        draw_tree(550, 0)
        draw_tree(600, 0)
        draw_tree(659, 0)
        draw_tree(700, 0)
        draw_tree(750, 0)
        draw_tree(800, 0)

        font = pygame.font.SysFont("Ariel", 50)
        text = font.render('Matthew Hall', True, config.WHITE)
        screen.blit(text, [0, 50])
        text = font.render('Grand Traverse Academy', True, config.WHITE)
        screen.blit(text, [0, 90])

        draw_rectangle(screen, [5, 445, 893, 593], (35, 35, 35),  0)

        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)

        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































