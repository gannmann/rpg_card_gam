import pygame_gui as pg_gui
import pygame as pg
import assets
import cards
import player

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
ROUND = 'BUY'

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
                    # start new game
                    GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
                    cards.init_decks()
                    player.init_players()
                    GAME_STATE = 'GAME'
        GUI_MANAGER.process_events(event)
    GUI_MANAGER.update(DT)
    SCREEN.fill((0, 0, 0))
    GUI_MANAGER.draw_ui(SCREEN)
    pg.display.update()

'''
Game Loop

Initialize game, then
  1. Buy Round
    a. 
  2. Story Round
    
  3. Combat Round
    a. draw environment
    b. draw monsters
    c. loop until combat is resolved.

'''
card_dragging = False
card_dragged = None
while MASTER_LOOP and GAME_STATE == 'GAME':
    DT = CLOCK.tick(FPS)/1000.0
    # input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            MASTER_LOOP = False
            # later make this go back to the main menu
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos

            if ROUND == 'BUY':
                for card in cards.P1_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P1.points += card.cost # add value of card
                        cards.DISCARD.append(card)
                        cards.P1_HAND.remove(card) # remove it
                for card in cards.P2_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P2.points += card.cost # add value of card
                        cards.DISCARD.append(card)
                        cards.P2_HAND.remove(card) # remove it
                for card in cards.P3_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P3.points += card.cost # add value of card
                        cards.DISCARD.append(card)
                        cards.P3_HAND.remove(card) # remove it
                for card in cards.P4_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P4.points += card.cost # add value of card
                        cards.DISCARD.append(card)
                        cards.P4_HAND.remove(card) # remove it

                for card in cards.SHOP_HAND:
                    if card.rect.collidepoint(event.pos):
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
        elif event.type == pg.MOUSEBUTTONUP:
            if ROUND == 'BUY':
                card_dragging = False
        elif event.type == pg.MOUSEMOTION:
            if ROUND == 'BUY':
                if card_dragging:
                    mouse_x, mouse_y = event.pos
                    card_dragged.rect.x = mouse_x + offset_x
                    card_dragged.rect.y = mouse_y + offset_y

        if event.type == pg.VIDEORESIZE:
            SCREEN_SIZE = event.size
            SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
            GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
        '''
        if event.type == pg.USEREVENT:
            if event.user_type == pg_gui.UI_BUTTON_PRESSED:
        '''
        GUI_MANAGER.process_events(event)
    GUI_MANAGER.update(DT)

    SCREEN.fill((0, 0, 0))
    GUI_MANAGER.draw_ui(SCREEN)
    
    cards.render_hand(SCREEN, SCREEN_SIZE, font=assets.POINT_FONT, card_dragged=card_dragged)
    

    player.render_player_labels(assets.POINT_FONT, SCREEN, SCREEN_SIZE)

    pg.display.update()

pg.quit()

