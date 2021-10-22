import sys

condition = sys.argv[1].upper()

if condition == "REGION" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        cle = colones[0]
        valeur = colones[-1]
        print(f'{cle}\t{valeur}')

elif condition == "PAYS" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        cle = colones[1]
        valeur = colones[-1]
        print(f'{cle}\t{valeur}')


elif condition == "ITEM" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        cle = colones[2]
        valeur = colones[-1]
        print(f'{cle}\t{valeur}')


elif condition == "VENTE" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        cle = (f'{colones[2]} {colones[3]}')
        valeur = colones[-1]
        print(f'{cle}\t{valeur}')

