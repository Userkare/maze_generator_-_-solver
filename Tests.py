from graphics import Point, Line, Window, Cell

class Tests:
    haus = [Line(Point(100,100),Point(300,100)),
            Line(Point(300,100),Point(300,300)),
            Line(Point(300,300),Point(100,300)),
            Line(Point(100,300),Point(100,100)),
            Line(Point(100,300),Point(200,400)),
            Line(Point(300,300),Point(200,400))]

    def test_haus(self, window: Window):
        for i in range(len(self.haus)):
            window.draw_line(self.haus[i], "black")

    