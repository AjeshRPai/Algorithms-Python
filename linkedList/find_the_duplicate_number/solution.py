from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]  # Slow pointer moves one step
            print(nums[fast])
            print(nums[nums[fast]])
            fast = nums[nums[fast]]  # Fast pointer moves two steps

        # Phase 2: Find the entrance to the cycle
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]  # Both slow and slow2 move one step
            slow2 = nums[slow2]

        # The point where they meet is the duplicate number
        return slow

# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Test case
    nums = [1, 3, 4, 2, 2]
    duplicate = solution.findDuplicate(nums)

    print(f"The duplicate number is: {duplicate}")