'''Draw a non-interactive picture, with precalculated Point locations,
using a loop.
'''

from graphics import GraphWin, Point, Line, Circle

def main():
    """just main func"""
    win = GraphWin('Balloons', 200, 300)
    win.yUp() # right side up coordinates

    base = Point(100, 50)

    for center in [Point(50, 200), Point(150, 220), Point(100, 225)]:
        line = Line(base, center)
        line.draw(win)
        balloon = Circle(center, 40)
        balloon.setOutline('yellow') # i like yellow
        balloon.setFill('green') # i like green
        balloon.draw(win)

    win.promptClose(win.getWidth()/2, 20)

main()
