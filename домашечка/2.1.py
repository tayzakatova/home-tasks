#Алгоритм Эдмондса - Карпа <*))>>=<
#ищем максимальный поток вс сети с вершинами и ребрами с пропускной способностью
from collections import deque

M = int(input())

G = {}

for _ in range(M):
    v1, v2, w = input().split()
    w = int(w)
    if v1 not in G:
        G[v1] = {}
    G[v1][v2] = w
    if v2 not in G:
        G[v2] = {}
    if v1 not in G[v2]:
        G[v2][v1] = 0

def edmonds_karp(graph, start, finish):
    max_flow = 0
    while True:
        queue = deque()
        queue.append(start)
        parent = {}
        visited = set()
        visited.add(start)
        min_capacity = {}
        min_capacity[start] = float('inf')

        found = False
        while queue and not found:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited and graph[node][neighbor] > 0:
                    parent[neighbor] = node
                    visited.add(neighbor)
                    min_capacity[neighbor] = min(min_capacity[node], graph[node][neighbor])
                    if neighbor == finish:
                        found = True
                        break
                    queue.append(neighbor)

        if not found:
            break

        flow = min_capacity[finish]
        max_flow += flow
        current = finish
        while current != start:
            prev = parent[current]
            graph[prev][current] -= flow
            graph[current][prev] += flow
            current = prev

    return max_flow

start = input("старт? ")
finish = input("финиш? ")

print("Максимиальный поток:", edmonds_karp(G, start, finish))
