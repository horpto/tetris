from tkinter import *
from tkinter.ttk import *
import tkinter as tk

class CellColor:
    EMPTY = 0
    RED = 1
    GREEN = 2
    BLUE = 3

class Tetris:
    cell_size = 25

    def __init__(self, root, width, height):
        self.root = root              
        self.width = width
        self.height = height

        self.field = [[CellColor.EMPTY] * height for i in range(width)]

        self.canvas = Canvas(
            width=width * self.cell_size, height=height * self.cell_size,
            bg='grey', borderwidth=1
        )

        self.score = 0
        self.label = Label(text="Score:")
        self.score_text = Label(text="100")

    def pack(self):
        self.canvas.pack(side=LEFT)
        self.label.pack(anchor=N, side=LEFT)
        self.score_text.pack(anchor=N, side=RIGHT)

def main():
    root = Tk()
    root.title("TetrisEd")

    game = Tetris(root, width=10, height=21)
    game.pack()

    print('mainloop')
    root.mainloop()

if __name__ == "__main__":
  main()
