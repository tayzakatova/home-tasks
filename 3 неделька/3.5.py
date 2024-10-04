import numpy as np
def matrix():
    data = list(map(int, input('Введите кол-во строк и столбцов матрицы через пробел:').split()))
    m, n = data[0], data[1]
    a = np.zeros((m, n))
    a[0][0] = 1
    i = 0
    j = 1
    counter = 1

    while 0 in a:
        while j < n and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j += 1
        j -= 1
        i += 1

        while i < m and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i += 1
        i -= 1
        j -= 1

        while j > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j -= 1
        j += 1
        i -= 1

        while i > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i -= 1
        i += 1
        j += 1
    return a
first_res = matrix()
def multiplication(first_res):
    for i in range(len(first_res)):
        first_res[i] = np.array(first_res[i]) * (i + 1)
    return first_res
print(multiplication(first_res))