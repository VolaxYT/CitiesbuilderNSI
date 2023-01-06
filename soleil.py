import turtle

'''
x = coordonnées x du centre de la rue
ySol = ccoordonnées y par rapport au sol
'''

def soleil(x, y, size):
    turtle.pensize(3)

    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    turtle.pensize(1)


'''
if __name__ == '__main__':
    soleil(0, 0)
    turtle.exitonclick()
    '''