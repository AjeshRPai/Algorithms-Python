import collections
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[0])


        def captureCell(r,c):
            if(
                min(r,c)<0
                or r == ROWS
                or c == COLUMNS
                or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            captureCell(r+1,c)
            captureCell(r-1,c)
            captureCell(r,c+1)
            captureCell(r,c-1)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLUMNS - 1]):
                    captureCell(r,c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        print(board)




if __name__ == '__main__':
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "X", "O"]
    ]
    solution.solve(board)
    print(board)
