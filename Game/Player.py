"""
a player has a hand
"""

from Game.Hand import Hand


class Player:
    def __init__(self):
        self._hands = []
        for i in range(5):
            self._hands.append(Hand())
        self._available_hands = [1, 2, 3, 4, 5]

    def get_hand(self, hand_num):
        return self._hands[hand_num]

    def get_available_hands(self):
        return self._available_hands

    def append_card(self, hand, card):
        self._hands[hand-1].append_card(card)
        if len(self._available_hands) == 1:
            self._available_hands = [1, 2, 3, 4, 5]
        else:
            self._available_hands.remove(hand)

    def replace_final_card(self, hand, card):
        self._hands[hand - 1].discard()
        self._hands[hand - 1].append_card(card)

    def get_hand_score(self, hand_number):
        return self._hands[hand_number].get_final_value()

    def get_card(self, hand_num, card_num):
        return self._hands[hand_num].get_card(card_num)
