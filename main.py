from graphics import Window, Line, Point  #called Window, Line, Point classes from graphics
from cell import Cell  #called Cell class from cell
from maze import Maze #called Maze class from maze

def main():  #create main
    win = Window(800, 600)  #create a Window to operate in

    start_x = 25  #creating test Maze paramaters
    start_y = 25
    num_rows = 22
    num_cols = 30
    size_x = 25
    size_y = 25

    maz = Maze(start_x, start_y, num_rows, num_cols, size_x, size_y, win)  #testing the Maze class

    maz.solve()  #runs the Maze solver

    win.wait_for_close()

main()  #calls main