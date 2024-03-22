# import numbers
# from tkinter import *
# import random
# from tkinter.messagebox import showinfo, showerror
# from mybutton import MyButton
# import time
# import re
from tkinter import *
import numbers
# from minesweeper import MineSweeper
import numbers
import random
from tkinter.messagebox import showinfo, showerror
# from mybutton import MyButton
import time
import re


class MyButton(Button):
    def _init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3,
                                       font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = numbers
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False
        self.count_flag = 0
        self.time_start = 0
        self.is_flag = False


class MineSweeper:
    window = Tk()
    window.title('MineSweeper')
    ROW = 5
    COLLUMNS = 5
    MINES = 5
    IS_GAMEOVER = False


def __init__(self):

    self.buttons = []
    for i in range(self.ROW+2):
        temp = []
        for j in range(self.COLLUMNS+2):
            btn = MyButton(self.window, x=i, y=j)
            btn.config(
                text='b', command=lambda button=btn: self.click(button))
            btn.bind('<Button-3>', self.right_click)
            temp.append(btn)
            self.buttons.append(temp)

            def create_widgets(self):
                count = 1
                self.falg_position - []
                self.count_flag = self.MINES
                menubar = Menu(self.window)
                self.window.config(menu=menubar)
                settings_menu = Menu(menubar, tearoff=0)
                settings_menu.add_command(
                    label='Start', command=self.reload)
                settings_menu.add_command(
                    label='Settings', command=self.create_settings_win)
                settings_menu.add_command(
                    label='Statistics', command=self.create_stat_win)
                settings_menu.add_command(
                    label='Exit', command=self.window.destroy)
                menubar.add_cascade(label='Menu', menu=settings_menu)

            def create_stat_win(self):
                pass

            def right_click(self):
                pass

            def click(self, click_button: MyButton):
                pass

            def start(self):
                self.create_widgets()
                self.window.mainloop()

                game = MineSweeper()
                game.start()
