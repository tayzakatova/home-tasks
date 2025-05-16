#я функция показывает сколько символов подряд в строке совпадает с ее началом
#типо [0, 0, 1, 0, 3, 0, 1] для 0102010
def restore_from_z(z):
    n = len(z)
    s = ['#'] * n
    s[0] = 'a'
    for i in range(1, n):
        if z[i] > 0:
            for j in range(z[i]):
                if s[i+j] == '#':
                    s[i+j] = s[j]
                elif s[i+j] != s[j]:
                    break
    for i in range(n):
        if s[i] == '#':
            s[i] = 'a'
    return ''.join(s)

z = [7,0,1,0,3,0,1]
print(restore_from_z(z))
