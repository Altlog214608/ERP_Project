import tkinter as tk

class HorizontalLine(tk.Frame):
    def __init__(self, root, x, y, length, color):
        super().__init__(root, width=length, height=1, bd=0, bg=color)
        self.x = x
        self.y = y
        self.place(x=x, y=y)

    def hide(self):
        self.place_forget()

    def show(self):
        self.place(x=self.x, y=self.y)

class VerticalLine(tk.Frame):
    def __init__(self, root, x, y, length, color):
        super().__init__(root, width=1, height=length, bd=0, bg=color)
        self.x = x
        self.y = y
        self.place(x=x, y=y)

    def hide(self):
        self.place_forget()

    def show(self):
        self.place(x=self.x, y=self.y)