from Game import Game


class GameHandler:
    def __init__(self, game_widget):
        self.game = None
        self.widget = game_widget

    def start_game(self):
        self.game = Game.Game()
        self.widget.clear_board()
        initial_cards = self.game.start_game()  # initial 11 cards (5 per player + 1 dealt)
        self.widget.set_initial_cards(initial_cards)
        self.p1_wait_for_move()

    def p1_wait_for_move(self):
        available_hands = self.game.p1.get_available_hands()
        self.widget.set_text_box_text('Choose hand to add the card to')
        self.widget.start_p1_turn(available_hands)

    def p1_play(self, chosen_hand):
        """
        """
        if chosen_hand not in self.game.p1.get_available_hands():
            raise Exception('hand chosen not available !')
        if self.game.get_round_num() == 5:
            if chosen_hand:
                self.game.p1_final_move(chosen_hand)
                self.widget.display_card(player_num=1, row=self.game.get_round_num()-1, hand=chosen_hand,
                                         card=self.game.dealt_card)
                new_dealt_card = self.game.deal_card()
                self.widget.set_dealt_card(new_dealt_card, faced_up=False)
                self.end_game()

        else:
            self.game.p1_play(chosen_hand)
            self.widget.display_card(player_num=1, row=self.game.get_round_num(), hand=chosen_hand, card=self.game.dealt_card)
            new_dealt_card = self.game.deal_card()
            self.widget.set_dealt_card(new_dealt_card, faced_up=False)
            self.p2_play()

    def p2_play(self):
        """
        :return: # of hand to place the card
        """
        self.widget.set_text_box_text("Wait for computer's move")
        chosen_hand = self.game.p2.play()
        self.widget.display_card(player_num=2, row=self.game.get_round_num(), hand=chosen_hand, card=self.game.dealt_card)
        self.game.p2_play(chosen_hand)
        new_dealt_card = self.game.deal_card()
        self.widget.set_dealt_card(new_dealt_card, faced_up=True)
        self.p1_wait_for_move()

    def end_game(self):
        self.widget.end_game()

    def calc_winning_hand(self, hand_number):
        w = self.game.compare_hands(hand_number)   # 0/1/2
        card_to_reveal = self.game.p2.get_card(hand_number, 4)
        if w == 1:
            self.widget.highlight_hand(1, hand_number, card_to_reveal)
        elif w == 2:
            self.widget.highlight_hand(2, hand_number, card_to_reveal)

    def calc_winner(self):
        w = self.game.calculate_winner()
        if w == 1:
            return True
        return False
