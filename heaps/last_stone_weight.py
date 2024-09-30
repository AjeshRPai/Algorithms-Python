import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the list to a max heap by negating all values
        # Python's heapq implements a min heap, so we use negative values for a max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Continue while there's more than one stone
        while len(max_heap) > 1:
            # Extract the two heaviest stones
            # heapq.heappop returns and removes the smallest element (which is our largest stone)
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)

            # If the stones have different weights, calculate the remaining weight
            # and add it back to the heap
            if heaviest != second_heaviest:
                remaining_weight = heaviest - second_heaviest
                heapq.heappush(max_heap, -remaining_weight)

        # If there's a stone left, return its weight; otherwise, return 0
        return -max_heap[0] if max_heap else 0


# Example usage
solution = Solution()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))  # Expected output: 1
print(solution.lastStoneWeight([1]))  # Expected output: 1
print(solution.lastStoneWeight([2, 2]))  # Expected output: 0