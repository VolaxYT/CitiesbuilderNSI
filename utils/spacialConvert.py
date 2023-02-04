import random

from trait import *
from couleurAleatoire import couleurAleatoire
import turtle

ratioX = 400 / 1100  # plus ou moins proche de l'axe des Y
ratioY = 300 / 1100  # plus ou moins proche de l'axe des X

objects = {}  # ensemble des figures à représenter

# explication : https://prnt.sc/sgCj3NLM07k5 (ligne à delete du projet final)
# valeur arbitraire pour les calculs de priorités et l'ordre de rendu des élements
def getPOV():
    # Si POV sans profondeur (plan en 2D)
    if ratioY == 0 and ratioX == 0:
        return 0
    # Si POV au dessus de l'axe x
    if ratioY >= 0:
        # Si POV à droite de l'axe y
        if ratioX >= 0:
            return 1
        # Si POV à gauche de l'axe y
        else:
            return 2
    # Si POV en dessous de l'axe x
    else:
        # Si POV à droite de l'axe y
        if ratioX >= 0:
            return -1
        # Si POV à gauche de l'axe y
        else:
            return -2

def getPriority(x,y,z):
    if getPOV() == 1:
        return (5000-x) * (3000+z) - y
    if getPOV() == 2:
        return (5000 + x) * (3000 + z) - y
    if getPOV() == -2:
        return (5000 + x) * (3000 + z) + y
    if getPOV() == -1 or getPOV() == 0:
        return (5000 - x) * (3000 + z) + y

def parse3D(x, y, z):
    return x + z * ratioX, y + z * ratioY, z

def trait3D(x1, y1, z1, x2, y2, z2):
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


def volume(x, y, z, longueur, hauteur, profondeur, couleur):
    turtle.colormode(255)
    startPos = parse3D(x, y, z)
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
    if getPOV() == 1 or getPOV() == -1:
        rectangle3D(base3, base4, plafond4, plafond3)
        rectangle3D(base4, base1, plafond1, plafond4)
    if getPOV() == 2 or getPOV() == -2:
        rectangle3D(base1, base2, plafond2, plafond1)
        turtle.end_fill()
        turtle.begin_fill()
        turtle.fillcolor(couleur)
        rectangle3D(base4, base1, plafond1, plafond4)
    turtle.end_fill()

    turtle.penup()

def process():
    for object in sorted(objects, reverse=True):
        print(object)
        figure = objects[object].split(';')
        volume(int(figure[0]), int(figure[1]),int(figure[2]),int(figure[3]),int(figure[4]), int(figure[5]), eval(figure[6]))

def generate(x, y, z, longueur, hauteur, profondeur, couleur):
    objects[getPriority(x,y,z)] = f'{x};{y};{z};{longueur};{hauteur};{profondeur};{couleur}'

if __name__ == '__main__':
    generate(400, 0, 500, 100, 100, 100, (255,0,0))
    generate(600, 0, 500, 100, 100, 100, (255,0,0))
    generate(500, 50, 400, 100, 150, 100, (255,0,0))
    generate(400, 0, 300, 100, 100, 100, (255,0,0))
    generate(600, 0, 300, 100, 100, 100, (255,0,0))

    generate(200, 0, 0, 100, 100, 100, (0,0,255))
    generate(0, 0, 200, 100, 100, 100, (0,0,255))
    generate(200, 0, 200, 100, 100, 100, (0,0,255))
    generate(100, 100, 100, 100, 150, 100, (0,0,255))
    generate(0, 0, 0, 100, 100, 100, (0,0,255))

    generate(160, 0, -400, 100, 100, 100, couleurAleatoire())
    generate(160, 100, -400, 100, 100, 100, couleurAleatoire())
    generate(160, 200, -400, 100, 100, 100, couleurAleatoire())

    turtle.Screen().tracer(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.pensize(4)

    #trait(0, -2000, 0, 2000)
    #trait(-2000, 0, 2000, 0)
    #traitVec(parse3D(0, 0, 2000), parse3D(0, 0, -2000))

    process()
    print(getPOV())
    turtle.Screen().update()
    turtle.done()
