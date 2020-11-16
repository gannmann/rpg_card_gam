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
DISCARD = []

class Card():
    def __init__(self, card_type, hand, name, desc, cost, img):
        self.type = card_type
        self.name = name
        self.desc = desc # description
        self.cost = cost
        self.img = img # image
        self.rect = self.img.get_rect()
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
    Card('STORY', STORY_DECK, 'Help Townspeople', 'dummy description', 1, assets.C1)
    Card('STORY', STORY_DECK, 'Buy Supplies', 'dummy description', 1, assets.C2)
    Card('STORY', STORY_DECK, 'Sell Supplies', 'dummy description', 1, assets.C3)
    Card('STORY', STORY_DECK, 'Build Reinforcements', 'dummy description', 1, assets.C4)
    Card('STORY', STORY_DECK, 'Check Perimeter', 'dummy description', 1, assets.C5)
    Card('STORY', STORY_DECK, 'Observe Livestock', 'dummy description', 1, assets.C6)
    Card('STORY', STORY_DECK, 'Talk to Townspeople', 'dummy description', 1, assets.C7)
    Card('STORY', STORY_DECK, 'Talk to Farmers', 'dummy description', 1, assets.C8)
    Card('STORY', STORY_DECK, 'Watch for Sus Chars', 'dummy description', 1, assets.C9)
    Card('STORY', STORY_DECK, 'Speak with Castle Servants', 'dummy description', 1, assets.C10)
    Card('STORY', STORY_DECK, 'Reinforce Castle', 'dummy description', 1, assets.C11)
    Card('STORY', STORY_DECK, 'Pray', 'dummy description', 1, assets.C12)

    Card('STORY', STORY_DECK, 'Help Townspeople', 'dummy description', 1, assets.C1)
    Card('STORY', STORY_DECK, 'Buy Supplies', 'dummy description', 1, assets.C2)
    Card('STORY', STORY_DECK, 'Sell Supplies', 'dummy description', 1, assets.C3)
    Card('STORY', STORY_DECK, 'Build Reinforcements', 'dummy description', 1, assets.C4)
    Card('STORY', STORY_DECK, 'Check Perimeter', 'dummy description', 1, assets.C5)
    Card('STORY', STORY_DECK, 'Observe Livestock', 'dummy description', 1, assets.C6)
    Card('STORY', STORY_DECK, 'Talk to Townspeople', 'dummy description', 1, assets.C7)
    Card('STORY', STORY_DECK, 'Talk to Farmers', 'dummy description', 1, assets.C8)
    Card('STORY', STORY_DECK, 'Watch for Sus Chars', 'dummy description', 1, assets.C9)
    Card('STORY', STORY_DECK, 'Speak with Castle Servants', 'dummy description', 1, assets.C10)
    Card('STORY', STORY_DECK, 'Reinforce Castle', 'dummy description', 1, assets.C11)
    Card('STORY', STORY_DECK, 'Pray', 'dummy description', 1, assets.C12)

    #Card('STORY', STORY_DECK, 'Investigate the Forest', 'dummy description', 2, assets.TEST_IMAGE)
    '''
    finish gen
    '''

    # Shuffling
    random.shuffle(STORY_DECK)

# BUY ROUND

    # Deal player cards
    deal_cards(STORY_DECK, 'PLAYERS')
    # insert attack here

    # Deal shop cards
    deal_cards(STORY_DECK, 'SHOP', 8)
    # insert attack here
    

def deal_cards(deck, hand, hand_size=4): # add clause if deck runs out to take discarded cards and reshuffle
    # IMPORTANT!!! Decks must be divisible by the player count
    if hand == 'PLAYERS':
        while (len(deck) != 0) and (len(P4_HAND) < hand_size):
            P1_HAND.append(deck.pop(len(deck)-1))
            P2_HAND.append(deck.pop(len(deck)-1))
            P3_HAND.append(deck.pop(len(deck)-1))
            P4_HAND.append(deck.pop(len(deck)-1))

    if hand == 'SHOP':
        for i in range(hand_size):
            SHOP_HAND.append(deck.pop(len(deck)-1))



def render_hand(screen, screen_size, font=assets.POINT_FONT, card_dragged=None):
    if card_dragged != None:
        screen.blit(card_dragged.img, card_dragged.rect)

    for card in P1_HAND:
        card.rect.left = 2*card.rect.width + P1_HAND.index(card)*card.rect.width
        card.rect.top = screen_size[1] - card.rect.height
        screen.blit(card.img, card.rect)#(20*P1_HAND.index(card), screen_size[1]-300))

    for card in P2_HAND:
        card.rect.left = 0
        card.rect.top = card.rect.height + P2_HAND.index(card)*card.rect.height
        screen.blit(card.img, card.rect)

    for card in P3_HAND:
        card.rect.left = 2*card.rect.width + P3_HAND.index(card)*card.rect.width
        card.rect.top = 0
        screen.blit(card.img, card.rect)

    for card in P4_HAND:
        card.rect.left = screen_size[0] - card.rect.width
        card.rect.top = card.rect.height + P4_HAND.index(card)*card.rect.height
        screen.blit(card.img, card.rect)

    for card in DISCARD:
        card.rect.left = DISCARD.index(card)*3 + screen_size[0]//2 - card.rect.width
        card.rect.top = screen_size[1] - 3*card.rect.height 
        screen.blit(card.img, card.rect)
    discard_text_surface = font.render('Discard', True, (255, 255, 255), (0, 0, 0))
    screen.blit(discard_text_surface, (screen_size[0]//2.5, screen_size[1]-12*discard_text_surface.get_rect().height))

    for card in SHOP_HAND:
        if card != card_dragged:
            card.rect.left = 2*card.rect.width + SHOP_HAND.index(card)*card.rect.width
            card.rect.top = card.rect.height*2
            screen.blit(card.img, card.rect)
    shop_text_surface = font.render('Shop', True, (255, 255, 255), (0, 0, 0))
    screen.blit(shop_text_surface, (screen_size[0]//2.5, 7*shop_text_surface.get_rect().height))

