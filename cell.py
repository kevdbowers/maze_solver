from graphics import Line, Point  #  import Line, Point classes

class Cell:  #create Cell class

    def __init__(self, win = None):  #constructor initiates wall existence, then initiates corner variables, takes an input window for cell location
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):  #draw method defines corners, then creates a cell with up to four walls
        if x1 < x2:
            self.x1 = x1
            self.x2 = x2
        else:
            self.x2 = x1
            self.x1 = x2
        if y1 < y2:
            self.y1 = y1
            self.y2 = y2
        else:
            self.y2 = y1
            self.y1 = y2

        if self.has_left_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            self.win.draw_line(line)
        if self.has_right_wall == True:
            line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            self.win.draw_line(line)
        if self.has_top_wall == True:
            line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            self.win.draw_line(line)
        if self.has_bottom_wall == True:
            line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            self.win.draw_line(line)
    
    def draw_move(self, to_cell, undo = False):  #creates a line between two cells by defining their centers and drawing between them
        if self.win is None:
            return
        
        line_color = "Red"
        if undo == True:
            line_color = "Gray"

        self_center_x = (self.x1 + self.x2) / 2
        self_center_y = (self.y1 + self.y2) / 2
        self_point = Point(self_center_x, self_center_y)

        to_cell_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) / 2
        to_cell_point = Point(to_cell_center_x, to_cell_center_y)
        
        new_line = Line(self_point, to_cell_point)
        self.win.draw_line(new_line, line_color)