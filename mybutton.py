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


class MineSweeper:
    def __init__(self):
        self.window = Tk()
        self.window.title('MineSweeper')
        self.ROW = 5
        self.COLUMNS = 5
        self.MINES = 5
        self.IS_GAMEOVER = False
        self.buttons = []
        for i in range(self.ROW + 2):
            temp = []
            for j in range(self.COLUMNS + 2):
                btn = MyButton(self.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind('<Button-3>', self.right_click)
                btn.grid(row=i, column=j)
                temp.append(btn)
            self.buttons.append(temp)
        self.create_widgets()

    def create_widgets(self):
        self.flag_position = []
        self.count_flag = self.MINES
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        settings_menu = Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Start', command=self.reload)
        settings_menu.add_command(
            label='Settings', command=self.create_settings_win)
        settings_menu.add_command(
            label='Statistics', command=self.create_stat_win)
        settings_menu.add_command(label='Exit', command=self.window.destroy)
        menubar.add_cascade(label='Menu', menu=settings_menu)

    def create_stat_win(self):
        pass

    def create_settings_win(self):
        pass

    def right_click(self, event):
        pass

    def click(self, click_button: MyButton):
        pass

    def start(self):
        self.window.mainloop()

    def reload(self):
        pass


game = MineSweeper()
game.start()
