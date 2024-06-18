import numpy as np


class UnionFind:
    def __init__(self, n):
        self.parent = np.arange(n)
        self.rank = np.zeros(n, dtype=int)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_from_adj_matrix(graph):
    n = graph.shape[0]
    edges = []

    # Extract edges from the adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i, j] != 0:
                edges.append((i, j, graph[i, j]))

    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    mst_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight


# Example usage:
# Adjacency matrix
adj_matrix = np.array([
    [0, 10, 6, 5, 0],
    [10, 0, 0, 15, 0],
    [6, 0, 0, 4, 0],
    [5, 15, 4, 0, 0],
    [0, 0, 0, 0, 0]
])

mst, mst_weight = kruskal_from_adj_matrix(adj_matrix)
print(mst)
print(mst_weight)