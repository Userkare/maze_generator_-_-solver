from graphics import Window, Cell
from Tests import Tests

def main():
    win = Window(800, 600)
    #Tests().test_haus(win)
    cell1 = Cell(100,300,100,300,win)
    cell2 = Cell(300,500,100,300,win)
    cell3 = Cell(500,700,100,300,win)

    cell1.draw()
    cell2.draw()
    cell3.draw()

    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)

    win.wait_for_close()



main()