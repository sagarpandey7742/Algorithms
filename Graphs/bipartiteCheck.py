# A graph is a bipartite if we can color the vertices
# in such a way that no two immediate neighbours have the same colour
# Formally an odd cycle is a non bipartite

# The graph is given in the following form:
# graph[i] is a list of indexes j for which the edge between nodes i and j exists.
# Each node is an integer between 0 and graph.length - 1.
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

def bipartiteCheck(graph):
    n = len(graph)
    g = {}
    for i in range(n):
        g[i] = graph[i]
    color = [0] * n

    def dfs(u):
        for v in g[u]:
            if color[v] == 0:
                color[v] = color[u] * -1  # colors available are 1 and -1
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False
            else:
                continue
        return True

    for i in g.keys():
        if color[i] == 0:
            color[i] = 1
            if not dfs(i):
                return False
    return True


# graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(bipartiteCheck(graph))
