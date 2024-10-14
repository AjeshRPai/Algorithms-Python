from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Initialize variables for Prim's algorithm
        total_cost = 0
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            print("cost and point for the next index")
            print(cost, point)

            if point in visited:
                continue

            total_cost += cost
            visited.add(point)

            for next_point in range(n):
                if next_point not in visited:

                    distance = manhattan_distance(points[point], points[next_point])
                    print(distance, next_point, points[next_point])
                    heapq.heappush(min_heap, (distance, next_point))

        return total_cost


# Test cases
def test_min_cost_connect():
    sol = Solution()

    # Test Case 1: Simple square
    test1 = [[0,0], [2,2], [3,10], [5,2]]
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