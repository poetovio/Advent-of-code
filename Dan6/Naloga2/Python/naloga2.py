tabela = {}

with open("input.txt", "r") as datoteka:
    vrednosti = [int(x) for x in datoteka.readline().split(",")]

    for vrednost in range(max(9, max(vrednosti))):
        tabela[vrednost] = 0
    for element in vrednosti:
        tabela[element] += 1

for x in range(256):
    nicle = tabela[0]
    tabela[0] = 0
    for y in range(1, len(tabela)):
        tabela[y - 1] += tabela[y]
        tabela[y] = 0
    tabela[6] += nicle
    tabela[8] += nicle

resitev = 0
for x in tabela:
    resitev += tabela[x]

print(resitev)