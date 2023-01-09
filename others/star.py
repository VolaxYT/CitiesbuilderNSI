import turtle

class Star:
    def draw(self):
        turtle.pensize(3)

        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(self.color)
        turtle.circle(self.size)
        turtle.end_fill()
        turtle.penup()
        turtle.pensize(1)

    def __init__(self, nom, color, x, y, size):
        self.nom = nom
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def __repr__(self):
        return repr(self.toString())

    def toString(self):
        return f"Star;'{self.nom}';{self.color};{self.x};{self.y};{self.size}"


'''
if __name__ == '__main__':
    soleil(0, 0)
    turtle.exitonclick()
    '''