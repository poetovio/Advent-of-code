import numpy as np
import sys

tabela = np.loadtxt('input.txt', delimiter=',', dtype='int_')

resitev = sys.maxsize

for x in range(np.max(tabela)):
    razlika = 0
    for y in tabela:
        razlika += (abs(x - y) * (abs(x - y) + 1))/2
        if(razlika > resitev):
            continue
    if(razlika < resitev):
        resitev = razlika
print(resitev)