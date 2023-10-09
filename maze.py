import time  #import time library
from cell import Cell  #import Cell class

class Maze:  #create Maze class

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):  #constructor initiates creation location for a maze along with size and cell-population
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self.create_cells()  #draws maze through create_cells method

    def create_cells(self):  #method for creating a list of the cells in the maze and then drawing them out
        self.cells = []
        for j in range(0, self.num_cols):
            row_list = []
            for i in range(0, self.num_rows):
                row_list.append(Cell(self.win))
            self.cells.append(row_list)

        self.break_entrance_and_exit()

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

    def break_entrance_and_exit(self):  #method creating the entrance and exit to the maze
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False

        exit_cell = self.cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_bottom_wall = False
