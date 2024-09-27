a = list(map(int, input().split()))
n = a[0]
l = a[1:]
S = sum(l)
print(int((1+n)*n/2 -S))
