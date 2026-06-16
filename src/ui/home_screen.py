"""Main menu screen."""

import tkinter as tk
from tkinter import font as tkfont
from src.utils.constants import *
from src.utils.ui_helpers import _draw_glow_rings, _hex_btn

class HomeScreen(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=BG_DARK)
        self._draw()

    def _draw(self):
        c = tk.Canvas(self, width=W, height=H, bg=BG_DARK, highlightthickness=0)
        c.pack(fill="both", expand=True)

        cx = W // 2
        cy = H // 2  # vertical center

        # Glow rings centered on screen
        _draw_glow_rings(c, cx, cy, [
            ("#0A2299", 230), ("#0B3DCC", 185), ("#0055FF", 145),
            ("#1166FF", 105), ("#003BBF", 70),  ("#051050", 40),
        ])

        # Logo text — vertically centered
        c.create_text(cx, cy - 100, text="Who Wants to Be a", fill=WHITE,
                      font=("Impact", 22, "bold"))
        c.create_text(cx, cy - 52, text="MILLIONAIRE", fill=GOLD,
                      font=("Impact", 50, "bold"))

        # START button — below logo with breathing room
        _hex_btn(c, cx, cy + 80, 240, 56, "START",
                 GOLD, BG_DARK, font=("Impact", 18, "bold"),
                 command=self.master.show_game)
