from typing import List
from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use dictionaries to keep track of seen numbers in rows, columns, and 3x3 subgrids (squares)
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # Key = (row // 3, col // 3) for 3x3 subgrids

        # Loop through every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip if the current cell is empty ('.')
                if board[r][c] == ".":
                    continue

                # Check if the current value already exists in the current row, column, or 3x3 square
                if (board[r][c] in rows[r] or
                        board[r][c] in cols[c] or
                        board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # Return False if there's a conflict

                # Add the value to the respective row, column, and square sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no conflicts are found, return True (the Sudoku board is valid)
        return True

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Valid Sudoku board
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(f"Test Case 1 -> Is valid Sudoku: {solution.isValidSudoku(board1)}")

    # Test Case 2: Invalid Sudoku board
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(f"Test Case 2 -> Is valid Sudoku: {solution.isValidSudoku(board2)}")

    # Test Case 3: Empty Sudoku board
    board3 = [["."] * 9 for _ in range(9)]
    print(f"Test Case 3 -> Is valid Sudoku: {solution.isValidSudoku(board3)}")

    # Test Case 4: Minimal Sudoku board (just a single valid number)
    board4 = [
        ["5", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    print(f"Test Case 4 -> Is valid Sudoku: {solution.isValidSudoku(board4)}")