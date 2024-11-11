from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = [[] for _ in range(n)]
        for u, v, cost in flights:
            graph[u].append((v, cost))

        prices = [float("inf")] * n
        prices[src] = 0

        # airport, cost, stops
        queue = deque([(src, 0, 0)])
        while queue:
            airport, current_cost, stops = queue.popleft()

            if stops > k:
                continue

            for neighbor, cost in graph[airport]:
                cost_on_route = current_cost + cost
                if prices[neighbor] > cost_on_route:
                    prices[neighbor] = cost_on_route
                    queue.append((neighbor, cost_on_route, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1