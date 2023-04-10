import time

from utils.trait import *
from utils.couleurAleatoire import couleurAleatoire
import turtle

ratioX = 400 / 1100  # plus ou moins proche de l'axe des Y
ratioY = 300 / 1100  # plus ou moins proche de l'axe des X

objects = {}  # ensemble des figures à représenter
axes = False

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
        return -x * (3000+z) - y
    if getPOV() == 2:
        return x * (3000 - z) - y
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
    if getPOV() == 1 or getPOV() == -1 or getPOV() == 0:
        rectangle3D(base3, base4, plafond4, plafond3)
        turtle.end_fill()
        turtle.begin_fill()
        turtle.fillcolor(couleur)
        rectangle3D(base4, base1, plafond1, plafond4)
    if getPOV() == 2 or getPOV() == -2:
        rectangle3D(base1, base2, plafond2, plafond1)
        turtle.end_fill()
        turtle.begin_fill()
        turtle.fillcolor(couleur)
        rectangle3D(base4, base1, plafond1, plafond4)
    turtle.end_fill()

    turtle.penup()

# Permet de dessiner tout les objets
def process():
    for object in sorted(objects, reverse=True):
        figure = objects[object].split(';')
        type = figure[0]

        print(f'{object} -> {type}')

        if type == "volume":
            volume(int(figure[1]), int(figure[2]), int(figure[3]), int(figure[4]),int(figure[5]), int(figure[6]), eval(figure[7]))
        if type == "porte":
            volume(int(figure[1]), int(figure[2]), int(figure[3]), 30, 50, 2, eval(figure[4]))
            volume(int(figure[1]) + 20, int(figure[2]) + 20, int(figure[3]), 3, 3, 3, (0,0,0))
        if type == "fenetre":
            volume(int(figure[1]), int(figure[2]) + 20, int(figure[3]), 30, 30, 2, eval(figure[4]))
        if type == "fenetre-balcon":
            volume(int(figure[1]), int(figure[2]), int(figure[3]), 30, 50, 2, eval(figure[4]))

            volume(int(figure[1]) - 7, int(figure[2]) + 20, int(figure[3]) - 5, 3, 3, 15, (0,0,0))
            volume(int(figure[1]) + 30, int(figure[2]) + 20, int(figure[3]) - 5, 3, 3, 15, (0,0,0))

            volume(int(figure[1]) - 5, int(figure[2]) + 20, int(figure[3]) - 5, 40, 3, 2, (0,0,0))
            volume(int(figure[1]) - 5, int(figure[2]) - 3, int(figure[3]) - 5, 40, 3, 15, (0,0,0))

            volume(int(figure[1]) - 7, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) - 2, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 3, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 8, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 13, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 18, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 23, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 28, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))
            volume(int(figure[1]) + 33, int(figure[2]) - 3, int(figure[3]) - 5, 1, 25, 2, (0,0,0))


def generate(type, x, y, z, options):
    objects[getPriority(x,y,z)] = f'{type};{x};{y};{z};{options}'
    return objects

if __name__ == '__main__':
    turtle.hideturtle()
    turtle.penup()
    turtle.Screen().tracer(0)
    ecart = 220

    for y in range(-1,2):
        tt = couleurAleatoire()
        generate("volume", y*ecart, 0, 0, f'{140};{60};{140};{tt}')
        generate("porte", y*ecart + 95, 0, 0, couleurAleatoire())

        for i in range(1,6):
            generate("volume", y*ecart, i*60, 0, f'{140};{60};{140};{tt}')
            generate("fenetre", y*ecart+55, i * 60, 0, (144, 144, 144))
            generate("fenetre-balcon", y*ecart+15, i * 60, 0, (144, 144, 144))
            generate("fenetre-balcon", y*ecart+95, i * 60, 0, (144, 144, 144))

    generate("volume", -800,-5,-30, f'{2500};{5};{30};{(0,0,0)}')
    # generate("volume", -1500,-25,0, f'{2500};{10};{75};{(0,0,0)}')

    # generate("volume", 400, 0, 500, f'{100};{100};{100};{(255,0,0)}')
    # generate("volume", 600, 0, 500, f'{100};{100};{100};{(255,0,0)}')
    # generate("volume", 500, 50, 400, f'{100};{100};{100};{(255,0,0)}')
    # generate("volume", 400, 0, 300, f'{100};{100};{100};{(255,0,0)}')
    # generate("volume", 600, 0, 300, f'{100};{100};{100};{(255,0,0)}')
    #
    # generate("volume", 200, 0, 0, f'{100};{100};{100};{(0,0,255)}')
    # generate("volume", 0, 0, 200, f'{100};{100};{100};{(0,0,255)}')
    # generate("volume", 200, 0, 200, f'{100};{100};{100};{(0,0,255)}')
    # generate("volume", 100, 100, 100, f'{100};{100};{100};{(0,0,255)}')

    # Axes x,y,z
    if axes:
        trait(0, -2000, 0, 2000)
        trait(-2000, 0, 2000, 0)
        traitVec(parse3D(0, 0, 2000), parse3D(0, 0, -2000))

    # Dessine toutes les figures - A faire une fois que toutes figures sont enregistrées grâce à la commande generate
    process()

    turtle.Screen().update()
    turtle.done()
