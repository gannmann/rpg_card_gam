import pygame as pg
import assets
pg.init()

class Card():
    def __init__(self, uid, hand, name, desc, img):
        self.uid = uid # unique to each individual card e.g. 2 of the same attack cards will have different ids
        self.hand = hand # Deck, Player 1, 2, 3, 4, or Discard; lists
        self.name = name
        self.desc = desc # description
        self.img = img # image

    def play(self):
        # plays the card and discards it
        pass

    def sell(self):
        # gives the player points and discards their card
        pass

    def discard(self):
        # removes card from the current hand and places it in the discard pile
        pass

    def render(self, screen):
        # location depends on order in hand and which hand
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

