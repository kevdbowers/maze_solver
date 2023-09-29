from tkinter import Tk, BOTH, Canvas  #importing necessary libraries

class Window:  #create window class

    def __init__(self, width, height):  #window constructor taking a width and height, creates and titles a widget, creates and packs a canvas, creates a "running" variable
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg = "white", height = height, width = width)
        self.canvas.pack(fill = BOTH, expand = 1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):  #redraw method, when called maintains the window
        self.root.update_idletasks()
        self.root.update()
        
    def wait_for_close(self):  #wait_for_close method, once the window is created maintains the window until closed
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window closed...")

    def close(self):  #removes the window
        self.running = False

    def draw_line(self, Line, fill_color = "Black"):  #draws a line in the window
        Line.draw(self.canvas, fill_color)

class Point:  #create Point class

    def __init__(self, x, y):  #constructor stores coordinates of the point
        self.x = x
        self.y = y

class Line:  #create Line class

    def __init__(self, point_1, point_2):  #constructor takes and holds coordinates of two points
        self.x1 = point_1.x
        self.y1 = point_1.y
        self.x2 = point_2.x
        self.y2 = point_2.y

    def draw(self, Canvas, fill_color = "black"):  #draw method for creating a line between two points
        Canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = fill_color, width = 2)
        Canvas.pack(fill = BOTH, expand = 1)