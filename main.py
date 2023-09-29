from graphics import Window, Line, Point  #Called Window, Line, Point class from graphics

def main():  #create main
    win = Window(800, 600)  #create a Window to operate in
    point_one = Point(50, 100)  #creating test Points
    point_two = Point(500, 200)
    lin = Line(point_one, point_two)  #creating a test Line
    win.draw_line(lin, "Red")
    win.wait_for_close()

main()  #calls main