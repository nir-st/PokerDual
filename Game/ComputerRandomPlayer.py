import random
from PyQt5.QtCore import QEventLoop, QTimer
from Game import Player


THINKING_TIME = 0.2  # in sec


class ComputerRandomPlayer(Player.Player):

    global THINKING_TIME

    def play(self):
        loop = QEventLoop()
        QTimer.singleShot(THINKING_TIME * 1000, loop.quit)
        loop.exec_()
        return random.choice(self.get_available_hands())
