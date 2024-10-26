import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        min_heap = [(grid[0][0], 0 , 0)]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        visited = set()
        visited.add((0,0))

        while min_heap:
            elevation, row, col = heapq.heappop(min_heap)

            # happy path and scneario
            if row == n - 1 and col == n-1:
                return elevation

            for dr , dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0<= new_row < n and 0<= new_col < n and (new_row,new_col) not in visited:
                    visited.add((new_row, new_col))
                    heapq.heappush(min_heap, (max(elevation, grid[new_row][new_col]), new_row, new_col))
        return -1


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    grid1 = [
        [0, 2],
        [1, 3]
    ]
    print(solution.swimInWater(grid1))  # Expected output: 3

    # Test case 2
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]
    ]
    print(solution.swimInWater(grid2))  # Expected output: 16

    # Test case 3
    grid3 = [
        [3, 2],
        [0, 1]
    ]
    print(solution.swimInWater(grid3))  # Expected output: 3






