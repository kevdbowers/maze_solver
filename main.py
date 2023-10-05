from graphics import Window, Line, Point  #called Window, Line, Point classes from graphics
from cell import Cell  #called Cell class from cell
from maze import Maze #called Maze class from maze

def main():  #create main
    win = Window(800, 600)  #create a Window to operate in
    point_one = Point(50, 100)  #creating test Points
    point_two = Point(500, 200)
    lin = Line(point_one, point_two)  #creating a test Line
    win.draw_line(lin, "Red")

    cel = Cell(win)  #creating a test Cell
    cel.has_bottom_wall = False
    cel.draw(50, 100, 500, 200)
    cel_2 = Cell(win)
    cel_2.has_top_wall = False
    cel_2.draw(100, 200, 750, 400)

    cel.draw_move(cel_2, True)  #drawing cell

    start_x = 100  #creating test Maze paramaters
    start_y = 200
    num_rows = 5
    num_cols = 6
    size_x = 50
    size_y = 50

    maz = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y, win)  #testing the Maze class

    win.wait_for_close()

main()  #calls main