import math
import tkinter as tk
from tkinter import ttk

# test2.py
# Simple scientific calculator with a tkinter UI


# Degree mode flag
deg_mode = False

# Wrapper math functions that respect degree/radian mode
def _to_rad(x):
    return math.radians(x) if deg_mode else x

def sin(x): return math.sin(_to_rad(x))
def cos(x): return math.cos(_to_rad(x))
def tan(x): return math.tan(_to_rad(x))
def asin(x): return math.degrees(math.asin(x)) if deg_mode else math.asin(x)
def acos(x): return math.degrees(math.acos(x)) if deg_mode else math.acos(x)
def atan(x): return math.degrees(math.atan(x)) if deg_mode else math.atan(x)
def ln(x): return math.log(x)
def log(x, base=10): return math.log(x, base)
def sqrt(x): return math.sqrt(x)
def fact(x): return math.factorial(int(x))
def pow_(x, y): return math.pow(x, y)

# Safe evaluation environment
SAFE_ENV = {
    "sin": sin, "cos": cos, "tan": tan,
    "asin": asin, "acos": acos, "atan": atan,
    "ln": ln, "log": log, "sqrt": sqrt,
    "fact": fact, "pow": pow_, "pi": math.pi, "e": math.e,
    "abs": abs, "round": round
}

class SciCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.resizable(False, False)
        self.expr = tk.StringVar()
        self.create_ui()
        self.bind_keys()

    def create_ui(self):
        entry = ttk.Entry(self, textvariable=self.expr, font=("Consolas", 16), justify="right")
        entry.grid(row=0, column=0, columnspan=6, padx=6, pady=6, sticky="we")
        entry.focus_set()

        btns = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("sqrt",1,4), ("C",1,5),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("^",2,4), ("⌫",2,5),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("(",3,4), (")",3,5),
            ("0",4,0), (".",4,1), ("±",4,2), ("+",4,3), ("pi",4,4), ("e",4,5),
            ("sin",5,0), ("cos",5,1), ("tan",5,2), ("ln",5,3), ("log",5,4), ("fact",5,5),
            ("asin",6,0), ("acos",6,1), ("atan",6,2), ("pow",6,3), ("deg",6,4), ("=",6,5),
        ]

        for (txt, r, c) in btns:
            action = lambda t=txt: self.on_button(t)
            ttk.Button(self, text=txt, command=action).grid(row=r, column=c, padx=3, pady=3, sticky="nsew")

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)

    def bind_keys(self):
        for k in "0123456789.+-*/()^":
            self.bind(k, lambda e, ch=k: self.insert_text(ch))
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<BackSpace>", lambda e: self.backspace())
        self.bind("<Escape>", lambda e: self.clear())

    def insert_text(self, text):
        cur = self.expr.get()
        self.expr.set(cur + text)

    def on_button(self, label):
        if label == "C":
            self.clear()
        elif label == "⌫":
            self.backspace()
        elif label == "=":
            self.evaluate()
        elif label == "±":
            self.toggle_sign()
        elif label == "pi":
            self.insert_text("pi")
        elif label == "e":
            self.insert_text("e")
        elif label == "sqrt":
            self.insert_text("sqrt(")
        elif label == "fact":
            self.insert_text("fact(")
        elif label == "pow":
            self.insert_text("pow(")
        elif label in ("sin","cos","tan","asin","acos","atan","ln","log"):
            self.insert_text(f"{label}(")
        elif label == "^":
            self.insert_text("**")
        elif label == "deg":
            self.toggle_deg()
        else:
            self.insert_text(label)

    def clear(self):
        self.expr.set("")

    def backspace(self):
        s = self.expr.get()
        self.expr.set(s[:-1])

    def toggle_sign(self):
        s = self.expr.get()
        if not s:
            return
        try:
            # try evaluate current and negate
            val = self._safe_eval(s)
            self.expr.set(str(-val))
        except Exception:
            # fallback: prefix with -(
            if s.startswith("-(") and s.endswith(")"):
                self.expr.set(s[2:-1])
            else:
                self.expr.set(f"-({s})")

    def toggle_deg(self):
        global deg_mode
        deg_mode = not deg_mode
        # Visual feedback: set window title
        self.title("Scientific Calculator - DEG" if deg_mode else "Scientific Calculator - RAD")

    def evaluate(self):
        s = self.expr.get()
        if not s:
            return
        try:
            # Replace implicit power tokens if any remain
            result = self._safe_eval(s)
            # Pretty format integers without .0
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expr.set(str(result))
        except Exception as e:
            self.expr.set("Error")

    def _safe_eval(self, expression):
        # sanitize simple common tokens
        expr = expression.replace("^", "**")
        # evaluate with restricted globals and allowed functions in locals
        return eval(expr, {"__builtins__": None}, SAFE_ENV)

if __name__ == "__main__":
    app = SciCalculator()
    app.mainloop()