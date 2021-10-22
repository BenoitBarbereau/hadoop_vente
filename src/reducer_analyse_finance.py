import sys

condition = sys.argv[1].upper()

if condition == "REGION" or condition == "PAYS" or condition == "ITEM" :
    Ncle = None
    val0 = 0

    for line in sys.stdin :
        cle, val = line.split('\t', 1) 
        if cle != Ncle and Ncle != None:
            print(f'{Ncle}\t{val0}')
            val0 = 0
        Ncle = cle
        try :
            val0 += float(val.strip())
        except :
            pass
    print(f'{Ncle}\t{val0}')


elif condition == "VENTE":
    Ncle = None
    val0 = 0
    cont = 0

    for line in sys.stdin :
        cle, val = line.split('\t', 1) 

        if cle != Ncle and Ncle != None:
            print(f'{Ncle}\t{val0}\t{cont}')
            val0 = 0
            cont = 0

        cont += 1
        Ncle = cle

        try :
            val0 += float(val.strip())
        except :
            pass

    print(f'{Ncle}\t{val0}\t{cont}')
