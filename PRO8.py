#Program No 8: Implement Uninformed Search Techniques in Python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour, visited)
    return visited

print("BFS:", bfs('A'))
print("DFS:", dfs('A'))
