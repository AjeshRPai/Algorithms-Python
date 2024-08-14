import collections
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        queue = deque()
        rows, columns = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                            row in range(rows)
                            and col in range(columns)
                            and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


if __name__ == '__main__':
    solution = Solution()
    grid = [[1,1,0],[0,1,1],[0,1,2]]

    output = solution.orangesRotting(grid)
    print(output)
