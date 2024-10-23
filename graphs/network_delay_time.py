import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], totalNodes: int, startNode: int) -> int:
        # Create adjacency list representation of the network
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        # Track visited nodes and initialize min heap with start node
        visited = set()
        minHeap = [(0, startNode)]  # (total_time, node)
        maxTime = 0

        # Dijkstra's algorithm
        while minHeap:
            currentTime, currentNode = heapq.heappop(minHeap)

            # Skip if already visited
            if currentNode in visited:
                continue

            # Mark as visited and update max time
            visited.add(currentNode)
            maxTime = currentTime

            # Explore neighbors
            for nextNode, travelTime in graph[currentNode]:
                if nextNode not in visited:
                    totalTime = currentTime + travelTime
                    heapq.heappush(minHeap, (totalTime, nextNode))

        # Return maxTime if all nodes visited, else -1
        return maxTime if len(visited) == totalNodes else -1


# Test cases
def test_network_delay():
    solution = Solution()

    # Test Case 1: Simple network
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    assert solution.networkDelayTime(times1, n1, k1) == 2, "Test case 1 failed"

    # Test Case 2: Disconnected network
    times2 = [[1, 2, 1]]
    n2, k2 = 3, 1
    assert solution.networkDelayTime(times2, n2, k2) == -1, "Test case 2 failed"

    # Test Case 3: Single node
    times3 = []
    n3, k3 = 1, 1
    assert solution.networkDelayTime(times3, n3, k3) == 0, "Test case 3 failed"



    print("All test cases passed!")


# Run tests
if __name__ == "__main__":
    test_network_delay()

