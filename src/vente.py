hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.3.jar -input ./sales_world_10k.csv -output ./test -mapper "python3 /home/mbds/mapper_analyse_finance.py X" -reducer "python3 /home/mbds/reducer_analyse_finance.py X"


import sys

condition = sys.argv[1]

if condition == "Region" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[0]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})

elif condition == "Pays" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[1]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})

elif condition == "Item" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = colones[2]
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})

elif condition == "Vente" :
    tab = []
    for line in sys.stdin :
        colones = line.split(',')
        clé = (f'{colones[3]}+{colones[2]}')
        valeur = colones[-1]
        print({clé}+' : ' + {valeur})







import sys

if condition == "Region" or condition == "Pays" or condition == "Item" :
    tabF=[]
    Nclé = None
    val0 = 0

    for line in sys.stdin :
        clé, val = line.split({' : '}) 

        if clé != Nclé and Nclé != None:
            print({Nclé}+' : ' + {val0})
            val0 = 0

        Nclé = clé

        try :
            val0 += float(val.strip())
        except :
            pass
    print({Nclé}+' : ' + {val0})


elif condition == "Vente" :
    tabF=[]
    Nclé = None
    val0 = 0
    cont = 0

    for line in sys.stdin :
        clé, val = line.split({' : '}) 

        if clé != Nclé and Nclé != None:
            print({Nclé}+' : ' + {val0} +' : '+{cont})
            val0 = 0
            cont =0

        cont += 1
        Nclé = clé

        try :
            val0 += float(val.strip())
        except :
            pass

    print({Nclé}+' : ' + {val0}+' : '+{cont})




