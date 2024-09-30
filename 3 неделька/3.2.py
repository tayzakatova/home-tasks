c = int(input())
def factor(n, a = []):
    for i in range(2, n):
        if n%i == 0:
            a.append(i)
            return factor(n//i, a)
    a.append(n)
    return a
print(factor(c))
            