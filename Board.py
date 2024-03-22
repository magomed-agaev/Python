import random
from Case import Case

class Board:
    def __init__(self, size, prob):
        self.size = size
        self.board = []
        self.won = False 
        self.lost = False
        self.empty = False
        for row in range(size[0]):
            row_list = []
            for col in range(size[1]):
                bomb = random.random() < prob
                case = Case(bomb)
                row_list.append(case)
            self.board.append(row_list)
        self.setNeighbors()
        self.setNumAround()
        self.setEmpty()

  

    def setEmpty(self):
        
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if not self.board[row][col].getHasBomb():
                    self.empty = True
                    self.reveal_empty(row, col)
                    return

    def reveal_empty(self, row, col):
       
        self.board[row][col].handleClick()
        neighbors_positions = [(row-1, col-1), (row-1, col), (row-1, col+1),
                               (row, col-1),                     (row, col+1),
                               (row+1, col-1), (row+1, col), (row+1, col+1)]
        for r, c in neighbors_positions:
            if 0 <= r < self.size[0] and 0 <= c < self.size[1]:
                if not self.board[r][c].getHasBomb() and not self.board[r][c].getClicked():
                    self.reveal_empty(r, c)



if __name__ == "__main__":
    game_board = Board((5, 5), 0.2)
    print("Plateau de jeu initial:")
    game_board.print_board()
