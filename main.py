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
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Fill the screen with a background color 
        screen.fill(config.WHITE)
        
        # Draw on the screen multiple lines starting from (0, 10) to (100, 110)
        # Each line will have a width of 5 pixels
        
        thickness = 5

        for y_offset in range(10, 110, 20):
           pygame.draw.line(screen, config.RED, [10, 20 + y_offset], [110, 120 + y_offset], thickness)
        
        # pygame.draw.line(screen, config.RED, start_pos, end_pos, thickness)
        # Draw on the screen multiple lines starting from (0, 10) to (100, 110)
        # Each line will have a width of 2 pixels
        thickness = 2 # In pixels

        for x_offset in range(10, 310, 60):
           pygame.draw.line(screen, config.RED, [100 + x_offset, 200], [210 + x_offset, 220], thickness)

        # Draw on the screen multiple lines from (0, 10) to (100, 110)
        # Each line will have a width of 5 pixels
        #y_offset = 10
        #x_offset = 10
        #thickness = 5
        #while y_offset < 100:
        #    pygame.draw.line(screen, config.RED, [0, x_offset + y_offset], [100, x_offset + y_offset], thickness)
        #    y_offset = y_offset + 10 # Increase value of y_offset by 10 each time the loop runs
        
        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)
    
    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































