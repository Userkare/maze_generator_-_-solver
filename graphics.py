from tkinter import Tk, BOTH, Canvas



class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line: "Line", color: str="black"):
        line.draw(self.__canvas, color)
        

class Point:
    def __init__(self,x:int ,y:int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill= color, width=2)

class Cell:
    def __init__(self, x1: int, x2: int, y1: int, y2: int, win: Window):
        
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)))

    def Get_center_Point(self):
        return Point((self.__x1 + self.__x2)//2, (self.__y1 + self.__y2)//2)

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"



        self.__win.draw_line(Line(self.Get_center_Point(), to_cell.Get_center_Point()), color)