a = list(map(int, input().split()))
k = 1
for i in range(len(a)):
    k *= a[i]
print(k**(1/len(a)))
