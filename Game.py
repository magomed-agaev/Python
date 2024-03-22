import tkinter as tk
from Board import Board
from Solver import Solver
import os

class Game:
    def __init__(self, size, prob):
        self.root = tk.Tk()
        self.board = Board(size, prob)
        self.sizeScreen = 800, 800
        self.canvas = tk.Canvas(self.root, width=self.sizeScreen[0], height=self.sizeScreen[1])
        self.canvas.pack()
        self.pieceSize = (self.sizeScreen[0] / size[1], self.sizeScreen[1] / size[0]) 
        self.loadPictures()
        self.solver = Solver(self.board)

    def loadPictures(self):
        self.images = {}
        imagesDirectory = "images"
        for fileName in os.listdir(imagesDirectory):
            if not fileName.endswith(".png"):
                continue
            path = os.path.join(imagesDirectory, fileName)
            img = tk.PhotoImage(file=path)
            self.images[fileName.split(".")[0]] = img
            
    def run(self):
        running = True
        while running:
            self.root.update()
            for event in self.root.event:
                if event.type == tk.QUIT:
                    running = False
                if event.type == tk.MOUSEBUTTONDOWN and not (self.board.getWon() or self.board.getLost()):
                    rightClick = event.num == 3
                    self.handleClick((event.x, event.y), rightClick)
                if event.type == tk.KEYDOWN:
                    self.solver.move()
            self.canvas.delete("all")
            self.draw()
            if self.board.getWon():
                self.win()
                running = False
        
    def draw(self):
        topLeft = (0, 0)
        for row in self.board.getBoard():
            for piece in row:
                image = self.images[self.getImageString(piece)]
                self.canvas.create_image(topLeft[0], topLeft[1], anchor="nw", image=image) 
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = (0, topLeft[1] + self.pieceSize[1])

    def getImageString(self, piece):
        if piece.getClicked():
            return str(piece.getNumAround()) if not piece.getHasBomb() else 'bomb-at-clicked-block'
        if self.board.getLost():
            if piece.getHasBomb():
                return 'unclicked-bomb'
            return 'wrong-flag' if piece.getFlagged() else 'empty-block'
        return 'flag' if piece.getFlagged() else 'empty-block'

    def handleClick(self, position, flag):
        index = tuple(int(pos // size) for pos, size in zip(position, self.pieceSize))[::-1] 
        self.board.handleClick(self.board.getPiece(index), flag)

    def win(self):
        win_label = tk.Label(self.root, text="You Win!", font=("Helvetica", 24))
        win_label.pack()

# Exemple d'utilisation
if __name__ == "__main__":
    game = Game((10, 10), 0.1)
    game.run()
