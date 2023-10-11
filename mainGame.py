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
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.up = y
        width = 50
        height = 50

        # Rect = X, Y, width, height
        self.image = pygame.draw.rect(screen,"gray",(x,y,width,height))
        # self.rect = self.image.get_rect(bottomleft = (left,up))


player = pygame.sprite.GroupSingle()
player.add(Player())

wall = pygame.sprite.GroupSingle()
wall.add(Wall(1,1))
wall.add(Wall(51,1))
wall.add(Wall(101,1))
wall.add(Wall(151,1))
wall.add(Wall(201,1))
wall.add(Wall(251,1))
wall.add(Wall(301,1))
wall.add(Wall(351,1))
wall.add(Wall(401,1))
wall.add(Wall(451,1))
wall.add(Wall(501,1))
wall.add(Wall(551,1))
wall.add(Wall(601,1))
wall.add(Wall(651,1))
wall.add(Wall(701,1))
wall.add(Wall(751,1))
wall.add(Wall(4g01,221))






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