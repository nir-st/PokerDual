"""
This class represents a deck of cards
Assume:
    suits: 0-clubs, 1-spades, 2-diamonds, 3-hearts
    rank : 1 to 14, (ace=14)
"""

import random
from CardDeck.Card import Card


def generate_deck():
    """
    :return: a deck of 52 cards
    """
    d = []
    for i in range(4):
        for j in range(13):
            d.append(Card(i, j+2))
    return d


def shuffle_deck(d):
    random.shuffle(d)


class Deck:
    def __init__(self):
        self._stack = generate_deck()
        shuffle_deck(self._stack)
        self._dealt = []

    def deal_card(self):
        card = self._stack.pop()
        self._dealt.append(card)
        return card

    def get_number_of_cards_left(self):
        return len(self._stack)

    def get_number_of_cards_dealt(self):
        return len(self._dealt)
