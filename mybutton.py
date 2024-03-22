from tkinter import *
from tkinter.messagebox import showinfo, showerror
import random


class MyButton(Button):
    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3,
                                       font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = 0
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False
        self.count_flag = 0
        self.time_start = 0
        self.is_flag = False

        def add_mine(self):
            self.is_mine = True

    def add_flag(self):
        self.is_flag = True
