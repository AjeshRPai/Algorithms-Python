class UnionFind:
    def __init__(self, size):
        # Initialize each element as its own parent
        self.parent = list(range(size))
        # Rank is used for union by rank optimization
        self.rank = [1] * size

    def find(self, x):
        # Find the root of the set x belongs to
        # Uses path compression for optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        # Unite the sets containing x and y
        root_x, root_y = self.find(x), self.find(y)

        # If x and y are already in the same set, we can't unite them
        if root_x == root_y:
            return False  # Indicates that a cycle is formed

        # Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are same, make one as root and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True  # Union successful


class Solution:
    def findRedundantConnection(self, edges):
        # Create a UnionFind data structure
        # Size is len(edges) + 1 because nodes are 1-indexed
        uf = UnionFind(len(edges) + 1)

        # Iterate through all edges
        for edge in edges:
            # Try to union the nodes connected by this edge
            if not uf.union(edge[0], edge[1]):
                # If union returns False, it means these nodes were already connected
                # This edge creates a cycle, so it's the redundant connection
                return edge

        # This line should never be reached if the input is valid
        # because the problem guarantees there's always a redundant connection
        return []


def test_redundant_connection_finder():
    solution = Solution()

    # Test case 1: Simple cycle
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print("Test case 1:", solution.findRedundantConnection(edges1))

    # Test case 2: Larger graph with cycle
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print("Test case 2:", solution.findRedundantConnection(edges2))

    # Test case 3: Multiple possible answers, should return the last edge
    edges3 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    print("Test case 3:", solution.findRedundantConnection(edges3))

    # Test case 4: Tree structure (no cycle)
    edges4 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print("Test case 4:", solution.findRedundantConnection(edges4))

if __name__ == '__main__':
    test_redundant_connection_finder()