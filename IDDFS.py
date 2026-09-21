from collections import defaultdict
import networkx as nx           # type: ignore
import matplotlib.pyplot as plt # type: ignore


class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = defaultdict(list)


    def addEdge(self, u, v):

        self.graph[u].append(v)


    # Depth Limited Search
    def DLS(self, src, target, maxDepth):

        if src == target:
            return True

        if maxDepth <= 0:
            return False

        for i in self.graph[src]:

            if self.DLS(i, target, maxDepth - 1):
                return True

        return False


    # Iterative Deepening DFS
    def IDDFS(self, src, target, maxDepth):

        for i in range(maxDepth + 1):

            if self.DLS(src, target, i):
                return True

        return False


# Create graph
g = Graph(7)

# Add edges
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)


# Source, target and maximum depth
src = 0
target = 6
maxDepth = 3


# IDDFS search
if g.IDDFS(src, target, maxDepth):
    print("Target is reachable from source within max depth")
else:
    print("Target is NOT reachable from source within max depth")


# ---------------- DRAW GRAPH ----------------

G = nx.DiGraph()

# Add the same edges
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 5)
G.add_edge(2, 6)


# Position of nodes
pos = {
    0: (0, 3),
    1: (-2, 2),
    2: (2, 2),
    3: (-3, 1),
    4: (-1, 1),
    5: (1, 1),
    6: (3, 1)
}


# Draw graph
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    arrows=True,
    font_size=12
)

plt.title("Graph for IDDFS")

plt.show()