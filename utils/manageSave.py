from batiments.immeuble.immeuble import Immeuble

def exportFile(fileName, objects):
    f = open("saves/" + fileName, "w")
    f.write(objects)
    f.close()

def importFile(fileName):
    f = open("saves/" + fileName)
    for line in f.read().splitlines():
        if line.replace('"', '').split(';')[0] == "Immeuble":
            parseImmeuble(line)

def parseImmeuble(immeubleString):
    options = immeubleString.replace('"', '').split(';')
    immeuble = Immeuble(options[1], int(options[2]), float(options[3]), float(options[4]), int(options[5]), eval(options[6]), eval(options[7]), str(options[8]), list(options[9].replace('[', '').replace(']', '').replace(",", '').replace(" ", "")))
    immeuble.draw()

