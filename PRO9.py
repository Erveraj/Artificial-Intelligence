#Program No 9: Implement Heuristic Search Techniques in Python.
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 4, 'E': 1, 'F': 2, 'G': 0
}

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        for neighbour, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_f = new_cost + heuristic[neighbour]
            heapq.heappush(
                queue,
                (new_f, new_cost, neighbour, path + [neighbour])
            )

path, cost = a_star('A', 'G')
print("Path:", path)
print("Cost:", cost)
