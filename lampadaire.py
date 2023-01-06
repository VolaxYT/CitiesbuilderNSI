from utils.trait import trait
import turtle

'''
xSol = coordonnées x par rapport au sol
ySol = ccoordonnées y par rapport au sol
'''

def lampadaire(xSol, ySol):
    turtle.pensize(3)
    #Base
    trait(xSol, ySol, xSol, ySol+45)
    #Extremités
    trait(xSol-20, ySol+45, xSol+20, ySol+45)
    #Lampe 1
    trait(xSol+20, ySol+45, xSol+20, ySol+35)
    turtle.goto(xSol+20, ySol+22)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(7)
    turtle.end_fill()
    turtle.penup()

    #Lampe 2
    turtle.goto(xSol-20, ySol+45)
    trait(xSol-20, ySol+45, xSol-20, ySol+35)
    turtle.goto(xSol-20, ySol+22)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(7)
    turtle.end_fill()
    turtle.pensize(1)
    

'''
if __name__ == '__main__':
    lampadaire(1, 10)
    turtle.exitonclick()
    '''