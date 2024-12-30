from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(20, 20, 10, 10, 20, 20, win)

    win.wait_for_close()



main()