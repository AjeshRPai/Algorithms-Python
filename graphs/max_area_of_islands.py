import collections
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        max_of_islands = 0
        visit = set()
        rows, columns = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(r, c) -> int:
            if r not in range(rows) and c not in range(columns) and grid[r][c] == "0" and (r, c) in visit:
                return 0

            visit.add((r,c))
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            return area

        for row in range(rows):
            for colum in range(columns):
                if grid[row][colum] == "1" and (row, colum) not in visit:
                    max_of_islands = max(max_of_islands,dfs(row, colum))

        return max_of_islands

if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands(grid=[
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
