"""
This class represents a hand.
A hand consists of 5 cards.
"""
from random import random, randint
from Game import HandEvaluator
from CardDeck import Card


class Hand:
    def __init__(self):
        self._cards = []

    def get_number_of_cards(self):
        return len(self._cards)

    def append_card(self, card):
        """
        appends a card
        """
        if len(self._cards) > 5:
            raise Exception("Attempting to append a card to a hand with 5 cards")
        self._cards.append(card)

    def get_final_value(self):
        """

        :return:
        """
        if len(self._cards) != 5:
            raise Exception("hand only has {number_of_cards} cards".format(number_of_cards=len(self._cards)))
        return HandEvaluator.evaluate_hand(self._cards)

    def discard(self):
        self._cards.pop(len(self._cards) - 1)

    def get_card(self, card_num):
        return self._cards[card_num]

    def __repr__(self):
        s = ""
        for card in self._cards:
            s += str(card) + ', '
        return s[:-2]

    def __gt__(self, other):
        return self.get_final_value() > other.get_final_value()

    def __lt__(self, other):
        return self.get_final_value() < other.get_final_value()

    def __eq__(self, other):
        return self.get_final_value() == other.get_final_value()


def gen_random_hand(kind=None):
    hand = Hand()
    generated = []
    if not kind:
        for i in range(5):
            rank = randint(2, 14)
            suit = randint(0, 3)
            while (rank, suit) in generated:
                rank = randint(2, 14)
                suit = randint(0, 3)
            hand.append_card(Card.Card(suit, rank))
            generated.append((rank, suit))

    elif kind == 'p':  # pair
        pair_rank = randint(2, 14)
        hand.append_card(Card.Card(0, pair_rank))
        hand.append_card(Card.Card(1, pair_rank))
        generated.append(pair_rank)
        for i in range(3):
            rank = randint(2, 14)
            suit = randint(0, 3)
            while rank in generated:
                rank = randint(2, 14)
                suit = randint(0, 3)
            hand.append_card(Card.Card(suit, rank))
            generated.append(rank)

    elif kind == 'tp':  # two pair
        kicker_rank = randint(2, 14)
        kicker_suit = randint(0, 3)
        hand.append_card(Card.Card(kicker_suit, kicker_rank))
        generated.append(kicker_rank)

        for i in range(2):
            rank = randint(2, 14)
            suit = randint(0, 2)
            while rank in generated:
                rank = randint(2, 14)
                suit = randint(0, 2)
            hand.append_card(Card.Card(suit, rank))
            hand.append_card(Card.Card(suit+1, rank))
            generated.append(rank)

    elif kind == 'tk':  # three of a kind
        triplets_rank = randint(2, 14)
        triplets_suit = randint(0, 1)
        hand.append_card(Card.Card(triplets_suit, triplets_rank))
        hand.append_card(Card.Card(triplets_suit+1, triplets_rank))
        hand.append_card(Card.Card(triplets_suit+2, triplets_rank))
        generated.append(triplets_rank)

        for i in range(2):
            rank = randint(2, 14)
            suit = randint(0, 2)
            while rank in generated:
                rank = randint(2, 14)
                suit = randint(0, 3)
            hand.append_card(Card.Card(suit, rank))
            generated.append(rank)

    elif kind == 'st':
        first_rank = randint(2, 10)
        hand.append_card(Card.Card(0, first_rank))
        hand.append_card(Card.Card(1, first_rank+1))
        hand.append_card(Card.Card(2, first_rank+2))
        hand.append_card(Card.Card(3, first_rank+3))
        hand.append_card(Card.Card(0, first_rank+4))

    elif kind == 'fl':
        suit = randint(0, 3)

        rank = randint(2, 12)
        hand.append_card(Card.Card(suit, rank))
        hand.append_card(Card.Card(suit, rank+2))
        generated.append(rank)
        generated.append(rank+2)

        for i in range(3):
            rank = randint(2, 14)
            while rank in generated:
                rank = randint(2, 14)
            hand.append_card(Card.Card(suit, rank))
            generated.append(rank)

    elif kind == 'fh':
        rank1 = randint(2, 14)
        rank2 = randint(2, 14)
        while rank1 == rank2:
            rank2 = randint(2, 14)

        suit = randint(0, 1)
        hand.append_card(Card.Card(suit, rank1))
        hand.append_card(Card.Card(suit+1, rank1))

        hand.append_card(Card.Card(suit, rank2))
        hand.append_card(Card.Card(suit+1, rank2))
        hand.append_card(Card.Card(suit+2, rank2))

    elif kind == 'fk':
        rank1 = randint(2, 14)
        rank2 = randint(2, 14)
        while rank1 == rank2:
            rank2 = randint(2, 14)

        suit = randint(0, 3)
        hand.append_card(Card.Card(suit, rank1))

        hand.append_card(Card.Card(0, rank2))
        hand.append_card(Card.Card(1, rank2))
        hand.append_card(Card.Card(2, rank2))
        hand.append_card(Card.Card(3, rank2))

    elif kind == 'sf':
        first_rank = randint(2, 10)
        suit = randint(0, 3)
        hand.append_card(Card.Card(suit, first_rank))
        hand.append_card(Card.Card(suit, first_rank+1))
        hand.append_card(Card.Card(suit, first_rank+2))
        hand.append_card(Card.Card(suit, first_rank+3))
        hand.append_card(Card.Card(suit, first_rank+4))

    return hand
