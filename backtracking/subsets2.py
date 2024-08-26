from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list to store all unique subsets
        result = []

        # Sort the input list to handle duplicates easily
        nums.sort()

        # Helper function to perform backtracking
        def backtrack(index, current_subset):
            # If we've considered all elements, add the current subset to the result
            if index == len(nums):
                result.append(current_subset.copy())
                return

            # Include the current element and move to the next
            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)
            # Backtrack: remove the last element added
            current_subset.pop()

            # Skip over duplicates by advancing the index past all identical elements
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            # Exclude the current element and move to the next distinct element
            backtrack(index + 1, current_subset)

        # Start the backtracking process with an empty subset
        backtrack(0, [])

        return result
