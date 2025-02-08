from graphics import Line, Point

class Cell:
    def __init__(self,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self,x1,y1,x2,y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"
        center_self_x = (max(self._x1,self._x2) - min(self._x1,self._x2))/2 + min(self._x1,self._x2)
        center_self_y = (max(self._y1,self._y2) - min(self._y1,self._y2))/2 + min(self._y1,self._y2)
        center_to_x = (max(to_cell._x1,to_cell._x2) - min(to_cell._x1,to_cell._x2))/2 + min(to_cell._x1,to_cell._x2)
        center_to_y = (max(to_cell._y1,to_cell._y2) - min(to_cell._y1,to_cell._y2))/2 + min(to_cell._y1,to_cell._y2)
        center_line = Line(
            Point(center_self_x,center_self_y),
            Point(center_to_x,center_to_y))
        self._win.draw_line(center_line,line_color)
        