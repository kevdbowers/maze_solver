from graphics import Window, Line, Point  #called Window, Line, Point, Cell class from graphics
from cell import Cell  #called Cell from cell

def main():  #create main
    win = Window(800, 600)  #create a Window to operate in
    point_one = Point(50, 100)  #creating test Points
    point_two = Point(500, 200)
    lin = Line(point_one, point_two)  #creating a test Line
    win.draw_line(lin, "Red")

    cell_point_one = Point(100, 200)  #creating test Points
    cell_point_two = Point(50, 500)
    cel = Cell(cell_point_one, cell_point_two, win)  #creating a test Cell
    cel.has_bottom_wall = False
    cel.draw()

    win.wait_for_close()

main()  #calls main