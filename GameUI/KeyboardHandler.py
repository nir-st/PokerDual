class KeyboardHandler:
    def __init__(self, main_window):
        self.main_window = main_window

    def key_enter(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'main_menu':
            self.main_window.main_menu_widget.select()
        elif state == 'in_game':
            self.main_window.game_widget.key_enter()

    def key_up(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'main_menu':
            self.main_window.main_menu_widget.change_selected('up')

    def key_down(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'main_menu':
            self.main_window.main_menu_widget.change_selected('down')

    def key_left(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'in_game':
            self.main_window.game_widget.key_left()

    def key_right(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'in_game':
            self.main_window.game_widget.key_right()

    def key_esc(self, state):
        """
        :param state: 'main_menu' / 'in_game'
        """
        if state == 'in_game':
            self.main_window.end_game()
