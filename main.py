import pygame_gui as pg_gui
import pygame as pg
import assets

pg.init()
pg.display.set_caption('RPG Card Game')
pg.key.set_repeat(200, 50)

SCREEN_SIZE = (640, 480)
SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)

ZOOM = 2 #2


SCREEN_BG = pg.Surface((SCREEN_SIZE))
SCREEN_BG.fill(pg.Color('#FFFFFF'))

MASTER_LOOP = True
GAME_STATE = 'MAIN_MENU'
CLOCK = pg.time.Clock()
FPS = 60


GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))

START_BUTTON = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), (100, 50)),
                                        text='Say Hello',
                                        manager=GUI_MANAGER)

while MASTER_LOOP:
    DT = CLOCK.tick(FPS)/1000.0
    # input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            MASTER_LOOP = False

        if event.type == pg.VIDEORESIZE:
            SCREEN_SIZE = event.size
            SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
            GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
            START_BUTTON = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), (100, 50)),
                                        text='Say Hello',
                                        manager=GUI_MANAGER)
        GUI_MANAGER.process_events(event)

    GUI_MANAGER.update(DT)
            
    SCREEN.fill((0, 0, 0))
    GUI_MANAGER.draw_ui(SCREEN)
    
    pg.display.update()

pg.quit()
