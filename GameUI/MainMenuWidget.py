from PyQt5 import QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


###############
### GLOBALS ###
###############

# Main menu fonts
FONT_MAIN_MENU_POINTING_TO = QFont()
FONT_MAIN_MENU_POINTING_TO.setFamily("Lucida Sans Typewriter")
FONT_MAIN_MENU_POINTING_TO.setPointSize(34)
FONT_MAIN_MENU_POINTING_TO.setBold(True)
FONT_MAIN_MENU_POINTING_TO.setWeight(75)

FONT_MAIN_MENU_REGULAR = QFont()
FONT_MAIN_MENU_REGULAR.setFamily("Lucida Sans Typewriter")
FONT_MAIN_MENU_REGULAR.setPointSize(32)

# instructions font
FONT_INSTRUCTIONS = QFont()
FONT_INSTRUCTIONS.setFamily("Miriam Fixed")
FONT_INSTRUCTIONS.setPointSize(10)

MAIN_MENU_INSTRUCTIONS_TEXT = "Use keyboard arrows and enter key"


class MainMenuWidget(QWidget):
    global FONT_MAIN_MENU_POINTING_TO
    global FONT_MAIN_MENU_REGULAR
    global FONT_INSTRUCTIONS
    global MAIN_MENU_INSTRUCTIONS_TEXT

    def __init__(self, main_window, window_height, window_width):
        super().__init__()
        self.resize(window_height, window_width)
        self.setObjectName(u"MainMenu")
        self.main_window = main_window
        self.main_stacked_widget = main_window.stacked_widget
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(335, 220, 272, 251))
        self.main_menu_buttons_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.main_menu_buttons_layout.setObjectName(u"main_menu_buttons_layout")
        self.main_menu_buttons_layout.setContentsMargins(0, 0, 0, 0)

        # Start Game button
        self.start_game_button = self.generate_start_button()
        self.main_menu_buttons_layout.addWidget(self.start_game_button)

        # Quit button
        self.quit_button = self.generate_quit_button()
        self.main_menu_buttons_layout.addWidget(self.quit_button)

        # instructions
        self.lbl_instructions = self.generate_menu_instructions(height=window_height - 190)
        self.lbl_instructions.setText(MAIN_MENU_INSTRUCTIONS_TEXT)

        self.selected = 'start_game'  # 'start_game' / 'quit

    def generate_start_button(self):
        start_game_button = QLabel(self.verticalLayoutWidget)
        start_game_button.setObjectName(u"btn_start_game")
        start_game_button.setText('START GAME')
        start_game_button.setFont(FONT_MAIN_MENU_POINTING_TO)
        start_game_button.setStyleSheet(u"color: red")
        start_game_button.setAlignment(QtCore.Qt.AlignCenter)
        return start_game_button

    def generate_quit_button(self):
        quit_button = QLabel(self.verticalLayoutWidget)
        quit_button.setObjectName(u"btn_Quit")
        quit_button.setText('QUIT')
        quit_button.setFont(FONT_MAIN_MENU_REGULAR)
        quit_button.setAlignment(QtCore.Qt.AlignCenter)
        return quit_button

    def generate_menu_instructions(self, height):
        instructions_label = QLabel(self)
        instructions_label.setObjectName(u"lbl_instructions")
        instructions_label.setGeometry(QRect(330, height, 280, 40))
        instructions_label.setFont(FONT_INSTRUCTIONS)
        instructions_label.setStyleSheet(u"color: blue")
        instructions_label.setAlignment(QtCore.Qt.AlignCenter)
        return instructions_label

    def change_selected(self, direction):
        """
        chage selection from main menu
        :param direction: string. 'up' or 'down'
        """
        if direction == 'up' and self.selected == 'quit':
            self.start_game_button.setFont(FONT_MAIN_MENU_POINTING_TO)
            self.quit_button.setFont(FONT_MAIN_MENU_REGULAR)
            self.start_game_button.setStyleSheet('color: red')
            self.quit_button.setStyleSheet('color: black')
            self.selected = 'start_game'
        elif direction == 'down' and self.selected == 'start_game':
            self.start_game_button.setFont(FONT_MAIN_MENU_REGULAR)
            self.quit_button.setFont(FONT_MAIN_MENU_POINTING_TO)
            self.start_game_button.setStyleSheet('color: black')
            self.quit_button.setStyleSheet('color: red')
            self.selected = 'quit'

    def select(self):
        if self.selected == 'start_game':
            self.main_window.start_game()
        else:
            self.main_window.quit()
