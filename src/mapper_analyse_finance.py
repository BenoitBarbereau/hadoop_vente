import sys

def mapper():
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[0]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[1]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[2]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = (f'{colones[3]}+{colones[2]}')
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})


if __name__ == "__main__":
    mapper()