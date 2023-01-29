from trait import *
from couleurAleatoire import *

ratioX = 400/1100  # plus ou moins proche de l'axe des Y
ratioY = 300/1100  # plus ou moins proche de l'axe des X

def parse3D(x,y,z):
    return x + z*ratioX, y + z*ratioY, z

def trait3D(x1,y1,z1, x2, y2, z2):
    point1 = parse3D(x1, y1, z1)
    point2 = parse3D(x2, y2, z2)

    turtle.penup()
    turtle.goto(point1[0], point1[1])
    turtle.pendown()
    turtle.goto(point2[0], point2[1])
    turtle.penup()

def rectangle3D(point1, point2, point3, point4):
    traitVec(point1, point2)
    traitVec(point2, point3)
    traitVec(point3, point4)
    traitVec(point4, point1)

def volume(x,y,z,longueur, hauteur, profondeur, couleur):
    turtle.colormode(255)
    startPos = parse3D(x,y,z)
    turtle.goto(startPos[0], startPos[1])
    turtle.pendown()

    base1 = parse3D(x, y, z)
    base2 = parse3D(x, y, z + profondeur)
    base3 = parse3D(x + longueur, y, z + profondeur)
    base4 = parse3D(x + longueur, y, z)

    plafond1 = parse3D(x, y + hauteur, z)
    plafond2 = parse3D(x, y + hauteur, z + profondeur)
    plafond3 = parse3D(x + longueur, y + hauteur, z + profondeur)
    plafond4 = parse3D(x + longueur, y + hauteur, z)

    turtle.begin_fill()
    turtle.fillcolor(couleur)
    rectangle3D(base1, base2, base3, base4)
    rectangle3D(plafond1, plafond2, plafond3, plafond4)
    turtle.end_fill()
    turtle.begin_fill()

    turtle.fillcolor(couleur)
    rectangle3D(base3, base4, plafond4, plafond3)
    rectangle3D(base4, base1, plafond1, plafond4)
    turtle.end_fill()


    turtle.penup()

if __name__ == '__main__':
    turtle.Screen().tracer(0)
    turtle.hideturtle()
    turtle.pensize(4)

    trait(0, -2000, 0, 2000)
    trait(-2000, 0, 2000, 0)
    traitVec(parse3D(0, 0, 2000), parse3D(0, 0, -2000))

    volume(400, 0, 500, 100, 100, 100, couleurAleatoire())
    volume(600, 0, 500, 100, 100, 100, couleurAleatoire())
    volume(500, 50, 400, 100, 150, 100, couleurAleatoire())
    volume(400, 0, 300, 100, 100, 100, couleurAleatoire())
    volume(600, 0, 300, 100, 100, 100, couleurAleatoire())

    volume(0,0,200,100,100,100, couleurAleatoire())
    volume(200,0,200,100,100,100, couleurAleatoire())
    volume(100,100,100,100,150,100, couleurAleatoire())
    volume(0,0,0,100,100,100, couleurAleatoire())
    volume(200,0,0,100,100,100, couleurAleatoire())

    turtle.Screen().update()
    turtle.done()
