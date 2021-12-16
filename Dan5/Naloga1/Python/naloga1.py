from os import X_OK
import numpy as np

vrstice = []
maxVelikost = 0
stevec = 0


seznam = []

class Objekt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

for vrstica in open("input.txt"):
    vrstice.append(vrstica.replace('\n', ''))

objekti = []
stvari = []
preveritevStvari = []

for vrstica in vrstice:
    objekt = []
    objekt = vrstica.split(' -> ')
    tabela = []
    for indeks in objekt:
        dela = indeks.split(',')
        for i in range(2):
            if(int(dela[i]) > int(maxVelikost)):
                maxVelikost = dela[i]
        stvar = Objekt(int(dela[0]), int(dela[1]))
        stvari.append(stvar)
            
        tabela.append(dela)
    objekti.append(tabela)

polje = np.zeros((int(maxVelikost) + 1, int(maxVelikost) + 1), dtype=np.int64)

steviloObjektov = 0
while(steviloObjektov < len(stvari)):
    x1 = stvari[steviloObjektov].x
    x2 = stvari[steviloObjektov + 1].x
    y1 = stvari[steviloObjektov].y
    y2 = stvari[steviloObjektov + 1].y

    if(x1 == x2):

        polje[y1][x1] += 1
        polje[y2][x2] += 1
        y = y1 - y2
        for i in range(1, abs(y)):
            if(y >= 1):
                polje[y1 - i][x1] += 1
            else:
                polje[y1 + i][x1] += 1
    elif(y1 == y2):

        polje[y2][x1] += 1
        polje[y2][x2] += 1

        x = x1 - x2
        for i in range(1, abs(x)):
            if(x1 > x2):
                polje[y2][x1 - i] += 1
            else:
                polje[y2][x1 + i] += 1
    elif(x1 > x2 and y1 > y2):
        polje[y1][x1] += 1
        polje[y2][x2] += 1

        x = x1 - x2
        y = y1 - y2

        if(abs(x) > abs(y)):
            for i in range(1, abs(x)):
                polje[y1 - i][x1 - i] += 1
        else:
            for i in range(1, abs(y)):
                polje[y1 - i][x1 - i] += 1
    elif(x1 < x2 and y1 < y2):
        polje[y1][x1] += 1
        polje[y2][x2] += 1

        x = x1 - x2
        y = y1 - y2

        if(abs(x) > abs(y)):
            for i in range(1, abs(x)):
                polje[y1 + i][x1 + i] += 1
        else:
            for i in range(1, abs(y)):
                polje[y1 + i][x1 + i] += 1
    elif(x1 < x2 and y1 > y2):
        polje[y1][x1] += 1
        polje[y2][x2] += 1

        x = x1 - x2
        y = y1 - y2

        if(abs(x) > abs(y)):
            for i in range(1, abs(x)):
                polje[y1 - i][x1 + i] += 1
        else:
            for i in range(1, abs(y)):
                polje[y1 - i][x1 + i] += 1
    elif(x1 > x2 and y1 < y2):
        polje[y1][x1] += 1
        polje[y2][x2] += 1

        x = x1 - x2
        y = y1 - y2

        if(abs(x) > abs(y)):
            for i in range(1, abs(x)):
                polje[y1 + i][x1 - i] += 1
        else:
            for i in range(1, abs(y)):
                polje[y1 + i][x1 - i] += 1      
    steviloObjektov += 2

stevec = 0
print(len(np.where(polje >= 2)[0]))