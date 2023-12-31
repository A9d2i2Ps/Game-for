
# Imports modules 
import pygame 
from sys import exit

# At start of game so can function properly
pygame.init()

# Store all the cords for the row
rowOne = 0
rowTwo = rowOne + 50
rowThree = rowTwo + 50
rowFour = rowThree + 50
rowFive = rowFour + 50
rowSix = rowFive + 50
rowSeven = rowSix + 50
rowEight = rowSeven + 50
rowNine = rowEight + 50
rowTen = rowNine + 50
rowEleven = rowTen + 50
rowTwelve = rowEleven + 50
rowThirteen = rowTwelve + 50
rowFourteen = rowThirteen + 50
rowFifteen = rowFourteen + 50
rowSixteen = rowFifteen + 50


# Stores all the cords for the column
colOne = 0
colTwo = colOne + 50
colThree = colTwo + 50
colFour = colThree + 50  
colFive = colFour + 50
colSix = colFive + 50
colSeven = colSix + 50
colEight = colSeven + 50
colNine = colEight + 50
colTen = colNine + 50
colEleven = colTen + 50
colTwelve = colEleven + 50
colThirteen = colTwelve + 50 # 600
colFourteen = colThirteen + 50
colFifteen = colFourteen + 50
colSixteen = colFifteen + 50

# Makes the screen that the game is played on
screen = pygame.display.set_mode((800,800))
gameIcon = pygame.image.load("images/icon.png")
gameStatus = 0
gameAlive = True
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)



# Sets the title for the game when screen pops up
pygame.display.set_caption('Bob')

# Sets the icon in the top left when game is run
pygame.display.set_icon(gameIcon)

# Class for the controlable character
class Player(pygame.sprite.Sprite):
    # Sets the default locations
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Images\purpleBall.png')
        self.rect = self.image.get_rect(topleft=(colTwo+15,rowOne+20)) 

# Grabs the player input and does an action based on input
    def playerInput(self):
        # Gets all the currently pressed key
        keys = pygame.key.get_pressed()
        # Player speed
        speed = 2
        
        # Checks if individual key is pressed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= speed
    # pygame
    # Constant      ASCII   Description
    # ---------------------------------

    # K_UP                  up arrow
    # K_LEFT                left arrow
    # K_DOWN                down arrow
    # K_RIGHT               right arrow
    # K_w           w       w
    # K_a           a       a
    # K_s           s       s
    # K_d           d       d
        
    # Calls functions inside class that need to be used
    def update(self):
        self.playerInput()
        # Kills sprite when 
        if gameStatus != 0:
            self.kill()

# Wall class for the "enemy wall"
class Wall(pygame.sprite.Sprite):
    
    # when class if called all default information on it
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

        # Rect = X, Y, width, height
        self.image = pygame.image.load('Images\wall.png')
        self.rect = self.image.get_rect(topleft=(x,y))

# Destination where player needs to reach
class Goal(pygame.sprite.Sprite):

    # when class if called all default information on it
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y

        # Rect = X, Y, width, height
        # Creates image and attaches rect in relation to image
        self.image = pygame.image.load('Images\goal.png')
        self.rect = self.image.get_rect(topleft=(x,y))

# Sets all the groups for each object
player = pygame.sprite.GroupSingle()
wall = pygame.sprite.Group()
goal = pygame.sprite.Group()

# Maze
map = [
# So player cant walk off

[wall.add(Wall(colTwo,rowOne-50))],
# Row One
[
    [ # Col 1-4
        wall.add(Wall(colOne,rowOne)),
        # wall.add(Wall(colTwo,rowOne)),
        wall.add(Wall(colThree,rowOne)),
        wall.add(Wall(colFour,rowOne)),
    ],
    [ # Col 5-8
        wall.add(Wall(colFive,rowOne)),
        wall.add(Wall(colSix,rowOne)),
        wall.add(Wall(colSeven,rowOne)),
        wall.add(Wall(colEight,rowOne)),
    ],
    [ # Col 9-12
        wall.add(Wall(colNine,rowOne)),
        wall.add(Wall(colTen,rowOne)),
        wall.add(Wall(colEleven,rowOne)),
        wall.add(Wall(colTwelve,rowOne)),
    ],
    [ # Col 13-16
        wall.add(Wall(colThirteen,rowOne)),
        wall.add(Wall(colFourteen,rowOne)),
        wall.add(Wall(colFifteen,rowOne)),
        wall.add(Wall(colSixteen,rowOne))
    ],
    ],

# Row Two
[
    [ # Col 1-4
        wall.add(Wall(colOne,rowTwo)),
        # wall.add(Wall(colTwo,rowTwo)),
        wall.add(Wall(colThree,rowTwo)),
        # wall.add(Wall(colFour,rowTwo)),
    ],
    [ # Col 5-8
        # wall.add(Wall(colFive,rowTwo)),
        # wall.add(Wall(colSix,rowTwo)),
        wall.add(Wall(colSeven,rowTwo)),
        # wall.add(Wall(colEight,rowTwo)),
    ],
    [ # Col 9-12
        # wall.add(Wall(colNine,rowTwo)),
        # wall.add(Wall(colTen,rowTwo)),
        # wall.add(Wall(colEleven,rowTwo)),
        wall.add(Wall(colTwelve,rowTwo)),
    ], 
    [ # Col 13-16
        wall.add(Wall(colThirteen,rowTwo)),
        wall.add(Wall(colFourteen,rowTwo)),
        wall.add(Wall(colFifteen,rowTwo)),
        wall.add(Wall(colSixteen,rowTwo))
    ]
],

# Row Three
[
    wall.add(Wall(colOne,rowThree)),
    # wall.add(Wall(colTwo,rowThree)),
    # wall.add(Wall(colThree,rowThree)),
    # wall.add(Wall(colFour,rowThree)),

    wall.add(Wall(colFive,rowThree)),
    # wall.add(Wall(colSix,rowThree)),
    # wall.add(Wall(colSeven,rowThree)),
    # wall.add(Wall(colEight,rowThree)),

    wall.add(Wall(colNine,rowThree)),
    wall.add(Wall(colTen,rowThree)),
    wall.add(Wall(colEleven,rowThree)),
    wall.add(Wall(colTwelve,rowThree)),

    wall.add(Wall(colThirteen,rowThree)),
    # wall.add(Wall(colFourteen,rowThree)),
    # wall.add(Wall(colFifteen,rowThree)),
    goal.add(Goal(colSixteen,rowThree)),
    ],

# Row Four
[
    wall.add(Wall(colOne,rowFour)),
    wall.add(Wall(colTwo,rowFour)),
    wall.add(Wall(colThree,rowFour)),
    wall.add(Wall(colFour,rowFour)),

    wall.add(Wall(colFive,rowFour)),
    # wall.add(Wall(colSix,rowFour)),
    wall.add(Wall(colSeven,rowFour)),
    # wall.add(Wall(colEight,rowFour)),

    wall.add(Wall(colNine,rowFour)),
    wall.add(Wall(colTen,rowFour)),
    wall.add(Wall(colEleven,rowFour)),
    wall.add(Wall(colTwelve,rowFour)),

    wall.add(Wall(colThirteen,rowFour)),
    wall.add(Wall(colFourteen,rowFour)),
    wall.add(Wall(colFifteen,rowFour)),
    wall.add(Wall(colSixteen,rowFour)),
    ],

# Row Five
[
    wall.add(Wall(colOne,rowFive)),
    wall.add(Wall(colTwo,rowFive)),
    wall.add(Wall(colThree,rowFive)),
    # wall.add(Wall(colFour,rowFive)),

    wall.add(Wall(colFive,rowFive)),
    # wall.add(Wall(colSix,rowFive)),
    wall.add(Wall(colSeven,rowFive)),
    # wall.add(Wall(colEight,rowFive)),

    # wall.add(Wall(colNine,rowFive)),
    wall.add(Wall(colTen,rowFive)),
    wall.add(Wall(colEleven,rowFive)),
    # wall.add(Wall(colTwelve,rowFive)),

    # wall.add(Wall(colThirteen,rowFive)),
    # wall.add(Wall(colFourteen,rowFive)),
    # wall.add(Wall(colFifteen,rowFive)),
    wall.add(Wall(colSixteen,rowFive)),
    ],

# Row Six
[
    wall.add(Wall(colOne,rowSix)),
    wall.add(Wall(colTwo,rowSix)),
    wall.add(Wall(colThree,rowSix)),
    # wall.add(Wall(colFour,rowSix)),

    # wall.add(Wall(colFive,rowSix)),
    # wall.add(Wall(colSix,rowSix)),
    wall.add(Wall(colSeven,rowSix)),
    wall.add(Wall(colEight,rowSix)),

    wall.add(Wall(colNine,rowSix)),
    wall.add(Wall(colTen,rowSix)),
    # wall.add(Wall(colEleven,rowSix)),
    # wall.add(Wall(colTwelve,rowSix)),

    wall.add(Wall(colThirteen,rowSix)),
    wall.add(Wall(colFourteen,rowSix)),
    # wall.add(Wall(colFifteen,rowSix)),
    wall.add(Wall(colSixteen,rowSix)),
    ],

# Row Seven
[
    wall.add(Wall(colOne,rowSeven)),
    wall.add(Wall(colTwo,rowSeven)),
    wall.add(Wall(colThree,rowSeven)),
    # wall.add(Wall(colFour,rowSeven)),

    wall.add(Wall(colFive,rowSeven)),
    wall.add(Wall(colSix,rowSeven)),
    wall.add(Wall(colSeven,rowSeven)),
    wall.add(Wall(colEight,rowSeven)),

    wall.add(Wall(colNine,rowSeven)),
    wall.add(Wall(colTen,rowSeven)),
    # wall.add(Wall(colEleven,rowSeven)),
    wall.add(Wall(colTwelve,rowSeven)),

    wall.add(Wall(colThirteen,rowSeven)),
    wall.add(Wall(colFourteen,rowSeven)),
    # wall.add(Wall(colFifteen,rowSeven)),
    wall.add(Wall(colSixteen,rowSeven)),
    ],

# Row Eight
[
    wall.add(Wall(colOne,rowEight)),
    wall.add(Wall(colTwo,rowEight)),
    # wall.add(Wall(colThree,rowEight)),
    # wall.add(Wall(colFour,rowEight)),

    wall.add(Wall(colFive,rowEight)),
    wall.add(Wall(colSix,rowEight)),
    # wall.add(Wall(colSeven,rowEight)),
    # wall.add(Wall(colEight,rowEight)),

    # wall.add(Wall(colNine,rowEight)),
    # wall.add(Wall(colTen,rowEight)),
    # wall.add(Wall(colEleven,rowEight)),
    # wall.add(Wall(colTwelve,rowEight)),

    wall.add(Wall(colThirteen,rowEight)),
    wall.add(Wall(colFourteen,rowEight)),
    # wall.add(Wall(colFifteen,rowEight)),
    wall.add(Wall(colSixteen,rowEight)),
    ],

# Row Nine
[
    wall.add(Wall(colOne,rowNine)),
    wall.add(Wall(colTwo,rowNine)),
    # wall.add(Wall(colThree,rowNine)),
    wall.add(Wall(colFour,rowNine)),

    wall.add(Wall(colFive,rowNine)),
    wall.add(Wall(colSix,rowNine)),
    # wall.add(Wall(colSeven,rowNine)),
    wall.add(Wall(colEight,rowNine)),

    wall.add(Wall(colNine,rowNine)),
    # wall.add(Wall(colTen,rowNine)),
    wall.add(Wall(colEleven,rowNine)),
    # wall.add(Wall(colTwelve,rowNine)),

    wall.add(Wall(colThirteen,rowNine)),
    wall.add(Wall(colFourteen,rowNine)),
    wall.add(Wall(colFifteen,rowNine)),
    wall.add(Wall(colSixteen,rowNine)),
    ],

# Row Ten
[
    goal.add(Goal(colOne,rowTen)),
    wall.add(Wall(colTwo,rowTen)),
    # wall.add(Wall(colThree,rowTen)),
    wall.add(Wall(colFour,rowTen)),

    # wall.add(Wall(colFive,rowTen)),
    # wall.add(Wall(colSix,rowTen)),
    # wall.add(Wall(colSeven,rowTen)),
    wall.add(Wall(colEight,rowTen)),

    wall.add(Wall(colNine,rowTen)),
    # wall.add(Wall(colTen,rowTen)),
    wall.add(Wall(colEleven,rowTen)),
    # wall.add(Wall(colTwelve,rowTen)),

    # wall.add(Wall(colThirteen,rowTen)),
    # wall.add(Wall(colFourteen,rowTen)),
    wall.add(Wall(colFifteen,rowTen)),
    goal.add(Goal(colSixteen,rowTen)),
    ],

# Row Eleven
[
    wall.add(Wall(colOne,rowEleven)),
    wall.add(Wall(colTwo,rowEleven)),
    # wall.add(Wall(colThree,rowEleven)),
    # wall.add(Wall(colFour,rowEleven)),

    # wall.add(Wall(colFive,rowEleven)),
    wall.add(Wall(colSix,rowEleven)),
    wall.add(Wall(colSeven,rowEleven)),
    wall.add(Wall(colEight,rowEleven)),

    # wall.add(Wall(colNine,rowEleven)),
    # wall.add(Wall(colTen,rowEleven)),
    wall.add(Wall(colEleven,rowEleven)),
    wall.add(Wall(colTwelve,rowEleven)),

    wall.add(Wall(colThirteen,rowEleven)),
    wall.add(Wall(colFourteen,rowEleven)),
    wall.add(Wall(colFifteen,rowEleven)),
    wall.add(Wall(colSixteen,rowEleven)),
    ],

# Row Twelve
[
    wall.add(Wall(colOne,rowTwelve)),
    wall.add(Wall(colTwo,rowTwelve)),
    wall.add(Wall(colThree,rowTwelve)),
    # wall.add(Wall(colFour,rowTwelve)),

    wall.add(Wall(colFive,rowTwelve)),
    wall.add(Wall(colSix,rowTwelve)),
    wall.add(Wall(colSeven,rowTwelve)),
    # wall.add(Wall(colEight,rowTwelve)),

    # wall.add(Wall(colNine,rowTwelve)),
    wall.add(Wall(colTen,rowTwelve)),
    wall.add(Wall(colEleven,rowTwelve)),
    # wall.add(Wall(colTwelve,rowTwelve)),

    # wall.add(Wall(colThirteen,rowTwelve)),
    # wall.add(Wall(colFourteen,rowTwelve)),
    # wall.add(Wall(colFifteen,rowTwelve)),
    wall.add(Wall(colSixteen,rowTwelve)),
],

# Row Thirteen
[
    wall.add(Wall((colOne),(rowThirteen))),
    wall.add(Wall(colTwo,rowThirteen)),
    wall.add(Wall(colThree,rowThirteen)),
    # wall.add(Wall(colFour,rowThirteen)),

    wall.add(Wall(colFive,rowThirteen)),
    wall.add(Wall(colSix,rowThirteen)),
    wall.add(Wall(colSeven,rowThirteen)),
    # wall.add(Wall(colEight,rowThirteen)),

    wall.add(Wall(colNine,rowThirteen)),
    wall.add(Wall(colTen,rowThirteen)),
    wall.add(Wall(colEleven,rowThirteen)),
    # wall.add(Wall(colTwelve,rowThirteen)),

    wall.add(Wall(colThirteen,rowThirteen)),
    wall.add(Wall(colFourteen,rowThirteen)),
    # wall.add(Wall(colFifteen,rowThirteen)),
    wall.add(Wall(colSixteen,rowThirteen))
    ],

# Row Fourteen
[
    goal.add(Goal(colOne,rowFourteen)),
    # wall.add(Wall(colTwo,rowFourteen)),
    wall.add(Wall(colThree,rowFourteen)),
    # wall.add(Wall(colFour,rowFourteen)),

    # wall.add(Wall(colFive,rowFourteen)),
    wall.add(Wall(colSix,rowFourteen)),
    wall.add(Wall(colSeven,rowFourteen)),
    # wall.add(Wall(colEight,rowFourteen)),

    # wall.add(Wall(colNine,rowFourteen)),
    # wall.add(Wall(colTen,rowFourteen)),
    # wall.add(Wall(colEleven,rowFourteen)),
    # wall.add(Wall(colTwelve,rowFourteen)),

    wall.add(Wall(colThirteen,rowFourteen)),
    wall.add(Wall(colFourteen,rowFourteen)),
    # wall.add(Wall(colFifteen,rowFourteen)),
    wall.add(Wall(colSixteen,rowFourteen)),
],

# Row Fifteen
[
    wall.add(Wall(colOne,rowFifteen)),
    # wall.add(Wall(colTwo,rowFifteen)),
    # wall.add(Wall(colThree,rowFifteen)),
    wall.add(Wall(colFour,rowFifteen)),

    # wall.add(Wall(colFive,rowFifteen)),
    # wall.add(Wall(colSix,rowFifteen)),
    # wall.add(Wall(colSeven,rowFifteen)),
    wall.add(Wall(colEight,rowFifteen)),

    wall.add(Wall(colNine,rowFifteen)),
    wall.add(Wall(colTen,rowFifteen)),
    wall.add(Wall(colEleven,rowFifteen)),
    wall.add(Wall(colTwelve,rowFifteen)),

    wall.add(Wall(colThirteen,rowFifteen)),
    wall.add(Wall(colFourteen,rowFifteen)),
    # wall.add(Wall(colFifteen,rowFifteen)),
    wall.add(Wall(colSixteen,rowFifteen)),
    ],

# Row Sixteen
[
    wall.add(Wall(colOne,rowSixteen)),
    wall.add(Wall(colTwo,rowSixteen)),
    wall.add(Wall(colThree,rowSixteen)),
    wall.add(Wall(colFour,rowSixteen)),

    wall.add(Wall(colFive,rowSixteen)),
    wall.add(Wall(colSix,rowSixteen)),
    wall.add(Wall(colSeven,rowSixteen)),
    wall.add(Wall(colEight,rowSixteen)),

    wall.add(Wall(colNine,rowSixteen)),
    wall.add(Wall(colTen,rowSixteen)),
    wall.add(Wall(colEleven,rowSixteen)),
    wall.add(Wall(colTwelve,rowSixteen)),

    wall.add(Wall(colThirteen,rowSixteen)),
    wall.add(Wall(colFourteen,rowSixteen)),
    goal.add(Goal(colFifteen,rowSixteen)),
    wall.add(Wall(colSixteen,rowSixteen))
    ]

]

# Checks if player is hitting something
def playerCollide(gameStatus):
        # 0 = game running  
        # 1 = player crashed into wall
        # 2 = player won
        while (gameStatus == 0):
            # Default game status
            gameStatus = 0
            
            # Checks for player collision in relation to the wall
            wallCollide = pygame.sprite.spritecollide(player.sprite,wall,False)
            # Checks if ccollision is being reported
            if(len(wallCollide) != 0):
                gameStatus = 1
                return gameStatus
            
            # Checks for player collision in relation to the goal
            goalCollide = pygame.sprite.spritecollide(player.sprite,goal,False)
            # Checks if ccollision is being reported
            if(len(goalCollide) != 0):
                gameStatus = 2
                return gameStatus
            
            return gameStatus
        else:
            return gameStatus
        


# Statement for running game
while (gameAlive):
    # Creates the player
    player.add(Player())

    # When playing game
    while (gameStatus == 0):
        # Checks for collision
        gameStatus = playerCollide(gameStatus)

        # Checks player input
        for event in pygame.event.get():
            # Checks if the player input is the exit botton and closes code if clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Creates the background that the maze runs over
        pygame.draw.rect(screen,"white",(0,0,800,800))

        # Renders in all the sprites
        wall.draw(screen)
        goal.draw(screen)
        player.draw(screen)

        # Calls the update function in the player class
        player.update()
        
        

        # Updates the screen and sets FPS limit to 60
        clock.tick(60)
        pygame.display.update()
    else:
        while (gameStatus == 1):
            # Sets background to you lost screen
            lostBackground = pygame.image.load('Images\youDie.jpg')
            lostBackgroundRect = lostBackground.get_rect(topleft=(0,0))
            screen.blit(lostBackground,lostBackgroundRect)
            # Checks player input
            for event in pygame.event.get():
            # Checks if the player input is the exit botton and closes code if clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            # Sets background to you lost screen
            if keys[pygame.K_SPACE]:
                gameStatus = 0

            wonMessage = font.render('Not Horray \nHit space to restart',False,(1,1,1))
            wonMessageRect = wonMessage.get_rect(midbottom = (400,600))
            # Updates screen
            pygame.display.update()         

        # Checks if player won
        while (gameStatus == 2):
            # Sets background for if you won
            wonBackground = pygame.image.load('Images\youWon.jpg')
            wonBackgroundRect = wonBackground.get_rect(topleft=(0,0))
            screen.blit(wonBackground,wonBackgroundRect)
            # Checks player input
            for event in pygame.event.get():
               # Checks if the player input is the exit botton and closes code if clicked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            keys = pygame.key.get_pressed()
            # Checks if user wants to restart game
            if keys[pygame.K_SPACE]:
                gameStatus = 0
            
            # Creates the message showed at end when you won
            wonMessage = font.render('Horray \nHit space to restart',False,(255,255,255))
            wonMessageRect = wonMessage.get_rect(midbottom = (400,600))              
            
            # Displays the message
            screen.blit(wonMessage,wonMessageRect)

            # Updates display
            pygame.display.update()
