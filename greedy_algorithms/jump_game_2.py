from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the left and right bounds of the current window
        l, r = 0, 0
        # Variable to store the number of jumps
        res = 0

        # Continue until we can reach the last index
        while r < len(nums) - 1:
            # Variable to track the furthest we can jump
            maxJump = 0
            # Explore all indices within the current window
            for i in range(l, r + 1):
                # Update the maxJump to the furthest reachable index
                maxJump = max(maxJump, i + nums[i])

            # Move the window
            l = r + 1
            r = maxJump
            # Increment jump count
            res += 1

        return res


# Driver code to test the solution with multiple test cases
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 3, 1, 1, 4], 2),  # Expected 2
        ([2, 3, 0, 1, 4], 2),  # Expected 2
        ([1, 2, 3], 2),  # Expected 2
        ([0], 0),  # Single element, no jumps needed
        ([1, 1, 1, 1, 1], 4),  # Need to jump at every step
        ([5, 9, 3, 2, 1, 0, 1], 1),  # Jump from the first index
        ([6, 2, 4, 0, 5, 1, 1, 4, 2, 9], 2)  # Large jump at start
    ]

    # Run tests
    for idx, (nums, expected) in enumerate(test_cases):
        result = solution.jump(nums)
        print(f"Test case {idx + 1}: {nums} => Result: {result}, Expected: {expected}")
        assert result == expected, f"Test case {idx + 1} failed"
    print("All test cases passed!")
