from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Distance from source to all other nodes.
        dist = [float('inf')] * n
        dist[src] = 0

        # Run only K+1 times since we want shortest distance in K hops
        for _ in range(k + 1):
            # Create a copy of the distance array
            temp = dist[:]
            for u, v, cost in flights:
                if dist[u] != float('inf') and dist[u] + cost < temp[v]:
                    temp[v] = dist[u] + cost

            # Explicitly update dist values to prevent reference issues
            dist = temp[:]

        return -1 if dist[dst] == float('inf') else dist[dst]

# Define test cases
test_cases = [
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),  # Basic case
    (4, [[0, 1, 100], [1, 2, 200]], 0, 3, 1, -1),  # No available route
    (3, [[0, 1, 50], [1, 2, 70], [0, 2, 120]], 0, 2, 1, 120),  # Direct flight is cheaper
    (4, [[0, 1, 10], [1, 2, 10], [2, 3, 30], [0, 3, 60]], 0, 3, 2, 50),  # Exact stops constraint
    (5, [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [0, 4, 300]], 0, 4, 3, 250),  # Large graph
    (3, [[0, 1, 50], [1, 2, 50], [0, 2, 120]], 0, 2, 0, 120),  # No stops allowed
    (4, [[0, 1, 10], [1, 2, 10], [2, 1, 5], [2, 3, 50]], 0, 3, 3, 70),  # Cycle detection
]

if __name__ == '__main__':
    # Instantiate solution object
    sol = Solution()
    # Run test cases
    for i, (n, flights, src, dst, k, expected) in enumerate(test_cases):
        result = sol.findCheapestPrice(n, flights, src, dst, k)
        print(f"Test Case {i + 1}: {'Passed' if result == expected else f'Failed (Expected {expected}, got {result})'}")

