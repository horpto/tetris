from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from enum import Enum
import random
import time


class CellColor(Enum):
    EMPTY = ""
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    @classmethod
    def choose_one(cls):
        return random.choice([c for c in cls if c != cls.EMPTY])

    def isnt_empty(self):
        return self != self.EMPTY

    def is_empty(self):
        return self == self.EMPTY

class Figure:
    cells = ()

    def can_turn(self, fields):
        pass

    def turn(self, fields):
        pass

    def can_move_down(self, fields):
        for y, x, c in self.cells:
            if y + 1 >= len(fields):
                return False
            if fields[y+1][x].isnt_empty() and \
                    all(y+1 != y_other or x != x_other for y_other, x_other, _ in self.cells):
                return False
        return True

    def move_down(self, fields):
        new_cells = []
        for y, x, color in self.cells:
            fields[y+1][x] = color
            new_cells.append((y+1, x, color))
        self.cells = new_cells

    def reset_fields(self, fields):
        for y, x, color in self.cells:
            fields[y][x] = CellColor.EMPTY

    def set_fields(self, fields):
        for y, x, color in self.cells:
            fields[y][x] = color


class SquareFigure(Figure):
    def __init__(self, i, j):
        self.y, self.x = i, j

        self.cells = [
            (i, j, CellColor.choose_one()), (i, j+1, CellColor.choose_one()),
            (i+1, j, CellColor.choose_one()), (i+1, j+1, CellColor.choose_one())
        ]


class Tetris:
    cell_size = 25

    def __init__(self, root, width=10, height=21, speed=0.3):
        self.root = root
        self.width = width
        self.height = height
        self.speed = speed # speed of figure falling (in seconds)

        self.fields = [[CellColor.EMPTY]*width  for i in range(height)]

        self.canvas_width = width * self.cell_size
        self.canvas_height = height * self.cell_size,
        self.canvas = Canvas(
            width=self.canvas_width, height=self.canvas_height,
            bg="grey",
        )

        self.score = 0
        self.score_label = Label(text="Score:")
        self.score_text = Label(text=str(self.score))

        self.prev_timer = 0
        self.current_figure = None

    def pack(self):
        self.canvas.pack(side=LEFT)
        self.score_label.pack(anchor=N, side=LEFT)
        self.score_text.pack(anchor=N, side=RIGHT)

    def configure(self):
        self.pack()
        self.current_figure = self._generate_new_figure()
        # TODO: delete debug figures
        SquareFigure(19,0).set_fields(self.fields)
        SquareFigure(19,2).set_fields(self.fields)
        SquareFigure(19,6).set_fields(self.fields)
        SquareFigure(19,8).set_fields(self.fields)

        self._draw_fields()
        self._bind_events()
        self._start_loop()

    def _generate_new_figure(self):
        return SquareFigure(0,4)

    def _draw_fields(self):
        global canvas
        canvas = self.canvas
        canvas.delete(ALL)

        y_offset = 0
        for row in self.fields:
            offset = 0
            for color in row:
                canvas.create_rectangle(offset, y_offset, offset + self.cell_size, y_offset + self.cell_size, fill=color.value)
                offset += self.cell_size
            y_offset += self.cell_size

    def _bind_events(self):
        pass

    def _start_loop(self):
        if time.monotonic() - self.prev_timer >= self.speed:
            self._iteration()
            self.prev_timer = time.monotonic()
        self.root.after(100, self._start_loop)

    def _iteration(self):
        figure = self.current_figure
        if figure.can_move_down(self.fields):
            figure.reset_fields(self.fields)
            figure.move_down(self.fields)
        else:
            row_count = self._remove_full_rows()
            self._add_to_score(row_count)
            self.current_figure = self._generate_new_figure()
            # TODO: check on full
        self._draw_fields()

    def _remove_full_rows(self):
        deleted_rows = [] # max 4

        for y in range(self.height):
            if all(cell.isnt_empty() for cell in self.fields[y]):
                deleted_rows.append(y)

        new_fields = [[CellColor.EMPTY]*self.width for i in range(len(deleted_rows))]
        new_fields.extend(row for i, row in enumerate(self.fields) if i not in deleted_rows)
        self.fields = new_fields
        return len(deleted_rows)

    def _add_to_score(self, rows_count):
        prize = {1: 100, 2: 300, 3: 700, 4: 1500}
        self.score += prize.get(rows_count, 0)
        self.score_text.configure(text=str(self.score))

def main():
    root = Tk()
    root.title("TetrisEd")

    game = Tetris(root)
    game.configure()

    root.mainloop()

if __name__ == "__main__":
  main()
