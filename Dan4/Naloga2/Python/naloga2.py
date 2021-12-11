vrstice = []

for vrstica in open("input.txt"):
    vrstice.append(vrstica.replace('\n', ''))

stevila = list(map(int, vrstice[0].split(',')))

kartice = []

def izberiZmagovalca(kartica):
    stevec = 0
    # pregled po vrsticah
    for i in range(5):
        for j in kartica[i]:
            if(j == '%'):
                stevec += 1
        if(stevec == 5):
            return True
        stevec = 0

    stevec = 0
    #pregled po stolpcih
    for i in range(5):
        for vrstica in kartica:
            if(vrstica[i] == '%'):
                stevec += 1
        if(stevec == 5):
            return True
        stevec = 0
    return False

def zmagovalnaKartica(stevila, kartice):
    for stevilo in stevila:
        for i in range(len(kartice)):
            for j in range(5):
                for k in range(5):
                    if(kartice[i][j][k] != '%'):
                        if(int(stevilo) == int(kartice[i][j][k])):
                            kartice[i][j][k] = '%'
        
        if(len(kartice) > 1):
            stevec = 0
            for kartica in kartice:
                if(izberiZmagovalca(kartica)):
                    kartice.remove(kartica)
        else:
            return kartice[0], stevilo

def izracunajVrednost(kartica):
    stevilo = 0
    for i in range(5):
        for j in range(5):
            if(kartica[i][j] != '%'):
                stevilo += int(kartica[i][j])
    return stevilo

x = 2
while(x < len(vrstice)):
    kartica = []
    for i in range(0, 5):
        vrstica = vrstice[x + i].split(' ')
        for y in vrstica:
            if(y == ''):
                vrstica.remove(y)
        kartica.append(vrstica)
    x += 6
    kartice.append(kartica)

zmagovalka, zmagovalnoStevilo = zmagovalnaKartica(stevila, kartice)

print(izracunajVrednost(zmagovalka) * zmagovalnoStevilo)
