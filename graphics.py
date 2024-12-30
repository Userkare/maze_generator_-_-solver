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
