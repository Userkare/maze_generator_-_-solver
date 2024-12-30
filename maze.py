import time
from graphics import Window
from cell import Cell



class Maze:
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window ):
        self.cells: list[list[Cell]] = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__creat_cells()

    def __creat_cells(self):
        for x in range(self.__num_rows):

            self.cells.append([])
            for y in range(self.__num_cols):

                self.cells[x].append(Cell(self.__win))
                self.__draw_call(x,y)



        
    def __draw_call(self, x: int, y: int):
            if self.__win is None:
                 return
            x_min = self.__x1 + x * self.__cell_size_x
            x_max = self.__x1 + (x + 1) * self.__cell_size_x
            y_min = self.__y1 + y * self.__cell_size_y
            y_max = self.__y1 + (y+ 1)  * self.__cell_size_y

            self.cells[x][y].draw(x_min, x_max, y_min, y_max)

            self.__animate()



    def __animate(self):
         self.__win.redraw()
         time.sleep(0.05)

