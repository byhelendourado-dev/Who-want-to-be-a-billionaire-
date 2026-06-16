
import tkinter as tk
from tkinter import font as tkfont
from src.utils.constants import *
from src.utils.ui_helpers import _draw_glow_rings, _hex_btn, _prize_box_red

class DefeatScreen(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=BG_DARK)
        self._draw()

    def _draw(self):
        c = tk.Canvas(self, width=W, height=H, bg=BG_DARK, highlightthickness=0)
        c.pack(fill="both", expand=True)

        cx = W // 2

        # Red glow rings for defeat mood
        _draw_glow_rings(c, cx, 230, [
            ("#3D0000", 210), ("#660000", 170), ("#990000", 130),
            ("#BB1111", 90),  ("#440000", 60),  ("#1A0000", 35),
        ])

        # Logo — dimmed/white
        c.create_text(cx, 165, text="Who Wants to Be a", fill="#AAAACC",
                      font=("Impact", 22, "bold"))
        c.create_text(cx, 215, text="MILLIONAIRE", fill="#CC4444",
                      font=("Impact", 50, "bold"))

        # Big X mark
        c.create_text(cx, 295, text="✗", fill="#FF2222",
                      font=("Arial", 52, "bold"))

        c.create_text(cx, 365, text="WRONG ANSWER!", fill="#FF4444",
                      font=("Impact", 34, "bold"))
        c.create_text(cx, 408, text="Better luck next time.", fill=WHITE,
                      font=("Arial", 14))

        # Prize earned (checkpoint)
        _prize_box_red(c, cx, 468, 320, 60, "You leave with:  1.000 €")

        _hex_btn(c, cx, 548, 230, 46, "TRY AGAIN",
                 WHITE, BG_DARK, font=("Impact", 13, "bold"),
                 border="#CC2222", command=self.master.show_home)
        _hex_btn(c, cx, 608, 230, 46, "EXIT",
                 WHITE, BG_DARK, font=("Impact", 13, "bold"),
                 border="#CC2222", command=self.master.quit)
