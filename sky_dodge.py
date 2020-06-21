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
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        #Move the sprite based on user keypresses
     def update(self, pressed_keys):
        if pressed_keys[K_UP]:
           self.rect.move_ip(0, -5) 
        if pressed_keys[K_DOWN]:
           self.rect.move_ip(0, 5) 
        if pressed_keys[K_LEFT]:
           self.rect.move_ip(-5, 0) 
        if pressed_keys[K_RIGHT]:
           self.rect.move_ip(5, 0) 

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

    pressed_keys = pygame.key.get_pressed()

    #Fill the screen with white
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)

    #update the display
    pygame.display.flip()
