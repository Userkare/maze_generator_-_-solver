
from graphics import Window, Point, Line


class Cell:
    def __init__(self, win: Window)-> None:
        
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x_links = None
        self.__x_rechs = None
        self.__y_unten = None
        self.__y_oben = None
        self.__win = win
        self.visited = False

    #(x_links, x_rechts, y_unten,y_oben)

    def draw(self,x_links: int, x_rechs: int, y_unten: int, y_oben: int):
        if self.__win is None:
            return
        
        self.__x_links = x_links
        self.__x_rechs = x_rechs
        self.__y_unten = y_unten
        self.__y_oben = y_oben

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x_links, self.__y_unten), Point(self.__x_links, self.__y_oben)))
        else:
            self.__win.draw_line(Line(Point(self.__x_links, self.__y_unten), Point(self.__x_links, self.__y_oben)), "white")

        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x_links, self.__y_unten), Point(self.__x_rechs, self.__y_unten)))
        else:
            self.__win.draw_line(Line(Point(self.__x_links, self.__y_unten), Point(self.__x_rechs, self.__y_unten)), "white")

        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x_rechs, self.__y_oben), Point(self.__x_links, self.__y_oben)))
        else:
            self.__win.draw_line(Line(Point(self.__x_rechs, self.__y_oben), Point(self.__x_links, self.__y_oben)), "white")

        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x_rechs, self.__y_oben), Point(self.__x_rechs, self.__y_unten)))
        else:
            self.__win.draw_line(Line(Point(self.__x_rechs, self.__y_oben), Point(self.__x_rechs, self.__y_unten)), "white")


    def Get_center_Point(self)-> None:
        return Point((self.__x_links + self.__x_rechs)//2, (self.__y_unten + self.__y_oben)//2)

    def draw_move(self, to_cell: "Cell", undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"



        self.__win.draw_line(Line(self.Get_center_Point(), to_cell.Get_center_Point()), color)