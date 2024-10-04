import numpy as np
n = int(input('Кол-во строк:'))
m = int(input('Кол-во столбцов'))
#Параметр m здесь не нужен, но во входных данных он есть, поэтому PEP8 ругается

coeff = []
values = []
def linal(n ,m):
    for i in range(n):
        coeff.append(list(map(int, input().split())))
    if np.linalg.det(coeff) == 0:
        return 'Решений нет'
    else:
        for i in range(len(coeff)):
            values.append(coeff[i][-1])
            coeff[i] = coeff[i][:-1]
        return np.linalg.solve(coeff, values)
print(linal(n,m))