
class GameStats():
    """ Trak stats for invaders from python """
    def __init__(self, infrompy_setings):
        """ Initialize stats. """
        self.infrompy_setings = infrompy_setings
        self.reset_stats()

        # Start the game in an inactive state.
        self.game_active =  False

        # high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        """ Initialize stats that can change during the game. """
        self.ships_left = self.infrompy_setings.ship_limit
        self.score = 0
        self.level = 1
