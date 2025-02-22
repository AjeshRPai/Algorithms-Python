from typing import List
import heapq

# O(E) iterate through edges to create adjacency list
# O(E * LOG V) For each edge there would be a value in heap, heap operation complexity is log V
# O(V * LOG V) For each node we are checking, there would be
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build adjacency list (graph)
        graph = {i: [] for i in range(n)}
        for u, v, cost in flights:
            graph[u].append((v, cost))

        # Min-heap (cost, current_node, stops_remaining)
        min_heap = [(0, src, k + 1)]

        # Distance dictionary to track the cheapest price at each node with a given number of stops
        dist = {}

        while min_heap:
            current_cost, node, stops_left = heapq.heappop(min_heap)

            # If we reach the destination, return the cost
            if node == dst:
                return current_cost

            # If we have remaining stops, explore neighbors
            if stops_left > 0:
                for neighbor, price in graph[node]:
                    new_cost = current_cost + price

                    # Push only if we haven't found a cheaper way to get to 'neighbor' with 'stops_left - 1'
                    if new_cost < dist.get((neighbor, stops_left - 1), float("inf")):
                        dist[(neighbor, stops_left - 1)] = new_cost
                        heapq.heappush(min_heap, (new_cost, neighbor, stops_left - 1))

        return -1  # If no route was found


# Define test cases
test_cases = [
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 200),  # Basic case
    (4, [[0,1,100],[1,2,200]], 0, 3, 1, -1),  # No available route
    (3, [[0,1,50],[1,2,70],[0,2,120]], 0, 2, 1, 120),  # Direct flight is cheaper
    (4, [[0,1,10],[1,2,10],[2,3,30],[0,3,60]], 0, 3, 2, 50),  # Exact stops constraint
    (5, [[0,1,100],[1,2,100],[2,3,100],[3,4,100],[0,4,300]], 0, 4, 3, 300),  # Fixed expected value
    (3, [[0,1,50],[1,2,50],[0,2,120]], 0, 2, 0, 120),  # No stops allowed
    (4, [[0,1,10],[1,2,10],[2,1,5],[2,3,50]], 0, 3, 3, 70),  # Cycle detection
]


if __name__ == '__main__':
    # Instantiate solution object
    sol = Solution()
    # Run test cases
    for i, (n, flights, src, dst, k, expected) in enumerate(test_cases):
        result = sol.findCheapestPrice(n, flights, src, dst, k)
        print(f"Test Case {i + 1}: {'Passed' if result == expected else f'Failed (Expected {expected}, got {result})'}")

