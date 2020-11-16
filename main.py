import random
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

SCREEN_BG = pg.Surface((SCREEN_SIZE))
SCREEN_BG.fill(pg.Color('#FFFFFF'))

MASTER_LOOP = True

CLOCK = pg.time.Clock()
FPS = 60

GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))

GAME_STATE = 'MAIN_MENU'
'''
GAME STATES:
MAIN_MENU
BUY_ROUND
STORY_ROUND
COMBAT_ROUND
'''
TURNS = 0

while MASTER_LOOP:
    while GAME_STATE == 'MAIN_MENU':
        DT = CLOCK.tick(FPS)/1000.0
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

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
                        GAME_STATE = 'BUY_ROUND'
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

    # BUY ROUND

    card_dragging = False
    card_dragged = None
    end_buy_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]//2.5, SCREEN_SIZE[1]//2), (150, 100)),
                                                        text='End Buy Round',
                                                        manager=GUI_MANAGER)

    # Shuffling

    cards.deal_cards('PLAYERS', 2)
    cards.deal_cards('SHOP', 4)

    while GAME_STATE == 'BUY_ROUND':
        DT = CLOCK.tick(FPS)/1000.0
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GAME_STATE = 'MAIN_MENU'
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                for card in cards.P1_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P1.points += card.cost # add value of card
                        if card.type == 'STORY':
                            cards.STORY_DISCARD.append(card)
                        elif card.type == 'ATTACK':
                            cards.ATTACK_DISCARD.append(card)
                        cards.P1_HAND.remove(card) # remove it
                for card in cards.P2_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P2.points += card.cost # add value of card
                        if card.type == 'STORY':
                            cards.STORY_DISCARD.append(card)
                        elif card.type == 'ATTACK':
                            cards.ATTACK_DISCARD.append(card)
                        cards.P2_HAND.remove(card) # remove it
                for card in cards.P3_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P3.points += card.cost # add value of card
                        if card.type == 'STORY':
                            cards.STORY_DISCARD.append(card)
                        elif card.type == 'ATTACK':
                            cards.ATTACK_DISCARD.append(card)
                        cards.P3_HAND.remove(card) # remove it
                for card in cards.P4_HAND:
                    if card.rect.collidepoint(x, y):
                        player.P4.points += card.cost # add value of card
                        if card.type == 'STORY':
                            cards.STORY_DISCARD.append(card)
                        elif card.type == 'ATTACK':
                            cards.ATTACK_DISCARD.append(card)
                        cards.P4_HAND.remove(card) # remove it

                for card in cards.SHOP_HAND:
                    if card.rect.collidepoint(event.pos):
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                # P1
                if mouse_y >= SCREEN_SIZE[1] - assets.CARD_HEIGHT and card_dragged is not None:
                    if player.P1.points >= card_dragged.cost:
                        cards.P1_HAND.append(card_dragged)
                        player.P1.points -= card_dragged.cost
                        cards.SHOP_HAND.remove(card_dragged) # remove it
                        card_dragged = None
                # P2
                if mouse_x <= assets.CARD_WIDTH and card_dragged is not None:
                    if player.P2.points >= card_dragged.cost:
                        cards.P2_HAND.append(card_dragged)
                        player.P2.points -= card_dragged.cost
                        cards.SHOP_HAND.remove(card_dragged) # remove it
                        card_dragged = None
                # P3
                if mouse_y <= assets.CARD_HEIGHT and card_dragged is not None:
                    if player.P3.points >= card_dragged.cost:
                        cards.P3_HAND.append(card_dragged)
                        player.P3.points -= card_dragged.cost
                        cards.SHOP_HAND.remove(card_dragged) # remove it
                        card_dragged = None
                # P4
                if mouse_x >= SCREEN_SIZE[0] - assets.CARD_WIDTH and card_dragged is not None:
                    if player.P4.points >= card_dragged.cost:
                        cards.P4_HAND.append(card_dragged)
                        player.P4.points -= card_dragged.cost
                        cards.SHOP_HAND.remove(card_dragged) # remove it
                        card_dragged = None

                card_dragging = False

            elif event.type == pg.MOUSEMOTION:
                if card_dragging:
                    mouse_x, mouse_y = event.pos
                    card_dragged.rect.x = mouse_x + offset_x
                    card_dragged.rect.y = mouse_y + offset_y

            if event.type == pg.VIDEORESIZE:
                SCREEN_SIZE = event.size
                SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
                GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
                end_buy_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]//2.5, SCREEN_SIZE[1]//2), (150, 100)),
                                                                    text='End Buy Round',
                                                                    manager=GUI_MANAGER)
            
            if event.type == pg.USEREVENT:
                if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == end_buy_button:
                        for card in cards.SHOP_HAND:
                            if card.type == 'STORY':
                                cards.STORY_DISCARD.append(card)
                            elif card.type == 'ATTACK':
                                cards.ATTACK_DISCARD.append(card)
                            cards.SHOP_HAND.remove(card)
                        GAME_STATE = 'STORY_ROUND'
            
            GUI_MANAGER.process_events(event)
        GUI_MANAGER.update(DT)

        SCREEN.fill((0, 0, 0))
        GUI_MANAGER.draw_ui(SCREEN)
        
        cards.render_hand(SCREEN, SCREEN_SIZE, font=assets.POINT_FONT, card_dragged=card_dragged, game_state=GAME_STATE)
        
        player.render_player_labels(assets.POINT_FONT, SCREEN, SCREEN_SIZE)

        pg.display.update()

    # STORY ROUND

    end_buy_button.kill()
    end_story_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]//2.5, SCREEN_SIZE[1]//2), (150, 100)),
                                                        text='End Story Round',
                                                        manager=GUI_MANAGER)
    while GAME_STATE == 'STORY_ROUND':
        DT = CLOCK.tick(FPS)/1000.0
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GAME_STATE = 'MAIN_MENU'

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                for card in cards.P1_HAND:
                    if card.rect.collidepoint(x, y) and card.type == 'STORY':
                        cards.STORY_HAND.append(card)
                        cards.P1_HAND.remove(card) # remove it/add it to the story hand (gets deleted after the story is over)
                for card in cards.P2_HAND:
                    if card.rect.collidepoint(x, y) and card.type == 'STORY':
                        cards.STORY_HAND.append(card)
                        cards.P2_HAND.remove(card) # remove it/add it to the story hand (gets deleted after the story is over)
                for card in cards.P3_HAND:
                    if card.rect.collidepoint(x, y) and card.type == 'STORY':
                        cards.STORY_HAND.append(card)
                        cards.P3_HAND.remove(card) # remove it/add it to the story hand (gets deleted after the story is over)
                for card in cards.P4_HAND:
                    if card.rect.collidepoint(x, y) and card.type == 'STORY':
                        cards.STORY_HAND.append(card)
                        cards.P4_HAND.remove(card) # remove it/add it to the story hand (gets deleted after the story is over)

            if event.type == pg.VIDEORESIZE:
                SCREEN_SIZE = event.size
                SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
                GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))
                end_story_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((SCREEN_SIZE[0]//2.5, SCREEN_SIZE[1]//2), (150, 100)),
                                                                    text='End Story Round',
                                                                    manager=GUI_MANAGER)
            if event.type == pg.USEREVENT:
                if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == end_story_button:
                        for card in cards.STORY_HAND:
                            cards.STORY_HAND.remove(card)
                            cards.STORY_DISCARD.append(card)
                        GAME_STATE = 'COMBAT_ROUND'
            
            GUI_MANAGER.process_events(event)
        GUI_MANAGER.update(DT)

        SCREEN.fill((0, 0, 0))
        GUI_MANAGER.draw_ui(SCREEN)
        
        cards.render_hand(SCREEN, SCREEN_SIZE, font=assets.POINT_FONT, card_dragged=card_dragged, game_state=GAME_STATE)
        
        player.render_player_labels(assets.POINT_FONT, SCREEN, SCREEN_SIZE)

        pg.display.update()

    # COMBAT ROUND
    end_story_button.kill()

    cards.deal_cards('MONSTER', hand_size=4)
    cards.deal_cards('ENV', hand_size=1)

    while GAME_STATE == 'COMBAT_ROUND':
        if len(cards.MONSTER_HAND) == 0:
            player.P1.points += 1
            player.P2.points += 1
            player.P3.points += 1
            player.P4.points += 1
            GAME_STATE = 'BUY_ROUND'
            TURNS += 1
            print(str(TURNS))

        DT = CLOCK.tick(FPS)/1000.0
        # input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                GAME_STATE = 'MAIN_MENU'
            if event.type == pg.MOUSEBUTTONDOWN:

                for card in cards.P1_HAND:
                    if card.rect.collidepoint(event.pos) and card.type=='ATTACK':
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
                for card in cards.P2_HAND:
                    if card.rect.collidepoint(event.pos) and card.type=='ATTACK':
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
                for card in cards.P3_HAND:
                    if card.rect.collidepoint(event.pos) and card.type=='ATTACK':
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
                for card in cards.P4_HAND:
                    if card.rect.collidepoint(event.pos) and card.type=='ATTACK':
                        card_dragging = True
                        card_dragged = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.rect.x - mouse_x
                        offset_y = card.rect.y - mouse_y
            elif event.type == pg.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos

                for card in cards.MONSTER_HAND:
                    if card.rect.collidepoint(event.pos) and card_dragged is not None:
                        if card_dragged in cards.P1_HAND:
                            cards.P1_HAND.remove(card_dragged)
                        elif card_dragged in cards.P2_HAND:
                            cards.P2_HAND.remove(card_dragged)
                        elif card_dragged in cards.P3_HAND:
                            cards.P3_HAND.remove(card_dragged)
                        elif card_dragged in cards.P4_HAND:
                            cards.P4_HAND.remove(card_dragged)

                        card.health -= card_dragged.damage # attack damage
                        cards.ATTACK_DISCARD.append(card_dragged)
                        card_dragged = None

                        if card.health <= 0:
                            cards.MONSTER_DISCARD.append(card)
                            cards.MONSTER_HAND.remove(card)

                card_dragging = False

            elif event.type == pg.MOUSEMOTION:
                if card_dragging:
                    mouse_x, mouse_y = event.pos
                    card_dragged.rect.x = mouse_x + offset_x
                    card_dragged.rect.y = mouse_y + offset_y

            if event.type == pg.VIDEORESIZE:
                SCREEN_SIZE = event.size
                SCREEN = pg.display.set_mode(SCREEN_SIZE, pg.RESIZABLE)
                GUI_MANAGER = pg_gui.UIManager((SCREEN_SIZE))

            #if event.type == pg.USEREVENT:
                #if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                            
            GUI_MANAGER.process_events(event)
        GUI_MANAGER.update(DT)

        SCREEN.fill((0, 0, 0))
        GUI_MANAGER.draw_ui(SCREEN)
        
        cards.render_hand(SCREEN, SCREEN_SIZE, font=assets.POINT_FONT, card_dragged=card_dragged, game_state=GAME_STATE)
        
        player.render_player_labels(assets.POINT_FONT, SCREEN, SCREEN_SIZE)
        # show player stats here

        pg.display.update()

pg.quit()

