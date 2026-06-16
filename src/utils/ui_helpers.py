from src.utils.constants import *

def _hex_points(cx, cy, w, h, r=10):
    hw, hh = w // 2, h // 2
    return [
        cx - hw + r, cy - hh,
        cx + hw - r, cy - hh,
        cx + hw,     cy - hh + r,
        cx + hw,     cy + hh - r,
        cx + hw - r, cy + hh,
        cx - hw + r, cy + hh,
        cx - hw,     cy + hh - r,
        cx - hw,     cy - hh + r,
    ]

def _hex_btn(canvas, cx, cy, w, h, text, fg, bg,
             font=None, border=GOLD, command=None):
    pts = _hex_points(cx, cy, w, h)
    btn_id = canvas.create_polygon(pts, fill=bg, outline=border,
                                   width=2, smooth=False)
    txt_id = canvas.create_text(cx, cy, text=text, fill=fg,
                                 font=font or ("Arial", 10, "bold"),
                                 justify="center")
    if command:
        for item in (btn_id, txt_id):
            canvas.tag_bind(item, "<ButtonPress-1>", lambda e: command())
            canvas.tag_bind(item, "<Enter>",
                lambda e, b=btn_id: canvas.itemconfig(b, fill=BTN_HOVER))
            canvas.tag_bind(item, "<Leave>",
                lambda e, b=btn_id, bg_=bg: canvas.itemconfig(b, fill=bg_))


def _answer_btn(canvas, cx, cy, w, h, letter, text, color, command=None):
    pts = _hex_points(cx, cy, w, h)
    btn = canvas.create_polygon(pts, fill=color, outline=CYAN,
                                 width=2, smooth=False)
    label = f"{letter}: {text}"
    txt = canvas.create_text(cx, cy, text=label,
                              fill=WHITE, font=("Arial", 10, "bold"),
                              anchor="center")
    if command:
        for item in (btn, txt):
            canvas.tag_bind(item, "<ButtonPress-1>", lambda e: command())


def _hexagon_shape(canvas, cx, cy, w, h, fill, outline, width=2):
    pts = _hex_points(cx, cy, w, h)
    canvas.create_polygon(pts, fill=fill, outline=outline,
                           width=width, smooth=False)


def _prize_box(canvas, cx, cy, w, h, text):
    pts = _hex_points(cx, cy, w, h)
    canvas.create_polygon(pts, fill=BTN_BLUE, outline=GOLD,
                           width=3, smooth=False)
    canvas.create_text(cx, cy, text=text, fill=GOLD,
                       font=("Impact", 28, "bold"))


def _prize_box_red(canvas, cx, cy, w, h, text):
    pts = _hex_points(cx, cy, w, h)
    canvas.create_polygon(pts, fill="#1A0505", outline="#CC2222",
                           width=3, smooth=False)
    canvas.create_text(cx, cy, text=text, fill="#FF6666",
                       font=("Impact", 18, "bold"))


def _draw_glow_rings(canvas, cx, cy, colors):
    for color, r in colors:
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                           outline=color, width=3, fill="")

