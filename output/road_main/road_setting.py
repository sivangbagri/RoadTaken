import pygame
import random

WIDTH = 550
HEIGHT = 650
TITLE = 'RoadTaken'
FPS = 60

# colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SKYBLUE = (0, 155, 155)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Teal = (0, 128, 128)
Silver = (192, 192, 192)
Fuchsia = (255, 0, 255)
Olive = (128, 128, 0)
Aqua = (0, 255, 255)

# font
FONT_NAME = 'BRLNSR'

# layers
CARS_LAYER = 0
GUIDE_LAYER = 2

ICON = pygame.image.load('road_assets/carbg.jpg')

# image loading
POLICE_IM = pygame.image.load('road_assets/police.png')
Players = ['road_assets/.png', 'road_assets/cyc.png', 'road_assets/sco.png', ]
BIKE = pygame.image.load('road_assets/bike.png')
NBIKE = pygame.image.load('road_assets/newbike.png')
CYC = pygame.image.load('road_assets/cyc.png')
SCO = pygame.image.load('road_assets/sco.png')
JEEP = pygame.image.load('road_assets/jeep.png')
CYC2 = pygame.image.load('road_assets/cyccl.png')
VIK = pygame.image.load('road_assets/newbike.png')
back = pygame.image.load('road_assets/topview.jpeg')
PED = pygame.image.load('road_assets/ped.png')
CHAR = pygame.image.load('road_assets/charr.png')
DIA = pygame.image.load('road_assets/buebox.png')
TANK = pygame.image.load('road_assets/tank.png')
FUEL = pygame.image.load('road_assets/power.png')
MIDDLE_BG = pygame.image.load('road_assets/forwhite.jpg')
END = pygame.image.load('road_assets/pem.jpeg')
START_BG = pygame.image.load('road_assets/door.jpg')
INTRO = pygame.image.load('road_assets/now.png')

# image scaling
TANK = pygame.transform.scale(TANK, (50, 50))
back_im = pygame.transform.scale(back, (WIDTH, HEIGHT))
FUEL = pygame.transform.scale(FUEL, (70, 70))
DIA = pygame.transform.scale(DIA, (300, 400))
MIDDLE_BG = pygame.transform.scale(MIDDLE_BG, (WIDTH, HEIGHT))
END = pygame.transform.scale(END, (WIDTH, HEIGHT + 60))
INTRO = pygame.transform.scale(INTRO, (500, 500))
BIKE = pygame.transform.scale(BIKE, (150, 150))
CYC = pygame.transform.scale(CYC, (100, 200))
SCO = pygame.transform.scale(SCO, (150, 150))
VIK = pygame.transform.scale(VIK, (150, 150))
NBIKE = pygame.transform.scale(NBIKE, (150, 150))

Player_im = [CYC, BIKE, SCO, CYC2, VIK, NBIKE]
REDC = pygame.image.load('road_assets/redlsm.png')
REDC = pygame.transform.scale(REDC, (200, 200))
Cars = ['road_assets/cars (1).png', 'road_assets/cars (2).png', 'road_assets/cars (3).png', 'road_assets/jeep.png',
        REDC]
Cars_im = []

for i in Cars:
    if i == REDC:
        Cars_im.append(i)
    else:
        Cars_im.append(pygame.image.load(i))
