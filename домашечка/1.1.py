#Эйлеров путь — это путь, проходящий по всем рёбрам графа и притом только по одному разу
def iseul(G):
    cnt_vert = 0
    start_path = None
    for node in G:
        if len(G[node]) % 2 != 0:
            cnt_vert += 1
            if start_path is None:
                start_path = node
    if cnt_vert == 0:
        if G:
            start_path = next(iter(G))
        return (True, start_path)
    elif cnt_vert == 2:
        return (True, start_path)
    else:
        return (False, None)

def findeulway(G):
    from copy import deepcopy
    graph = deepcopy(G)
    eulerian, start = iseul(graph)
    if not eulerian:
        return []

    path = []

    def dfs(v):
        while graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            dfs(u)
        path.append(v)

    dfs(start)
    path.reverse()
    return path

G = {'A': ['B'], 'B': ['A', 'C', 'D'], 'C': ['B', 'D'], 'D': ['B', 'C']}

print(findeulway(G))