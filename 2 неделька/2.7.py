a = list(input())
k = a[0]
for i in range(0, len(a)-1):
    if a.count(a[i+1]) > a.count(a[i]):
        k = a[i+1]
print(k)