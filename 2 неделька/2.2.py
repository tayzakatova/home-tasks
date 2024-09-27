a = list(input().split(' '))
b = int(a[0])
c = a[1]
for p in range(0, (len(c)//b)+1):
    d = c[b*p: b*(p+1)]
    k = d[::-1]
    c = c.replace(d, k)
print(c)

