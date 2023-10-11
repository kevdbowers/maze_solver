import random, time  #import random and time librarries
from cell import Cell  #import Cell class

class Maze:  #create Maze class

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):  #constructor initiates creation location for a maze along with size and cell-population
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        if seed != None:  #if a seed is given for the maze use it, if not generate a random seed, testing purposes only
            random.seed(seed)
        else:
            random.seed()

        self.create_cells()  #draws maze through create_cells method
        self.break_entrance_and_exit()  #defining entrance and exit cells so that they're left open
        self.break_rand_walls(0, 0)  #generating random maze
        self.reset_cells_visited()  #calls visited reset method

    def create_cells(self):  #method for creating a list of the cells in the maze and then drawing them out
        self.cells = []
        for j in range(0, self.num_cols):
            row_list = []
            for i in range(0, self.num_rows):
                row_list.append(Cell(self.win))
            self.cells.append(row_list)

    def animate(self):  #method to put a delay on the drawn cells for human readability
        self.win.redraw()
        time.sleep(.05)

    def break_entrance_and_exit(self):  #method creating the entrance and exit to the maze
        entrance_cell = self.cells[0][0]
        entrance_cell.has_top_wall = False

        exit_cell = self.cells[self.num_cols - 1][self.num_rows - 1]
        exit_cell.has_bottom_wall = False

    def break_rand_walls(self, col, row):  #method to remove walls throughout the maze randomly unless a specific seed is called
        self.cells[col][row].visited = True  #marks the current cell as visited
        while True:  #loop adding every unvisited cell to a list then drawing those cells
            neighbors = []
            if col > 0 and self.cells[col - 1][row].visited == False:
                neighbors.append([col - 1, row])
            if col < self.num_cols - 1 and self.cells[col + 1][row].visited == False:
                neighbors.append([col + 1, row])
            if row > 0 and self.cells[col][row - 1].visited == False:
                neighbors.append([col, row - 1])
            if row < self.num_rows - 1 and self.cells[col][row + 1].visited == False:
                neighbors.append([col, row + 1])
            if neighbors == []:
                if self.win == None:
                    return
                x_var = self.x1 + (col * self.cell_size_x)
                y_var = self.y1 + (row * self.cell_size_y)
                self.cells[col][row].draw(x_var, y_var, x_var + self.cell_size_x, y_var + self.cell_size_y)
                self.animate()
                return
            
            next_direction = random.randint(0, len(neighbors) - 1)  #randomly selects the next cell selected from an unvisited neighbor, then determines what walls it won't have
            next_cell = neighbors[next_direction]
            if next_cell[0] == col - 1:
                self.cells[col][row].has_left_wall = False
                self.cells[col - 1][row].has_right_wall = False
            if next_cell[0] == col + 1:
                self.cells[col][row].has_right_wall = False
                self.cells[col + 1][row].has_left_wall = False
            if next_cell[1]  == row - 1:
                self.cells[col][row].has_top_wall = False
                self.cells[col][row - 1].has_bottom_wall = False
            if next_cell[1]  == row + 1:
                self.cells[col][row].has_bottom_wall = False
                self.cells[col][row + 1].has_top_wall = False

            self.break_rand_walls(next_cell[0], next_cell[1])  #recursive call to ensure every cell is defined and drawn

    def reset_cells_visited(self):  #creates a method to reset the .visited variable of every cell to False
        for j in range(0, self.num_cols):
            for i in range(0, self.num_rows):
                self.cells[j][i].visited = False

    def solve(self, j = 0, i = 0):  #creates the solve method which initiates a solver at 0, 0 and returns the result
        return self.solver(j, i)
    
    def solver(self, j, i):  #creates the solver method which marks the current cell as visited, then recursively searches cells in a maze until reaching the exit, if possible.
        self.animate()
        self.cells[j][i].visited = True
        if self.cells[self.num_cols - 1][self.num_rows - 1].visited == True:
            return True
        
        if self.cells[j][i].has_left_wall == False and j > 0 and self.cells[j - 1][i].visited == False:
            self.cells[j][i].draw_move(self.cells[j - 1][i])
            solved = self.solver(j - 1, i)
            if solved == True:
                return True
            self.cells[j][i].draw_move(self.cells[j - 1][i], True)

        if self.cells[j][i].has_right_wall == False and j < self.num_cols - 1 and self.cells[j + 1][i].visited == False:
            self.cells[j][i].draw_move(self.cells[j + 1][i])
            solved = self.solver(j + 1, i)
            if solved == True:
                return True
            self.cells[j][i].draw_move(self.cells[j + 1][i], True)

        if self.cells[j][i].has_top_wall == False and i > 0 and self.cells[j][i - 1].visited == False:
            self.cells[j][i].draw_move(self.cells[j][i - 1])
            solved = self.solver(j, i - 1)
            if solved == True:
                return True
            self.cells[j][i].draw_move(self.cells[j][i - 1], True)
        
        if self.cells[j][i].has_bottom_wall == False and i < self.num_rows - 1 and self.cells[j][i + 1].visited == False:
            self.cells[j][i].draw_move(self.cells[j][i + 1])
            solved = self.solver(j, i + 1)
            if solved == True:
                return True
            self.cells[j][i].draw_move(self.cells[j][i + 1], True)
        
        return False
    

