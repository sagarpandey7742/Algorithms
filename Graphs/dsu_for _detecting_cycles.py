# For detecting cycles in undirected graphs

# find() return the absolute parent of the current node
# union() merges the disjoint sets such that new_rank = max(rank(a), rank(b))
# where a and b are the sets being merged

def findRedundantConnection(edges):
    n = len(edges)
    parent = [-1] * n
    rank = [0] * n

    def find(node):
        if parent[node] == -1:
            return node
        parent[node] = find(parent[node])  # Path compression
        return parent[node]

    def union(u, v):
        if rank[u] > rank[v]:
            parent[v] = u
        elif rank[u] < rank[v]:
            parent[u] = v
        else:
            parent[u] = v
            rank[v] += 1

    for edge in edges:
        u = edge[0] - 1
        v = edge[1] - 1
        if find(u) == find(v):
            return edge
        union(find(u), find(v))


edges = [[1, 2], [1, 3], [2, 3]]

# edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

# edges = [[1, 2], [3, 4], [2, 3], [1, 5], [5, 4]]

print(findRedundantConnection(edges))
