fin = open(r"C:\Users\taisi\Desktop\study\inf\2 неделька\текстик.txt", "r", encoding='utf-8')
a = str(fin.readlines())
a = list(a)
res = 0
if len(a) == 2:
    if a[1] == '.':
        res += 1 
if len(a) == 3:
     if a[1] == '.' or a[2] == '.':
          res += 1
if a[len(a)-1] == '.' and a[len(a) - 1] != '.':
     res += 1
for i in range(0, len(a) - 2):
    if a[i+1] == '.' and a[i] != '.' and a[i+2] != '.':
        res += 1
    if a[i+1] == '.' and a[i] == '.' and a[i+2] == '.':
        res += 1
for i in range (0, len(a) - 1):
        if a[i] == '?' and a[i + 1] == '!':
            res +=1
        if a[i] == '?' and a[i + 1] != '!':
             res += 1
        if a[i + 1] == '!' and a[i] != '?':
             res += 1

print(res)