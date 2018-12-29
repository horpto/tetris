from tkinter import *
from tkinter.ttk import *
import tkinter as tk

class CellColor:
    EMPTY = ""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class Tetris:
    cell_size = 25

    def __init__(self, root, width, height):
        self.root = root              
        self.width = width
        self.height = height

        self.field = [[CellColor.RED]*width  for i in range(height)]

        self.canvas_width = width * self.cell_size
        self.canvas_height = height * self.cell_size,
        self.canvas = Canvas(
            width=self.canvas_width, height=self.canvas_height,
            bg="grey",
        )

        self.score = 0
        self.label = Label(text="Score:")
        self.score_text = Label(text=str(self.score))

    def pack(self):
        self.canvas.pack(side=LEFT)
        self.label.pack(anchor=N, side=LEFT)
        self.score_text.pack(anchor=N, side=RIGHT)

    def draw_field(self):
        global canvas
        canvas = self.canvas

        canvas.delete()

        y_offset = 0
        for row in self.field:
            offset = 0
            for color in row:
                canvas.create_rectangle(offset, y_offset, offset + self.cell_size, y_offset + self.cell_size, fill=color)
                offset += self.cell_size
            y_offset += self.cell_size
        canvas.create_line
        
        
def main():
    root = Tk()
    root.title("TetrisEd")

    game = Tetris(root, width=10, height=21)
    game.pack()

    game.draw_field()

    print('mainloop')
    root.mainloop()

if __name__ == "__main__":
  main()
