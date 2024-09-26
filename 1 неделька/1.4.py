f = open('input.txt')
#f.read()
k = 0
c = 1
a = list(map(int,f.readline().split(' ')))
b = f.readline().strip()
if b == '+':
    for i in range(len(a)):
        k += a[i]
    res = k
if b =='-':
    for i in range(len(a)):
        k -= a[i]
    res = k
if b == '*':
    for i in range(len(a)):
        c *= a[i]
    res = c
g = open('output.txt', 'w')
g.write(str(res))