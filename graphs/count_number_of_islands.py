import collections
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visit = set()
        rows, columns = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(row, column):
            if row < rows or column < columns or grid[row][column] == "0" or (row, column) in visit:
                return

            visit.add([row, column])
            for dr, dc in directions:
                dfs(row + dr, column + dc)

        # conditions to return
        # if the value is 0
        # if its already visited  - already checked
        # if its out of the rows and cols

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == "1" and (row, col) not in visit:
                    islands += 1
                    dfs(row, col)


## 2nd solution
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    queue = deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                            grid[x][y] = '0'  # mark as visited
                            for dx, dy in directions:
                                queue.append((x + dx, y + dy))

        return num_islands

class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visit = set()
        rows, columns = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def bfs(row, column):
            queue = collections.deque()
            visit.add((row,column))
            queue.append((row,column))

            while queue:
                row, column = queue.popleft()
                for dr,dc in directions:
                    r,c = row+dr, column+dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visit:
                        queue.append((r,c))
                        visit.add((r,c))

        for row in range(rows):
            for colum in range(columns):
                if grid[row][colum] == "1" and (row, colum) not in visit:
                    islands += 1
                    bfs(row, colum)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIslands(grid=[
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))
