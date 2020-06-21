import pygame

# IMport pygame.locals for easier access to coordinates 
# Updated to conform to flake8 and black standards 

from pygame.locals import(
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
)

#Define constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by etending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite)
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get


# Initialize pygame
pygame.init()

# Create the screen object and set size with constants
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player

player = Player()

# Variable to keep main loop running
running = True

while running:
    #look at every event in the queue
    for event in pygame.event.get():
        #did the user hit a key:?
        if event.type == KEYDOWN:
            # Was it the escape key? if so, stop the loop. 
            if event.key == K_ESCAPE:
                running = False
        #Did the user click the window close button? if so stop the loop
        elif event.type == QUIT:
            running = False

    #Fill the screen with white
    screen.fill((0, 0, 0))

    #Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    #Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    surf_center = (
            (SCREEN_WIDTH-surf.get_width())/2,
            (SCREEN_HEIGHT-surf.get_height())/2
    )
    # This line says "Draw surf on to the screen on the center"
    screen.blit(surf, surf_center)
    pygame.display.flip()
