from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Create adjacency list to store edges: {point_index: [(manhattan_distance, other_point_index)]}
        graph = [[] for _ in range(n)]

        # Build the graph - calculate distances between all points
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # Calculate Manhattan distance
                distance = abs(x1 - x2) + abs(y1 - y2)
                # Add edges in both directions
                graph[i].append((distance, j))
                graph[j].append((distance, i))

        # Initialize variables for Prim's algorithm
        total_cost = 0
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)

        # Run Prim's algorithm
        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)

            # Skip if already visited
            if point in visited:
                continue

            # Add cost to total and mark as visited
            total_cost += cost
            visited.add(point)

            # Add all edges to unvisited neighbors
            for neighbor_cost, neighbor in graph[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor))

        return total_cost


# Test cases
def test_min_cost_connect():
    sol = Solution()

    # Test Case 1: Simple square
    test1 = [[0, 0], [1, 1], [1, 0], [0, 1]]
    print("Test 1:", sol.minCostConnectPoints(test1))  # Expected: 4

    # Test Case 2: Line of points
    test2 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print("Test 2:", sol.minCostConnectPoints(test2))  # Expected: 20

    # Test Case 3: Single point
    test3 = [[0, 0]]
    print("Test 3:", sol.minCostConnectPoints(test3))  # Expected: 0

    # Test Case 4: Two points
    test4 = [[3, 12], [-2, 5]]
    print("Test 4:", sol.minCostConnectPoints(test4))  # Expected: 12


if __name__ == "__main__":
    test_min_cost_connect()