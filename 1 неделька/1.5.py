N = str(input())
b = int(input())
c = int(input())

def per1(N, b):
    k = 0
    l = len(N)
    for i in range(l):
        p = int(N[i])
        k += p * ( b ** (l - i - 1))
    return k

k = int(per1(N, b))


def per2(k, c):
    if k == 0:
        return "0"
    
    x = ""
    while k > 0:
        t = k % c
        x = str(t) + x
        k //= c
    return x

print(per2(k, c))
