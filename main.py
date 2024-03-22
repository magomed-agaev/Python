import tkinter as tk


class Minesweeper:

    window = tk.Tk()
    # window.title("MineSweeper")
    ROW = 5
    COLUMNS = 7

    def __init__(self):
        # CREATION DES BUTTONS
        self.buttons = []
        for i in range(Minesweeper.ROW):
            temp = []
            for j in range(Minesweeper.COLUMNS):
                btn = tk.Button(Minesweeper.window, width=3,
                                font='Calibri 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        # RANGEMENT DES BUTTONS AVEC GRID
        for i in range(Minesweeper.ROW):
            for j in range(Minesweeper.COLUMNS):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)
# APPEL DES FUNCTIONS CREES

    def start(self):
        self.create_widgets()
        self.print_buttons()
        Minesweeper.window.mainloop()

    def print_buttons(self):
        for row_btn in game.buttons:
            print(row_btn)


# print(buttons)
game = Minesweeper()
game.start()
