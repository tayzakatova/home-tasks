#задачка как в контесте последнем у меня тут реализовано костыльно, но зато свое
a = int(input())
n = input()
m = input()
k = 0
h = 0
t = ''
j = ''
n1 = n + '1' + n + '1'
n0 = n + '0' + n + '0'

p = n1.find(m)
if p != -1:
    k = 1
    if p == 0:
        t = n1[2*a - 2]
    if p == 1:
        t = n1[2*a - 1]
    if p >= 2:
        t = n1[p - 1]
print(p)
p = n0.find(m)
if p != -1:
    h = 1
    if p == 0:
        j = n0[2*a - 2]
    if p == 1:
        j = n0[2*a - 1]
    if p >= 2:
        j = n0[p - 1]

print(k, h)
#print(p)
print(n1)
if k == h == 1:
    print('Random')
if k == 0 and h == 1:
    if j == '1':
        print('Yes')
    if j == '0':
        print('No')
if k == 1 and h == 0:
    if t == '1':
        print('Yes')
    if t == '0':
        print('No')
