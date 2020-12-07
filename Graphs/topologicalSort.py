# Topological sort is the works only on DAG
# Where the nodes are sorted in increasing order of their out-degree and in descending order of in-degree
# Node A comes before B if there exists a directed edge from A->B

from collections import defaultdict


def hasCycle(u, visited):
    #   0-> Unvisited
    #   1-> Processing
    #   2-> Processed

    if visited[u] == 1:
        # This node is being processed and we reach it again, so cycle
        return True
    if visited[u] == 2:
        # Already processed
        return False
    for v in graph[u]:
        if hasCycle(v, visited):
            return True
    visited[u] = 2
    # Mark as processed
    return False


def topologicalSortUtil(graph, u, visited, ans):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            topologicalSortUtil(graph, v, visited, ans)
    ans.append(u)


def topologicalSort(graph, n):
    # Firstly check if the graph is a DAG
    visited = [0] * n
    flag = 0
    for i in range(n):
        if hasCycle(i, visited):
            flag = 1
            break
    if flag:
        print("The graph is not a directed acyclic graph")
    else:
        visited = [0] * n
        ans = []
        for i in range(n):
            if visited[i] == 0:
                topologicalSortUtil(graph, i, visited, ans)
        print(*ans[::-1])


graph = defaultdict(list)

graph[5].append(0)
graph[5].append(2)
graph[0].append(2)
graph[0].append(3)
graph[3].append(1)
graph[4].append(1)
graph[4].append(2)

topologicalSort(graph, 6)
