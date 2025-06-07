
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def minimum_edges_to_remove(N, M, edges):
    uf = UnionFind(N)
    edges_to_remove = 0

    for a, b in edges:
        # Convert to 0-based index
        a -= 1
        b -= 1
        if not uf.union(a, b):
            edges_to_remove += 1

    return edges_to_remove

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N, M = map(int, data[0].split())
    edges = [tuple(map(int, line.split())) for line in data[1:]]

    result = minimum_edges_to_remove(N, M, edges)
    print(result)