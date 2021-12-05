stevec = 0


with open("input.txt", "r") as datoteka:
    stevila = datoteka.readlines()

    for x in range(3, len(stevila)):
        if(int(stevila[x]) > int(stevila[x - 3])):
            stevec += 1

print(stevec)