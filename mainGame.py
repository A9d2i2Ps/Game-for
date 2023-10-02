import pygame

from  sys import exit
from win32api import GetSystemMetrics


# Width of screen first height of screen second
detail = [GetSystemMetrics(0),GetSystemMetrics(1)]
# detail = [1600,800]

# At start of game so can function properly
pygame.init()



# Makes the screen that the game is played on
screen = pygame.display.set_mode((detail[0]/2,detail[1]/2))
gameIcon = pygame.image.load("images/icon.png")
text_font = pygame.font.Font("Font/Pixeltype.ttf")

clock = pygame.time.Clock()



class assets():

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, width, height, image):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       print(image)
       self.image = pygame.image.load(image)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

background_image = 'C:\\Users\\mlgpi\\Documents\\Code\\GameFor\\Images\\ocean.png'

background = pygame.sprite.GroupSingle()
background.add = assets(detail[0],detail[1],background_image)



screen.blit(background_image,(detail[0],detail[1]))

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


    pygame.display.update()
    clock.tick(60)