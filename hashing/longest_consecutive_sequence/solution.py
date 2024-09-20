from typing import List


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to a set for O(1) lookups
        numSet = set(nums)
        longest = 0

        # Iterate over each number in the set
        for n in numSet:
            # Only check for the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                # Count the length of the consecutive sequence
                while (n + length) in numSet:
                    length += 1
                # Update longest sequence if current one is longer
                longest = max(length, longest)

        return longest


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: General case with consecutive numbers
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Longest consecutive sequence length (nums1): {solution.longestConsecutive(nums1)}")  # Expected: 4

    # Test Case 2: Case with no consecutive numbers
    nums2 = [10, 20, 30, 40]
    print(f"Longest consecutive sequence length (nums2): {solution.longestConsecutive(nums2)}")  # Expected: 1

    # Test Case 3: Empty input list
    nums3 = []
    print(f"Longest consecutive sequence length (nums3): {solution.longestConsecutive(nums3)}")  # Expected: 0

    # Test Case 4: Case with duplicate numbers
    nums4 = [1, 2, 2, 3, 4, 5]
    print(f"Longest consecutive sequence length (nums4): {solution.longestConsecutive(nums4)}")  # Expected: 5

    # Test Case 5: Case with negative numbers
    nums5 = [-1, 0, 1, 2, -2, -3]
    print(f"Longest consecutive sequence length (nums5): {solution.longestConsecutive(nums5)}")  # Expected: 6
