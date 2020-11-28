from collections import defaultdict
from math import inf


def floydWarshall(adj,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    for i in range(n):
        if adj[i][i] < 0:
            print("Negative edge detected")


graph = defaultdict(list)

edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
n=5
for edge in edges:
    u = edge[0]
    v = edge[1]
    w = edge[2]
    graph[u].append([v, w])
    graph[v].append([u, w])


adj = [[inf for i in range(n)] for j in range(n)]

for i in range(n):
    adj[i][i]=0
for u in graph.keys():
    for path in graph[u]:
        v = path[0]
        adj[u][v] = path[1]

floydWarshall(adj,n)
for i in range(len(graph.keys())):
    for j in range(len(graph.keys())):
        print("From",i, " -> ", "to",j, " = ", adj[i][j])
