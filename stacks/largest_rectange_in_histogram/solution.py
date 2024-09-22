from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  # To store the maximum area
        stack = []   # Stack to store (index, height) tuples

        # Iterate over all bars in the histogram
        for i, h in enumerate(heights):
            start = i
            # While the current bar is shorter than the bar on top of the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))  # Calculate max area
                start = index  # Update the start position for the current bar
            stack.append((start, h))  # Push current bar with updated start

        # Calculate the area for any remaining bars in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))  # Calculate max area for remaining bars

        return maxArea  # Return the maximum area found


if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: Standard histogram
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"Input: {heights1}, Largest Area: {solution.largestRectangleArea(heights1)}")  # Expected: 10

    # Test Case 2: Histogram with all equal heights
    heights2 = [4, 4, 4, 4, 4]
    print(f"Input: {heights2}, Largest Area: {solution.largestRectangleArea(heights2)}")  # Expected: 20

    # Test Case 3: Single height
    heights3 = [5]
    print(f"Input: {heights3}, Largest Area: {solution.largestRectangleArea(heights3)}")  # Expected: 5

    # Test Case 4: Empty histogram (no bars)
    heights4 = []
    print(f"Input: {heights4}, Largest Area: {solution.largestRectangleArea(heights4)}")  # Expected: 0

    # Test Case 5: Decreasing heights
    heights5 = [6, 5, 4, 3, 2, 1]
    print(f"Input: {heights5}, Largest Area: {solution.largestRectangleArea(heights5)}")  # Expected: 12

