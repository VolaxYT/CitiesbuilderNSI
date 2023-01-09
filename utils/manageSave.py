import turtle

from batiments.immeuble.immeuble import Immeuble
from others.lampadaire import Lampadaire
from others.star import Star
from sol import sol

def exportFile(fileName, objects):
    f = open("saves/" + fileName, "w")
    f.write(objects)
    f.close()

def importFile(fileName):
    f = open("saves/" + fileName)

    lines = f.read().splitlines()
    options = lines[0].replace('"', '').split(';')
    turtle.setup(int(options[3]), int(options[4]))


    if bool(options[2]):
        turtle.Screen().tracer(0)

    # Dessin du sol de la rue
    sol(-(int(options[4]) / 4))

    for line in lines:
        if line.replace('"', '').split(';')[0] == "Immeuble":
            parseImmeuble(line)
        if line.replace('"', '').split(';')[0] == "Lampadaire":
            parseLampadaire(line)
        if line.replace('"', '').split(';')[0] == "Star":
            parseStar(line)

    if bool(options[2]):
        turtle.Screen().update()

def parseImmeuble(immeubleString):
    options = immeubleString.replace('"', '').split(';')
    immeuble = Immeuble(options[1], int(options[2]), float(options[3]), float(options[4]), int(options[5]), eval(options[6]), eval(options[7]), str(options[8]), list(options[9].replace('[', '').replace(']', '').replace(",", '').replace(" ", "")))
    immeuble.draw()

def parseLampadaire(lampadaireString):
    options = lampadaireString.replace('"', '').split(';')
    lampadaire = Lampadaire(options[1], float(options[2]), float(options[3]))
    lampadaire.draw()

def parseStar(starString):
    options = starString.replace('"', '').split(';')
    star = Star(options[1], options[2], float(options[3]), float(options[4]), int(options[5]))
    star.draw()
