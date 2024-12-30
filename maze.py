import random
import time
from graphics import Window
from cell import Cell



class Maze:
    animation_spped: float = 0.01

    def __init__(self, x1: int, y1: int,
                 num_rows: int, num_cols: int, 
                 cell_size_x: int, cell_size_y: int, 
                 win: Window = None, seed = None)-> None:
        self._cells: list[list[Cell]] = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        if seed is not None:
             random.seed(seed)

        self.__creat_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.solve_depth_first()
        

    def __creat_cells(self)-> None:
        for colum in range(self.__num_cols):

            self._cells.append([])
            for row in range(self.__num_rows):

                self._cells[colum].append(Cell(self.__win))
                self.__draw_call(colum,row)
   
    def __draw_call(self, x: int, y: int)-> None:
            if self.__win is None:
                 return
            x_links = self.__x1 + x * self.__cell_size_x
            x_rechts = self.__x1 + (x + 1) * self.__cell_size_x
            y_oben = self.__y1 + y * self.__cell_size_y
            y_unten = self.__y1 + (y+ 1)  * self.__cell_size_y

            self._cells[x][y].draw(x_links, x_rechts, y_unten, y_oben)

            self.__animate()



    def __animate(self)-> None:
         self.__win.redraw()
         time.sleep(self.animation_spped)


    def __break_entrance_and_exit(self)-> None:
        self._cells[0][0].has_top_wall = False
        self.__draw_call(0,0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_call(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, x: int, y: int)-> None:
        #print(f"zerstöre Wälle @ {x}, {y}")
        self._cells[x][y].visited = True

        while True:
            to_visit: list[tuple[int,int]] = []
            if x >= 1 and self._cells[x-1][y].visited == False:
                to_visit.append((x-1,y))

            if x < self.__num_cols - 1 and self._cells[x+1][y].visited == False:
                to_visit.append((x+1,y))

            if y >= 1 and self._cells[x][y-1].visited == False:
                to_visit.append((x,y-1))

            if y < self.__num_rows - 1 and self._cells[x][y+1].visited == False:
                to_visit.append((x,y+1))

            posibil_directions=len(to_visit)
            if posibil_directions == 0:
                self.__draw_call(x,y)
                return

            random_direction = random.randrange(posibil_directions)
            next_idex = to_visit[random_direction]


            if next_idex[0] == x + 1:
                print(f"zerstöre right @ {x}, {y}")
                self._cells[x][y].has_right_wall = False
                self._cells[x + 1][y].has_left_wall = False

            if next_idex[0] == x - 1:
                print(f"zerstöre left @ {x}, {y}")
                self._cells[x][y].has_left_wall = False
                self._cells[x - 1][y].has_right_wall = False

            if next_idex[1] == y + 1:
                print(f"zerstöre bottom @ {x}, {y}")
                self._cells[x][y].has_bottom_wall = False
                self._cells[x][y + 1].has_top_wall = False

            if next_idex[1] == y - 1:
                print(f"zerstöre top  @ {x}, {y}")
                self._cells[x][y].has_top_wall = False
                self._cells[x][y - 1].has_bottom_wall = False

            self.__break_walls_r(next_idex[0],next_idex[1])

    def __reset_cells_visited(self)-> None:
        for colum in range(self.__num_cols):
            for row in range(self.__num_rows):
                self._cells[colum][row].visited = False

    def solve_depth_first (self) -> bool:
        self.__solve_depth_first_r(0, 0)

    def __solve_depth_first_r(self, x: int, y: int)-> bool:
        self.__animate()

        if x == self.__num_cols - 1 and y == self.__num_rows - 1:
            return True
        
        self._cells[x][y].visited = True


        # right
        if (x < self.__num_cols - 1 
            and self._cells[x+1][y].visited == False 
            and self._cells[x][y].has_right_wall == False):

            self._cells[x][y].draw_move(self._cells[x+1][y])
            found = self.__solve_depth_first_r(x+1, y)
            if found:
                return True
            else:
                self._cells[x][y].draw_move(self._cells[x+1][y],True)

        #left
        if (x >= 1 
            and self._cells[x-1][y].visited == False 
            and self._cells[x][y].has_left_wall == False):

            self._cells[x][y].draw_move(self._cells[x-1][y])
            found = self.__solve_depth_first_r(x-1, y)
            if found:
                return True
            else:
                self._cells[x][y].draw_move(self._cells[x-1][y],True)

        #bottom
        if (y < self.__num_rows - 1 
            and self._cells[x][y+1].visited == False
            and self._cells[x][y].has_bottom_wall == False):
            
            self._cells[x][y].draw_move(self._cells[x][y+1])
            found = self.__solve_depth_first_r(x, y+1)
            if found:
                return True
            else:
                self._cells[x][y].draw_move(self._cells[x][y+1],True)

        #top
        if (y >= 1 
            and self._cells[x][y-1].visited == False
            and self._cells[x][y].has_top_wall == False):

            self._cells[x][y].draw_move(self._cells[x][y-1])
            found = self.__solve_depth_first_r(x, y-1)
            if found:
                return True
            else:
                self._cells[x][y].draw_move(self._cells[x][y-1],True)


        return False

        


