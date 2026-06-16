"""Question screen."""
import tkinter as tk
from tkinter import font as tkfont
from src.utils.constants import *
from src.utils.ui_helpers import _hexagon_shape, _hex_points, _hex_btn


class GameScreen(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, bg=BG_DARK)

        self.question = master.game_question
        self.options = master.game_options
        self.correct = master.game_correct
        self.game_end = master.game_end

        self.selected = None      # index of selected answer (0-3)
        self.btn_ids  = []        # list of (polygon_id, text_id) per answer
        self._canvas  = None
        self._confirm_btn = None  # (polygon_id, text_id)

        self._draw()

    def _draw(self):
        c = tk.Canvas(self, width=W, height=H, bg=BG_DARK, highlightthickness=0)
        c.pack(fill="both", expand=True)
        self._canvas = c

        left_cx  = 305
        right_cx = 710
        tw       = 210

        # ── Lifelines ───────────────────────────────────────────────
        lifelines = [("↻", "Skip"), ("👥", "Audience"), ("50:50", "50:50")]
        lx_start = left_cx - 100
        for i, (icon, label) in enumerate(lifelines):
            x = lx_start + i * 100
            c.create_oval(x-26, 18, x+26, 70,
                          fill=BLUE_GLOW, outline=BTN_BORDER, width=2)
            c.create_text(x, 44, text=icon, fill=WHITE,
                          font=("Arial", 13, "bold"))
            c.create_text(x, 84, text=label, fill=WHITE,
                          font=("Arial", 8))

        # ── Question box ─────────────────────────────────────────────
        _hexagon_shape(c, left_cx, 175, 530, 72,
                       fill=BLUE_GLOW, outline=CYAN, width=2)
        c.create_text(left_cx, 175, text=self.question, fill=WHITE,
                      font=("Arial", 12, "bold"), justify="center")

        # ── Answer buttons (2×2 grid, selectable) ───────────────────
        ans_w, ans_h = 248, 46
        positions = [
            (left_cx - 132, 268), (left_cx + 132, 268),
            (left_cx - 132, 330), (left_cx + 132, 330),
        ]
        self.btn_ids = []
        for idx, ((letter, text, _), (x, y)) in enumerate(zip(self.options, positions)):
            pts = _hex_points(x, y, ans_w, ans_h)
            btn = c.create_polygon(pts, fill=BTN_BLUE, outline=CYAN,
                                   width=2, smooth=False)
            lbl = c.create_text(x, y, text=f"{letter}: {text}",
                                 fill=WHITE, font=("Arial", 10, "bold"),
                                 anchor="center")
            self.btn_ids.append((btn, lbl))
            for item in (btn, lbl):
                c.tag_bind(item, "<ButtonPress-1>",
                           lambda e, i=idx: self._select(i))

        # ── CONFIRM button (starts disabled / dimmed) ────────────────
        pts = _hex_points(left_cx, 400, 220, 46)
        cb = c.create_polygon(pts, fill="#1A1A3A", outline="#444466",
                               width=2, smooth=False)
        ct = c.create_text(left_cx, 400, text="CONFIRM ANSWER",
                            fill="#666688", font=("Impact", 13, "bold"))
        self._confirm_btn = (cb, ct)
        # bindings added dynamically in _select

        # ── Money table ──────────────────────────────────────────────
        for i, (level, prize) in enumerate(MONEY_LEVELS):
            row_y = 95 + i * 36
            is_current = (level == self.master.game_level)
            bg     = MONEY_ROW_HL if is_current else MONEY_ROW_BG
            fg     = BG_DARK      if is_current else MONEY_TEXT
            num_fg = MONEY_GOLD   if is_current else "#8888BB"
            c.create_rectangle(right_cx - tw//2, row_y - 13,
                                right_cx + tw//2, row_y + 13,
                                fill=bg, outline="#1A3A8F", width=1)
            c.create_text(right_cx - 65, row_y, text=str(level),
                          fill=num_fg, font=("Arial", 9, "bold"))
            c.create_text(right_cx + 35, row_y, text=prize,
                          fill=fg, font=("Arial", 9, "bold"))

        # Back button
        _hex_btn(c, right_cx, 500, 160, 34, "← BACK",
                 WHITE, BG_DARK, font=("Arial", 9, "bold"),
                 border=BTN_BORDER, command=self.master.show_home)

    def _select(self, idx):
        """Highlight selected answer in green, reset others."""
        self.selected = idx
        c = self._canvas
        for i, (btn, lbl) in enumerate(self.btn_ids):
            if i == idx:
                c.itemconfig(btn, fill=BTN_CORRECT, outline=WHITE)
            else:
                c.itemconfig(btn, fill=BTN_BLUE, outline=CYAN)

        # Activate confirm button
        cb, ct = self._confirm_btn
        c.itemconfig(cb, fill="#0A3A0A", outline=BTN_CORRECT)
        c.itemconfig(ct, fill=WHITE)
        c.tag_unbind(cb, "<ButtonPress-1>")
        c.tag_unbind(ct, "<ButtonPress-1>")
        for item in (cb, ct):
            c.tag_bind(item, "<ButtonPress-1>", lambda e: self._confirm())
            c.tag_bind(item, "<Enter>",
                       lambda e, b=cb: c.itemconfig(b, fill="#0D550D"))
            c.tag_bind(item, "<Leave>",
                       lambda e, b=cb: c.itemconfig(b, fill="#0A3A0A"))

    def _confirm(self):
        if self.selected == self.correct:
            if self.game_end:
                self.master.show_victory()
            else:
                self.master.next_question()
        else:
            self.master.show_defeat()
