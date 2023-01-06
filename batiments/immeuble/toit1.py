# module toit1 (triangulaire)
from utils.trait import trait
import turtle

def toit1(x, ySol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        ySol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixel
    '''
    turtle.fillcolor('black')
    turtle.hideturtle()
    trait(x - 80, ySol + niveau*60, x + 80, ySol + niveau*60)
    turtle.begin_fill()
    trait(x, ySol + niveau*60 + 40, x, ySol + niveau*60)
    trait(x + 80, ySol + niveau*60, x, ySol + niveau*60 + 40)
    turtle.end_fill()
    turtle.begin_fill()
    trait(x, ySol + niveau*60 + 40, x, ySol + niveau*60)
    trait(x - 80, ySol + niveau*60, x, ySol + niveau*60 + 40)
    turtle.end_fill()

'''
if __name__ == '__main__':
    toit1(0,0,4)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    '''