import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from GameWidget import GameWidget
from MainMenuWidget import MainMenuWidget
import KeyboardHandler


# Globals
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 950


class MainWindow(QMainWindow):

    global WINDOW_HEIGHT
    global WINDOW_WIDTH

    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setWindowTitle('Poker Dual')
        self.resize(WINDOW_HEIGHT, WINDOW_WIDTH)
        self.app = app
        # self.ui = GameUI.GameUI(self)
        self.keyboard_handler = KeyboardHandler.KeyboardHandler(self)
        self.state = "main_menu"  # 'main_menu' / 'in_game'
        self.stacked_widget = self.init_main_stacked_widget()
        self.game_widget = GameWidget(self, WINDOW_HEIGHT, WINDOW_WIDTH)
        self.stacked_widget.addWidget(self.game_widget)
        self.main_menu_widget = MainMenuWidget(self, WINDOW_HEIGHT, WINDOW_WIDTH)
        self.stacked_widget.addWidget(self.main_menu_widget)
        self.main_menu_widget.show()
        self.game_widget.hide()

    def init_main_stacked_widget(self):
        """
        create and return the main stackedWidget object
        """
        stacked_widget = QStackedWidget(self)
        stacked_widget.setObjectName(u"stacked_widget")
        stacked_widget.setGeometry(QRect(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH))
        return stacked_widget

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.keyboard_handler.key_enter(self.state)
        elif event.key() == Qt.Key_Up:
            self.keyboard_handler.key_up(self.state)
        elif event.key() == Qt.Key_Down:
            self.keyboard_handler.key_down(self.state)
        elif event.key() == Qt.Key_Left:
            self.keyboard_handler.key_left(self.state)
        elif event.key() == Qt.Key_Right:
            self.keyboard_handler.key_right(self.state)
        elif event.key() == Qt.Key_Escape:
            self.keyboard_handler.key_esc(self.state)

    def quit(self):
        sys.exit(self.app.exec_())

    def start_game(self):
        self.stacked_widget.setCurrentWidget(self.game_widget)
        self.main_menu_widget.hide()
        self.game_widget.show()
        self.state = 'in_game'
        self.game_widget.start_game()

    def end_game(self):
        self.stacked_widget.setCurrentWidget(self.main_menu_widget)
        self.main_menu_widget.show()
        self.game_widget.hide()
        self.state = 'main_menu'
