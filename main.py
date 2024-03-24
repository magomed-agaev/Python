import tkinter as tk
from Button import MyButton
from random import shuffle
from tkinter.messagebox import showinfo

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
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

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
        #  AFFICHAGE DES BOMBES APRES LE 1ER CLICK
        if Minesweeper.IS_FIRST_CLICK:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            self.print_buttons()

        if clicked_button.is_mine:
            clicked_button.config(text="*", background='red',
                                  disabledforeground='black')
            clicked_button.is_open = True
            Minesweeper.IS_GAME_OVER = True
            showinfo('Game Over', 'You lose')
            # SI JOUER PERDS AFFICHER LES BOMBES RESTANTES
            for i in range(1, Minesweeper.ROW+1):
                for j in range(1, Minesweeper.COLUMNS+1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            clicked_button.config(text=clicked_button.count_bomb,
                                  disabledforeground=color)
            clicked_button.is_open = True
            if clicked_button.count_bomb:
                clicked_button.config(
                    text=clicked_button.count_bomb, disabledforeground=color)
                clicked_button.is_open = True
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:

            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb,
                               disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx - dy) == 1:
                            continue

                        next_btn = self.buttons[x+dx][y+dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= Minesweeper.ROW and \
                                1 <= next_btn.y <= Minesweeper.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def create_widgets(self):
        count = 1
        # RANGEMENT DES BUTTONS AVEC GRID
        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j)
                count += 1
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

    def insert_mines(self, number: int):
        index_mines = self.get_mines_places(number)
        print(index_mines)

        for i in range(1, Minesweeper.ROW+1):
            for j in range(1, Minesweeper.COLUMNS+1):
                btn = self.buttons[i][j]

                if btn.number in index_mines:
                    btn.is_mine = True

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
    def get_mines_places(exclude_number: int):
        indexes = list(range(1, Minesweeper.COLUMNS * Minesweeper.ROW + 1))
        print(f'exclude button n{exclude_number}')
        indexes.remove(exclude_number)
        shuffle(indexes)
        return indexes[:Minesweeper.MINES]


# print(buttons)
game = Minesweeper()
game.start()
