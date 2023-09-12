import pygame

from  sys import exit
from win32api import GetSystemMetrics


# Width of screen first height of screen second
detail = [GetSystemMetrics(0),GetSystemMetrics(1)]
detail = [1600,800]

# At start of game so can function properly
pygame.init()



# Makes the screen that the game is played on
screen = pygame.display.set_mode((detail[0]/2,detail[1]/2))
gameIcon = pygame.image.load("images/icon.png")
text_font = pygame.font.Font("Font/Pixeltype.ttf")

clock = pygame.time.Clock()

test_surface = pygame.Surface((200,100))
test_surface.fill("pink")

# Sets the title for the game when screen pops up
pygame.display.set_caption('Bob')

pygame.display.set_icon(gameIcon)

# Statement for running game
while True:
    # Checks player input
    for event in pygame.event.get():
        # Checks if the player input is the exit botton and closes code if clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(test_surface,(200,100))        
    pygame.display.update()
    clock.tick(60)