import tkinter as tk
from Button import MyButton
from random import shuffle

colors = {
    1: 'blue',
    2: 'green',
    3: 'orange',
    4: 'yellow',
    5: 'pink',
    6: 'brown',
    7: 'gray',
    8: 'purple',
}


class Minesweeper:

    window = tk.Tk()
    # window.title("MineSweeper")
    ROW = 10
    COLUMNS = 7
    MINES = 15

    def __init__(self):
        # CREATION DES BUTTONS
        self.buttons = []

        for i in range(Minesweeper.ROW+2):
            temp = []
            for j in range(Minesweeper.COLUMNS+2):
                btn = MyButton(Minesweeper.window, x=i, y=j, number=0)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)

            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        if clicked_button.is_mine:
            clicked_button.config(text="*", background='red',
                                  disabledforeground='black')
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            clicked_button.config(text=clicked_button.count_bomb,
                                  disabledforeground=color)
            if clicked_button.count_bomb:
                clicked_button.config(
                    text=clicked_button.count_bomb, disabledforeground=color)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def create_widgets(self):
        # RANGEMENT DES BUTTONS AVEC GRID
        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)
# APPEL DES FUNCTIONS CREES

    def open_all_buttons(self):
        # RANGEMENT DES BUTTONS AVEC GRID
        for i in range(Minesweeper.ROW+2):
            for j in range(Minesweeper.COLUMNS+2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text="*", background='red',
                               disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb,
                               fg=color)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        # self.open_all_buttons()
        print(self.get_mines_places())
        Minesweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbor = self.buttons[i+row_dx][j+col_dx]
                            if neighbor.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, Minesweeper.COLUMNS * Minesweeper.ROW + 1))
        shuffle(indexes)
        return indexes[:Minesweeper.MINES]


# print(buttons)
game = Minesweeper()
game.start()
