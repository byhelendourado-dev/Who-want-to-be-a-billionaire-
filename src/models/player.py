"""Player class."""
from src.utils.constants import game_levels

class Player:

    def __init__(self):
        self.current_score = ""
        self.level = 0
        self.lifeline_usage = 3
``
    def get_score(self):
        return self.current_score

    def get_level(self):
        return self.level


    def update_score(self): 
        self.current_score = game_levels[self.level]
        return self.current_score
        

    def advance_level(self):
        if self.level < 10:
            self.level +=  1
            return self.level
        return 0

    def use_lifeline(self):
        if self.lifeline_usage > 0:
            self.lifeline_usage -= 1
            return True

        return False

