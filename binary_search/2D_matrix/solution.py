from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search to find the potential row where the target could be
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:  # Target is larger than the last element in the row
                top = row + 1
            elif target < matrix[row][0]:  # Target is smaller than the first element in the row
                bot = row - 1
            else:
                break  # Target is within the range of the current row

        # If no valid row is found, return False
        if not (top <= bot):
            return False

        # Binary search within the selected row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Target present in the matrix
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3
    print(solution.searchMatrix(matrix1, target1))  # Expected: True

    # Test Case 2: Target absent in the matrix
    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    print(solution.searchMatrix(matrix2, target2))  # Expected: False

    # Test Case 3: Target at the boundary of the matrix
    matrix3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    target3 = 9
    print(solution.searchMatrix(matrix3, target3))  # Expected: True

    # Test Case 4: Single row matrix
    matrix4 = [[1, 3, 5, 7]]
    target4 = 5
    print(solution.searchMatrix(matrix4, target4))  # Expected: True

    # Test Case 5: Single column matrix
    matrix5 = [[1], [2], [3], [4], [5]]
    target5 = 4
    print(solution.searchMatrix(matrix5, target5))  # Expected: True