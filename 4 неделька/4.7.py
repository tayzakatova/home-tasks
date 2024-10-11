#Я не смогла найти файлик, который там просят, поэтому просто сделала по своему
with open('для4.7.txt', 'r', encoding="utf-8") as f:
    s = f.read()
s = s.replace('!', ' ')
s = s.replace('.', ' ')
s = s.replace(',', ' ')
#сделать так со всеми знаками по необходимости
s = s.lower()
a = s.split()
d = {}
for i in a:
    d[i] = a.count(i)
d = dict(sorted(d.items()))
h = list(d.items())[:10]
for key, value in h:
    print(f'{key}: {value}')   