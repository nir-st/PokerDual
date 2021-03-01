"""
represents a game
a game consists of two players and a deck
"""

from CardDeck import Deck
from Game.HumanPlayer import HumanPlayer
from Game.ComputerRandomPlayer import ComputerRandomPlayer


class Game:

    def __init__(self):
        self.deck = Deck.Deck()
        self.p1 = HumanPlayer()
        self.p2 = ComputerRandomPlayer()
        self._turn = 1
        self._round = 1
        self.p1_score = 0
        self.p2_score = 0

    def start_game(self):
        """
        play all regular turns
        """
        initial_cards = []
        for i in range(5):
            card = self.deck.deal_card()
            self.p1.append_card(i+1, card)
            initial_cards.append(card)
        for i in range(5):
            card = self.deck.deal_card()
            self.p2.append_card(i+1, card)
            initial_cards.append(card)

        dealt_card = self.deck.deal_card()
        initial_cards.append(dealt_card)

        self.dealt_card = dealt_card

        return initial_cards

    def p1_play(self, chosen_hand):
        self.p1.append_card(chosen_hand, self.dealt_card)
        self._turn += 1

    def p2_play(self, chosen_hand):
        self.p2.append_card(chosen_hand, self.dealt_card)
        if self._turn % 10 == 0:
            self._round += 1
        self._turn += 1

    def p1_final_move(self, chosen_hand):
        self.p1.replace_final_card(chosen_hand, self.dealt_card)

    def p2_final_move(self, chosen_hand):
        self.p2.replace_final_card(chosen_hand, self.dealt_card)

    def get_round_num(self):
        return self._round

    def deal_card(self):
        """
        deal a new card and return it
        """
        self.dealt_card = self.deck.deal_card()
        return self.dealt_card

    def compare_hands(self, hand_number):
        """
        :param hand_number: int, 1-5
        :return: int, 0/1/2 (draw, p1 wins, p2 wins)
        """
        player1_hand_score = self.p1.get_hand_score(hand_number)
        player2_hand_score = self.p2.get_hand_score(hand_number)

        if player1_hand_score > player2_hand_score:
            self.p1_score += 1
            return 1
        if player1_hand_score < player2_hand_score:
            self.p2_score += 1
            return 2
        return 0

    def calculate_winner(self):
        if self.p1_score > self.p2_score:
            return 1
        return 2
