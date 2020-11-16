import random
import pygame as pg
import assets
pg.init()

# deck hands
STORY_DECK = []
REACTION_DECK = []
ATTACK_DECK = []
ENV_DECK = []
MONSTER_DECK = []
P1_HAND = []
P2_HAND = []
P3_HAND = []
P4_HAND = []
SHOP_HAND = []
STORY_HAND = []
MONSTER_HAND = []
ENV_CARD = None

STORY_DISCARD = []
ATTACK_DISCARD = []
MONSTER_DISCARD = []

class Card():
    def __init__(self, card_type, hand, name, desc, cost, img,
                 damage=None, health=None, attack=None, defense=None, speed=None):
        self.type = card_type
        self.name = name
        self.desc = desc # description
        self.cost = cost
        self.img = img # image
        self.rect = self.img.get_rect()

        if damage:
            self.damage = damage
        if health:
            self.health = health
        if attack:
            self.attack = attack
        if defense:
            self.defense = defense
        if speed:
            self.speed = speed

        hand.append(self)
    
    def play(self):
        # plays the card and discards it
        pass

    def sell(self):
        # gives the player points and discards their card
        pass

    def discard(self):
        # removes card from the current hand and places it in the discard pile
        pass

class AttackCard(Card):
    def __init__(self, damage, element):
        super().__init__()
        self.damage = damage
        self.element = element

# Attack Cards


# Story Cards


# Environment Cards


# Monster Cards

'''
Rather than having a deck class, decks will just be array lists of cards
1. Generate card decks
2. Shuffle decks
3. Draw cards into player hands
4. Draw cards into shop
5. When next turn button is clicked
  1. Play story cards (moves them to middle of screen)
  2. When next turn button is clicked
    1. discard played story cards
    2. Draw random environment
    3. Draw random monsters
'''

def init_decks():
    Card('STORY', STORY_DECK, 'Help Townspeople', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Buy Supplies', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Sell Supplies', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Build Reinforcements', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Check Perimeter', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Observe Livestock', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Talk to Townspeople', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Talk to Farmers', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Watch for Sus Chars', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Speak with Castle Servants', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Reinforce Castle', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Pray', 'dummy description', 1, assets.C0)

    Card('STORY', STORY_DECK, 'Help Townspeople', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Buy Supplies', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Sell Supplies', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Build Reinforcements', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Check Perimeter', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Observe Livestock', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Talk to Townspeople', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Talk to Farmers', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Watch for Sus Chars', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Speak with Castle Servants', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Reinforce Castle', 'dummy description', 1, assets.C0)
    Card('STORY', STORY_DECK, 'Pray', 'dummy description', 1, assets.C0)

    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 1', 'dummy description', 1, assets.C0, damage=1)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 2', 'dummy description', 1, assets.C0, damage=2)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 2', 'dummy description', 1, assets.C0, damage=2)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 2', 'dummy description', 1, assets.C0, damage=2)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 2', 'dummy description', 1, assets.C0, damage=2)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 3', 'dummy description', 1, assets.C0, damage=3)
    Card('ATTACK', ATTACK_DECK, 'Dummy Attack 3', 'dummy description', 1, assets.C0, damage=3)

    # monsters
    Card('MONSTER', MONSTER_DECK, 'Kobold', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Kobold', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Kobold', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Kobold', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Orc', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Orc', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Orc', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Orc', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Skeleton', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Skeleton', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Skeleton', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Skeleton', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Zombie', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Zombie', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Zombie', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Zombie', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gnoll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gnoll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gnoll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gnoll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Spider', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Spider', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Spider', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Spider', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Giant', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Giant', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Giant', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Giant', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Imp', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Imp', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Imp', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Imp', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Vampire', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Vampire', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Vampire', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Vampire', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Werewolf', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Werewolf', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Werewolf', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Werewolf', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Elemental', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Elemental', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Elemental', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Elemental', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Ooze', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Ooze', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Ooze', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Ooze', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gargoyle', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gargoyle', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gargoyle', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Gargoyle', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Troll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Troll', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Dragon', 'dummy description', 1, assets.C0, damage=1, health=1)
    Card('MONSTER', MONSTER_DECK, 'Dragon', 'dummy description', 1, assets.C0, damage=1, health=1)

    # elements


    # environment
    Card('ENV', ENV_DECK, 'Acid', 'dummy description', 1, assets.ACID_ENV)
    Card('ENV', ENV_DECK, 'Fire', 'dummy description', 1, assets.FIRE_ENV)
    Card('ENV', ENV_DECK, 'Ice', 'dummy description', 1, assets.ICE_ENV)
    Card('ENV', ENV_DECK, 'Metal', 'dummy description', 1, assets.METAL_ENV)
    Card('ENV', ENV_DECK, 'Nature', 'dummy description', 1, assets.NATURE_ENV)
    Card('ENV', ENV_DECK, 'Water', 'dummy description', 1, assets.WATER_ENV)
    Card('ENV', ENV_DECK, 'Wind', 'dummy description', 1, assets.WIND_ENV)

    #Card('STORY', STORY_DECK, 'Investigate the Forest', 'dummy description', 2, assets.TEST_IMAGE)
    '''
    finish gen
    '''

    # Shuffling
    #random.shuffle(STORY_DECK)

# BUY ROUND

    # Deal player cards
    #eal_cards(STORY_DECK, 'PLAYERS')
    # insert attack here

    # Deal shop cards
    #deal_cards(STORY_DECK, 'SHOP', 8)
    # insert attack here

def reshuffle():
    if len(STORY_DECK) == 0:
        for card in STORY_DISCARD:
            STORY_DECK.append(card)
            STORY_DISCARD.remove(card)
    if len(ATTACK_DECK) == 0:
        for card in ATTACK_DISCARD:
            ATTACK_DECK.append(card)
            ATTACK_DISCARD.remove(card)
    if len(MONSTER_DECK) == 0:
        for card in MONSTER_DISCARD:
            MONSTER_DECK.append(card)
            MONSTER_DISCARD.remove(card)
    random.shuffle(STORY_DECK)
    random.shuffle(ATTACK_DECK)
    random.shuffle(MONSTER_DECK)

def deal_cards(hand, hand_size=2): # add clause if deck runs out to take discarded cards and reshuffle
    # IMPORTANT!!! Decks must be divisible by the player count
    reshuffle()

    if hand == 'PLAYERS':
        while len(P1_HAND) < hand_size:
                P1_HAND.append(STORY_DECK.pop())
                reshuffle()
                P1_HAND.append(ATTACK_DECK.pop())
                reshuffle()
        while len(P2_HAND) < hand_size:
                P2_HAND.append(STORY_DECK.pop())
                reshuffle()
                P2_HAND.append(ATTACK_DECK.pop())
                reshuffle()
        while len(P3_HAND) < hand_size:
                P3_HAND.append(STORY_DECK.pop())
                reshuffle()
                P3_HAND.append(ATTACK_DECK.pop())
                reshuffle()
        while len(P4_HAND) < hand_size:
                P4_HAND.append(STORY_DECK.pop())
                reshuffle()
                P4_HAND.append(ATTACK_DECK.pop())
                reshuffle()

    if hand == 'SHOP':
        while len(SHOP_HAND) < hand_size:
            SHOP_HAND.append(STORY_DECK.pop())
            reshuffle()
            SHOP_HAND.append(ATTACK_DECK.pop())
            reshuffle()

    if hand == 'MONSTER':
        while len(MONSTER_HAND) < hand_size:
            MONSTER_HAND.append(MONSTER_DECK.pop())
            reshuffle()

def render_card_text(screen, card):
    card_text = assets.CARD_FONT.render( ' (' + str(card.cost) + ') ' + card.name, True, (0, 0, 0))
    screen.blit(card_text, card.rect)

def render_hand(screen, screen_size, font=assets.POINT_FONT, card_dragged=None, game_state = None):

    for card in P1_HAND:
        if card != card_dragged:
            card.rect.left = 2*card.rect.width + P1_HAND.index(card)*card.rect.width
            card.rect.top = screen_size[1] - card.rect.height
            screen.blit(card.img, card.rect)#(20*P1_HAND.index(card), screen_size[1]-300))
            render_card_text(screen, card)

    for card in P2_HAND:
        if card != card_dragged:
            card.rect.left = 0
            card.rect.top = card.rect.height + P2_HAND.index(card)*card.rect.height
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    for card in P3_HAND:
        if card != card_dragged:
            card.rect.left = 2*card.rect.width + P3_HAND.index(card)*card.rect.width
            card.rect.top = 0
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    for card in P4_HAND:
        if card != card_dragged:
            card.rect.left = screen_size[0] - card.rect.width
            card.rect.top = card.rect.height + P4_HAND.index(card)*card.rect.height
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    for card in STORY_DISCARD:
        if card != card_dragged:
            card.rect.left = STORY_DISCARD.index(card)*3 + screen_size[0]//2 + card.rect.width
            card.rect.top = screen_size[1] - 3*card.rect.height
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    for card in ATTACK_DISCARD:
        if card != card_dragged:
            card.rect.left = ATTACK_DISCARD.index(card)*3 + screen_size[0]//2
            card.rect.top = screen_size[1] - 3*card.rect.height
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    for card in MONSTER_DISCARD:
        if card != card_dragged:
            card.rect.left = MONSTER_DISCARD.index(card)*3 + screen_size[0]//2 + 2*card.rect.width
            card.rect.top = screen_size[1] - 3*card.rect.height
            screen.blit(card.img, card.rect)
            render_card_text(screen, card)

    if game_state == 'BUY_ROUND':
        for card in SHOP_HAND:
            if card != card_dragged:
                card.rect.left = 2*card.rect.width + SHOP_HAND.index(card)*card.rect.width
                card.rect.top = card.rect.height*2
                screen.blit(card.img, card.rect)
                render_card_text(screen, card)
        shop_text_surface = font.render('Shop', True, (255, 255, 255), (0, 0, 0))
        screen.blit(shop_text_surface, (screen_size[0]//2.5, 7*shop_text_surface.get_rect().height))

    if game_state == 'STORY_ROUND':
        for card in STORY_HAND:
            if card != card_dragged:
                card.rect.left = 2*card.rect.width + STORY_HAND.index(card)*card.rect.width
                card.rect.top = card.rect.height*2
                screen.blit(card.img, card.rect)
                render_card_text(screen, card)
        shop_text_surface = font.render('Story', True, (255, 255, 255), (0, 0, 0))
        screen.blit(shop_text_surface, (screen_size[0]//2.5, 7*shop_text_surface.get_rect().height))
    
    if game_state == 'COMBAT_ROUND':
        for card in MONSTER_HAND:
            if card != card_dragged:
                card.rect.left = 2*card.rect.width + MONSTER_HAND.index(card)*card.rect.width
                card.rect.top = card.rect.height*2
                screen.blit(card.img, card.rect)
                render_card_text(screen, card)

    if card_dragged != None:
        screen.blit(card_dragged.img, card_dragged.rect)
        render_card_text(screen, card_dragged)



