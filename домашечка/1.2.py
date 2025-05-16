
import heapq

def johnson(graph):
    graph['s'] = {}
    for node in graph:
        if node != 's':
            graph['s'][node] = 0

    dist = {v: float('inf') for v in graph}
    dist['s'] = 0

    for _ in range(len(graph) - 1):
        updated = False
        for u in graph:
            for v in graph[u]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    updated = True
        if not updated:
            break

    for u in graph:
        for v in graph[u]:
            if dist[u] + graph[u][v] < dist[v]:
                print("Отрицательный цикл обнаружен")
                return None, None

    h = dist

    reweighted = {}
    for u in graph:
        if u == 's':
            continue
        reweighted[u] = {}
        for v in graph[u]:
            if v == 's':
                continue
            reweighted[u][v] = graph[u][v] + h[u] - h[v]

    def dijkstra(start):
        d = {v: float('inf') for v in reweighted}
        d[start] = 0
        pq = [(0, start)]
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > d[u]:
                continue
            for v in reweighted[u]:
                if d[v] > d[u] + reweighted[u][v]:
                    d[v] = d[u] + reweighted[u][v]
                    heapq.heappush(pq, (d[v], v))
        return d

    nodes = sorted(reweighted.keys())
    result = {u: dijkstra(u) for u in nodes}

    n = len(nodes)
    dist_matrix = [[float('inf')] * n for _ in range(n)]

    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if v in result[u]:
                dist_matrix[i][j] = result[u][v] - h[u] + h[v]

    return dist_matrix, nodes

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': -3, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

dist_matrix, nodes = johnson(graph)

if dist_matrix:
    for row in dist_matrix:
        print(row)
