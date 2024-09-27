a = list(input())
a = [a[-1]] + a[:-1]
print(*a, sep=' ')