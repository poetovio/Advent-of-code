stevec = 0

with open("input.txt", "r") as datoteka:
    vrstica = int(datoteka.readline())
    while True:
        line = datoteka.readline()
        if not line:
            break
        if(int(line) > vrstica):
            stevec += 1
        vrstica = int(line)

print(stevec)
