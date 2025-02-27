import heapq
from typing import List

from heaps.last_stone_weight import solution
from trie.word_search import solution


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]

        # Track nodes which are included in MST.
        in_mst = [False] * n

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)

            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue

            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1

            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + \
                                  abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_weight, next_node))

        return mst_cost



if __name__ == '__main__':
    # Example Graph (Adjacency List)
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 2)],
        'D': [('B', 4), ('C', 2)]
    }

    # Run Prim's Algorithm
    solution = Solution()
    mst_cost, mst = solution.minCostConnectPoints(graph)
    print("Minimum Spanning Tree Cost:", mst_cost)
    print("Edges in MST:", mst)