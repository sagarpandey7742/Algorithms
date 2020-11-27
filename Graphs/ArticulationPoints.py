from collections import defaultdict

V = 5
vis = [-1] * V
low = [-1] * V
parent = [-1] * V
articulationPoints = [False] * V
graph = defaultdict(list)


def dfs(u, vis, low, parent, articulationPoints, time):
    vis[u] = low[u] = time
    time += 1
    children = 0
    for v in graph[u]:
        if vis[v] == -1:
            children += 1
            parent[v] = u
            dfs(v, vis, low, parent, articulationPoints, time)
            low[u] = min(low[u], low[v])

            if parent[u] == -1 and children > 1:
                articulationPoints[u] = True

            if parent[u] != -1 and low[v] >= vis[u]:
                articulationPoints[u] = True
        elif v != parent[u]:
            low[u] = min(low[u], low[v])


def findArticulationPoints():
    for i in range(V):
        if vis[i] == -1:
            dfs(i, vis, low, parent, articulationPoints, 0)
    print("Articulation Points")
    for i in range(V):
        if articulationPoints[i]:
            print(i, end=" ")


# # answer 0 3
# graph[0].append(2)
# graph[2].append(0)
# graph[0].append(3)
# graph[3].append(0)
# graph[1].append(0)
# graph[0].append(1)
# graph[2].append(1)
# # graph[2].append(4)
# # graph[4].append(2)
# graph[1].append(2)
# graph[3].append(4)
# graph[4].append(3)

# # answer 0 3
# graph[1].append(0)
# graph[0].append(2)
# graph[2].append(1)
# graph[0].append(3)
# graph[3].append(4)

# # answer 1 2
# graph[0].append(1)
# graph[1].append(2)
# graph[2].append(3)


findArticulationPoints()
