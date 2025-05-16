def dfs(g, u, t, vis, f):
    if u == t:
        return f
    vis.add(u)
    for v in g[u]:
        if v not in vis and g[u][v] > 0:
            pushed = dfs(g, v, t, vis, min(f, g[u][v]))
            if pushed > 0:
                g[u][v] -= pushed
                g[v][u] += pushed
                return pushed
    return 0

def maxflow(g, s, t):
    flow = 0
    while True:
        vis = set()
        pushed = dfs(g, s, t, vis, 10**9)
        if pushed == 0:
            break
        flow += pushed
    return flow

n = int(input()) #эт число банков
a = list(map(int, input().split()))#хотят предприятия
b = list(map(int, input().split()))#хотят банки
m = int(input())#сколько связей есть

g = {}
s = 'S'
t = 'T'
g[s] = {}
g[t] = {}

for i in range(n):
    g[i] = {}
    g[s][i] = a[i]
    g[i][s] = 0

for j in range(n):
    g[n + j] = {}
    g[n + j][t] = b[j]
    g[t][n + j] = 0

for _ in range(m):
    i, j = map(int, input().split())
    if i not in g:
        g[i] = {}
    if n + j not in g:
        g[n + j] = {}
    g[i][n + j] = 10**9
    g[n + j][i] = 0

res = maxflow(g, s, t)
if res == sum(a):
    print('YES')
else:
    print('NO')


'''
экземпл данных которые можно забить
2
4 6
5 5
3
0 0
1 0
1 1
'''