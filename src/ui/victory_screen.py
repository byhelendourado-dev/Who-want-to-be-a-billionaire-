"""End game screen."""

import tkinter as tk
from tkinter import font as tkfont
from src.utils.constants import *
from src.utils.ui_helpers import _draw_glow_rings, _hex_btn, _prize_box

class VictoryScreen(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=BG_DARK)
        self._draw()

    def _draw(self):
        c = tk.Canvas(self, width=W, height=H, bg=BG_DARK, highlightthickness=0)
        c.pack(fill="both", expand=True)

        cx = W // 2

        _draw_glow_rings(c, cx, 230, [
            ("#0A2299", 210), ("#0B3DCC", 170), ("#0055FF", 130),
            ("#1166FF", 90),  ("#003BBF", 60),  ("#051050", 35),
        ])

        c.create_text(cx, 165, text="Who Wants to Be a", fill=WHITE,
                      font=("Impact", 22, "bold"))
        c.create_text(cx, 215, text="MILLIONAIRE", fill=GOLD,
                      font=("Impact", 50, "bold"))

        c.create_text(cx, 300, text="CONGRATULATIONS!", fill=GOLD,
                      font=("Impact", 34, "bold"))
        c.create_text(cx, 345, text="You Win!", fill=WHITE,
                      font=("Arial", 16))

        _prize_box(c, cx, 415, 300, 65, "25.000 €")

        _hex_btn(c, cx, 505, 230, 46, "PLAY AGAIN",
                 WHITE, BG_DARK, font=("Impact", 13, "bold"),
                 border=BTN_BORDER, command=self.master.show_home)
        _hex_btn(c, cx, 568, 230, 46, "EXIT",
                 WHITE, BG_DARK, font=("Impact", 13, "bold"),
                 border=BTN_BORDER, command=self.master.quit)
