"""
This class represents a card
Assume:
    suits: 0-clubs, 1-spades, 2-diamonds, 3-hearts
    rank : 2 to 14, (ace=14)
"""


class Card:
    def __init__(self, suit, rank):
        if rank < 2 or rank > 14:
            raise Exception("invalid card rank: {rank}".format(rank=rank))
        if suit not in range(4):
            raise Exception("invalid card sign: {suit}".format(suit=suit))
        self._suit = suit
        self._rank = rank

    def get_number(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def get_value(self):
        return self._rank

    def __repr__(self):
        return '{rank}{suit}'.format(rank=rank_names[self._rank], suit=suit_names[self._suit])


suit_names = {
    0: '♣',
    1: '♠',
    2: '♦',
    3: '♥'
}


rank_names = {
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
}