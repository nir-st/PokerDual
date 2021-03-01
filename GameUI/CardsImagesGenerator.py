############################################################
#    Assume:                                               #
#        suits: 0-clubs, 1-spades, 2-diamonds, 3-hearts    #
#        rank : 1 to 14, (ace=14)                          #
############################################################

from CardDeck.Card import Card


def get_card_image_name(card):
    suit = card.get_suit()
    rank = card.get_number()
    if suit == 0:
        i_suit = 'C'
    elif suit == 1:
        i_suit = 'S'
    elif suit == 2:
        i_suit = 'D'
    elif suit == 3:
        i_suit = 'H'
    elif suit > 3 or suit < 0:
        raise Exception('card suit invalid ! (' + suit + ')')
    if rank == 14:
        i_rank = 'A'
    elif rank == 11:
        i_rank = 'J'
    elif rank == 12:
        i_rank = 'Q'
    elif rank == 13:
        i_rank = 'K'
    elif rank < 1 or rank > 14:
        raise Exception('card rank invalid ! (' + rank + ')')
    elif 0 < rank < 11:
        i_rank = rank
    filename = str(i_rank) + i_suit
    return filename
