import pygame
import sys
from GameObject import GameObject

pygame.init()
pygame.mixer.init()

#Title of game
pygame.display.set_caption("Pacman")

#Sound/Music
sound = pygame.mixer.Sound("Sound/punch.wav")

#Screen Size
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

#Sprite Start Position
PlayerX, PlayerY, = 0, 0
ClydeX, ClydeY = 500, 400

#Font
myFont = pygame.font.SysFont("Courier New", 72, True, True)

#Sprites
graphic_Obj = pygame.image.load("image/Pacman.Png")
graphic_Obj = pygame.transform.scale(graphic_Obj, (40, 40))
graphic_ObjSize = graphic_Obj.get_size()
player = GameObject(160, 200, 40, 40)

#Enemies
#enemy_Obj = pygame.image.load("image/ClydePng.png")
#enemy_Obj = pygame.transform.scale(enemy_Obj, (40, 40))
#enemy_ObjSize = enemy_Obj.get_size()

#Wall Sprite
#wall_obj = pygame.image.load("image/BUILDAMUR.gif")
#wall_obj = pygame.transform.scale(wall_obj, (40, 40))
#wall_objSize = wall_obj.get_size()

#Cheese Sprite
cheese_Obj = pygame.image.load("image/Yellow_icon.svg.png")
cheese_Obj = pygame.transform.scale(cheese_Obj, (15, 15))
cheese_ObjSize = cheese_Obj.get_size()

#Big Cheese Sprite
big_cheese_Obj = pygame.image.load("image/big cheese.png")
big_cheese_Obj = pygame.transform.scale(big_cheese_Obj, (25, 25))

#Clock
clock = pygame.time.Clock()

#Rotating the sprite
#left = pygame.transform.flip(graphic_Obj, True, False)
#right = pygame.transform.flip(left, True, False)
#up = pygame.transform.rotate(graphic_Obj, 90)
#down = pygame.transform.rotate(graphic_Obj, -90)

#SameDirectionTIcker
sameDirectionTicker = 0


#Load the playable level

walls = []

def loadScene():
    posX, posY = 0, 0

    try:
        file = open("level.dat")
        for line in file.readlines():
            for char in line:
                if char == "1":
                    pygame.draw.rect(screen, (0,0,255), (posX, posY, 40, 40))
                    walls.append(GameObject(posX, posY, 40,40))

                posX = posX + 40
            posY = posY + 40
            posX = 0
    except:
        print("Error in loading scene")


loadScene()



def loadItems():
    itemposX, itemposY = 0, 0

    try:
        file = open("level.dat")
        for line in file.readlines():
            for char in line:
                if char == "C":
                    screen.blit(cheese_Obj, (itemposX, itemposY))
                if char == "B":
                    screen.blit(big_cheese_Obj, (itemposX, itemposY))

                itemposX = itemposX + 41
            itemposY = itemposY + 42
            itemposX = 0
    except:
        print("Error in loading items")


loadItems()

currDirection, nextDirection = "", ""
wallObj = walls[0]



while True:

    #fps
    clock.tick(60)

    #Gets what happens on the screen, mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Movement

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:  # event.key == pygame.K_RIGHT:
        if nextDirection != "right":
            nextDirection = "right"
    if keys[pygame.K_LEFT]:
        if nextDirection != "left":
            nextDirection = "left"
    if keys[pygame.K_UP]:
        if nextDirection != "up":
            nextDirection = "up"
    if keys[pygame.K_DOWN]:
        if nextDirection != "down":
            nextDirection = "down"

    #player.setPosition(PlayerX, PlayerY)

    if currDirection == "right":
        PlayerX = PlayerX + 5
    elif currDirection == "left":
        PlayerX = PlayerX - 5
    elif currDirection == "up":
        PlayerY = PlayerY - 5
    elif currDirection == "down":
        PlayerY = PlayerY + 5

#Detect movement

    if currDirection != nextDirection:
        if nextDirection == "right" and pygame.Surface.get_at(screen, (player.getX() + player.getWidth() + 1, player.getY() + 1)) != (0, 0, 255) and pygame.Surface.get_at(screen, (player.getX() + player.getWidth() + 1, player.getY() + player.getHeight() - 1)) != (0, 0, 255):
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)
        elif nextDirection == "left" and pygame.Surface.get_at(screen, (player.getX() - 1, player.getY() + 1)) != (0, 0, 255) and pygame.Surface.get_at(screen, (player.getX() - 1, player.getY() + player.getHeight() - 1)) != (0, 0, 255):
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)
        elif nextDirection == "up" and pygame.Surface.get_at(screen, (player.getX() + 1, player.getY() - 1)) != (0, 0, 255) and pygame.Surface.get_at(screen, (player.getX() + player.getWidth() - 1, player.getY() - 1)) != (0, 0, 255):
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)
        elif nextDirection == "down" and pygame.Surface.get_at(screen, (player.getX() + 1, player.getY() + player.getHeight() + 1)) != (0, 0, 255) and pygame.Surface.get_at(screen, (player.getX() + player.getWidth() - 1, player.getY() + player.getHeight() + 1)) != (0, 0, 255):
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)
        elif nextDirection != "" and currDirection == "" or (currDirection == "right" and nextDirection == "left") or (currDirection == "left" and nextDirection == "right") or (currDirection == "down" and nextDirection == "up") or (currDirection == "up" and nextDirection == "down"):
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)


    print(wallObj)
    #print(player.getX(), player.getY())


    pygame.draw.rect(screen, (0,0,0), (player.getX(), player.getY(),40,40))
    if player.intersects(wallObj):
        if currDirection != nextDirection:
            currDirection = nextDirection
            wallObj = player.locateCollisionObj(walls, currDirection)
        screen.blit(graphic_Obj, (player.getX(), player.getY()))
    else:
        player.setPosition(player.getX() + PlayerX, player.getY() + PlayerY)
        screen.blit(graphic_Obj, (player.getX(), player.getY()))

    PlayerX, PlayerY = 0, 0


    #Borders to grapich object
    #if PlayerX + graphic_ObjSize[0] > 800:
        #PlayerX = 800 - graphic_ObjSize[0]
    #if PlayerX < 0:
        #PlayerX = 0
    #if PlayerY + graphic_ObjSize[0] > 600:
        #PlayerY = 600 - graphic_ObjSize[0]
    #if PlayerY < 0:
        #PlayerY = 0

    #Create scenes/items
    #loadItems()

    #Create sprite
    #screen.blit(graphic_Obj, (PlayerX, PlayerY))
    #screen.blit(enemy_Obj, (ClydeX, ClydeY))

    #Updates and refreshes screen
    pygame.display.update()
    #screen.fill((0, 0, 0))