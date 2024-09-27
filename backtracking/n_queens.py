def solveNQueens(n):
    # Initialize the chessboard with empty squares
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Sets to keep track of occupied columns and diagonals
    cols = set()  # Columns where queens are placed
    posDiag = set()  # Positive diagonals (row + col) with queens
    negDiag = set()  # Negative diagonals (row - col) with queens

    # List to store all valid solutions
    solutions = []

    def is_safe(row, col):
        # Check if it's safe to place a queen at the given position
        return not (col in cols or
                    (row + col) in posDiag or
                    (row - col) in negDiag)

    def place_queen(row, col):
        # Place a queen on the board and mark the attacked positions
        board[row][col] = 'Q'
        cols.add(col)
        posDiag.add(row + col)
        negDiag.add(row - col)

    def remove_queen(row, col):
        # Remove a queen from the board and unmark the attacked positions
        board[row][col] = '.'
        cols.remove(col)
        posDiag.remove(row + col)
        negDiag.remove(row - col)

    def backtrack(row):
        # Base case: If all queens are placed, add the solution
        if row == n:
            solutions.append([''.join(r) for r in board])
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(row, col):
                place_queen(row, col)
                backtrack(row + 1)  # Recursively place queens in the next row
                remove_queen(row, col)  # Backtrack: remove the queen and try next position

    # Start the backtracking process from the first row
    backtrack(0)
    return solutions


# Helper function to print a single board solution
def print_solution(board):
    for row in board:
        print(' '.join(row))
    print()


if __name__ == '__main__':
    # Test cases
    print("4-Queens Problem:")
    solutions_4 = solveNQueens(4)
    for i, solution in enumerate(solutions_4):
        print(f"Solution {i + 1}:")
        print_solution(solution)

    print("8-Queens Problem:")
    solutions_8 = solveNQueens(8)
    print(f"Number of solutions for 8-Queens: {len(solutions_8)}")
    print("First solution:")
    print_solution(solutions_8[0])

    print("1-Queen Problem:")
    solutions_1 = solveNQueens(1)
    print_solution(solutions_1[0])