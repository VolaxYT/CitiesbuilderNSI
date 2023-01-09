from utils.trait import trait
import turtle

'''
xSol = coordonnées x par rapport au sol
ySol = ccoordonnées y par rapport au sol
'''

class Lampadaire:
    def draw(self):
        turtle.pensize(3)
        # Base
        trait(self.xSol, self.ySol, self.xSol, self.ySol + 45)
        # Extremités
        trait(self.xSol - 20, self.ySol + 45, self.xSol + 20, self.ySol + 45)
        # Lampe 1
        trait(self.xSol + 20, self.ySol + 45, self.xSol + 20, self.ySol + 35)
        turtle.goto(self.xSol + 20, self.ySol + 22)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("yellow")
        turtle.circle(7)
        turtle.end_fill()
        turtle.penup()

        # Lampe 2
        turtle.goto(self.xSol - 20, self.ySol + 45)
        trait(self.xSol - 20, self.ySol + 45, self.xSol - 20, self.ySol + 35)
        turtle.goto(self.xSol - 20, self.ySol + 22)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor("yellow")
        turtle.circle(7)
        turtle.end_fill()
        turtle.pensize(1)
        turtle.penup()

    def __init__(self, nom, xSol, ySol):
        self.nom = nom
        self.xSol = xSol
        self.ySol = ySol

    def __repr__(self):
        return repr(self.toString())

    def toString(self) -> str:
        return f"Lampadaire;'{self.nom}';{self.xSol};{self.ySol}"


'''
if __name__ == '__main__':
    lampadaire(1, 10)
    turtle.exitonclick()
    '''