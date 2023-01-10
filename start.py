
from tkinter import *

import rue
import sys
from rue import *
from utils.manageSave import *

# Relancer la fenêtre de la turtle et mettre à jour tout les paramètres
def refreshParamsAndRelaunch():
    param.width = int(widthEntry.get())
    param.height = int(heightEntry.get())
    param.maxEtages = int(maxEtagesEntry.get())
    param.lampadairesChance = int(lampdairesChanceScale.get())
    param.allowSoleil = bool(soleilButton.config('text')[-1] == "True")
    param.allowLampadaires = bool(lampadairesButton.config('text')[-1] == "True")
    param.instantDrawing = bool(instantDrawingButton.config('text')[-1] == "True")
    param.importFileName = str(importFileNameEntry.get())
    param.randomStreet = bool(randomStreetButton.config('text')[-1] == "True")
    rue.elementsList = []

    wn = turtle.Screen()
    wn.clearscreen()

    main()


# Fonction pour arrêter turtle et fermer le programme
def end():
    turtle.bye()
    turtle.Screen().bye()
    sys.exit()


def save():
    if saveFileNameEntry.get() != "" and saveFileNameEntry.get() != ".txt" and isRandomSteet():
        objects = f"Main;'Rue';{param.isInstantDrawing()};{param.getWidth()};{param.getHeight()}\n"

        for batiment in rue.elementsList:
            objects += str(batiment) + "\n"

        exportFile(str(saveFileNameEntry.get()), objects)

# Fonction pour faire le boutton "switch" du soleil
def onOffSoleil():
    if soleilButton.config('text')[-1] == 'True':
        soleilButton.config(text='False')
    else:
        soleilButton.config(text='True')


# Fonction pour faire le boutton "switch" des lampadaires
def onOffLampadaires():
    if lampadairesButton.config('text')[-1] == 'True':
        lampadairesButton.config(text='False')
    else:
        lampadairesButton.config(text='True')


# Fonction pour faire le boutton "switch" du dessin instantané
def onOffInstantDrawing():
    if instantDrawingButton.config('text')[-1] == 'True':
        instantDrawingButton.config(text='False')
    else:
        instantDrawingButton.config(text='True')


# Fonction pour faire le boutton "switch" du dessin aléatoire de la rue
def onOffRandomStreet():
    if randomStreetButton.config('text')[-1] == 'True':
        randomStreetButton.config(text='False')
    else:
        randomStreetButton.config(text='True')


if __name__ == '__main__':
    # Fenêtre des paramètres
    win = Tk()
    win.title("Paramètres")
    optionsNumber = 10
    win.geometry(f"250x{optionsNumber * 45}")
    win.resizable(False, False)

    Label(win, text="Random street", font=("Courier", 8)).place(x=3, y=0 * 40 + 15)
    randomStreetButton = Button(text=str(isRandomSteet()), width=10, command=onOffRandomStreet)
    randomStreetButton.place(x=133, y=0 * 40 + 15)

    Label(win, text="Import File Name ", font=("Courier", 8)).place(x=3, y=1 * 40 + 15)
    importFileNameEntry = Entry(win, width=14)
    importFileNameEntry.insert(0, "test.txt")
    importFileNameEntry.place(x=133, y=1 * 40 + 15)

    Label(win, text="Save File Name ", font=("Courier", 8)).place(x=3, y=2 * 40 + 15)
    saveFileNameEntry = Entry(win, width=14)
    saveFileNameEntry.insert(0, "test.txt")
    saveFileNameEntry.place(x=133, y=2 * 40 + 15)

    # Modifier la largeur de la fenêtre "Dessine ta rue"
    Label(win, text="Width", font=("Courier", 8)).place(x=3, y=3 * 40 + 15)
    widthEntry = Entry(win, width=5)
    widthEntry.insert(0, param.getWidth())
    widthEntry.place(x=133, y=3 * 40 + 15)

    # Modifier la hauteur de la fenêtre "Dessine ta rue"
    Label(win, text="Height", font=("Courier", 8)).place(x=3, y=4 * 40 + 15)
    heightEntry = Entry(win, width=5)
    heightEntry.insert(0, param.getHeight())
    heightEntry.place(x=133, y=4 * 40 + 15)

    # Modifier le nombre d'étages max par immeuble
    Label(win, text="Max Etages", font=("Courier", 8)).place(x=3, y=5 * 40 + 15)
    maxEtagesEntry = Entry(win, width=2)
    maxEtagesEntry.insert(0, param.getMaxEtages())
    maxEtagesEntry.place(x=133, y=5 * 40 + 15)

    # Modifier si le soleil apparait
    Label(win, text="Soleil", font=("Courier", 8)).place(x=3, y=6 * 40 + 15)
    soleilButton = Button(text=str(isAllowSoleil()), width=10, command=onOffSoleil)
    soleilButton.place(x=133, y=6 * 40 + 15)

    # Modifier si les lampadaires apparaissent
    Label(win, text="Lamps", font=("Courier", 8)).place(x=3, y=7 * 40 + 15)
    lampadairesButton = Button(text=str(isAllowLampdaires()), width=10, command=onOffLampadaires)
    lampadairesButton.place(x=133, y=7 * 40 + 15)

    # Modifier la chance qu'un lampadaire soit crée sur 100
    Label(win, text="Lamps Spawn Chance", font=("Courier", 8)).place(x=3, y=8 * 40 + 20)
    lampdairesChanceScale = Scale(win, from_=0, to=100, orient=HORIZONTAL)
    lampdairesChanceScale.set(getLampadairesChance())
    lampdairesChanceScale.place(x=133, y=8 * 40 + 2)

    Label(win, text="Instant Drawing", font=("Courier", 8)).place(x=3, y=9 * 40 + 15)
    instantDrawingButton = Button(text=str(isInstantDrawing()), width=10, command=onOffInstantDrawing)
    instantDrawingButton.place(x=133, y=9 * 40 + 15)

    # Button pour sauvegarder la génération
    save = Button(win, text="Save", command=save)
    save.place(x=10, y=optionsNumber * 40 + 10)

    # Button pour relancer la génération
    relaunch = Button(win, text="Relancer la génération", command=refreshParamsAndRelaunch)
    relaunch.place(x=48, y=optionsNumber * 40 + 10)

    # Button pour fermer le programme
    close = Button(win, text="Fermer", command=end)
    close.place(x=180, y=optionsNumber * 40 + 10)

    main()
    win.mainloop()