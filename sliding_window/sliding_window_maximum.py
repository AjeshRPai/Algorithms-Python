from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()  # This will store indices of elements

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if window and window[0] <= i - k:
                window.popleft()

            # Remove all smaller elements from the back of the window
            while window and nums[window[-1]] < num:
                window.pop()

            # Add current element's index to the window
            window.append(i)

            # If we've reached the window size, add the max to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result

if __name__ == '__main__':
    solution = Solution()

    # Test case 1: Normal case
    nums1, k1 = [1,3,-1,-3,5,3,6,7], 3
    print(f"Test 1: nums = {nums1}, k = {k1}")
    print(f"Result: {solution.maxSlidingWindow(nums1, k1)}")
    print(f"Expected: [3,3,5,5,6,7]\n")

    # Test case 2: Window size equal to array length
    nums2, k2 = [1,-1], 2
    print(f"Test 2: nums = {nums2}, k = {k2}")
    print(f"Result: {solution.maxSlidingWindow(nums2, k2)}")
    print(f"Expected: [1]\n")

    # Test case 3: Window size 1
    nums3, k3 = [1,3,2,5,8,7], 1
    print(f"Test 3: nums = {nums3}, k = {k3}")
    print(f"Result: {solution.maxSlidingWindow(nums3, k3)}")
    print(f"Expected: [1,3,2,5,8,7]\n")

    # Test case 4: Descending order array
    nums4, k4 = [9,8,7,6,5,4,3,2,1], 3
    print(f"Test 4: nums = {nums4}, k = {k4}")
    print(f"Result: {solution.maxSlidingWindow(nums4, k4)}")
    print(f"Expected: [9,8,7,6,5,4,3]\n")

    # Test case 5: Ascending order array
    nums5, k5 = [1,2,3,4,5,6,7,8,9], 3
    print(f"Test 5: nums = {nums5}, k = {k5}")
    print(f"Result: {solution.maxSlidingWindow(nums5, k5)}")
    print(f"Expected: [3,4,5,6,7,8,9]\n")

test_max_sliding_window()