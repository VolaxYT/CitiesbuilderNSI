from batiments.immeuble.immeuble import Immeuble

def parse_tuple(string):
    try:
        s = eval(string)
        if type(s) == tuple:
            return s
        return
    except:
        return


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
    print(immeubleString)
    options = immeubleString.replace('"', '').split(';')
    immeuble = Immeuble(options[1], int(options[2]), float(options[3]), float(options[4]), int(options[5]), parse_tuple(options[6]), parse_tuple(options[7]), str(options[8]), list(options[9].replace('[', '').replace(']', '').replace(",", '').replace(" ", "")))
    immeuble.draw()

