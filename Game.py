import pygame, sys

pygame.init()
pygame.mixer.init()

#Title of game
pygame.display.set_caption("PacMan V.2000")

#Sound/Music
sound = pygame.mixer.Sound("Sound/punch.wav")

#Screen Size
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

#Sprite Start Position
PlayerX, PlayerY, = 400,300
ClydeX, ClydeY = 500, 400

#Font
myFont = pygame.font.SysFont("Courier New", 72, True, True)

#Sprites
graphic_Obj = pygame.image.load("image/PacMan.png")
graphic_Obj = pygame.transform.scale(graphic_Obj, (40, 40))
graphic_ObjSize = graphic_Obj.get_size()

#Enemies
enemy_Obj = pygame.image.load("image/ClydePng.png")
enemy_Obj = pygame.transform.scale(enemy_Obj, (40, 40))
enemy_ObjSize = enemy_Obj.get_size()

#Cheese Sprite
cheese_Obj = pygame.image.load("image/Yellow_icon.svg.png")
cheese_Obj = pygame.transform.scale(cheese_Obj, (20, 20))

#Clock
clock = pygame.time.Clock()

#Rotating the sprite
left = pygame.transform.flip(graphic_Obj, True, False)
right = pygame.transform.flip(left, True, False)
up = pygame.transform.rotate(graphic_Obj, 90)
down = pygame.transform.rotate(graphic_Obj, -90)


#Load the playable level
def loadScene():
    posX, posY = 0, 0

    try:
        file = open("level.dat")
        for line in file.readlines():
            for char in line:
                if char == "W":
                    pygame.draw.rect(screen, (0, 0, 200), (posX, posY, 40, 40))

                posX = posX + 40
            posY = posY + 40
            posX = 0
    except:
        print("Error in level.dat")


def loadItems():
    itemposX, itemposY = 0, 0

    try:
        file = open("level.dat")
        for line in file.readlines():
            for char in line:
                if char == "c":
                   screen.blit(cheese_Obj, (itemposX, itemposY))
                   #pygame.draw.circle(screen,(255, 255, 0), [itemposX, itemposY], 7)

                itemposX = itemposX + 40
            itemposY = itemposY + 40
            itemposX = 0
    except:
        print("Error in loading items")


while True:

    #fps
    clock.tick(60)

    #Gets what happens on the screen, mouse clicks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Movement
    keys = pygame.key.get_pressed()

    #Move direction
    if keys[pygame.K_RIGHT]:
        PlayerX = PlayerX + 5
        graphic_Obj = right
    elif keys[pygame.K_LEFT]:
        PlayerX = PlayerX + (-5)
        graphic_Obj = left
    elif keys[pygame.K_UP]:
        PlayerY = PlayerY + -5
        graphic_Obj = up
    elif keys[pygame.K_DOWN]:
        PlayerY = PlayerY + 5
        graphic_Obj = down

    #Borders to grapich object
    if PlayerX + graphic_ObjSize[0] > 760:
        PlayerX = 760 - graphic_ObjSize[0]
    if PlayerX < 40:
        PlayerX = 40
    if PlayerY + graphic_ObjSize[0] > 560:
        PlayerY = 560 - graphic_ObjSize[0]
    if PlayerY < 40:
        PlayerY = 40

    #Create scenes/items
    loadScene()
    loadItems()

    #Create sprite
    screen.blit(graphic_Obj, (PlayerX, PlayerY))
    screen.blit(enemy_Obj, (ClydeX, ClydeY))

    #Updates and refreshes screen
    pygame.display.update()
    screen.fill((0, 0, 0))