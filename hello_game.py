# Simple pygame program

import pygame
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode((500, 500))

# Run until user asks to quit
running = True
while running:
    
    # Did the user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the ackground color with white
    screen.fill((255, 255, 255))

    #Draw a solid blue circle
    pygame.draw.circle(screen, (0, 0, 244), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

#Done! Time to quit
pygame.quit()
