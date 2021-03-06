import pygame as pg
pg.init()
pg.font.init()

POINT_FONT = pg.font.Font('assets/Fira_Code/static/FiraCode-Medium.ttf', 16)
CARD_FONT = pg.font.Font('assets/Fira_Code/static/FiraCode-Medium.ttf', 8)

ACID_ENV = pg.image.load('assets/acid_env.png')
FIRE_ENV = pg.image.load('assets/fire_env.png')
ICE_ENV = pg.image.load('assets/ice_env.png')
METAL_ENV = pg.image.load('assets/metal_env.png')
NATURE_ENV = pg.image.load('assets/nature_env.jpg')
WATER_ENV = pg.image.load('assets/water_env.png')
WIND_ENV = pg.image.load('assets/wind_env.png')

C0 = pg.image.load('assets/test_card_2.png')
C1 = pg.image.load('assets/card_1.jpg')
C2 = pg.image.load('assets/card_2.jpg')
C3 = pg.image.load('assets/card_3.jpg')
C4 = pg.image.load('assets/card_4.jpg')
C5 = pg.image.load('assets/card_5.jpg')
C6 = pg.image.load('assets/card_6.jpg')
C7 = pg.image.load('assets/card_7.jpg')
C8 = pg.image.load('assets/card_8.jpg')
C9 = pg.image.load('assets/card_9.jpg')
C10 = pg.image.load('assets/card_10.jpg')
C11 = pg.image.load('assets/card_11.jpg')
C12 = pg.image.load('assets/card_12.jpg')

CARD_WIDTH = C1.get_rect().width
CARD_HEIGHT = C1.get_rect().height
