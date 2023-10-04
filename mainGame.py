import pygame

from sys import exit
from win32api import GetSystemMetrics


# Width of screen first height of screen second
detail = [GetSystemMetrics(0),GetSystemMetrics(1)]
# detail = [1600,800]

# At start of game so can function properly
pygame.init()



# Makes the screen that the game is played on
screen = pygame.display.set_mode((800,800))
gameIcon = pygame.image.load("images/icon.png")
text_font = pygame.font.Font("Font/Pixeltype.ttf")

clock = pygame.time.Clock()

background_surface = pygame.image.load('images/background.jpg')
background_rect = background_surface.get_rect(topleft = (1,1))
screen.blit(background_surface,background_rect)

# Sets the title for the game when screen pops up
pygame.display.set_caption('Bob')

pygame.display.set_icon(gameIcon)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.draw.circle(screen,"purple",(400,400),20)
        # self.rect = self.image.get_rect()

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        rect = self.rect
        super().__init__()
        self.image = pygame.draw.rect(screen,"gray",rect)
        # self.rect = self.image.get_rect()


player = pygame.sprite.GroupSingle()
player.add(Player())

wall = pygame.sprite.GroupSingle()
wall.add(Wall())

# Statement for running game
while True:
    # Checks player input
    for event in pygame.event.get():
        # Checks if the player input is the exit botton and closes code if clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)