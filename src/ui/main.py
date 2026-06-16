
import tkinter as tk
from tkinter import font as tkfont
from src.ui.defeat_screen import DefeatScreen
from src.ui.home_screen import HomeScreen
from src.ui.game_screen import GameScreen
from src.ui.victory_screen import VictoryScreen
from src.utils.constants import *
from src.core.game import Game

class MillionaireApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Who Wants to Be a Millionaire")
        self.configure(bg=BG_DARK)
        self.resizable(False, False)
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        self.current_frame = None
        self.show_home()
        self.game = Game()

        self.game_question = ""
        self.game_options = []
        self.game_correct = 0
        self.game_end = False
        self.game_level = 0
        self.start_game()
        self._questions()

    def _switch(self, FrameClass, **kwargs):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = FrameClass(self, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

    def show_home(self):         self._switch(HomeScreen)
    def show_victory(self):      self._switch(VictoryScreen)
    def show_defeat(self, *a):   self._switch(DefeatScreen)

    def show_game(self):
        self.start_game()
        self._questions()  
        self._switch(GameScreen)

    def next_question(self):
        self._questions()
        self._switch(GameScreen)

    def start_game(self):
        self.game.start_game()

    def _questions(self):
        self.game.next_question()
        q = self.game.load_question()

        self.game_question = q["question"]
        self.game_correct = q["correct_answer"]
        print(self.game_correct)
        self.game_options  = [
            ("A", q["answers"][0],  BTN_CORRECT),
            ("B", q["answers"][1],  BTN_BLUE),
            ("C", q["answers"][2],  BTN_BLUE),
            ("D", q["answers"][3],  BTN_BLUE),
        ]

        self.game_end = self.game.end_game()
        self.game_level = self.game.get_player_level()
  