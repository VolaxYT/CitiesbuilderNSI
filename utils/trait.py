# module trait

import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()

def traitVec(p1, p2):
    '''
    Paramètres
        p1 : coordonnées du début du trait
        p2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    turtle.penup()
    turtle.goto(p1[0], p1[1])
    turtle.pendown()
    turtle.goto(p2[0], p2[1])
    turtle.penup()

if __name__ == '__main__':
    trait(-300,300,100,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()