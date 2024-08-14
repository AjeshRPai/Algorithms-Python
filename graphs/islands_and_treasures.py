import collections
from collections import deque
from typing import List


def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    visit = set()
    queue = deque()
    rows, columns = len(grid), len(grid[0])

    # this adds the cell to visit and queue
    # return if the value is -1
    def addCell(r, c):
        if (min(r, c) < 0
                or r == rows
                or c == columns
                or (r, c) in visit
                or grid[r][c] == -1
        ):
            return
        visit.add((r, c))
        queue.append([r, c])

        # gets the main cells(treasure cells) so that we can check the neighbours first

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                visit.add((r, c))
                queue.append([r, c])

    dist = 0
    # iterate through the queue and visit the neigbouring item of each treasure
    # on each treasure, visit the cells
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            grid[r][c] = dist
            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)
        dist += 1


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        queue = deque()
        rows, columns = len(grid), len(grid[0])

        def addCell(r, c):
            if (min(r, c) < 0
                    or r == rows
                    or c == columns
                    or grid[r][c] == -1
                    or (r, c) in visit):
                return

            visit.add((r, c))
            queue.append([r, c])

        for row in range(rows):
            for colum in range(columns):
                if grid[row][colum] == 0:
                    queue.append((row, colum))
                    visit.add((row, colum))

        dist = 0
        while queue:
            print(queue)
            for i in range(len(queue)):
                print(i)
                r, c = queue.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

        print(grid)


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    solution.islandsAndTreasure(grid)
