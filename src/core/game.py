"""Game class."""
from src.models.player import Player
from src.utils import question_loader as ql 

class Game:
    def __init__(self):
        self.player = None
        self.question = ""

    def start_game(self): 
        self.player = Player()

    def next_question(self):
        self.player.advance_level()
        self.player.update_score()

    def load_question(self):
        self.question = ql.random_question(self.player.get_level())
        return self.question

    def process_answer(self, answer):
        if answer == self.question["correct_answer"]:
            return True

        return False

    def end_game(self):
        return True if self.player.get_level() == 10 else False

    def get_player_level(self):
        return self.player.get_level()









# #Responsibilities:

# Control game flow
# Load questions
# Display screens
# Handle player input
# Determine win/lose conditions

# Methods:

# start_game()
# load_questions()
# display_question()
# process_answer()
# next_question()
# end_game()
# restart_game()