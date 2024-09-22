from typing import List

# https://neetcode.io/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: empty array means no water can be trapped
        if not height:
            return 0

        l, r = 0, len(height) - 1  # Two pointers at start and end
        leftMax, rightMax = height[l], height[r]  # Initialize max heights
        res = 0  # Result to store total trapped water

        # Process until both pointers meet
        while l < r:
            if leftMax < rightMax:
                # Move left pointer to the right
                l += 1
                # Update the left max boundary
                leftMax = max(leftMax, height[l])
                # Calculate the water trapped and add to the result
                res += leftMax - height[l]
            else:
                # Move right pointer to the left
                r -= 1
                # Update the right max boundary
                rightMax = max(rightMax, height[r])
                # Calculate the water trapped and add to the result
                res += rightMax - height[r]

        return res

if __name__ == '__main__':
    solution = Solution()

    # Test Case 1: Basic example with trapped water
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"Input: {height1}, Trapped water: {solution.trap(height1)}")  # Expected: 6

    # Test Case 2: No water trapped (decreasing slope)
    height2 = [4, 3, 2, 1, 0]
    print(f"Input: {height2}, Trapped water: {solution.trap(height2)}")  # Expected: 0

    # Test Case 3: Flat surface (no height difference)
    height3 = [0, 0, 0]
    print(f"Input: {height3}, Trapped water: {solution.trap(height3)}")  # Expected: 0

    # Test Case 4: Large spikes with no water trapped
    height4 = [9, 6, 5, 4, 5, 6, 9]
    print(f"Input: {height4}, Trapped water: {solution.trap(height4)}")  # Expected: 15
