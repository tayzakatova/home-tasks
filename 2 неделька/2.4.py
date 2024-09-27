a = list(input())
for i in range(0, len(a)-2, 2):
    a[i], a[i+1] = a[i+1], a[i]
print(*a, sep=' ')