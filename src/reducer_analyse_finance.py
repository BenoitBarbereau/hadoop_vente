import sys

def reducer():
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

if __name__ == "__main__":
    reducer()