import pygame_gui as pg_gui
import pygame as pg
import json
import assets

# later implement styling with css according to pygame gui documentation

pg.init()
pg.display.set_caption('RPG Card Game')
pg.key.set_repeat(200, 50)

SCREEN_SIZE = (640, 480)
SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)

ZOOM = 2 #2


SCREEN_BG = pg.Surface((SCREEN_SIZE))
SCREEN_BG.fill(pg.Color('#FFFFFF'))

MASTER_LOOP = True

CLOCK = pg.time.Clock()
FPS = 60

GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))

GAME_STATE = 'MAIN_MENU'

while MASTER_LOOP and GAME_STATE == 'MAIN_MENU':
    DT = CLOCK.tick(FPS)/1000.0
    # input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            MASTER_LOOP = False

        if event.type == pg.VIDEORESIZE:
            SCREEN_SIZE = event.size
            SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
            GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
            title_label = pg_gui.elements.UILabel(relative_rect=pg.Rect((0, SCREEN_SIZE[1]/5), (SCREEN_SIZE[0], 50)),
                                                    text='Untitled RPG Card Game',
                                                    manager=GUI_MANAGER)
            start_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]/2 -50, SCREEN_SIZE[1]/2), (100, 50)),
                                                    text='Start Game',
                                                    manager=GUI_MANAGER)
            player_count_button = pg_gui.elements.UIDropDownMenu(relative_rect=pg.Rect((SCREEN_SIZE[0]/2 -150, SCREEN_SIZE[1]/2), (100, 50)),
                                                    manager=GUI_MANAGER,
                                                    options_list=['2 Players', '3 Players', '4 Players'], starting_option='4 Players')

        if event.type == pg.USEREVENT:
            if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    GAME_STATE = 'GAME'
        GUI_MANAGER.process_events(event)
    GUI_MANAGER.update(DT)

    SCREEN.fill((0, 0, 0))
    GUI_MANAGER.draw_ui(SCREEN)
    
    pg.display.update()



pg.quit()

