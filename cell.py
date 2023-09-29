from graphics import Line, Point  #  import Line, Point classes

class Cell:  #create Cell class

    def __init__(self, point_1, point_2, win):  #constructor initiates wall existence, then takes and holds two points for cell corners, takes an input window for cell location
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        if point_1.x < point_2.x:
            self.x1 = point_1.x
            self.x2 = point_2.x
        else:
            self.x2 = point_1.x
            self.x1 = point_2.x
        if point_1.y < point_2.y:
            self.y1 = point_1.y
            self.y2 = point_2.y
        else:
            self.y2 = point_1.y
            self.y1 = point_2.y
        self.win = win

    def draw(self):  #draw method creates a cell with up to four walls
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