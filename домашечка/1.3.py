import math
rates1 = [('RUB', 'USD', 0.013), ('USD', 'EUR', 0.9), ('EUR', 'RUB', 85),] #денег не будет
rates = [('RUB', 'USD', 0.013), ('USD', 'EUR', 0.9), ('EUR', 'RUB', 86),] #деньги будут

currencies = []
for r in rates:
    if r[0] not in currencies:
        currencies.append(r[0])
    if r[1] not in currencies:
        currencies.append(r[1])

dist = {}
for c in currencies:
    dist[c] = 1000000000  #боооооольшое число

start = currencies[0]
dist[start] = 0

edges = []
for r in rates:
    u = r[0]
    v = r[1]
    rate = r[2]
    weight = -math.log(rate)
    edges.append((u, v, weight))

for i in range(len(currencies) - 1):
    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

can_make_money = False
for edge in edges:
    u = edge[0]
    v = edge[1]
    w = edge[2]
    if dist[u] + w < dist[v]:
        can_make_money = True

if can_make_money:
    print("Сегодня комплекный обед с меня")
else:
    print("Мы не будем богатеями")
