from graphics import Window, Point, Line

def main():
    win = Window(800,600)
    point1 = Point(1,1)
    point2 = Point(500,500)
    line1 = Line(point1,point2)
    win.draw_line(line1,"black")
    win.wait_for_close()

if __name__ == "__main__":
    main()