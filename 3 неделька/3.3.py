s = list(input().split())
a = int(s[0])
b = int(s[1])
#a, b = map(int(input().split()))
'''def mod(a):
    if a >= 0:
        return(a)
    if a < 0:
        return((-1)*a)
m = min(mod(a), mod(b))
k = 0
for i in range(m, 0, -1):
    if a % i == 0 and b % i == 0:
        nod = i
        break'''
def f(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x_1, y_1, d = f(b, a % b)
        x = y_1
        y = x_1 - (a // b) * y_1
        return x, y, d    
print(f(a, b))        

