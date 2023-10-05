import time  #import time library
from cell import Cell  #import Cell class

class Maze:  #create Maze class

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):  #constructor initiates creation location for a maze along with size and cell-population
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()  #draws maze through create_cells method

    def create_cells(self):  #method for creating the cells in the maze and then drawing them out
        self.cells = []
        for j in range(0, self.num_cols):
            row_list = []
            for i in range(0, self.num_rows):
                row_list.append(Cell(self.win))
            self.cells.append(row_list)

        j = 0
        for col in self.cells:
            i = 0
            for cel in col:
                x_var = self.x1 + (i * self.cell_size_x)
                y_var = self.y1 + (j * self.cell_size_y)
                cel.draw(x_var, y_var, x_var + self.cell_size_x, y_var + self.cell_size_y)
                self.animate()
                i += 1
            j += 1

    def animate(self):  #method to put a delay on the drawn cells for human readability
        self.win.redraw()
        time.sleep(.05)