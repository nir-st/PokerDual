"""
evaluating hands
"""

from CardDeck.Card import Card


def evaluate_hand(hand):
    """
    :param hand: a list of 5 cards
    :return: int: value of the hand
    """
    if len(hand) != 5:
        raise Exception("hand has {number_of_cards} cards".format(number_of_cards=hand.get_number_of_cards()))
    are_same_suit, kicker = check_same_suit(hand)
    is_straight, kicker = check_straight(hand)
    ordered = hand_as_ordered_list(hand)
    if are_same_suit and is_straight:
        return 9, kicker  # STRAIGHT FLUSH
    if are_same_suit:
        return [6] + ordered  # FLUSH
    if is_straight:
        return 5, kicker  # STRAIGHT

    cards_dict = generate_card_dict(hand)  # dictionary: {card_rank: card_count_in_hand}

    if len(cards_dict) == 2:  # Four of a Kind OR Full House
        for rank in cards_dict:
            if cards_dict[rank] == 4 or cards_dict[rank] == 1:  # four of a kind

                return tuple([8] + [x[0] for x in sorted(list(cards_dict.items()), key=lambda x: x[1], reverse=True)])  # FOUR OF A KIND
            else:
                return tuple([7] + [x[0] for x in sorted(list(cards_dict.items()), key=lambda x: x[1], reverse=True)])

    elif len(cards_dict) == 3:  # Three of a Kind OR Two Pair
        for rank in cards_dict:
            if cards_dict[rank] == 3:
                return tuple([4] + [x[0] for x in sorted(list(cards_dict.items()), key=lambda x: (x[1], x[0]), reverse=True)])  # THREE OF A KIND
            elif cards_dict[rank] == 2:
                return tuple([3] + [x[0] for x in sorted(list(cards_dict.items()), key=lambda x: (x[1], x[0]), reverse=True)])  # TWO PAIR

    elif len(cards_dict) == 4:  # Pair
        return tuple([2] + [x[0] for x in sorted(list(cards_dict.items()), key=lambda x: (x[1], x[0]), reverse=True)])  # PAIR
    else:
        return tuple([1] + ordered)  # HIGH CARD


def check_straight(cards):
    """
    check if hand is a straight
    returns boolean & updated highest card (in case of straight ending with 5)
    """
    if len(cards) != 5:
        raise Exception("{number_of_cards} cards sent to is_straight()".format(number_of_cards=len(cards)))
    card_nums = [card.get_number() for card in cards]
    if 1 in card_nums:
        if sorted(card_nums) == [1, 2, 3, 4, 5]:
            return True, 5
        if sorted(card_nums) == [1, 10, 11, 12, 13]:
            return True, 14
        return False, 14
    return sorted(card_nums) == list(range(min(card_nums), max(card_nums) + 1)), max(card_nums)


def check_same_suit(cards):
    """
    check the all cards are the same suit
    returns boolean
    """
    kicker = max([card.get_number() for card in cards])
    first_suit = cards[0].get_suit()
    for card in cards[1:]:
        if card.get_suit() != first_suit:
            return False, kicker
    return True, kicker


def generate_card_dict(cards):
    """
    returns a dictionary: {card_rank: card_count_in_hand}
    """
    d = {}
    for card in cards:
        if card.get_number() in d:
            d[card.get_number()] += 1
        else:
            d[card.get_number()] = 1
    return d


def hand_as_ordered_list(cards):
    return sorted([card.get_number() for card in cards], reverse=True)
