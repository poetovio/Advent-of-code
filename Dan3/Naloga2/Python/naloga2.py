indeks = 0
datoteka = []

with open("input.txt") as file:
    datoteka = [x for x in file.read().split()]

datoteka2 = datoteka.copy()

while len(datoteka) > 1:
    one = 0
    zero = 0
    enke = []
    nule = []
    for x in range(0, len(datoteka)):
        if(datoteka[x][indeks] == '1'):
            one += 1
            enke.append(datoteka[x])
        else:
            zero += 1
            nule.append(datoteka[x])
    if(one >= zero):
        datoteka = enke
    else:
        datoteka = nule
    indeks += 1

kisik = int(datoteka[0], 2)

print(kisik)

datoteka = datoteka2
indeks = 0
while len(datoteka) > 1:
    one = 0
    zero = 0
    enke = []
    nule = []
    for x in range(0, len(datoteka)):
        if(datoteka[x][indeks] == '1'):
            one += 1
            enke.append(datoteka[x])
        else:
            zero += 1
            nule.append(datoteka[x])
    if(one >= zero):
        datoteka = nule
    else:
        datoteka = enke
    indeks += 1

co2 = 0
stevec = len(datoteka[0])
for x in datoteka[0]:
    co2 += pow(2, stevec - 1) * int(x)
    stevec -= 1

print(co2)

print(kisik * co2)