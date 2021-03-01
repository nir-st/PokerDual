from statistics import mean

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


# globals
IMAGE_PATH = 'PokerSini\\GameUI\\cards_images\\arrow.png'
ARROW_SIZE = 32
ARROW_POS_1 = 97
ARROW_POS_2 = 227
ARROW_POS_3 = 357
ARROW_POS_4 = 487
ARROW_POS_5 = 617


class GamePointer:

    global IMAGE_PATH
    global ARROW_SIZE

    def __init__(self, game_widget, pointer_height):
        """

        :param game_widget:
        :param availablel_hands: list of integers
        """
        self.pointer_height = pointer_height
        self.available_hands = [1, 2, 3, 4, 5]
        self.location = 3  # (1-5)
        self.widget = game_widget
        self.pointer = self.init_pointer()
        self.active = False

    def init_pointer(self):
        pointer = QLabel(self.widget)
        pointer.setGeometry(QRect(ARROW_POS_3, self.pointer_height, ARROW_SIZE, ARROW_SIZE))
        pointer.setPixmap(QPixmap(IMAGE_PATH))
        pointer.setScaledContents(True)
        return pointer

    def activate(self, available_hands):
        self.active = True
        self.pointer.show()
        self.location = min(available_hands, key=lambda x: abs(x-mean(available_hands)))
        self.available_hands = available_hands
        self.move(self.location)

    def move(self, new_location):
        """
        move the pointer to a new location
        :param new_location: int, number between 1-5
        """
        if new_location == 1:
            self.pointer.move(ARROW_POS_1, self.pointer_height)
        elif new_location == 2:
            self.pointer.move(ARROW_POS_2, self.pointer_height)
        elif new_location == 3:
            self.pointer.move(ARROW_POS_3, self.pointer_height)
        elif new_location == 4:
            self.pointer.move(ARROW_POS_4, self.pointer_height)
        elif new_location == 5:
            self.pointer.move(ARROW_POS_5, self.pointer_height)

    def move_left(self):
        if self.location > 1:
            positions = [pos for pos in self.available_hands if pos < self.location]
            if positions:
                self.location = max(positions)
                self.move(self.location)

    def move_right(self):
        if self.location < 5:
            positions = [pos for pos in self.available_hands if pos > self.location]
            if positions:
                self.location = min(positions)
                self.move(self.location)

    def act(self):
        if self.active:
            self.pointer.hide()
            self.active = False
            self.widget.choose_hand(self.location)
