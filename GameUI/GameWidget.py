from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QHBoxLayout, QLayout, QFrame
from GameHandler import GameHandler
import CardsImagesGenerator
from GamePointer import GamePointer


SPACE_BETWEEN_CARDS_SAME_ROW = 20
SPACE_BETWEEN_ROWS = 40
CARD_IMAGES_PATH = "PokerSini\\GameUI\\cards_images\\"
POINTER_HEIGHT = 375
FACED_DOWN_CARD_FILENAME = 'Blue_back.jpg'
WINNING_MESSAGE = 'YOU WON! YOU BEAST!'
LOSING_MESSAGE = 'YOU LOST YOU FUCKING LOSER'

class GameWidget(QWidget):

    global CARD_IMAGES_PATH
    global SPACE_BETWEEN_ROWS
    global SPACE_BETWEEN_CARDS_SAME_ROW
    global POINTER_HEIGHT
    global FACED_DOWN_CARD_FILENAME
    global WINNING_MESSAGE
    global LOSING_MESSAGE

    def __init__(self, main_window, window_height, window_width):
        super().__init__()
        self.game_handler = GameHandler(self)

        # lists of 5 widgets
        self.p2_rows_widgets = self.init_player_rows_widgets(initial_height=0)
        self.p1_rows_widgets = self.init_player_rows_widgets(initial_height=360)

        # 2D lists. [row][hand]
        self.p2_card_widgets = []
        self.p1_card_widgets = []

        self.dealt_card = self.init_dealt_card_ui()
        self.instructions_label = self.init_instructions_label(height=window_height-180)
        self.init_table_card_widgets()
        self.pointer = GamePointer(self, POINTER_HEIGHT)

        self.text_box = self.init_text_box()

        self.state = 0  # 0: playing, 1-5: showing final hands

    def init_text_box(self):
        text_box = QLabel(self)
        text_box.setWordWrap(True)
        text_box.setAlignment(Qt.AlignCenter)
        text_box.setGeometry(QRect(725, 435, 190, 100))
        font = QFont()
        font.setPointSize(12)
        text_box.setFont(font)
        text_box.setStyleSheet("color: blue; border: 1px solid blue")
        return text_box

    def set_text_box_text(self, text):
        self.text_box.setText(text)

    def init_dealt_card_ui(self):
        dealt_card = QLabel(self)
        dealt_card.setGeometry(QRect(770, 250, 110, 160))
        dealt_card.setMinimumSize(QSize(110, 160))
        dealt_card.setMaximumSize(QSize(110, 160))
        dealt_card.setScaledContents(True)
        return dealt_card

    def set_dealt_card(self, card, faced_up=True):
        if faced_up:
            file_name = CardsImagesGenerator.get_card_image_name(card)
        else:
            file_name = FACED_DOWN_CARD_FILENAME
        self.dealt_card.setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))

    def init_instructions_label(self, height):
        game_instructions = QLabel(self)
        game_instructions.setGeometry(QRect(290, height, 371, 16))
        font = QFont()
        font.setPointSize(9)
        game_instructions.setFont(font)
        game_instructions.setStyleSheet(u"color: blue")
        game_instructions.setText("Use keyboard arrows and enter key. Press ESC to quit the game.")
        game_instructions.setWordWrap(True)
        return game_instructions

    def init_table_card_widgets(self):
        for i in range(5):
            layout = QHBoxLayout(self.p2_rows_widgets[i])
            layout.setSizeConstraint(QLayout.SetFixedSize)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(SPACE_BETWEEN_CARDS_SAME_ROW)
            cards = []
            for j in range(5):
                card = QLabel(self.p2_rows_widgets[i])
                card.setMinimumSize(QSize(110, 160))
                card.setMaximumSize(QSize(110, 160))
                card.setScaledContents(True)
                layout.addWidget(card)
                cards.append(card)
            self.p2_card_widgets.append(cards)

        for i in range(5):
            layout = QHBoxLayout(self.p1_rows_widgets[i])
            layout.setSizeConstraint(QLayout.SetFixedSize)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(SPACE_BETWEEN_CARDS_SAME_ROW)
            cards = []
            for j in range(5):
                card = QLabel(self.p1_rows_widgets[i])
                card.setMinimumSize(QSize(110, 160))
                card.setMaximumSize(QSize(110, 160))
                card.setScaledContents(True)
                layout.addWidget(card)
                cards.append(card)
            self.p1_card_widgets.append(cards)

    def init_player_rows_widgets(self, initial_height):
        h = initial_height
        widgets = []
        for i in range(5):
            widget = QWidget(self)
            widget.setGeometry(QRect(60, h + SPACE_BETWEEN_ROWS, 671, 211))
            widgets.append(widget)
            h = h + SPACE_BETWEEN_ROWS
        return widgets

    def set_initial_cards(self, initial_cards):
        """
        :param initial_cards: list, 11 initial cards (5 per player + 1 dealt)
        """
        i = 0
        for card in self.p1_card_widgets[0]:
            file_name = CardsImagesGenerator.get_card_image_name(initial_cards[i])
            card.setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))
            i += 1
        for card in self.p2_card_widgets[0]:
            file_name = CardsImagesGenerator.get_card_image_name(initial_cards[i])
            card.setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))
            i += 1
        self.set_dealt_card(initial_cards[i])

    def start_game(self):
        self.game_handler.start_game()

    def key_right(self):
        self.pointer.move_right()

    def key_left(self):
        self.pointer.move_left()

    def key_enter(self):
        if self.state == 0:
            self.pointer.act()
        elif self.state < 5:
            self.game_handler.calc_winning_hand(self.state-1)
            self.state += 1
        elif self.state == 5:
            self.game_handler.calc_winning_hand(self.state - 1)
            won = self.game_handler.calc_winner()
            if won:
                self.set_text_box_text(WINNING_MESSAGE)
            else:
                self.set_text_box_text(LOSING_MESSAGE)
            self.state = 6

    def start_p1_turn(self, available_hands):
        self.pointer.activate(available_hands)

    def choose_hand(self, chosen_hand):
        """
        :return:
        """
        self.game_handler.p1_play(chosen_hand)

    def display_card(self, player_num, row, hand, card):
        """
        :param player_num: int, 1/2
        :param row: int
        :param hand: int, 1-5
        :param card: card object
        """
        file_name = CardsImagesGenerator.get_card_image_name(card)
        if player_num == 1:
            self.p1_card_widgets[row][hand-1].setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))
        elif player_num == 2:
            if row == 4:
                self.p2_card_widgets[row][hand - 1].setPixmap(QPixmap(CARD_IMAGES_PATH + FACED_DOWN_CARD_FILENAME))
            else:
                self.p2_card_widgets[row][hand-1].setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))

    def clear_board(self):
        self.state = 0
        for row in self.p2_card_widgets:
            for card in row:
                card.setPixmap(QPixmap())
                card.setStyleSheet('')
        for row in self.p1_card_widgets:
            for card in row:
                card.setPixmap(QPixmap())
                card.setStyleSheet('')

    def end_game(self):
        self.state = 1
        self.set_text_box_text("Press enter to reveal hand")

    def highlight_hand(self, player_number, hand_number, card_to_reveal):
        if player_number == 1:
            for i in range(5):
                self.p1_card_widgets[i][hand_number].setStyleSheet('border: 2px solid yellow')
        elif player_number == 2:
            for i in range(5):
                self.p2_card_widgets[i][hand_number].setStyleSheet('border: 2px solid yellow')
        file_name = CardsImagesGenerator.get_card_image_name(card_to_reveal)
        self.p2_card_widgets[4][hand_number].setPixmap(QPixmap(CARD_IMAGES_PATH + file_name))
