# module toit2 (plat)

import turtle
from utils.trait import trait

def toit2(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.fillcolor("black")
    turtle.begin_fill()
    trait(x - 80, ySol + niveau*60, x +80, ySol + niveau*60)
    turtle.goto(x - 80, ySol + niveau*60)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.end_fill()
    turtle.begin_fill()
    trait(x - 80, ySol + niveau*60 +10, x +80, ySol + niveau*60 +10)
    turtle.goto(x + 80, ySol + niveau*60)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.end_fill()

if __name__ == '__main__':
    toit2(0,0,2)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()